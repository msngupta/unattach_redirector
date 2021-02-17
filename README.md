# unattach_redirector
Redirects the file_name links to a preset base_url

## File linking
* The file names (say abcd.xyz) in the modified emails are linked to https://unattach.appspot.com/get_file/abcd.xyz
* The links redirects to https://domain.xyz/path/abcd.xyz using a preset base_url (say https://domain.xyz/path)
* To set the base_url use the following syntax (https://unattach.appspot.com/set_path?base_path=https://domain.xyz/path/). Bookmark the link for easy access.
* Once the base_url is set using the above link, it is stored in the browser session as a cookie (unattach_base_url)
