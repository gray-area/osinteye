#!/usr/bin/env python3

import logging
import argparse
import requests
from datetime import datetime
from lib.colors import red,green,white,reset
from plugins import pypi,testpypi,about_me,instagram,github,dockerhub


class osintEye:
	def __init__(self,args):
		self.session = requests.session()
		self.session.headers = {'User-Agent': 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_7) AppleWebKit/605.1.15 (KHTML, like Gecko) Version/14.1.1 Safari/605.1.15'}
		
		if args.about:
			self.url = f'https://about.me/{args.username}'
		elif args.instagram:
			self.url = f'https://www.instagram.com/{args.username}/?__a=1'
		elif args.github:
			self.url = f'https://api.github.com/users/{args.username}'
		elif args.dockerhub:
			self.url = f'https://hub.docker.com/v2/users/{args.username}'
		elif args.pypi:
			self.url = f'https://pypi.org/user/{args.username}'
		elif args.testpypi:
			self.url = f'https://test.pypi.org/user/{args.username}'
		elif args.twitter:
			self.url = f'https://www.twitter.com/{args.username}'
		elif args.facebook:
			self.url = f'https://www.facebook.com/{args.username}'
		elif args.linkedin:
			self.url = f'https://www.linkedin.com/{args.username}'

	def main(self):
		if args.about:
			about_me.about_me(self)
		elif args.instagram:
			instagram.instagram(self)
		elif args.github:
			github.github(self,args)
		elif args.dockerhub:
			dockerhub.dockerhub(self)
		elif args.pypi:
			pypi.pypi(self,args)
		elif args.testpypi:
			testpypi.testpypi(self,args)
		elif args.twitter:
			twitter.twitter(self,args)
		elif args.facebook:
			facebook.facebook(self,args)
		elif args.linkedin:
			facebook.linkedin(self,args)
		else:
		    exit(f'{white}osint{red}eye{white}: use {green}-h{white} or {green}--help{white} to show usage.{reset}')
	                                                          

parser = argparse.ArgumentParser(description=f'{white}osinteye — by Richard Mwewa | https://about.me/rly0nheart{reset}',epilog=f'{white}osint{red}eye{white}  is a username enumeration & reconnaisance suite that extracts a target\'s information as it appears online.{reset}')
parser.add_argument('username',help=f'target username')
parser.add_argument('--pypi',help='search on pypi',action='store_true')
parser.add_argument('--testpypi',help='search on testpypi',action='store_true')
parser.add_argument('--about',help='search on about.me',action='store_true')
parser.add_argument('--github',help='search on github',action='store_true')
parser.add_argument('--instagram',help='search on instagram',action='store_true')
parser.add_argument('--dockerhub',help='search on dockerhub',action='store_true')
parser.add_argument('--twitter',help='search on twitter',action='store_true')
parser.add_argument('--facebook',help='search on facebook',action='store_true')
parser.add_argument('--linkedin',help='search on linkedin',action='store_true')
parser.add_argument('-v', '--verbose', help='enable verbosity',action='store_true')
parser.add_argument('--version',version=f'v1.3.0 Released on 21st March 2022',action='version')
args = parser.parse_args()
start_time = datetime.now()
if args.verbose:
    logging.basicConfig(format=f"{white}[{green}*{white}] %(message)s{reset}",level=logging.DEBUG)
