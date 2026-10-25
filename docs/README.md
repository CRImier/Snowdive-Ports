# Documentation on Snowdive-compatible boards

This board documents Zero-compatible board pinouts to check for Snowdive ZERO top board compatibility.

Every pinout is derived from the schematic as attached, checking that GPIO names match the GPIO names on the CPU symbols (which helped catch signal name errors like in the Radxa Rock S0 schematic).

`top_zero_v0` files should support Snowdive ZERO top board V0 and V1.

## Boards included

* Banana Pi M2
* Banana Pi M4
* Radxa Rock S0
* Radxa Cubie A7Z
* Radxa Zero V1.5
* Radxa Zero 3W
* Orange Pi 2W

### Boards excluded

Uses SMD header, is very bothersome to solder to the ZERO board:

* Orange Pi 3W

Such boards can still be used, but please do contact me if you want it included.
