#!/usr/bin/env python3
import os,sys
sys.path.append(os.getcwd()+"/.lib/")

import random
import argparse
import requests
from pprint import pprint
from headers import user_agents
from colors import red,green,white,reset


class osintEye:
	def __init__(self,args):
		self.session = requests.session()
		self.session.headers = {"User-Agent": f"{random.choice(user_agents)}"}
		
	def main(self):
		if args.instagram:
			self.instagram()
		elif args.github:
			self.github()
		elif args.dockerhub:
			self.dockerhub()
		elif args.gsearch:
			self.gsearch()
		else:
			self.instagram()
			self.github()
			self.dockerhub()
			
			
	# Getting instagram profile information	
	def instagram(self):
		response = self.session.get(f'https://www.instagram.com/{args.username}/?__a=1')
		if response.status_code == 404:
			exit(f"{white}[{red}x{white}] Instagram: user @{green}{args.username}{red} not found{reset}")
		response = response.json()
		user = response['graphql']['user']
		if args.raw:
			pprint(response['graphql']['user'])
		else:
		    # I personally think these were unnecessary but, why not? lol
		    profile_pic_url = user['profile_pic_url_hd']
		    external_url = user['external_url']
		    # If -sU or --short-urls is passed, all urls in results will be shortened
		    # This same logic will be applied to all results
		    if args.urlshortener:
		    	profile_pic_url = self.urlshortener(user['profile_pic_url_hd'])
		    	external_url = self.urlshortener(user['external_url'])
		    	
		    info = {'Profile photo': profile_pic_url,
		            'Username': user['username'],
		            'User ID': user['id'],
		            'External URL': external_url,
		            'Bio': user['biography'],
		            'Followers': user['edge_followed_by']['count'],
		            'Following': user['edge_follow']['count'],
		            'Pronouns': user['pronouns'],
		            'Images': user['edge_owner_to_timeline_media']['count'],
		            'Videos': user['edge_felix_video_timeline']['count'],
		            'Reels': user['highlight_reel_count'],
		            'Private': user['is_private'],
		            'Is Verified?': user['is_verified'],
		            'Business account': user['is_business_account'],
		            'Professional account': user['is_professional_account'],
		            'Recently joined': user['is_joined_recently'],
		            'Business category': user['business_category_name'],
		            'Category': user['category_enum'],
		            'Has guides?': user['has_guides'],
		    }
		    print(f"\n{white}{user['full_name']} ({green}Instagram{white}){reset}")
		    for key, value in info.items():
		    	print(f"{white}├─ {key}: {green}{value}{reset}")
		    print("\n")
		    	
		    
	
	# Getting github profile information    	
	def github(self):
	    response = self.session.get(f"https://api.github.com/users/{args.username}")
	    if response.status_code == 404:
	    	exit(f"{white}[{red}x{white}] GitHub: user @{green}{args.username}{red} not found{reset} ")
	    response = response.json()
	    if args.raw:
	    	pprint(response)
	    else:
	        avatar_url = response['avatar_url']
	        if args.urlshortener:
	        	avatar_url = self.urlshortener(response['avatar_url'])
	        	
	        info = {'Profile photo': avatar_url,
	                'Username': response['login'],
	                'User ID': response['id'],
	                'Node ID': response['node_id'],
	                'Bio': response['bio'],
	                'Blog': response['blog'],
	                'Location': response['location'],
	                'Followers': response['followers'],
    	            'Following': response['following'],
	                'Twitter handle': response['twitter_username'],
	                'Gists (public)': response['public_gists'],
	                'Repositories (public)': response['public_repos'],
	                'Organization': response['company'],
	                'Is hireable?': response['hireable'],
	                'Is Site admin?': response['site_admin'],
	                'Joined On': response['created_at'],
	                'Last Updated': response['updated_at'],
	        }
	        print(f"\n{white}{response['name']} ({green}Github{white}){reset}")
	        for key,value in info.items():
	            print(f"{white}├─ {key}: {green}{value}{reset}")
	        print("\n")
	        
	        # Followers
	        print(f"\n{white}[{green}*{white}] Fetching @{green}{args.username}{white}' Github followers...{reset}")
	        response = self.session.get(f"https://api.github.com/users/{args.username}/followers?per_page=100").json()
	        if args.raw:
	        	pprint(response)
	        else:
	            for follower in response:
	                avatar_url = follower['avatar_url']
	                profile_url = follower['html_url']
	                if args.urlshortener:
	                	avatar_url = self.urlshortener(follower['avatar_url'])
	                	profile_url = self.urlshortener(follower['html_url'])
	                	
	                results = {'ID': follower['id'],
   	                         'Node ID': follower['node_id'],
   	                         'Profile photo': avatar_url,
   	                         'Gravatar ID': follower['gravatar_id'],
   	                         'Account type': follower['type'],
   	                         'Profile': profile_url,
   	                         'Is Site admin?': follower['site_admin'],
	                }
	                print(f"\n{white}{follower['login']}{reset}")
	                for key,value in results.items():
	                	print(f"{white}├─ {key}: {green}{value}{reset}")
	                print("\n")
	            
	        # Repositories
	        print(f"\n{white}[{green}*{white}] Fetching @{green}{args.username}{white}' Github repositories...{reset}")
	        response = self.session.get(f"https://api.github.com/users/{args.username}/repos?per_page=100").json()
	        if args.raw:
	        	pprint(response)
	        else:
	            for repo in response:
	            	license = repo['license']
	            	if license is not None:
	            		license = repo['license']['name']
	            		repo_info = {'ID': repo['id'],
	            		             'Private': repo['private'],
	            		             'Forks': repo['forks'],
	            		             'Stars': repo['stargazers_count'],
	            		             'Watchers': repo['watchers'],
	            		             'License': license,
	            		             'Branch': repo['default_branch'],
	            		             'Visibility': repo['visibility'],
	            		             'Language': repo['language'],
	            		             'About': repo['description'],
	            		             'Open issues': repo['open_issues'],
	            		             'Topics': repo['topics'],
	            		             'Archived': repo['archived'],
	            		             'Homepage': repo['homepage'],
	            		             'Created at': repo['created_at'],
	            		             'Updated at': repo['updated_at'],
	            		             'Pushed at': repo['pushed_at'],
	            		             'Clone url': repo['clone_url'],
	            		             'SSH url': repo['ssh_url'],
	            		}
	            		print(f"\n{white}{repo['full_name']}{reset}")
	            		for key,value in repo_info.items():
	            		    print(f"{white}├─ {key}: {green}{value}{reset}")
	            		print(f"{white}-{reset}"*100)
	                
	                
	# Search users on Github                
	def gsearch(self):
	    response = self.session.get(f"https://api.github.com/search/users?q={args.username}&per_page=100").json()
	    if args.raw:
	        pprint(response)
	    else:
	        for data in response['items']:
	            avatar_url = data['avatar_url']
	            profile_url = data['html_url']
	            if args.urlshortener:
	            	avatar_url = self.urlshortener(data['avatar_url'])
	            	profile_url = self.urlshortener(data['html_url'])
	            results = {'ID': data['id'],
	                       'Node ID': data['node_id'],
	                       'Profile photo': avatar_url,
	                       'Gravatar ID': data['gravatar_id'],
	                       'Account type': data['type'],
	                       'Profile': profile_url,
	                       'Is Site admin?': data['site_admin'],
	                       'Score': data['score'],
	            }
	            print(f"\n{white}{data['login']}{reset}")
	            for key,value in results.items():
	                print(f"{white}├─ {key}: {green}{value}{reset}")
	            print(f"{white}={reset}"*100)
	            
	                
	# Getting user's DockerHub profile information'              
	def dockerhub(self):
	    response = self.session.get(f"https://hub.docker.com/v2/users/{args.username}")
	    if response.status_code == 404:
	    	exit(f"{white}[{red}x{white}] DockerHub: user @{green}{args.username}{red} not found{reset} ")
	    response = response.json()
	    if args.raw:
	        pprint(response)
	    else:
	        profile_url = response['profile_url']
	        gravatar_url = response['gravatar_url']
	        if args.urlshortener:
	        	profile_url = self.urlshortener(response['profile_url'])
	        	gravatar_url = self.urlshortener(response['gravatar_url'])
	        	
	        data = {'ID': response['id'],
	                'Profile': profile_url,
	                'Gravatar': gravatar_url,
	                'Username': response['username'],
	                'Location': response['location'],
	                'Account type': response['type'],
	                'Organization': response['company'],
	                'Joined on': response['date_joined'],
	        }
	        print(f"\n{white}{response['full_name']} ({green}DockerHub{white}){reset}")
	        for key,value in data.items():
	            print(f"{white}├─ {key}: {green}{value}{reset}")
	        print(f"{white}={reset}"*100)	        
	    
	# Shorten url
	def urlshortener(self,url):
	    response = requests.get(f"http://tinyurl.com/api-create.php?url={url}")
	    return response.text                    
	
	                                                          
	               	   
