import urllib,urllib2,re,os
import xbmcplugin,xbmcgui,xbmcaddon
from BeautifulSoup import BeautifulSoup, BeautifulStoneSoup

__settings__ = xbmcaddon.Addon(id='plugin.audio.twit')
__language__ = __settings__.getLocalizedString
home = __settings__.getAddonInfo('path')
fanart = xbmc.translatePath( os.path.join( home, 'fanart.jpg' ) )


def categories():
        addDir(__language__(30038),'none',7,xbmc.translatePath( os.path.join( home, 'icon.png' ) ))
        addLink(__language__(30000),'http://twit.am/listen',3,xbmc.translatePath( os.path.join( home, 'resources', 'live.png' ) ))
        addDir(__language__(30001),'http://twit.tv/show/this-week-in-tech',1,'http://static.mediafly.com/publisher/images/ba85558acd844c7384921f9f96989a37/icon-600x600.png')
        addDir(__language__(30002),'http://twit.tv/show/tech-news-today',1,'http://static.mediafly.com/publisher/images/c21d95482417436ead61b0890a8fc282/icon-600x600.png')
        addDir(__language__(30003),'http://twit.tv/show/fourcast',1,'http://static.mediafly.com/publisher/images/f7f40bcf20c742cfb55cbccb56c2c68c/icon-600x600.png')
        addDir(__language__(30004),'http://twit.tv/show/ipad-today',1,'http://static.mediafly.com/publisher/images/201bc64beb6b4956971650fd1462a704/icon-600x600.png')
        addDir(__language__(30005),'http://twit.tv/show/all-about-android',1,'http://static.mediafly.com/publisher/images/7874016b2dd3490fa1e8b606dff4d2fa/icon-600x600.png')
        addDir(__language__(30006),'http://twit.tv/show/tech-history-today',1,'http://static.mediafly.com/publisher/images/88fcc18ed4234a2e9f96a13f74afe7b9/icon-600x600.png')
        addDir(__language__(30007),'http://twit.tv/show/this-week-in-google',1,'http://static.mediafly.com/publisher/images/8248233e64fc4c68b722be0ec75d637d/icon-600x600.png')
        addDir(__language__(30008),'http://twit.tv/show/windows-weekly',1,'http://static.mediafly.com/publisher/images/ad659facf4cb4fe795b595d9b4275daf/icon-600x600.png')
        addDir(__language__(30009),'http://twit.tv/show/macbreak-weekly',1,'http://static.mediafly.com/publisher/images/a24b7b336fb14a2ba3f1e31223f622ac/icon-600x600.png')
        addDir(__language__(30010),'http://twit.tv/show/triangulation',1,'http://static.mediafly.com/publisher/images/c60ef74e0a3545e490d7cefbc369d168/icon-600x600.png')
        addDir(__language__(30011),'http://twit.tv/show/twit-photo',1,'http://static.mediafly.com/publisher/images/ca045f623e7d48509c8f4ff9a1ab7259/icon-600x600.png')
        addDir(__language__(30012),'http://twit.tv/show/the-tech-guy',1,'http://static.mediafly.com/publisher/images/d51aaf03dcfe4502a49e885d4201c278/icon-600x600.png')
        addDir(__language__(30013),'http://twit.tv/show/security-now',1,'http://static.mediafly.com/publisher/images/1ac666ad22d940239754fe953207fb42/icon-600x600.png')
        addDir(__language__(30014),'http://twit.tv/show/the-social-hour',1,'http://twit.tv/files/imagecache/coverart/coverart/tsh600.jpg')
        addDir(__language__(30015),'http://twit.tv/show/weekly-daily-giz-wiz',1,'http://static.mediafly.com/publisher/images/72acf86f350b40c5b5fd132dcacc78be/icon-600x600.png')
        addDir(__language__(30016),'http://twit.tv/show/nsfw',1,'http://static.mediafly.com/publisher/images/54f4a471ae6c418d89647968a2ea9c91/icon-600x600.png')
        addDir(__language__(30017),'http://twit.tv/show/dr-kikis-science-hour',1,'http://static.mediafly.com/publisher/images/c9ed18a67b134406a4d5fd357db8b0c9/icon-600x600.png')
        addDir(__language__(30018),'http://twit.tv/show/floss-weekly',1,'http://static.mediafly.com/publisher/images/06cecab60c784f9d9866f5dcb73227c3/icon-600x600.png')
        addDir(__language__(30019),'http://twit.tv/show/this-week-in-law',1,'http://static.mediafly.com/publisher/images/b2911bcc34174461ba970d2e38507340/icon-600x600.png')
        addDir(__language__(30020),'http://twit.tv/show/twit-live-specials',1,'http://static.mediafly.com/publisher/images/eed22d09b9524474ac49bc022b556b2b/icon-600x600.png')
        addDir(__language__(30021),'http://twit.tv/show/home-theater-geeks',1,'http://static.mediafly.com/publisher/images/441a40308195459b8e24f341dc68885c/icon-600x600.png')
        addDir(__language__(30022),'http://twit.tv/show/frame-rate',1,'http://static.mediafly.com/publisher/images/5a081f72180e41939e549ec7d12be24d/icon-600x600.png')
        addDir(__language__(30023),'http://twit.tv/show/this-week-in-computer-hardware',1,'http://static.mediafly.com/publisher/images/f76d60fdd2ea4822adbc50d2027839ce/icon-600x600.png')
        addDir(__language__(30024),'http://twit.tv/show/ham-nation',1,'http://static.mediafly.com/publisher/images/7a948708b1a3462bab8721556dd26704/icon-600x600.png')
        addDir(__language__(30025),'http://twit.tv/show/futures-in-biotech',1,'http://leoville.tv/podcasts/coverart/fib600audio.jpg')
        addDir(__language__(30026),'http://twit.tv/show/this-week-in-radio-tech',1,'http://static.mediafly.com/publisher/images/ab7b2412afa84674971e4c93665d0e06/icon-600x600.png')
        addDir(__language__(30036),'http://twit.tv/show/before-you-buy',1,'http://static.mediafly.com/publisher/images/dee7de4f87034d4d917ed446df3616e4/icon-600x600.png')
        addDir(__language__(30037),'http://twit.tv/show/game-on',1,'http://static.mediafly.com/publisher/images/3f551d9b6ef9476fb76f92ccd4b37826/icon-600x600.png')


