#!/usr/bin/env python3

__author__	= 'Adrian Sanabria-Diaz'
__license__	= 'MIT'
__version__	= '0.0.1'
__maintainer__	= 'Adrian Sanabria-Diaz'
__status__	= 'Development'

import os

def get_operating_system():
    opsys = os.system('ls /usr/share/xsessions/')
    return opsys

def run_update():
	updates = [
	'update',
	'upgrade'
		]
	
	for update in updates:
		os.system('sudo apt ' + update)

def install_programs():
	programs = [
		'htop',
		'openssh-server',
		'openssh-client',
		'sl',
		'synaptic',
		'filezilla',
		'net-tools',
		'nmap',
		'cmatrix',
		'cowsay',
		'fortune',
		'aview',
		'aafire',
		'bb',
		'rig'
		]
	
	for program in programs:
		os.system('sudo apt install ' + program)

def configure_programs():
	print('Configuring...')

get_operating_system()
run_update()
install_programs()
configure_programs()
