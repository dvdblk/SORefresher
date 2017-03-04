from grab import Grab
import logging

import config


def login():
    g = Grab()
    g.go("stackoverflow.com")
    url = g.tree.xpath('//div[@class="-ctas"]/a/@href')[0]
    g.go(url)

    post_data = g.form_fields()
    post_data.update({
        "email": config.EMAIL,
        "password": config.PASSWORD,
    })

    g.setup(post=post_data)
    g.go(url)

    try:
        g.tree.xpath('//div[@class="-badges"]')[0]
        print("Successfully logged in")
    except:
        print("Login unsuccessful")

if __name__ == "__main__":
    logging.basicConfig(level=logging.DEBUG)
    login()
