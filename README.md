# subdomain-tool

This is a small tool that allows you to create subdomains from a site. The script uses the cloudflare API to create these records.
This tool will not work with .tk/.ml/.cf/.ga/.gq domains, as they are blocked by cloudflare.
This tool is not safe and may allow people to steal user information, perform Man in the middle attacks, perform scams over these domain or may lead to the loose of the domain.

## running this
to run this, simply download all the files, change the email, zoneid and cloudflare api token in main.py and run main.py. You may need to install the following requirements before:
- flask
- CloudFlare

## helping
Were happy to accept pull requests making this tool better.

## websites using this
- https://s.pichisdns.com

If you want your site listed here, open a Pull requests or file a issue.
