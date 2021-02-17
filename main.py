from flask import Flask, make_response, request, redirect
import urllib.parse
import validators

app = Flask(__name__)


@app.route('/', defaults={'path': ''})
@app.route('/<path:path>')
def main_redirect(path):
    return redirect("https://github.com/msngupta/unattach_redirector")

@app.route('/get_file/<filename>')
def get_file(filename):
    if 'unattach_base_path' in request.cookies:
            base_url = request.cookies['unattach_base_path']
            return redirect(urllib.parse.urljoin(base_url, filename))
    else:
        p_url = urllib.parse.urlparse(request.url)
        eg_url = p_url.scheme+"://"+p_url.netloc
        eg_url += "/set_path?=https://domain.xyz/path/"
        return "Base path not found.<br/>Set using this syntax " + eg_url


@app.route('/set_path')
def set_path():
    base_path = str(request.args.get("base_path"))
    if not validators.url(base_path):
        eg_url = "https://domain.xyz/path/"
        return "Invalid base_path, use the following syntax <br> " + eg_url 
    resp = make_response('Base redirection path cookie set to '+base_path)
    resp.set_cookie('unattach_base_path',base_path)
    return resp


if __name__ == '__main__':
    app.run(host='127.0.0.1', port=8080, debug=True)
