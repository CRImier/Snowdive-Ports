import os
import yaml
import jinja2
import string
from copy import copy

with open("boards.yaml", 'r') as f:
    c = f.read()
config = yaml.safe_load(c)

#print(config)

loader = jinja2.FileSystemLoader(searchpath="./")
env = jinja2.Environment(loader=loader)

# currently unused
gpios = {
  0: {"name":"pi_pwr_en",  "type":"out", "state":True , "hog":True},
  1: {"name":"esp_en",     "type":"out", "state":True },
  3: {"name":"esp_pwr_en", "type":"out", "state":True },
  6: {"name":"disp_extin", "type":"out", "state":True },
  7: {"name":"disp_rst",   "type":"out", "state":True },
  12:{"name":"usbcmux_c",  "type":"out", "state":True , "hog":True},
  14:{"name":"usbcmux_s",  "type":"out", "state":False, "hog":True},
}
# debug for now
gpios = {
  6: {"name":"disp_extin", "type":"out", "state":True },
  7: {"name":"disp_rst",   "type":"out", "state":True },
  12:{"name":"usbcmux_c",  "type":"out", "state":True , "hog":True},
  14:{"name":"usbcmux_s",  "type":"out", "state":False, "hog":True},
}

# This currently only accounts for Zero branch boards, since CM- and CatchAll- Snowdive branches haven't been designed yet
start = "snowdive-zero"

output_dir = "output/"
os.makedirs(output_dir, exist_ok=True)

def normalize_gpios(config):
    """ This function converts GPIO strings like "A2" or "B0" into GPIO numbers (i.e. 2 or 8) """
    config = copy(config)
    gpio_numbering = config.get("gpio_numbering", "")
    if not gpio_numbering: return config
    if gpio_numbering == "rpi": return config # no changes necessary
    # all parameters ending with gpio_num will be normalized according to the numbering scheme
    gpio_params = [param for param in board_config if param.endswith("gpio_str")]
    for gpio_param in gpio_params:
        if gpio_numbering in ["h3", "rk3308"]:
            gpio_param_str = config[gpio_param]
            gpio_letter, gpio_num = gpio_param[0].upper(), gpio_param[1:]
            gpio_num = int(gpio_num.lstrip("-")) # processing either "NUM" or "-NUM"
            # TODO h3 exception for r_pio (L port)
            # accounting for gpio letter:
            gpio_num = gpio_num + 8 * string.ascii_uppercase.index(gpio_letter)
            config[gpio_param] = gpio_num
    return config

for type in ["standalone", "palmtop"]:
    template_filename = f"{start}-{type}.dtst"
    template = env.get_template(template_filename)
    for board in config["boards"]:
        board_config = normalize_gpios(config["boards"][board])
        if not board_config.get("finished", False):
            continue
        untested_marker = "-UNTESTED" if not board_config.get("tested", False) else ""
        filename = f"{start}-{type}-{board}{untested_marker}.dts"
        print(f"Compiling {filename} for {board.upper()}:\n")
        dts = template.render(gpios=gpios, **board_config)
        #print(dts)
        with open(output_dir+filename, "w") as f:
            f.write(dts)


#i2c_bus="1", int_a_gpio='<0 18 0>', int_b_gpio='<2 12 0>', gpio_target="pinctrl", pin_prefix="rockchip,", compat=compat)
#filename = "snowdive-zero-standalone-bpi-m2.dts"
#compat = '"allwinner,sun4i-a10", "allwinner,sun7i-a20", "allwinner,sun8i-h3", "allwinner,sun50i-a64", "allwinner,sun50i-h5"'
#dts = template.render(gpios=gpios, i2c_bus="3", int_a_gpio='"PA2"', int_b_gpio='"PA3"', gpio_target="pio", pin_prefix="", compat=compat)
#print(dts)
# Radxa ROCK Pi S0 (untested)
# int_a: GPIO0_C2: 0 18
# int_b: GPIO2_B4  2 11
#print(dts)