def index(url,iconimage):
        headers = {'User-agent' : 'Mozilla/5.0 (Windows NT 6.1; WOW64; rv:6.0) Gecko/20100101 Firefox/6.0'}
        req = urllib2.Request(url,None,headers)
        response = urllib2.urlopen(req)
        link=response.read()
        soup = BeautifulSoup(link, convertEntities=BeautifulSoup.HTML_ENTITIES)
        items = soup.findAll('div', attrs={'class' : 'view-content'})[3]('div', attrs={'class' : 'field-content'})
        for i in items:
            name = i.a.string
            url = i.a['href']
            addLink(name,url,2,iconimage)
        try:
            page = 'http://twit.tv'+soup('li', attrs={'class' : "pager-next"})[0].a['href']
            addDir('Next Page',page,1,iconimage)
        except:
            pass


def getAudio(url):
        headers = {'User-agent' : 'Mozilla/5.0 (Windows NT 6.1; WOW64; rv:6.0) Gecko/20100101 Firefox/6.0'}
        req = urllib2.Request(url,None,headers)
        response = urllib2.urlopen(req)
        link=response.read()
        soup = BeautifulSoup(link, convertEntities=BeautifulSoup.HTML_ENTITIES)
        item = xbmcgui.ListItem(path = soup('a', attrs={'class' : "audio download"})[0]['href'])
        xbmcplugin.setResolvedUrl(int(sys.argv[1]), True, item)


def playLive(url):
        item = xbmcgui.ListItem(path=url)
        xbmcplugin.setResolvedUrl(int(sys.argv[1]), True, item)


