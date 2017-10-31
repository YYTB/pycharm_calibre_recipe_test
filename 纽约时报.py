# coding=utf-8
from BeautifulSoup import BeautifulSoup
import datetime, re  # 导入日期时间模块，各版面的url根据发行日期改变。

html = '''

<!DOCTYPE html>
<html lang="zh">
    <head>
        <meta charset="utf-8">
<meta http-equiv="X-UA-Compatible" content="IE=edge,chrome=1">
<meta name="keywords" content="">
<meta name="description" content="">
<meta name="lang" property="lang" content="zh-hans">
<meta name="apple-itunes-app" content="app-id=807498298, app-argument=nytimescn://section:business">

<link rel="apple-touch-icon-precomposed" sizes="144×144" href="//static01.nyt.com/images/icons/ios-ipad-144x144.png" />
<link rel="apple-touch-icon-precomposed" sizes="114×114" href="//static01.nyt.com/images/icons/ios-iphone-114x144.png" />
<link rel="apple-touch-icon-precomposed" href="//static01.nyt.com/images/icons/ios-default-homescreen-57x57.png" />

<meta id="WT.cg_n" name="WT.cg_n" content="business">
<meta id="WT.z_gpt" name="WT.z_gpt" content="Section Front">
<meta id="WT.LANG" name="WT.LANG" content="zh-hans">
<meta id="WT.z_rmid" name="WT.z_rmid" content="007f010057f459f863f90017">
<script type="text/javascript">
 var sso_email_sub = "";
 var js_static_path = "//d3q1qj9jzsu8nw.cloudfront.net/js";
 var imgs_static_path = "//d1f1eryiqyjs0r.cloudfront.net/style/imgs";
 var style_static_path = "//d1f1eryiqyjs0r.cloudfront.net/style";
 var jsonp_path = "//d3lar09xbwlsge.cloudfront.net";
 var hot_stories_path = "/async/mostviewed/all/?lang=zh-hans";

</script>


<meta property="og:title" content="商业与经济 - 纽约时报中文网 国际纵览" />
<meta property="og:type" content="website" />
<meta property="og:url" content="https://cn.nytimes.com/" />
<meta property="og:image" content="//static01.nyt.com/images/icons/t_logo_291_black.png" />
<meta property="og:description" content="">
<meta property="og:site_name" content="纽约时报中文网 国际纵览">

<meta property="fb:pages" content="1504603339831430">


<meta name="PT" content="Section Front">
<meta name="PST" content="News">
<meta name="CG" content="business">
<meta name="SCG" content="">
<meta name="sourceApp" content="nyt-china-web">

<link rel="alternate" href="https://cn.nytimes.com/business/" hreflang="zh-Hans-CN" />
<link rel="alternate" href="https://cn.nytimes.com/business/zh-hant/" hreflang="zh-Hant-TW" />

<title>商业与经济 - 纽约时报中文网 国际纵览</title>
<link href="/css/section.css?v=ac6822c" rel="stylesheet"/>
<link href="//d1f1eryiqyjs0r.cloudfront.net/style/css/slideshow/slideshow.min.css?v=ac6822c" rel="stylesheet"/>
<script type="text/javascript">
 var adConfList = [], target = {"edn": "cn","typ": "sf","plat": "web","lan": "chi","sub": "anon","prop": "cnnyt"};
 adConfList.push( { "index": 0,"size": [[728,90],[970,250],[970,90]],"namespace": "29390238/cnnyt/business","id": "nytcn-gpt-ad-TopAd-0","pos": "" } );
 adConfList.push( { "index": 1,"size": [[300,250],[300,600]],"namespace": "29390238/cnnyt/business","id": "nytcn-gpt-ad-MiddleRight-1","pos": "" } );
 adConfList.push( { "index": 2,"size": [[300,250]],"namespace": "29390238/cnnyt/business","id": "nytcn-gpt-ad-Box1-2","pos": "mktg" } );
</script>

<script>
 var dfpNameSpace = "29390238/cnnyt";
</script>


<script data-main="/js/section"> window.js_version="ac6822c"; var require = { urlArgs : "v="+'ac6822c' }; </script>
<script data-main="/js/section" src="/js/vendor/require-jquery.js?v=ac6822c"></script>

<link rel="shortcut icon" type="image/x-icon" href="/favicon.ico">
<link rel="alternate" type="application/rss+xml" title="纽约时报中文网 国际纵览" href="https://cn.nytimes.com/rss.html"/>

<script>

  (function(i,s,o,g,r,a,m){i['GoogleAnalyticsObject']=r;i[r]=i[r]||function(){
  (i[r].q=i[r].q||[]).push(arguments)},i[r].l=1*new Date();a=s.createElement(o),
  m=s.getElementsByTagName(o)[0];a.async=1;a.src=g;m.parentNode.insertBefore(a,m)
  })(window,document,'script','//www.google-analytics.com/analytics.js','ga');

  ga('create', 'UA-31857435-1', 'auto', {'allowLinker': true});
  ga('require', 'linkid');
  ga('require', 'linker');
  ga('linker:autoLink', ['nytimes.com', 'nytstyle.com', 'cloudfront.net', 'sxzhchina.com', 'cnsxzh.com'] );
  ga('send', 'pageview');

</script>

<script>
!function(f,b,e,v,n,t,s){if(f.fbq)return;n=f.fbq=function(){n.callMethod?
n.callMethod.apply(n,arguments):n.queue.push(arguments)};if(!f._fbq)f._fbq=n;
n.push=n;n.loaded=!0;n.version='2.0';n.queue=[];t=b.createElement(e);t.async=!0;
t.src=v;s=b.getElementsByTagName(e)[0];s.parentNode.insertBefore(t,s)}(window,
document,'script','https://connect.facebook.net/en_US/fbevents.js');

 fbq('init', '592202027582499');
fbq('track', "PageView");</script>
<noscript><img height="1" width="1" style="display:none"
src="https://www.facebook.com/tr?id=592202027582499&ev=PageView&noscript=1"
/></noscript>

<script  type="text/javascript">
 (function ()
     {
         var js = document.createElement('script');
         js.src = '//gwiqcdn.globalwebindex.net/gwiq/gwiq.js';
         js.type = 'text/javascript';
         js.async = 'true';
         js.onload = js.onreadystatechange = function ()
         {
             var rs = this.readyState;
             if (rs && rs != 'complete' && rs != 'loaded') return;
             try
             {
                 gwiq.asyncjs("cid=c0297&site=cn");

             } catch (e) { }
         };
         var s = document.getElementsByTagName('script')[0];
         s.parentNode.insertBefore(js, s);
     })();
</script>

<script type="text/javascript">
    var langkey = document.cookie.match(/langkey=([a-zA-Z\-]*);?/) ? document.cookie.match(/langkey=([a-zA-Z\-]*);?/)[1] : '';
    if(langkey != '') {
        var newhref = document.location.href.replace('zh-hans/', '').replace('zh-hant/', '');
        var url = query_string = anchor = '';
        var links_arr = newhref.split('#');

        if(links_arr.length > 1) anchor = links_arr[1];
        links_arr = links_arr[0].split('?');
        url = links_arr[0];
        if(links_arr.length > 1) query_string = links_arr[1];

        newhref = url;
        if(newhref[newhref.length - 1]  != '/') newhref += '/';
        if(langkey == 'zh-hant') newhref += 'zh-hant/';
        if(query_string != '') newhref += '?' + query_string;
        if(anchor != '') newhref += '#' + anchor;

        if(document.location.href != newhref && newhref.indexOf('en-us') == -1 && newhref.indexOf('dual') == -1) document.location.href = newhref;
    }
</script>

<!-- Google Tag Manager -->
<script>(function(w,d,s,l,i){w[l]=w[l]||[];w[l].push({'gtm.start': new Date().getTime(),event:'gtm.js'});var f=d.getElementsByTagName(s)[0], j=d.createElement(s),dl=l!='dataLayer'?'&l='+l:'';j.async=true;j.src= 'https://www.googletagmanager.com/gtm.js?id='+i+dl;f.parentNode.insertBefore(j,f); })(window,document,'script','dataLayer','GTM-KTDZV8V'); </script>
<!-- End Google Tag Manager -->

<!-- chartbeat -->
<script type='text/javascript'>var _sf_startpt=(new Date()).getTime()</script>
<!-- /chartbeat -->

        <!-- taboola -->
<script type="text/javascript">
    window._taboola = window._taboola || [];
    _taboola.push({article:'auto'});
    !function (e, f, u) {
    e.async = 1;
    e.src = u;
    f.parentNode.insertBefore(e, f);
    }(document.createElement('script'),
    document.getElementsByTagName('script')[0],
    '//cdn.taboola.com/libtrc/nytimeschina/loader.js');
</script>
<!-- /taboola -->


	  <link href="/css/section_lib/basic_section_private.css" rel="stylesheet" />
	  <script src="/js/pagemain/viewmore_v1_main.js"></script>
    </head>
    <body class="alternativePage">
        <div id="topTool">
            <div class="localeTool">
  <a rel="nofollow" class="on" href="https://cn.nytimes.com/tools/r.html?url=/business/&langkey=zh-hans">简体</a> |
  <a rel="nofollow" class="" href="https://cn.nytimes.com/tools/r.html?url=/business/zh-hant/&langkey=zh-hant">繁體</a> 
</div>

        </div>
        <div id="page">
			<div id="user_info" class="user-info" >
    <a href="/apps" target="_blank">移动应用 • Apps</a>
    <span styl="padding: 0 5px;" > | </span>
    <a href="https://sso.nytcn.me/email/?source=top-right" target="_blank">订阅新闻电邮</a>
</div>

            <div class="cf" id="alternativeHeader">
				
				
                <a href="/" title="纽约时报中文网 国际纵览" class="nyt-logo-small">
<svg width="310" height="25" role="img" aria-label="The New York Times">
<image width="310" height="25" xmlns:xlink="http://www.w3.org/1999/xlink" xlink:href="/img/nameplate-s.svg" src="/img/nameplate-s@2x.png" alt="The New York Times" border="0"></image>
</svg>
</a>

				<h2 class="business ">商业与经济</h2>
                <div class="searchBox"> 
<form class="searchForm" name="searchBox" action="/search" method="GET">
<input type="text" name="query" class="searchQuery" placeholder="搜索纽约时报"/>
<input type="submit" class="searchSubmit" value="搜索"/>
</form>
</div>

            </div>
            <div class="cf no-content" id="nav">
  <ul class="navList">
      <li class="mainSection ">
        <a  href="/">首页</a>
		<div class="noLine"></div>
      </li>
      <li class="mainSection  drop">
        <a  href="/world/">国际</a>
		<div class="noLine"></div>
        <ul>
          <li class=""> <a href="/asia-pacific/">亚太</a> </li>
          <li class=""> <a href="/south-asia/">南亚</a> </li>
          <li class=""> <a href="/usa/">美国</a> </li>
          <li class=""> <a href="/americas/">美洲</a> </li>
          <li class=""> <a href="/europe/">欧洲</a> </li>
          <li class=""> <a href="/mideast/">中东</a> </li>
          <li class=""> <a href="/africa/">非洲</a> </li>
        </ul>
      </li>
      <li class="mainSection  drop">
        <a  href="/china/">中国</a>
		<div class="noLine"></div>
        <ul>
          <li class=""> <a href="/two-meetings/">两会报道</a> </li>
          <li class=""> <a href="/policy/">时政</a> </li>
          <li class=""> <a href="/china-ec/">经济</a> </li>
          <li class=""> <a href="/society/">社会</a> </li>
          <li class=""> <a href="/foreign-relations/">中外关系</a> </li>
          <li class=""> <a href="/hk-taiwan/">港澳台</a> </li>
        </ul>
      </li>
      <li class="mainSection on drop">
        <a  href="/business/">商业与经济</a>
		<div class="noLine"></div>
        <ul>
          <li class=""> <a href="/global-ec/">全球经济</a> </li>
          <li class=""> <a href="/global-biz/">全球商业</a> </li>
          <li class=""> <a href="/china-ec/">中国经济</a> </li>
          <li class=""> <a href="/china-biz/">中国商业</a> </li>
          <li class=""> <a href="/dealbook/">交易录</a> </li>
        </ul>
      </li>
      <li class="mainSection  drop">
        <a  href="/lens/">镜头</a>
		<div class="noLine"></div>
        <ul>
          <li class=""> <a href="/lens/">新闻</a> </li>
          <li class=""> <a href="//cn.nytstyle.com/lens/">生活</a> </li>
        </ul>
      </li>
      <li class="mainSection  drop">
        <a  href="//cn.nytstyle.com/technology/">科技</a>
		<div class="noLine"></div>
        <ul>
          <li class=""> <a href="//cn.nytstyle.com/bits/">科技公司</a> </li>
          <li class=""> <a href="//cn.nytstyle.com/entrepreneurs/">创业</a> </li>
          <li class=""> <a href="//cn.nytstyle.com/personal-tech/">科技与你</a> </li>
        </ul>
      </li>
      <li class="mainSection  drop">
        <a  href="//cn.nytstyle.com/education/">教育与职场</a>
		<div class="noLine"></div>
        <ul>
          <li class=""> <a href="//cn.nytstyle.com/basic-ed/">教育</a> </li>
          <li class=""> <a href="//cn.nytstyle.com/career/">职场</a> </li>
        </ul>
      </li>
      <li class="mainSection  drop">
        <a  href="//cn.nytstyle.com/culture/">文化</a>
		<div class="noLine"></div>
        <ul>
          <li class=""> <a href="//cn.nytstyle.com/books/">阅读</a> </li>
          <li class=""> <a href="//cn.nytstyle.com/art/">艺术</a> </li>
          <li class=""> <a href="//cn.nytstyle.com/film-tv/">电影与电视</a> </li>
          <li class=""> <a href="//cn.nytstyle.com/sports/">体育</a> </li>
        </ul>
      </li>
      <li class="mainSection  drop">
        <a  href="//cn.nytstyle.com/style/">风尚</a>
		<div class="noLine"></div>
        <ul>
          <li class=""> <a href="//cn.nytstyle.com/fashion/">时尚</a> </li>
          <li class=""> <a href="//cn.nytstyle.com/food-wine/">美食与美酒</a> </li>
          <li class=""> <a href="//cn.nytstyle.com/living/">生活方式</a> </li>
        </ul>
      </li>
      <li class="mainSection  drop">
        <a  href="//cn.nytstyle.com/health/">健康</a>
		<div class="noLine"></div>
        <ul>
          <li class=""> <a href="//cn.nytstyle.com/well/">个人健康</a> </li>
          <li class=""> <a href="//cn.nytstyle.com/health-research/">新知</a> </li>
        </ul>
      </li>
      <li class="mainSection ">
        <a  href="//cn.nytstyle.com/travel/">旅游</a>
		<div class="noLine"></div>
      </li>
      <li class="mainSection ">
        <a  href="//cn.nytstyle.com/real-estate/">房地产</a>
		<div class="noLine"></div>
      </li>
      <li class="mainSection  drop">
        <a  href="/opinion/">观点与评论</a>
		<div class="noLine"></div>
        <ul>
          <li class=""> <a href="/op-column/">专栏作者</a> </li>
          <li class=""> <a href="/op-ed/">观点</a> </li>
          <li class=""> <a href="/cartoon/">漫画</a> </li>
          <li class=""> <a href="/letters/">读者来信</a> </li>
        </ul>
      </li>
      <li class="mainSection topicnav">
        <a  href="//cn.nytimes.com/topic/20160427/pulitzers-topic/?utm_source=news&utm_medium=nav&utm_campaign=nav-topic-nyt-pulitzer-prize">时报普利策获奖作品</a>
		<div class="noLine"></div>
      </li>
  </ul>
  <ul class="subNavList">
	  <li class=""> <a href="/global-ec/">全球经济</a> </li>
	  <li class=""> <a href="/global-biz/">全球商业</a> </li>
	  <li class=""> <a href="/china-ec/">中国经济</a> </li>
	  <li class=""> <a href="/china-biz/">中国商业</a> </li>
	  <li class=""> <a href="/dealbook/">交易录</a> </li>
  </ul>
</div>

			<div id='nytcn-gpt-ad-TopAd-0' class="ad ad-dfp ad-TopAd dfp_ad_container">
</div>

            <div class="cf" id="sectionWrapper">
                <div class="cf layoutAB">
                    <div id="sectionLeadPackage"><div class="collection-list  first last ">
                        <div class="collection-item  first last ">
                            
<h3 class="sectionLeadHeader"><a target="_blank" href="/business/20171031/xi-jinping-american-executives/" title="习近平会见中美商业领袖，重申深化改革承诺">习近平会见中美商业领袖，重申深化改革承诺</a></h3>
<h6 class="byline">孟宝勒, 储百亮 <span class="time">12:29</span></h6>
<div class="photoWrapper ">
	<a href="/business/20171031/xi-jinping-american-executives/" title="习近平会见中美商业领袖，重申深化改革承诺">
        <img class="img-lazyload" src="" data-url="https://static01.nyt.com/images/2017/10/31/business/31CHINA1/31CHINA1-articleLarge.jpg" alt="本月，习近平的影像在大屏幕上显示。周一，习近平会见了中国和美国企业家代表。" width="600" height="400"/>
	</a>
    <p class="photoCredit">Greg Baker/Agence France-Presse — Getty Images</p>
    <p class="photoCaption">本月，习近平的影像在大屏幕上显示。周一，习近平会见了中国和美国企业家代表。</p>
</div>

<p class="summary">习近平同时强调中国的主权和安全至关重要。中国正收紧对互联网和先进技术的限制，苹果等企业均受影响，这也加剧了跨国企业对其开放和改革承诺的怀疑。 <a target="_blank" href="/business/20171031/xi-jinping-american-executives/" class="more">阅读更多</a></p>

                        </div>
                    </div></div>
					<div class="sectionAutoList columnAplusB ">
						<div class="basic-list">
							<ul class="autoList">
                                <li class="autoListStory first"><h4 class="kicker"></h4>
<div class="thumbnail">
	<a href="/world/20171030/russia-venezula-oil-rosneft/" title="如何在美国后院获得战略优势？俄罗斯：用石油">
        <img class="img-lazyload" data-url="https://static01.nyt.com/images/2017/10/21/business/00RUSSIAOIL1/00RUSSIAOIL1-thumbLarge.jpg" src="" alt="俄罗斯总统普京（右）本月在克里姆林宫会见委内瑞拉总统马杜罗。" width="75" height="75"/>
	</a>
</div>

<h3 class="regularSummaryHeadline"><a target="_blank" href="/world/20171030/russia-venezula-oil-rosneft/" title="如何在美国后院获得战略优势？俄罗斯：用石油">如何在美国后院获得战略优势？俄罗斯：用石油</a></h3>
<h6 class="byline"> <span class="en_byline">CLIFFORD KRAUSS</span> <span class="time"></span> </h6>
<p class="summary">俄罗斯日益将石油作为地缘政治工具，挑战美国利益。它取代了中国在委内瑞拉的角色，以石油业务为中心提供经济援助。作为回报，莫斯科正在华盛顿的后院获得战略优势。</p>
</li><li class="autoListStory "><h4 class="kicker"></h4>
<div class="thumbnail">
	<a href="/business/20171030/brooklyn-nets-joseph-tsai-alibaba/" title="阿里联合创始人收购NBA球队股份">
        <img class="img-lazyload" data-url="https://static01.nyt.com/images/2017/10/28/business/28nets/28nets-thumbLarge.jpg" src="" alt="2014年，阿里巴巴联合创始人之一蔡崇信在纽约证券交易所敲钟，庆祝该公司上市。" width="75" height="75"/>
	</a>
</div>

<h3 class="regularSummaryHeadline"><a target="_blank" href="/business/20171030/brooklyn-nets-joseph-tsai-alibaba/" title="阿里联合创始人收购NBA球队股份">阿里联合创始人收购NBA球队股份</a></h3>
<h6 class="byline"> <span class="en_byline">MICHAEL J. DE LA MERCED</span>, <span class="en_byline">JOE DRAPE</span> <span class="time"></span> </h6>
<p class="summary">蔡崇信将收购布鲁克林篮网队49%的股份，篮网目前估值约23亿美元。据福布斯估计，蔡崇信身价约90亿美元。近年来，多家中国企业斥巨资收购体育资产。</p>
</li><li class="autoListStory "><h4 class="kicker">科技</h4>
<div class="thumbnail">
	<a href="//cn.nytstyle.com/technology/20171024/artificial-intelligence-experts-salaries/" title="硅谷科技巨头的“天价”高薪付给了谁？">
        <img class="img-lazyload" data-url="https://static01.nyt.com/images/2017/10/23/business/23TALENTWAR-1/00TALENTWAR-1-thumbLarge.jpg" src="" alt="" width="75" height="75"/>
	</a>
</div>

<h3 class="regularSummaryHeadline"><a target="_blank" href="//cn.nytstyle.com/technology/20171024/artificial-intelligence-experts-salaries/" title="硅谷科技巨头的“天价”高薪付给了谁？">硅谷科技巨头的“天价”高薪付给了谁？</a></h3>
<h6 class="byline"> <span class="en_byline">CADE METZ</span> <span class="time"></span> </h6>
<p class="summary">硅谷的科技巨头们在人工智能领域押下巨额赌注，以超高薪水和公司股票吸引技术人才。很多高校学者也受到高薪诱惑进入科技公司，给学术界带来巨大的人员流失。</p>
</li><li class="autoListStory "><h4 class="kicker"></h4>
<div class="thumbnail">
	<a href="//cn.nytstyle.com/culture/20171024/flameless-cremation/" title="美国流行殡葬新方式：化尸体为液体">
        <img class="img-lazyload" data-url="https://static01.nyt.com/images/2017/10/20/us/20xp-cremation-2/20xp-cremation-2-thumbLarge.jpg" src="" alt="明尼苏达州温顿，一家殡仪馆的“水焚葬”装置。" width="75" height="75"/>
	</a>
</div>

<h3 class="regularSummaryHeadline"><a target="_blank" href="//cn.nytstyle.com/culture/20171024/flameless-cremation/" title="美国流行殡葬新方式：化尸体为液体">美国流行殡葬新方式：化尸体为液体</a></h3>
<h6 class="byline"> 纽约时报中文网 <span class="time"></span> </h6>
<p class="summary">在美国，一种新的处理遗体的方式正受到越来越多人的欢迎。这种环保的“水焚葬”能将遗体溶解后化为棕色液体，可作为肥料使用，其产生的碳排放仅为火葬的十分之一。</p>
</li><li class="autoListStory "><h4 class="kicker"></h4>
<div class="thumbnail">
	<a href="/china/20171024/china-xi-business-entrepreneurs/" title="习近平权威之下，惴惴不安的中国企业家">
        <img class="img-lazyload" data-url="https://static01.nyt.com/images/2017/10/24/world/24china-biz-1/24china-biz-1-thumbLarge.jpg" src="" alt="左起顺时针：已数月没有露面的肖建华和吴小晖、遭到留党察看的房地产大亨任志强以及寻求政治庇护的郭文贵。" width="75" height="75"/>
	</a>
</div>

<h3 class="regularSummaryHeadline"><a target="_blank" href="/china/20171024/china-xi-business-entrepreneurs/" title="习近平权威之下，惴惴不安的中国企业家">习近平权威之下，惴惴不安的中国企业家</a></h3>
<h6 class="byline"> 黄瑞黎 <span class="time"></span> </h6>
<p class="summary">习近平推动加强国有企业，呼吁商人对党忠诚，以强调国家对私营企业的权威。牵涉政界的商人更面临危险的政治环境。分析称许多企业家已对中国未来丧失信心。</p>
</li><li class="autoListStory "><h4 class="kicker"></h4>
<div class="thumbnail">
	<a href="/business/20171024/china-pollution-economy/" title="中国治理污染新举措或加剧经济增速放缓">
        <img class="img-lazyload" data-url="https://static01.nyt.com/images/2017/10/24/world/24china-enviro-1/24china-enviro-1-thumbLarge.jpg" src="" alt="上海黄浦江，在燃煤电厂附近捕鱼的人。" width="75" height="75"/>
	</a>
</div>

<h3 class="regularSummaryHeadline"><a target="_blank" href="/business/20171024/china-pollution-economy/" title="中国治理污染新举措或加剧经济增速放缓">中国治理污染新举措或加剧经济增速放缓</a></h3>
<h6 class="byline"> <span class="en_byline">KEITH BRADSHER</span> <span class="time"></span> </h6>
<p class="summary">中国政府正加大对污染制造者的打击力度，违规企业可能被勒令关厂。此举的代价可能是经济增速放缓，但官员试图向公众和企业保证，治污不会破坏经济增长。</p>
</li><li class="autoListStory "><h4 class="kicker"></h4>
<div class="thumbnail">
	<a href="/business/20171023/tesla-plant-in-china-may-be-a-first/" title="特斯拉有望在中国全资建厂，成业内第一家">
        <img class="img-lazyload" data-url="https://static01.nyt.com/images/2017/10/23/business/00TESLACHINA/00TESLACHINA-thumbLarge.jpg" src="" alt="北京，一辆特拉斯汽车在充电站。" width="75" height="75"/>
	</a>
</div>

<h3 class="regularSummaryHeadline"><a target="_blank" href="/business/20171023/tesla-plant-in-china-may-be-a-first/" title="特斯拉有望在中国全资建厂，成业内第一家">特斯拉有望在中国全资建厂，成业内第一家</a></h3>
<h6 class="byline"> <span class="en_byline">KEITH BRADSHER</span>, <span class="en_byline">NATALIE KITROEFF</span> <span class="time"></span> </h6>
<p class="summary">知情人士称，特斯拉已与上海市政府初步达成协议，将在自贸区内开办全资工厂。这可能意味着其生产的汽车将被征收高额关税，但也让特斯拉拥有对自身商业秘密的掌控权。</p>
</li><li class="autoListStory "><h4 class="kicker"></h4>
<div class="thumbnail">
	<a href="/business/20171023/alibaba-amazon-southeast-asia-lazada/" title="印度和东南亚：阿里巴巴与亚马逊的新战场">
        <img class="img-lazyload" data-url="https://static01.nyt.com/images/2017/09/30/business/00seasia-lazada1/00seasia-lazada1-thumbLarge.jpg" src="" alt="新加坡RedMart的仓库。这个网络生鲜店是阿里巴巴布局东南亚的一个据点。" width="75" height="75"/>
	</a>
</div>

<h3 class="regularSummaryHeadline"><a target="_blank" href="/business/20171023/alibaba-amazon-southeast-asia-lazada/" title="印度和东南亚：阿里巴巴与亚马逊的新战场">印度和东南亚：阿里巴巴与亚马逊的新战场</a></h3>
<h6 class="byline"> <span class="en_byline">JANE A. PETERSON</span> <span class="time"></span> </h6>
<p class="summary">作为中美各自国内市场的电商霸主，阿里巴巴和亚马逊在印度和东南亚市场上的竞争正在变得日益激烈。该地区商业前景可观，两家公司迥异的商业模式也将接受考验。</p>
</li><li class="autoListStory "><h4 class="kicker"></h4>
<div class="thumbnail">
	<a href="/china/20171023/china-xi-jinping-datong/" title="在“煤都”大同，习近平的“中国梦”难以兑现">
        <img class="img-lazyload" data-url="https://static01.nyt.com/images/2017/10/22/world/22CHINA-REFORM-2/18china-reform-1-thumbLarge.jpg" src="" alt="中国山西省小窑头村外的太阳能板，煤炭资源锐减，导致当地人开始寻找新的收入来源。" width="75" height="75"/>
	</a>
</div>

<h3 class="regularSummaryHeadline"><a target="_blank" href="/china/20171023/china-xi-jinping-datong/" title="在“煤都”大同，习近平的“中国梦”难以兑现">在“煤都”大同，习近平的“中国梦”难以兑现</a></h3>
<h6 class="byline"> 储百亮 <span class="time"></span> </h6>
<p class="summary">在农村和大同这样的欠发达地区，习近平的中国梦没有兑现为人们最需要的东西，改善他们的生活。尽管严厉打击腐败，但从中获益更多的是官员而不是老百姓。</p>
</li><li class="autoListStory "><h4 class="kicker"></h4>
<div class="thumbnail">
	<a href="//cn.nytstyle.com/morning-brief/20171020/xi-jinping-catalonia-north-korea/" title="早报：图解十九大报告；MH370搜寻工作重启">
        <img class="img-lazyload" data-url="https://static01.nyt.com/images/2017/10/19/briefing/20ambriefing-asia-slide-ZOX5/20ambriefing-asia-slide-ZOX5-thumbLarge.jpg" src="" alt="习近平主席的主导地位，使人们难以预测谁会在党代会进入政治局。其中一个有望入常的人选是汪洋。" width="75" height="75"/>
	</a>
</div>

<h3 class="regularSummaryHeadline"><a target="_blank" href="//cn.nytstyle.com/morning-brief/20171020/xi-jinping-catalonia-north-korea/" title="早报：图解十九大报告；MH370搜寻工作重启">早报：图解十九大报告；MH370搜寻工作重启</a></h3>
<h6 class="byline"> <span class="en_byline">CHARLES McDERMID</span> <span class="time"></span> </h6>
<p class="summary">汪洋有望“入常”，或成经济改革推手；腾讯推出“为习近平鼓掌”程序；新西兰150年来最年轻总理准备就职；趣店上市首日股价大涨……新闻早报带你速览今日要闻。</p>
</li><li class="autoListStory "><h4 class="kicker"></h4>
<div class="thumbnail">
	<a href="/business/20171020/china-reform-economy-communist-party/" title="汪洋有望“入常”，能否成为经济改革推手？">
        <img class="img-lazyload" data-url="https://static01.nyt.com/images/2017/10/20/business/00CHINAECON1/00CHINAECON1-thumbLarge.jpg" src="" alt="中国广州的文化中心海心沙亚运公园是受欢迎的散步和购物去处。该公园是最近为协助提高该城市及邻近的广东省的声誉、吸引人们到此处开发的许多项目之一。" width="75" height="75"/>
	</a>
</div>

<h3 class="regularSummaryHeadline"><a target="_blank" href="/business/20171020/china-reform-economy-communist-party/" title="汪洋有望“入常”，能否成为经济改革推手？">汪洋有望“入常”，能否成为经济改革推手？</a></h3>
<h6 class="byline"> <span class="en_byline">KEITH BRADSHER</span> <span class="time"></span> </h6>
<p class="summary">中共领导层即将迎来权力洗牌，前广东省委书记汪洋有望跻身“七常委”，他被视为推动整体经济改革的有力人选。但习近平日益集中的权力可能会阻碍这一努力。</p>
</li><li class="autoListStory "><h4 class="kicker"></h4>
<div class="thumbnail">
	<a href="/business/20171019/china-economy-gdp/" title="中国第三季度GDP同比增长6.8%">
        <img class="img-lazyload" data-url="https://static01.nyt.com/images/2017/10/19/business/19CHINAGDP1/19CHINAGDP1-thumbLarge.jpg" src="" alt="上海的购物者。零售支出、住房销售和贸易数字表明中国经济在政府引导下稳步增长。" width="75" height="75"/>
	</a>
</div>

<h3 class="regularSummaryHeadline"><a target="_blank" href="/business/20171019/china-economy-gdp/" title="中国第三季度GDP同比增长6.8%">中国第三季度GDP同比增长6.8%</a></h3>
<h6 class="byline"> <span class="en_byline">KEITH BRADSHER</span> <span class="time"></span> </h6>
<p class="summary">国有银行的大量贷款、活跃的政府支出以及强劲的出口，帮助中国经济保持活跃而稳定的增长。但信贷累积和膨胀的债务问题仍然给中国金融体系的稳定性蒙上阴影。</p>
</li><li class="autoListStory "><h4 class="kicker"></h4>
<div class="thumbnail">
	<a href="//cn.nytstyle.com/morning-brief/20171019/xi-jinping-rohingya-islamic-state/" title="早报：中国日报撤争议社论；三星创始人被调查">
        <img class="img-lazyload" data-url="https://static01.nyt.com/images/2017/10/18/briefing/19BRIEFING-asia-slide-42R5/19BRIEFING-asia-slide-42R5-thumbLarge.jpg" src="" alt="习近平超长篇幅的开幕演讲为中国为期一周的党代会设下了基调。他宣布了一个“新时代”的到来，并且在评价中强调中国是“强国”。" width="75" height="75"/>
	</a>
</div>

<h3 class="regularSummaryHeadline"><a target="_blank" href="//cn.nytstyle.com/morning-brief/20171019/xi-jinping-rohingya-islamic-state/" title="早报：中国日报撤争议社论；三星创始人被调查">早报：中国日报撤争议社论；三星创始人被调查</a></h3>
<h6 class="byline"> <span class="en_byline">CHARLES McDERMID</span> <span class="time"></span> </h6>
<p class="summary">习近平十九大报告关键议题解读；美国秘密组织为女性打上“烙印”；解密文件显示美国曾默许印尼反共大屠杀；蒂勒森谴责缅甸军方暴行……新闻早报带你速览今日要闻。</p>
</li><li class="autoListStory "><h4 class="kicker"></h4>
<div class="thumbnail">
	<a href="//cn.nytstyle.com/morning-brief/20171018/raqqa-kirkuk-marawi/" title="早报：习近平十九大示强权；中国培育“海水稻”">
        <img class="img-lazyload" data-url="https://static01.nyt.com/images/2017/10/17/briefing/18BRIEFING-asia-slide-D909/18BRIEFING-asia-slide-D909-thumbLarge.jpg" src="" alt="作为数十年来中国最有权势的领导人，习近平主席开始了他的第二次党代会，准备为另一个五年任期加冕。" width="75" height="75"/>
	</a>
</div>

<h3 class="regularSummaryHeadline"><a target="_blank" href="//cn.nytstyle.com/morning-brief/20171018/raqqa-kirkuk-marawi/" title="早报：习近平十九大示强权；中国培育“海水稻”">早报：习近平十九大示强权；中国培育“海水稻”</a></h3>
<h6 class="byline"> <span class="en_byline">CHARLES McDERMID</span> <span class="time"></span> </h6>
<p class="summary">特朗普新版旅行禁令再被叫停；叙利亚夺回ISIS“首都”拉卡；菲律宾解放马拉维；道指首破2.3万点；阿富汗警察局遭袭23人亡……新闻早报带你速览今日要闻。</p>
</li><li class="autoListStory "><h4 class="kicker"></h4>
<div class="thumbnail">
	<a href="/business/20171018/how-a-healthy-economy-can-shorten-life-spans/" title="为何经济发展会导致人的寿命变短？">
        <img class="img-lazyload" data-url="https://static01.nyt.com/images/2017/10/17/business/17up-healthworkdeath/up-healthworkdeath-thumbLarge.jpg" src="" alt="德克萨斯州帕萨迪纳的炼油厂。随着工业化国家的经济愈发繁荣，也产生更多的空气污染，缩短了一些人的寿命。" width="75" height="75"/>
	</a>
</div>

<h3 class="regularSummaryHeadline"><a target="_blank" href="/business/20171018/how-a-healthy-economy-can-shorten-life-spans/" title="为何经济发展会导致人的寿命变短？">为何经济发展会导致人的寿命变短？</a></h3>
<h6 class="byline"> <span class="en_byline">AUSTIN FRAKT</span> <span class="time"></span> </h6>
<p class="summary">总体而言，经济繁荣会提高生活标准，促进人们的健康。但经济快速增长往往也意味着空气污染、人们的压力增大、更多的车祸。这些因素在短时期内会造成死亡率上升。</p>
</li><li class="autoListStory "><h4 class="kicker"></h4>
<div class="thumbnail">
	<a href="//cn.nytstyle.com/morning-brief/20171017/ophelia-kirkuk-bowe-bergdahl-your-tuesday-briefing/" title="早报：特朗普将访亚太；中国“防火长城”加固">
        <img class="img-lazyload" data-url="https://static01.nyt.com/images/2017/10/16/briefing/17BRIEFING-asia-promo-slide-CLQH/17BRIEFING-asia-promo-slide-CLQH-thumbLarge-v2.jpg" src="" alt="在上月举办的中国互联网安全大会上，一块电子屏展示了中国所遭受网络攻击。" width="75" height="75"/>
	</a>
</div>

<h3 class="regularSummaryHeadline"><a target="_blank" href="//cn.nytstyle.com/morning-brief/20171017/ophelia-kirkuk-bowe-bergdahl-your-tuesday-briefing/" title="早报：特朗普将访亚太；中国“防火长城”加固">早报：特朗普将访亚太；中国“防火长城”加固</a></h3>
<h6 class="byline"> <span class="en_byline">CHARLES McDERMID</span> <span class="time"></span> </h6>
<p class="summary">科学家观测到两颗中子星相撞图像；亚洲头号恐怖分子死亡；处在失传边缘的中国唢呐技艺；英国布克奖今日揭晓；朝鲜街头时尚观察……新闻早报带你速览今日要闻。</p>
</li><li class="autoListStory "><h4 class="kicker">热点透视</h4>
<div class="thumbnail">
	<a href="/business/20171016/china-private-investment/" title="中国加大私营部门管控力度">
        <img class="img-lazyload" data-url="https://static01.nyt.com/images/2017/10/14/business/14chinaviews3/14chinaviews3-thumbLarge.jpg" src="" alt="在中国唐山百丰钢铁有限公司的仓库，一名工人正在将钢铁装载到卡车上。" width="75" height="75"/>
	</a>
</div>

<h3 class="regularSummaryHeadline"><a target="_blank" href="/business/20171016/china-private-investment/" title="中国加大私营部门管控力度">中国加大私营部门管控力度</a></h3>
<h6 class="byline"> <span class="en_byline">CHRISTOPHER BEDDOR</span> <span class="time"></span> </h6>
<p class="summary">习近平希望能重振私营部门的信心，也在加大对其的管制力度。国企与私企之间的界限变得模糊，政府正在用各种形式向企业渗透，包括将党委纳入私营企业的治理结构。</p>
</li><li class="autoListStory "><h4 class="kicker"></h4>
<div class="thumbnail">
	<a href="/business/20171016/china-online-stakes-control/" title="中国政府参股网络媒体，欲直接插手内容管控">
        <img class="img-lazyload" data-url="https://static01.nyt.com/images/2017/10/14/business/14CHINAINTERNET2/14CHINAINTERNET2-thumbLarge.jpg" src="" alt="随着智能手机渗透到生活的方方面面，互联网和社交媒体平台成了越来越受欢迎的新闻来源。" width="75" height="75"/>
	</a>
</div>

<h3 class="regularSummaryHeadline"><a target="_blank" href="/business/20171016/china-online-stakes-control/" title="中国政府参股网络媒体，欲直接插手内容管控">中国政府参股网络媒体，欲直接插手内容管控</a></h3>
<h6 class="byline"> <span class="en_byline">RAYMOND ZHONG</span>, 黄瑞黎 <span class="time"></span> </h6>
<p class="summary">此次“试点”入股的对象为铁血网及Zaker。这种“特殊管理股”会让政府官员获得这些公司的董事席位，并有权审查其内容。分析称这种模式可能在未来全面推行。</p>
</li><li class="autoListStory last"><h4 class="kicker"></h4>
<div class="thumbnail">
	<a href="//cn.nytstyle.com/morning-brief/20171016/mogadishu-iran-north-korea/" title="早报：美韩军演；造假事件令中国科学界蒙羞">
        <img class="img-lazyload" data-url="https://static01.nyt.com/images/2017/10/15/briefing/16BRIEFING-asia-slide-5LIN/16BRIEFING-asia-slide-5LIN-thumbLarge.jpg" src="" alt="美国核动力潜艇“密歇根号”。美韩海军联合军演于今日开始，“密歇根号”也将参与其中。" width="75" height="75"/>
	</a>
</div>

<h3 class="regularSummaryHeadline"><a target="_blank" href="//cn.nytstyle.com/morning-brief/20171016/mogadishu-iran-north-korea/" title="早报：美韩军演；造假事件令中国科学界蒙羞">早报：美韩军演；造假事件令中国科学界蒙羞</a></h3>
<h6 class="byline"> <span class="en_byline">CHARLES McDERMID</span> <span class="time"></span> </h6>
<p class="summary">朝鲜黑客大军全球出击；红军小学重塑中国思想政治教育；索马里致命袭击超200人死亡；中国摄影展被指种族歧视；费德勒上海夺冠……新闻早报带你速览今日要闻。</p>
</li>
							</ul>
						</div>
					</div>
					<div class="pagination">
    <ul class="cf">
         <li class="first current"><span>1</span></li>  <li class=""><a href='/business/2/'>2</a></li>  <li class=""><a href='/business/3/'>3</a></li>  <li class=""><a href='/business/4/'>4</a></li>  <li class=""><a href='/business/5/'>5</a></li>  <li class=""><a href='/business/6/'>6</a></li>  <li class=""><a href='/business/7/'>7</a></li>  <li class="next"><a href='/business/2/'>下一页 >></a></li> 
    </ul>
</div>

                </div>
                <div class="cf layoutC">
                    <div id="hotStory" data-url="/async/mostviewed/all/?lang=zh-hans">
    <i class="lazyload-loading"></i>
</div>
<script id="hotStoryTpl" type="text/html">
<div class="tabB">
    <div class="tabs">
        <a href="#tabC_mostView" class="item active">最受欢迎</a><a href="#tabC_mostViewedWeek" class="inactive">一周最热文章</a><a href="#tabC_mostViewedSlideshow" class="inactive">热门图集</a>
    </div>
    <div class="tab-content">
        <div id="tabC_mostView" class="tab_c active">
            <ol class="hotStoryList">
                {#each list.daily as value#}
                <li><a href="{#value.url#}?utm_source=mostviewed-daily&utm_medium=cpc&utm_campaign=mostviewed" title="{#value.headline#}" class="daily_popular_{#value.type#}">{#value.headline#}</a></li>
                {#/each#}
            </ol>
        </div>
        <div id="tabC_mostViewedWeek" class="tab_c inactive">
            <ol class="hotStoryList">
                {#each list.weekly as value#}
                <li><a href="{#value.url#}?utm_source=mostviewed-daily&utm_medium=cpc&utm_campaign=mostviewed" title="{#value.headline#}" class="daily_popular_{#value.type#}">{#value.headline#}</a></li>
                {#/each#}
            </ol>
        </div>
        <div id="tabC_mostViewedSlideshow" class="tab_c inactive">
            <ol class="hotStoryList">
                {#each list.weekly_slideshow as value#}
                <li><a href="{#value.url#}?utm_source=mostviewed-daily&utm_medium=cpc&utm_campaign=mostviewed" title="{#value.headline#}" class="daily_popular_{#value.type#}">{#value.headline#}</a></li>
                {#/each#}
            </ol>
        </div>
    </div>
</div>
</script>

                    
                    <div id="taboola-right-rail-thumbnails"></div>
<script type="text/javascript">
 window._taboola = window._taboola || [];
 _taboola.push({
     mode: 'thumbnails-rr3',
     container: 'taboola-right-rail-thumbnails',
     placement: 'Right Rail Thumbnails',
     target_type: 'mix'
 });
</script>

                    <div id='nytcn-gpt-ad-MiddleRight-1' class="ad ad-dfp ad-MiddleRight dfp_ad_container">
</div>

                    
					<div id='nytcn-gpt-ad-Box1-2' class="ad ad-dfp ad-Box1 dfp_ad_container">
</div>

                </div>
				<div class="vertical-line"></div>
                <!-- the list ends here -->
            </div>
            
            <script type="text/javascript">
  window._taboola = window._taboola || [];
  _taboola.push({flush: true});
</script>

            <div class="cf no-content" id="footer">
    <div class="copyright">
        © 2017 The New York Times Company.
    </div>
    <ul class="footerLinkList">
        <li class="footerLink"><a rel="nofollow" href="/help/ad/">广告</a></li>
        <li class="footerLink"><a rel="nofollow" href="/help/about-us/">关于我们</a></li>
        <li class="footerLink"><a rel="nofollow" href="/help/contact/">联系我们</a></li>
        <li class="footerLink"><a rel="nofollow" href="/help/privacy/">隐私权声明</a></li>
        <li class="footerLink"><a rel="nofollow" href="/help/tos/">服务条款</a></li>
        <li class="footerLink"><a rel="nofollow" href="/help/cooperation/">友情链接</a></li>
        <li class="footerLink"><a rel="nofollow" href="/help/copyright-statement/">版权声明</a></li>
        <li class="footerLink"><a rel="nofollow" href="mailto:cn.help@nytimes.com?subject=FEEDBACK">意见反馈</a></li>
        <li class="last footerLink"><a rel="nofollow" id="rssIcon" href="/rss.html">RSS</a></li>
    </ul>
</div>
<div class="download_app">
    <a href="https://itunes.apple.com/app/apple-store/id807498298?pt=13036&ct=news-hp&mt=8" target="_blank" class="apple_store_icon" title="点击下载iOS APP">
        <span class="visually_hidden">点击下载iOS APP</span>
    </a>
    <span class="app_store qr_code" title="扫描二维码下载">
        <span class="visually_hidden">
            扫描二维码下载iOS APP
        </span>
    </span>
    <a href="https://play.google.com/store/apps/details?id=com.nytimes.cn" class="google_play_icon" target="_blank" title="点击下载Android APP">
        <span class="visually_hidden">点击下载Android APP</span>
    </a>
    <span class="google_play qr_code" title="扫描二维码下载">
        <span class="visually_hidden">
            扫描二维码下载Android APP
        </span>
    </span>
    <a href="https://raw.githubusercontent.com/chinanyt/apps/master/version/apk/latest.apk" target="_blank" class="download_apk" title="点击下载Android APK">
        <span class="visually_hidden">点击下载Android APK</span>
    </a>
    <span class="download_apk qr_code" title="扫描二维码下载">
        <span class="visually_hidden">
            扫描二维码下载Android APK
        </span>
    </span>
</div>



<!-- chartbeat -->
<script type='text/javascript'>
    var _sf_async_config={};
    /** CONFIGURATION START **/
    _sf_async_config.uid = 16698;
    _sf_async_config.domain = 'cn.nytimes.com';
    _sf_async_config.useCanonical = true;
    _sf_async_config.sections = '';
    _sf_async_config.authors = '';
    /** CONFIGURATION END **/
    (function(){
      function loadChartbeat() {
        window._sf_endpt=(new Date()).getTime();
        var e = document.createElement('script');
        e.setAttribute('language', 'javascript');
        e.setAttribute('type', 'text/javascript');
        e.setAttribute('src', '//static.chartbeat.com/js/chartbeat.js');
        document.body.appendChild(e);
      }
      var oldonload = window.onload;
      window.onload = (typeof window.onload != 'function') ?
         loadChartbeat : function() { oldonload(); loadChartbeat(); };
    })();
</script>
<!-- /chartbeat -->


        </div>
    </body>
</html>

'''


