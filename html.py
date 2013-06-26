#---coding:UTF-8--
# get html head


def get_html_head():
    message = "<!DOCTYPE html PUBLIC \"-//W3C//DTD XHTML 1.0 Transitional//EN\" \"http://www.w3.org/TR/xhtml1/DTD/xhtml1-transitional.dtd\">"
    message += "<html xmlns=\"http://www.w3.org/1999/xhtml\">"
    message += "<head>"
    message += "<meta http-equiv=\"Content-Type\" content=\"text/html; charset=utf-8\" />"
    message += "<title>token issue</title><body>"
    return message

# get end html


def get_end_html():
    return "</body>\n</html>"

# get table head


def get_talbe_head(width, border, args):
    head = "<table width=\"" + width + \
        "\" border=\"" + border + "\" align=\"center\">\n"
    head += "<tr>\n"
    for arg in args:
        head += "<td align=\"center\">" + arg + "</td>"
    head += "</tr>"
    return head

# get table end


def get_talbe_end():
    return "</table>"

# get tr head


def get_tr_head():
    return "<tr>"

# get tr end


def get_tr_end():
    return "</tr>"

# get td head


def get_td_whit_rowspan(rowspan, value):
    return "<td rowspan=\"" + rowspan + "\">" + value + "</td>\n"

# get td head


def get_td(value):
    return "<td>" + value + "</td>\n"


# call main function
if __name__ == '__main__':
    print get_talbe_head('1200', '1', ['AppId', 'UserCount', 'TokenType', 'OauthCount'])
