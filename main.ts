/* Copyright (c) 2020 MTHS All rights reserved
 *
 * Created by: Michael B
 * Created on: Sep 2023
 * This program turns LED on and off
*/

// setup
basic.clearScreen()
pins.digitalWritePin(DigitalPin.P16,0)
basic.showIcon(IconNames.Happy)

basic.showString('Hello, World!')