def ans0():
    url_prefix = 'https://cn.nytimes.com'
    # liebie_dic = {'世界': 'world', '中国': 'china', '商业': 'business'}
    # print(liebie_dic['中国'])
    # liebie_list = ['世界','中国', '商业']
    # for lan in liebie_list:
    #     url_list = []
    #     vol_tl = lan + '新闻'
    #     for nu in range(1, 3):
    #         vol_ul = url_prefix + '/' + liebie_dic[lan] + '/' + str(nu) + '/'
    #         url_list.append(vol_ul)
    #
    #     print(url_list)
    #     print(vol_tl)


    soup = BeautifulSoup(''.join(html))
    article_link = []
    artiultag = soup.find('ul', attrs={'class': 'autoList'})
    for li in artiultag.findAll('li'):
        # print(li)

        find_today = re.compile('href=\".*(\d\d\d\d)(\d\d)(\d\d)/')
        month = find_today.search(str(li))  # 把上面构建的表达式作用于findAll找出来的内容
        if r'.nytstyle.' in month.group():
            continue
        # try/except结构主要是用于正则表达式查找，如果不用这个结构，在部分标签当中查找不到内容的时候，下面引用查找结果group()就会报错，造成崩溃。
        try:
            # print(month.group())
            d1 = datetime.date.today()  # 获取今天的日期
            d2 = datetime.date(int(month.group(1)), int(month.group(2)), int(month.group(3)))  # 获取新闻的日期
            days_betwen = (d1 - d2).days  # 获取时间差，结果为整数
            # print(d2)
            # print(days_betwen)
            if days_betwen <= 30:  # 限定抓取几天内的新闻，当天的则为days_betwen == 0
                article_link.append(str(li))  # 注意要转换为字符串，beautifusoup不接受列表和其他类型的数据
        except:
            pass

    # print(article_link)
    soup2 = BeautifulSoup(''.join(article_link))

    # 下面的for循环在上面找出指定日期范围内的正文链接当中提取url链接，并配合'http://www.jxta.gov.cn/'形成最终的正文链接
    for link in soup2.findAll('a'):
        imagelink = re.compile(r'src="')
        ilinkfind = imagelink.findall(str(link))
        if ilinkfind:
            continue
        # if '/tag/' in link['href']:
        #     continue
        # print(link)
        print(url_prefix + link['href'])
        # # title_find = re.compile(r'<.*><span>.*</span>(.*)</a>')
        # # title_search = title_find.search(str(link))
        # # print(link['href'])
        print(link.contents[0].strip())


#
ans0()


