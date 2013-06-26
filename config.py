#---coding:UTF-8--

# log root path /data/boyu/token_issue/logs/
log_root_path = "/data/boyu/token_issue/logs/"

# log  names
log_names = ["178.log", "179.log"]
# token types, 0 sclient_credentials, 1 authorization_code, 2 refresh_token, 3 password ,4 client_side
# you can add some value when you have new oauth
token_types = {0: 'client_credentials(仅应用信息的授权)', 1: 'authorization_code(通过code换取token)',
               2: 'refresh_token(token过期后刷新)', 3: 'password(用户名密码方式)', 4: 'client_side(直接获取token)'}
# email receiver, you can edit this
email_receiver = ["example@xxx.com"]

# subject of email
subject = '授权日活跃统计'
