# Creepy
Dead simple web crawler for Python

There are already a lot of web crawlers for Python, such as Scrapy. Creepy is
yet another web crawler for Python, which ains to provide a simple and light way
to write web crawlers.

## Example usage
    from creepy import Crawler

    class MyCrawler(Crawler):
        def process_document(self, doc):
            if doc.status == 200:
                print '[%d] %s' % (doc.status, doc.url)
    	    # Do something with doc.text (the content of the page)
    	else:
    	    pass
    
    crawler = MyCrawler()
    crawler.set_follow_mode(Crawler.F_SAME_HOST)
    crawler.add_url_filter('\.(jpg|jpeg|gif|png|js|css|swf)$')
    crawler.crawl('http://www.example.com/')

## Installation
1. Install from PyPI:  
`pip install creepy`
2. Arch Linux users can find it on AUR or using [Yaourt](https://wiki.archlinux.org/index.php/Yaourt):  
`yaourt -S python2-creepy-git`

## Bugs
* Please report bugs to the github issure tracker.

## Contributing
1. Fork it
2. Create your feature branch (git checkout -b my-new-feature)
3. Commit your changes (git commit -am 'Add some feature')
4. Push to the branch (git push origin my-new-feature)
5. Create new Pull Request