parser = argparse.ArgumentParser(description=f"{white}osint{red}Eye{white}: is a user {green}reconaissance{white} tool user that extracts a target's information from {green}GitHub{white}, {green}Instagram{white} and {green}DockerHub{white}.  developed by {green}Richard Mwewa {white}| https://github.com/{green}rlyonheart{reset}")
parser.add_argument("username",help=f"{white}[{green}REQUIRED{white}] target username{reset}")
parser.add_argument("-sU","--shorten-urls",dest="urlshortener",help=f"{white}[{green}OPTIONAL{white}] if passed, all urls in results will be shortened{reset}",action="store_true")
parser.add_argument("-I","--instagram",dest="instagram",help=f"{white}[{green}OPTIONAL{white}] get target's Instagram information{reset}",action="store_true")
parser.add_argument("-G","--github",dest="github",help=f"{white}[{green}OPTIONAL{white}] get target's GitHub information{reset}",action="store_true")
parser.add_argument("-D", "--dockerhub",dest="dockerhub",help=f"{white}[{green}OPTIONAL{white}] get target's DockerHub information{reset}",action="store_true")
parser.add_argument("-sG", "--github-search", dest="gsearch",help=f"{white}[{green}OPTIONAL{white}] search a username on github and get related results{reset} ", action="store_true")
parser.add_argument("-r","--raw",dest="raw",help=f"{white}[{green}OPTIONAL{white}] return output in raw {green}json{white} format{reset}",action="store_true")
parser.add_argument("-v", "--verbose", help=f"{white}[{green}RECOMMENDED{white}] run osint{red}Eye{white} in verbose mode{reset}", dest="verbose", action="store_true")
args = parser.parse_args()