def indexTwitFeed():
        headers = {'User-agent' : 'Mozilla/5.0 (Windows NT 6.1; WOW64; rv:6.0) Gecko/20100101 Firefox/6.0'}
        url ='http://twit.tv/node/feed'
        req = urllib2.Request(url,None,headers)
        response = urllib2.urlopen(req)
        link=response.read()
        soup = BeautifulStoneSoup(link, convertEntities=BeautifulStoneSoup.XML_ENTITIES)
        for i in soup('item'):
            title = i.title.string
            # url = i.link
            date = i.pubdate.string.rsplit(' ', 1)[0]
            html = i.description.contents[0]
            episode_name = BeautifulSoup(html, convertEntities=BeautifulSoup.HTML_ENTITIES)('div', attrs={'class' : "field-item odd"})[0].string.replace('  ','').replace('\n','')
            try:
                thumb = re.compile('<img src="(.+?)"').findall(html)[0]
            except:
                thumb = xbmc.translatePath( os.path.join( home, 'icon.png' ) )
            try:
                aud_url = re.compile('<div class="field-label-inline-first">\n              MP3 feed URL:&nbsp;</div>\n                    (.+?)        </div>').findall(html)[0]
                addLink(title+' - '+episode_name, aud_url, 3, thumb)
            except:
                print '--- There was a problem adding episode %s ---' % title


def get_params():
        param=[]
        paramstring=sys.argv[2]
        if len(paramstring)>=2:
            params=sys.argv[2]
            cleanedparams=params.replace('?','')
            if (params[len(params)-1]=='/'):
                params=params[0:len(params)-2]
            pairsofparams=cleanedparams.split('&')
            param={}
            for i in range(len(pairsofparams)):
                splitparams={}
                splitparams=pairsofparams[i].split('=')
                if (len(splitparams))==2:
                    param[splitparams[0]]=splitparams[1]
        return param


def addLink(name,url,mode,iconimage):
        u=sys.argv[0]+"?url="+urllib.quote_plus(url)+"&mode="+str(mode)+"&name="+urllib.quote_plus(name)+"&iconimage="+urllib.quote_plus(iconimage)
        ok=True
        liz=xbmcgui.ListItem(name, iconImage=iconimage, thumbnailImage=iconimage)
        liz.setInfo( type="Audio", infoLabels={ "Title": name} )
        liz.setProperty('IsPlayable', 'true')
        liz.setProperty( "Fanart_Image", fanart )
        ok=xbmcplugin.addDirectoryItem(handle=int(sys.argv[1]),url=u,listitem=liz)
        return ok


def addDir(name,url,mode,iconimage):
        u=sys.argv[0]+"?url="+urllib.quote_plus(url)+"&mode="+str(mode)+"&name="+urllib.quote_plus(name)+"&iconimage="+urllib.quote_plus(iconimage)
        ok=True
        liz=xbmcgui.ListItem(name, iconImage=iconimage, thumbnailImage=iconimage)
        liz.setInfo( type="Audio", infoLabels={ "Title": name } )
        liz.setProperty( "Fanart_Image", fanart )
        ok=xbmcplugin.addDirectoryItem(handle=int(sys.argv[1]),url=u,listitem=liz,isFolder=True)
        return ok


params=get_params()
url=None
name=None
mode=None

try:
    url=urllib.unquote_plus(params["url"])
except:
    pass
try:
    name=urllib.unquote_plus(params["name"])
except:
    pass
try:
    iconimage=urllib.unquote_plus(params["iconimage"])
except:
    pass
try:
    mode=int(params["mode"])
except:
    pass

print "Mode: "+str(mode)
print "URL: "+str(url)
print "Name: "+str(name)

if mode==None or url==None or len(url)<1:
    print ""
    categories()

elif mode==1:
    print ""
    index(url,iconimage)

elif mode==2:
    print ""
    getAudio(url)

elif mode==3:
    print ""
    playLive(url)

elif mode==7:
    print ""
    indexTwitFeed()

xbmcplugin.endOfDirectory(int(sys.argv[1]))