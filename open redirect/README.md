**Method**

```
* Burp Proxy history & Burp Sitemap (look at URLs with parameters)
* Google dorking. E.g: inurl:redirectUrl=http site:target.com
* Functionalities usually associated with redirects:
	Login, Logout, Register & Password reset pages
	Change site language
	Links in emails
* Read JavaScript code
* Bruteforcing
	Look for hidden redirect parameters, for e.g.:
		/redirect?url={payload}&next={payload}&redirect={payload}&redir={payload}&rurl={payload}&redirect_uri={payload}
		/?url={payload}&next={payload}&redirect={payload}&redir={payload}&rurl={payload}&redirect_uri={payload}

* Try using the same parameter twice:
	 ?next=whitelisted.com&next=google.com
* If periods filtered, use an IPv4 address in decimal notation 
	http://www.geektools.com/geektools-cgi/ipconv.cgi
* Try a double-URL and triple-URL encoded version of payloads
* Try redirecting to an IP address (instead of a domain) using different notations: 
	IPv6, IPv4 in decimal, hex or octal
* For XSS, try replacing alert(1) with prompt(1) & confirm(1)
* If extension checked, 
	try ?image_url={payload}/.jpg
* Try target.com/?redirect_url=.uk (or [any_param]=.uk). 
	If it redirects to target.com.uk, then it’s vulnerable! target.com.uk and target.com are different domains.
* Chaining open redirect with
	SSRF
	OAuth token disclosure
	XSS
	CRLF injection

```


**Common Injection Parameters**

```
/{payload}
?next={payload}
?url={payload}
?target={payload}
?rurl={payload}
?dest={payload}
?destination={payload}
?redir={payload}
?redirect_uri={payload}
?redirect_url={payload}
?redirect={payload}
/redirect/{payload}
/cgi-bin/redirect.cgi?{payload}
/out/{payload}
/out?{payload}
?view={payload}
/login?to={payload}
?image_url={payload}
?go={payload}
?return={payload}
?returnTo={payload}
?return_to={payload}
?checkout_url={payload}
?continue={payload}
?return_path={payload}

```