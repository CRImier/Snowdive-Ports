# Snowdive ports

This repository has information and helper files for using different SBCs with Snowdive boards.

* `devicetree/zero`: software for creating DeviceTree overlays for various SBCs that can be attached to Snowdive boards
* `docs`: manually compiled pin tables detailing SBC compatibility with Snowdive boards, for ease of comparison and software porting purposes
* `schematics`: schematic PDFs used as sources for information in this repo

Currently, documents and enables the Snowdive ZERO top board compatibility; this repository will be updated once other top boards are available.

## SBCs to be supported

* Raspberry Pi Zero 1/1W/2W
* Banana Pi M2
* Banana Pi M4
* Radxa Rock S0
* Radxa Cubie A7Z
* Radxa Zero V1.5 (GPIO fixes required)
* Radxa Zero 3W
* Orange Pi 2W

## Upcoming

* Luckfox Lyra Zero W
* MangoPi MQ Pro (RISC-V)

## Candidates for support

* MangoPi MQ Quad
* Luckfox Pico Zero
* AC57-Canmv K230D ZERO (Banana Pi) (RISC-V)

## Not currently considered

Support can be discussed.

* Orange Pi 3W (**SMD pin header**)
* Radxa Zero 2 (**SMD pin header**)
