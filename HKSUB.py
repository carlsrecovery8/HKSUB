#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
------------------------------------------------------------------------------
	HKSUB - 04.03.18.02.10.00 - M7-HKGATO (UMBRELLA)
------------------------------------------------------------------------------
"""

## # LIBRARIES # ##
import re
import requests

## # CONTEXT VARIABLES # ##
version = 1.2

## # MAIN FUNCTIONS # ##

def parse_args():
	import argparse
	parser = argparse.ArgumentParser()
	parser.add_argument('-d', '--domain', type=str, required=True, help="Target domain.")
	parser.add_argument('-o', '--output', type=str, help="Output file.")
	return parser.parse_args()

def banner():
	global version
	b = '''    ...''''........''''..."|pv -qL 700
               ..''....                ...'''.."|pv -qL 700
            .',...       ..   ..   ..       ...,'."|pv -qL 700
          ',...      .                  .       ..;'"|pv -qL 700
        ',...    .    ...................   ..    ..;'"|pv -qL 700
      ';..  ..    ...........................   ..  ..;'"|pv -qL 700
     ;..       .......' ...'..'..'.............       .';"|pv -qL 700
   .;..  ..  .........'.''..........'''..........  ..  ..:."|pv -qL 700
  .;..     ..'......''...  .          ..''.........     ..:."|pv -qL 700
:..  .  ........''...;;c,        'c:;....''.....'.  .. ..:"|pv -qL 700
;..     .......''. .ldck.   ..     .xlx:, ..'.....'.     ..;"|pv -qL 700
.;.  .. ..' ...''. 'lx0dx ;dkO0kl.   odkod'  .'.....'.  .  .;."|pv -qL 700
,..     .'.. .''.  :x0Ok0'    xXK.   kkOOdx   .'... '..    ..;"|pv -qL 700
;.. .. ..' ...,.   ;KOKKKXk:;cNWNO;cOXNXKXd   .'.....'.  .  .:"|pv -qL 700
;..    .......'.    oNWMMMMMWOkxOXMMMMMMWO.   ..'....'.     .:"|pv -qL 700
;..    .......'.     .xNMMMM0kocOkMMMMNO;     ..'....'.     .:"|pv -qL 700
;.. .. ... ...,.        ...':kOOk;'....       .''....'.  .  .:"|pv -qL 700
,..     .' ...''.           .O00O             .'... '..    ..,"|pv -qL 700
.;.  .. ... ...''.          .oxx;            .,.....'.  .  .;."|pv -qL 700
 ;..     .......''.          .::.          ..'.....'.     ..;"|pv -qL 700
  :..  .  ........''.         '          ..'.' ...'.  .. ..:"|pv -qL 700
  .:..     ..'......''..              ..''.'.......     ..:."|pv -qL 700
   .:..  ..  ..........'''..........''''.' ......   .  ..:"|pv -qL 700
     ,'.       .............'..'.'..' .........       .';"|pv -qL 700
      .;..  ..    ....... ...................   ..  ..:."|pv -qL 700
        ';..     .   ....................    .    ..;'"|pv -qL 700
          .,'.       .                  .       .';."|pv -qL 700
            .','..   .   ..   ..   ..       ..','."|pv -qL 700
                .'''...                ...'''."|pv -qL 700
                    ...''''''''''''''''..."|pv -qL 700
	'''.format(v=version)
	print(b)
	
def clear_url(target):
	return re.sub('.*www\.','',target,1).split('/')[0].strip()

def save_subdomains(subdomain,output_file):
	with open(output_file,"a") as f:
		f.write(subdomain + '\n')
		f.close()

def main():
	banner()
	args = parse_args()

	subdomains = []
	target = clear_url(args.domain)
	output = args.output

	req = requests.get("https://crt.sh/?q=%.{d}&output=json".format(d=target))

	if req.status_code != 200:
		print("[X] Information not available!") 
		exit(1)

	for (key,value) in enumerate(req.json()):
		subdomains.append(value['name_value'])

	
	print("\n[!] ---- TARGET: {d} ---- [!] \n".format(d=target))

	subdomains = sorted(set(subdomains))

	for subdomain in subdomains:
		print("[-]  {s}".format(s=subdomain))
		if output is not None:
			save_subdomains(subdomain,output)

	print("\n\n[!]  Done. Have a nice day! ;).")


main()
	
