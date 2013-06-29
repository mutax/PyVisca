#! /usr/bin/env python
# -*- coding: utf8 -*-
#
#    PyVisca - Implementation of the Visca serial protocol in python
#    Copyright (C) 2013  Florian Streibelt pyvisca@f-streibelt.de
#
#    This program is free software; you can redistribute it and/or modify
#    it under the terms of the GNU General Public License as published by
#    the Free Software Foundation, version 2 only.
#
#    This program is distributed in the hope that it will be useful,
#    but WITHOUT ANY WARRANTY; without even the implied warranty of
#    MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
#    GNU General Public License for more details.
#
#    You should have received a copy of the GNU General Public License
#    along with this program; if not, write to the Free Software
#    Foundation, Inc., 51 Franklin Street, Fifth Floor, Boston, MA  02110-1301
#    USA

"""PyVisca by Florian Streibelt <pyvisca@f-streibelt.de>"""

#
# This is used for testing the functionality while developing,
# expect spaghetti code...
#

def main():

	from pyviscalib.visca import Visca
	from  time import sleep

	v=Visca()

	v.cmd_adress_set()

	v.cmd_if_clear_all()

	CAM=1

#	v.cmd_cam_power_off(CAM)

	v.cmd_cam_power_on(CAM)

	v.cmd_cam_auto_power_off(CAM,2)

	v.cmd_datascreen_on(CAM)


	sleep(3)
	v.cmd_ptd_abs(CAM,pp=-1440,tp=-360)
	sleep(3)
	v.cmd_cam_memory_set(CAM,0)

	sleep(3)
	v.cmd_ptd_abs(CAM,pp=1440,tp=360)
	sleep(3)
	v.cmd_cam_memory_set(CAM,1)

	sleep(3)
	v.cmd_ptd_abs(CAM,pp=0,tp=0)
	sleep(3)
	v.cmd_cam_memory_set(CAM,2)

	sleep(5)
	v.cmd_cam_memory_recall(CAM,0)
	sleep(3)
	v.cmd_cam_memory_recall(CAM,1)
	sleep(3)
	v.cmd_cam_memory_recall(CAM,2)


#	sleep(1)
#	v.cmd_cam_zoom_tele(CAM)
#	sleep(2)
#	v.cmd_cam_zoom_stop(CAM)
#	sleep(3)
#
#	v.cmd_cam_zoom_wide(CAM)
#	sleep(7)

#	v.cmd_cam_zoom_tele_speed(CAM,0)
#	sleep(7)
#	v.cmd_cam_zoom_wide_speed(CAM,0)
#	sleep(7)
#	v.cmd_cam_zoom_tele_speed(CAM,7)
#	sleep(7)
#	v.cmd_cam_zoom_wide_speed(CAM,7)
#	sleep(7)

	#maximum digital zoom:
#	v.cmd_cam_zoom_direct(CAM,0x7000)
#	sleep(7)
	#maximum optical zoom
#	v.cmd_cam_zoom_direct(CAM,0x4000)
#	sleep(7)
	#no zoom
#	v.cmd_cam_zoom_direct(CAM,0x0)

#	v.cmd_cam_dzoom_off(CAM)
#	v.cmd_cam_zoom_direct(CAM,0x7000)
#	sleep(7)
#	v.cmd_cam_wide_cinema(CAM)
#	sleep(7)
#	v.cmd_cam_wide_full(CAM)
#	sleep(7)
#	v.cmd_cam_wide_off(CAM)
#	sleep(7)

#	v.cmd_cam_lr_reverse_on(CAM)
#	sleep(2)
#	v.cmd_cam_lr_reverse_off(CAM)

#	v.cmd_cam_zoom_direct(CAM,0x7000)
#	sleep(3)
#	v.cmd_cam_freeze_on(CAM)
#	sleep(2)

#	v.cmd_cam_zoom_direct(CAM,0x0)
#	sleep(4)
#	v.cmd_cam_freeze_off(CAM)

#	v.cmd_cam_picture_effect_off(CAM)

#	for i in range(0,9):
#		v.cmd_cam_picture_effect(CAM,i)
#		sleep(3)

#	for i in range(0,5):
#		v.cmd_cam_digital_effect(CAM,i)
#		for level in range(0,0x21):
#			v.cmd_cam_digital_effect_level(CAM,level)
#			sleep(2)

#	v.cmd_ptd_up(CAM)
#	sleep(3)
#	v.cmd_ptd_down(CAM)
#
#	sleep(3)
#
#	v.cmd_ptd_up(CAM,2)
#	sleep(3)
#	v.cmd_ptd_down(CAM,2)
#
#
#	v.cmd_ptd_left(CAM)
#	sleep(3)
#	v.cmd_ptd_right(CAM,2)
#	sleep(3)
#	v.cmd_ptd_right(CAM)
#	sleep(1)
#	v.cmd_ptd_left(CAM)
#	sleep(1)
#	v.cmd_ptd_right(CAM)


#	v.cmd_ptd_upleft(CAM)
#	sleep(2)
#
#	v.cmd_ptd_upright(CAM)
#	sleep(2)
#
#	v.cmd_ptd_downleft(CAM)
#	sleep(2)
#
#	v.cmd_ptd_downright(CAM)
#	sleep(2)
#
#	v.cmd_ptd_home(CAM)
#	sleep(2)
#	v.cmd_ptd_reset(CAM)

	v.cmd_cam_power_off(CAM)

if __name__ == '__main__':
    try:
        main()
    except KeyboardInterrupt:
        pass


