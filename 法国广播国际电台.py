# coding=utf-8
from BeautifulSoup import BeautifulSoup
import datetime,re  # 导入日期时间模块，各版面的url根据发行日期改变。

html = '''

<!DOCTYPE html>

        <!--[if lt IE 8]>      <html dir="ltr" lang="zh-Hans" data-locale="cn" data-locale-long="zh_CN" data-locale-name="Chinese (China)" data-locale-facebook="zh_CN" data-locale-twitter="zh-cn" data-locale-google="zh-CN" data-locale-linkedin="zh_CN" class="lang-cn no-js lt-ie8 lt-ie9"> <![endif]-->
<!--[if IE 8]>         <html dir="ltr" lang="zh-Hans" data-locale="cn" data-locale-long="zh_CN" data-locale-name="Chinese (China)" data-locale-facebook="zh_CN" data-locale-twitter="zh-cn" data-locale-google="zh-CN" data-locale-linkedin="zh_CN" class="lang-cn no-js lt-ie9"> <![endif]-->
<!--[if gt IE 8]><!--> <html dir="ltr" lang="zh-Hans" data-locale="cn" data-locale-long="zh_CN" data-locale-name="Chinese (China)" data-locale-facebook="zh_CN" data-locale-twitter="zh-cn" data-locale-google="zh-CN" data-locale-linkedin="zh_CN" class="lang-cn no-js"> <!--<![endif]-->

    <head prefix="og: http://ogp.me/ns# fb: http://ogp.me/ns/fb# article: http://ogp.me/ns/article#">
                        <meta http-equiv="content-type" content="text/html; charset=utf-8">

        <title>中国时事</title>

                <meta http-equiv="X-UA-Compatible" content="IE=edge">        <meta name="viewport" content="width=device-width, initial-scale=1, maximum-scale=1">

        
            



                    
    <meta name="title" content="&#x4E2D;&#x56FD;&#x65F6;&#x4E8B;" />
    <meta name="description" content="&#x540C;&#x6B65;&#x3001;&#x968F;&#x65F6;&#x8DDF;&#x8E2A;&#x4E2D;&#x56FD;&#x65F6;&#x4E8B;&#xFF1A;&#x91C7;&#x8BBF;&#x3001;&#x62A5;&#x9053;&#x3001;&#x7279;&#x522B;&#x4E13;&#x9898;&#x2026;&#x2026;" />
    
    <link rel="search" type="application/opensearchdescription+xml" href="/opensearch_cn.xml?version=20171011171259" title="法广" />

    <meta name="apple-mobile-web-app-capable" content="yes">
    <meta name="apple-mobile-web-app-status-bar-style" content="black-translucent">
    <meta name="apple-mobile-web-app-title" content="法广">
    <meta name="application-name" content="法广">
    <link rel="shortcut icon" href="/favicon.ico?version=20171011171259" type="image/x-icon">
    <link rel="apple-touch-icon" href="/apple-touch-icon-57x57.png?version=20171011171259" sizes="57x57">
    <link rel="apple-touch-icon" href="/apple-touch-icon-60x60.png?version=20171011171259" sizes="60x60">
    <link rel="apple-touch-icon" href="/apple-touch-icon-72x72.png?version=20171011171259" sizes="72x72">
    <link rel="apple-touch-icon" href="/apple-touch-icon-76x76.png?version=20171011171259" sizes="76x76">
    <link rel="apple-touch-icon" href="/apple-touch-icon-114x114.png?version=20171011171259" sizes="114x114">
    <link rel="apple-touch-icon" href="/apple-touch-icon-120x120.png?version=20171011171259" sizes="120x120">
    <link rel="apple-touch-icon" href="/apple-touch-icon-144x144.png?version=20171011171259" sizes="144x144">
    <link rel="apple-touch-icon" href="/apple-touch-icon-152x152.png?version=20171011171259" sizes="152x152">
    <link rel="apple-touch-icon" href="/apple-touch-icon-180x180.png?version=20171011171259" sizes="180x180">
    <link rel="icon" type="image/png" href="/favicon-16x16.png?version=20171011171259" sizes="16x16">
    <link rel="icon" type="image/png" href="/favicon-32x32.png?version=20171011171259" sizes="32x32">
    <link rel="icon" type="image/png" href="/favicon-48x48.png?version=20171011171259" sizes="48x48">
    <link rel="icon" type="image/png" href="/favicon-64x64.png?version=20171011171259" sizes="64x64">
    <link rel="icon" type="image/png" href="/favicon-96x96.png?version=20171011171259" sizes="96x96">
    <link rel="icon" type="image/png" href="/favicon-160x160.png?version=20171011171259" sizes="160x160">
    <link rel="icon" type="image/png" href="/favicon-192x192.png?version=20171011171259" sizes="192x192">
    <meta name="msapplication-TileColor" content="#454349">
    <meta name="msapplication-TileImage" content="/mstile-144x144.png?version=20171011171259">
    <link rel="icon" type="image/x-icon" href="/favicon.ico?version=20171011171259">

                

    
            <meta property="og:site_name" content="法广" />
    <meta property="og:url" content="http://cn.rfi.fr/%E4%B8%AD%E5%9B%BD/all/" />
    <meta property="og:type" content="article" />
    <meta property="og:image" content="http://cn.rfi.fr/bundles/aefhermesrfi/img/vf-missing-image.png?version=20171011171259" />

    <meta property="og:image:width" content="1200">
    <meta property="og:image:height" content="627">
    <meta property="og:image:type" content="image/png">

    <meta property="og:title" content="&#x4E2D;&#x56FD;&#x65F6;&#x4E8B;" />
    <meta property="og:description" content="&#x540C;&#x6B65;&#x3001;&#x968F;&#x65F6;&#x8DDF;&#x8E2A;&#x4E2D;&#x56FD;&#x65F6;&#x4E8B;&#xFF1A;&#x91C7;&#x8BBF;&#x3001;&#x62A5;&#x9053;&#x3001;&#x7279;&#x522B;&#x4E13;&#x9898;&#x2026;&#x2026;" />
    <meta property="fb:app_id" content="113191652055439" />
    <meta property="fb:pages" content="155677885272" />
    
            <meta name="twitter:card" content="summary_large_image" />
    <meta name="twitter:url" content="http://cn.rfi.fr/%E4%B8%AD%E5%9B%BD/all/" />
    <meta name="twitter:creator" content="@RFI_Cn" />
    <meta name="twitter:site" content="@RFI_Cn" />
    <meta name="twitter:image" content="http://static.rfi.fr/meta_og_twcards/RFI_TW.png" />
    <meta name="twitter:title" content="&#x4E2D;&#x56FD;&#x65F6;&#x4E8B;" />
    <meta name="twitter:description" content="&#x540C;&#x6B65;&#x3001;&#x968F;&#x65F6;&#x8DDF;&#x8E2A;&#x4E2D;&#x56FD;&#x65F6;&#x4E8B;&#xFF1A;&#x91C7;&#x8BBF;&#x3001;&#x62A5;&#x9053;&#x3001;&#x7279;&#x522B;&#x4E13;&#x9898;&#x2026;&#x2026;" />

    <link href="https://plus.google.com/109123137235348587446/" rel="publisher" />

        <meta name="twitter:domain" content="cn.rfi.fr" />
    <meta name="twitter:account_id" content="32861321" />
    <meta name="twitter:app:id:iphone" content="551782765" />
    <meta name="twitter:app:id:ipad" content="551782765" />
    <meta name="twitter:app:id:googleplay" content="com.rfi.androidapp" />
    <meta name="twitter:app:name:iphone" content="RFI - 法国国际广播电台" />
    <meta name="twitter:app:name:ipad" content="RFI - 法国国际广播电台" />
    <meta name="twitter:app:name:googleplay" content="RFI - 法国国际广播电台" />
    <meta property="og:locale" content="zh_CN" />
    <meta name="apple-itunes-app" content="551782765" />
    <meta name="msApplication-ID" content="57d03d56-dd7c-449e-8fa1-a87c090f54df" />
    <meta name="msApplication-PackageFamilyName" content="FRANCE24.FRANCE24-MCD-RFI_3zfmvk45gp28r" />


                            
    <link rel="alternate" href="android-app://com.rfi.androidapp/rfi/cn/section/china" />
    <meta name="twitter:app:url:googleplay" content="rfi://cn/section/china" />


    <link rel="alternate" type="application/rss+xml" title="中国时事" href="http://cn.rfi.fr/%E4%B8%AD%E5%9B%BD/rss" />

            

                                                        <link rel="canonical" href="http://cn.rfi.fr/%E4%B8%AD%E5%9B%BD/all/"/>
                    
        
                    <link rel="alternate" media="only screen and (max-width: 640px)" href="http://m.cn.rfi.fr/%E4%B8%AD%E5%9B%BD/all/" >
        
                            <link rel="stylesheet" type="text/css" href="/css/compiled/cn/main.css?version=20171011171259">
    
            <link rel="stylesheet" type="text/css" href="/css/compiled/print.css?version=20171011171259" media="print">
    
        
                        <script type="text/javascript" src="/bundles/aefhermesrfi/js/hacks.js?version=20171011171259"></script>

                        <script type="text/javascript">
                var domainConfig = {
    baseDomain: "rfi.fr",
                defaultSubdomain: "cn",
    mobileSubdomain: "m.cn",
    tabletSubdomain: "t.cn",
    currentSubdomain: "cn",
    currentLocale: {
        short: "cn",
                long: "zh_CN"
            }
};
var isAefHermes = true;


    window.janrainEnabled = true;

            </script>

            <script type="text/javascript">
                var metaPageTitle = '';
                var newMetaPageTitle = '';
                var metaPageDesc = '';
                var specialEventId = '';
            </script>

                        
                             <script type="text/javascript" src="/js/compiled/mobile-redirect.js?version=20171011171259"></script>
            
            <script type="text/javascript" data-main="/js/main.cn.built.js?version=20171011171259" src="/js/require.js?version=20171011171259" async></script>

        
                                                                                                                                            <script class='tc-config-vars' type="text/javascript"><!--
var tms_vars = {};
tms_vars["page"] = "tc_name_aef_hermes_rfi_china";
tms_vars["env_context"] = "main";
tms_vars["reqtag"] = "";
tms_vars["locale"] = "cn";
tms_vars["aef_libelle_contenu_page"] = "home_section";
tms_vars["aef_id_contenu"] = "A76B1A1A\x2DF489\x2D4338\x2DB738\x2D8CC0D52614E4";
tms_vars["aef_marque"] = "rfi";
tms_vars["aef_rep1"] = "chine";
tms_vars["aef_rep2"] = "defaut";
tms_vars["aef_rep3"] = "defaut";
tms_vars["aef_rep_global"] = "chine";
tms_vars["aef_thema"] = "";
tms_vars["aef_type_page1"] = "section";
tms_vars["aef_auteur"] = "";
tms_vars["aef_acces"] = "gratuit";
tms_vars["nom_page"] = "accueil";
tms_vars["aef_dpubli"] = "2017\x2D10\x2D30";
tms_vars["aef_hpubli"] = "13\x3A00";
tms_vars["env_work"] = 'cn_prod';
tms_vars["aef_version_environnement"] = 'v2.46.9';
        var tc_vars = {};
window.tc_vars = tms_vars;
//--></script>
                                            
                                        
    <script type="application/ld+json">{"@context":"http:\/\/schema.org","@type":"ItemList","url":"http:\/\/cn.rfi.fr\/%E4%B8%AD%E5%9B%BD\/all\/","itemListElement":[{"@type":"ListItem","position":1,"url":"http:\/\/cn.rfi.fr\/%E4%B8%AD%E5%9B%BD\/20171030-%E4%B8%AD%E5%9B%BD%E5%A4%8D%E6%98%9F%E6%94%B6%E8%B4%AD%E6%B3%95%E5%9B%BD%E8%8D%AF%E5%93%81%E5%88%86%E9%94%80%E5%85%AC%E5%8F%B8-tridem"},{"@type":"ListItem","position":2,"url":"http:\/\/cn.rfi.fr\/%E4%B8%AD%E5%9B%BD\/20171030-%E4%B8%AD%E7%BA%AA%E5%A7%94%E5%AE%9A%E6%80%A7%E5%AD%99%E6%94%BF%E6%89%8D%E4%B8%BA%E9%87%8E%E5%BF%83%E5%AE%B6-%E5%9D%9A%E5%86%B3%E9%93%B2%E9%99%A4"},{"@type":"ListItem","position":3,"url":"http:\/\/cn.rfi.fr\/%E4%B8%AD%E5%9B%BD\/20171030-%E4%B8%AD%E5%9B%BD%E5%AE%98%E5%91%98%E4%BC%B8%E6%89%8B%E9%A6%99%E6%B8%AF%E6%95%99%E8%82%B2-%E4%B8%AD%E5%8F%B2%E5%BF%A7%E6%88%90%E6%B4%97%E8%84%91%E6%95%99%E8%82%B2"},{"@type":"ListItem","position":4,"url":"http:\/\/cn.rfi.fr\/%E4%B8%AD%E5%9B%BD\/20171030-%E7%8B%AC%E7%AB%8B%E4%B8%AD%E6%96%87%E7%AC%94%E4%BC%9A%E5%91%BC%E5%90%81%E4%B8%AD%E5%9B%BD%E5%BD%93%E5%B1%80%E8%BF%98%E4%BA%8E%E6%A1%82%E6%B0%91%E6%B5%B7%E8%87%AA%E7%94%B1"},{"@type":"ListItem","position":5,"url":"http:\/\/cn.rfi.fr\/%E4%B8%AD%E5%9B%BD\/20171029-%E5%AD%94%E9%93%89%E4%BD%91%E8%AE%BF%E6%97%A5%E4%B8%BA%E6%9D%8E%E5%85%8B%E5%BC%BA%E8%AE%BF%E6%97%A5%E9%93%BA%E8%B7%AF"},{"@type":"ListItem","position":6,"url":"http:\/\/cn.rfi.fr\/%E4%B8%AD%E5%9B%BD\/20171029-%E9%98%B2%E8%8C%83%E6%9A%97%E6%9D%80%E7%AF%A1%E5%85%9A%E5%A4%BA%E6%9D%83%E4%BC%A0%E5%BD%93%E5%B1%80%E4%B8%A5%E6%9F%A5%E4%B8%AD%E5%8D%97%E6%B5%B7%E4%BF%9D%E9%95%96%E8%AD%A6%E5%8D%AB%E5%8F%B8%E6%9C%BA%E8%83%8C%E6%99%AF"},{"@type":"ListItem","position":7,"url":"http:\/\/cn.rfi.fr\/%E4%B8%AD%E5%9B%BD\/20171029-%E4%B9%A0%E5%AE%B6%E5%86%9B%E6%94%BF%E6%B2%BB%E5%B1%80%E6%96%B0%E8%B4%B5%E6%9D%8E%E5%BC%BA%E4%B8%BB%E6%94%BF%E4%B8%8A%E6%B5%B7"},{"@type":"ListItem","position":8,"url":"http:\/\/cn.rfi.fr\/%E4%B8%AD%E5%9B%BD\/20171029-%E6%94%BF%E6%B2%BB%E5%B1%80%E6%94%B9%E4%B8%BA%E6%AF%8F%E5%B9%B4%E8%A6%81%E5%90%91%E4%B9%A0%E8%BF%91%E5%B9%B3%E8%BF%B0%E8%81%8C%E6%84%8F%E5%91%B3%E6%9E%B6%E7%A9%BA%E5%B8%B8%E5%A7%94%E9%9B%86%E4%BD%93%E9%A2%86%E5%AF%BC"},{"@type":"ListItem","position":9,"url":"http:\/\/cn.rfi.fr\/%E4%B8%AD%E5%9B%BD\/20171028-%E7%89%B9%E6%9C%97%E6%99%AE%E8%AE%BF%E5%8D%8E%E5%89%8D%E7%BE%8E%E5%95%86%E5%8A%A1%E9%83%A8%E5%88%9D%E8%A3%81%E4%B8%AD%E5%9B%BD%E9%93%9D%E7%AE%94%E5%80%BE%E9%94%80"},{"@type":"ListItem","position":10,"url":"http:\/\/cn.rfi.fr\/%E4%B8%AD%E5%9B%BD\/20171028-%E5%8D%97%E4%BA%AC%E5%A4%A7%E5%B1%A0%E6%9D%80%E9%81%87%E9%9A%BE%E5%90%8C%E8%83%9E%E7%BA%AA%E5%BF%B5%E9%A6%86%E9%A6%86%E9%95%BF%E5%90%81%E5%AE%89%E5%80%8D%E5%8F%82%E8%A7%82"},{"@type":"ListItem","position":11,"url":"http:\/\/cn.rfi.fr\/%E4%B8%AD%E5%9B%BD\/20171028-%E8%83%A1%E6%98%A5%E5%8D%8E%E8%B0%83%E7%A6%BB%E5%B9%BF%E4%B8%9C%E5%8E%BB%E5%90%91%E4%B8%8D%E6%98%8E%E5%8F%97%E5%85%B3%E6%B3%A8"},{"@type":"ListItem","position":12,"url":"http:\/\/cn.rfi.fr\/%E4%B8%AD%E5%9B%BD\/20171028-%E8%94%A1%E8%8B%B1%E6%96%87%E8%BF%87%E5%A2%83%E7%BE%8E%E5%9B%BD-%E5%8C%97%E4%BA%AC%E2%80%9C%E4%B8%A5%E6%AD%A3%E4%BA%A4%E6%B6%89%E2%80%9D"},{"@type":"ListItem","position":13,"url":"http:\/\/cn.rfi.fr\/%E4%B8%AD%E5%9B%BD\/20171028-19%E5%90%8D%E5%8F%B0%E6%B9%BE%E4%BA%BA%E5%9C%A8%E6%9F%AC%E6%B6%89%E7%94%B5%E4%BF%A1%E8%AF%88%E9%AA%97%E8%A2%AB%E9%81%A3%E9%80%81%E4%B8%AD%E5%9B%BD%E5%A4%A7%E9%99%86%E5%8F%B0%E6%B9%BE%E6%8A%97%E8%AE%AE"},{"@type":"ListItem","position":14,"url":"http:\/\/cn.rfi.fr\/%E4%B8%AD%E5%9B%BD\/20171028-%E9%87%91%E8%9E%8D%E6%97%B6%E6%8A%A5%E6%8F%AD%E5%BC%80%E7%BB%9F%E6%88%98%E9%83%A8%E7%A5%9E%E7%A7%98%E9%9D%A2%E7%BA%B1%E8%A7%A3%E6%9E%90%E4%B8%AD%E5%9B%BD%E8%BD%AF%E5%AE%9E%E5%8A%9B%E7%9A%84%E6%B3%95%E5%AE%9D"},{"@type":"ListItem","position":15,"url":"http:\/\/cn.rfi.fr\/%E4%B8%AD%E5%9B%BD\/20171028-%E4%B9%A0%E6%80%BB%E5%85%A8%E9%9D%A2%E5%AF%B9%E9%A6%99%E6%B8%AF%E7%AE%A1%E6%B2%BB%E6%9D%83%E5%8E%9F%E6%9D%A5%E5%8F%AA%E9%92%88%E5%AF%B9%E6%9E%81%E5%B0%91%E6%95%B0%E4%BA%BA"}]}</script>

            </head>

    <body class="desktop player-closed ">
                                    <header>
                <div class="wrapper">
                                            <div class="logo">
                            <a class="modeless" href="/">
                                                                法广-法国国际广播电台-时事与新闻直播
                                                                                                                                </a>
                        </div>
                                        <nav id="nav-main">
                                                                            <ul>
                                                                                                                    <li>
                                            

                                                                                                                                                                                                                                                                                                                                                                                                                                                                    
                                                                                    <a href="/" class="modeless " title="法广-法国国际广播电台-时事与新闻直播">首页</a>
                                                                            
                                                                                    </li>
                                                                                                            <li>
                                            

                                                                                                                                                                                                                                                                                                                                                                                                                                                                    
                                                                                    <a href="/%E4%B8%AD%E5%9B%BD/" class="modeless active" title="中国时事">中国</a>
                                                                            
                                                                                    </li>
                                                                                                            <li>
                                            

                                                                                                                                                                                                                                                                                                                                                                                                                                                                    
                                                                                    <a href="/%E6%B8%AF%E6%BE%B3%E5%8F%B0/" class="modeless " title="港澳台时事">港澳台</a>
                                                                            
                                                                                    </li>
                                                                                                            <li>
                                            

                                                                                                                                                                                                                                                                                                                                                                                                                                                                    
                                                                                    <a href="/%E6%B3%95%E5%9B%BD/" class="modeless " title="法国时事">法国</a>
                                                                            
                                                                                    </li>
                                                                                                            <li>
                                            

                                                                                                                                                                                                                                                                                                                                                                                                                                                                    
                                                                                    <a href="/%E4%BA%9A%E6%B4%B2/" class="modeless " title="亚洲时事">亚洲</a>
                                                                            
                                                                                    </li>
                                                                                                            <li>
                                                                    <span>世界</span>
                                                                                        <ul>
                                                                                                                    <li>
                                            

                                                                                                                                                                                                                                                                                                                                                                                                                                                                    
                                                                                    <a href="/%E9%9D%9E%E6%B4%B2/" class="modeless " title="非洲时事">非洲</a>
                                                                            
                                                                                    </li>
                                                                                                            <li>
                                            

                                                                                                                                                                                                                                                                                                                                                                                                                                                                    
                                                                                    <a href="/%E4%B8%AD%E4%B8%9C/" class="modeless " title="中东与阿拉伯世界时事">中东</a>
                                                                            
                                                                                    </li>
                                                                                                            <li>
                                            

                                                                                                                                                                                                                                                                                                                                                                                                                                                                    
                                                                                    <a href="/%E6%AC%A7%E6%B4%B2/" class="modeless " title="欧洲时事">欧洲</a>
                                                                            
                                                                                    </li>
                                                                                                            <li>
                                            

                                                                                                                                                                                                                                                                                                                                                                                                                                                                    
                                                                                    <a href="/%E7%BE%8E%E6%B4%B2/" class="modeless " title="美洲时事">美洲</a>
                                                                            
                                                                                    </li>
                        </ul>

                                                            </li>
                                                                                                            <li>
                                            

                                                                                                                                                                                                                                                                                                                                                                                                                                                                    
                                                                                    <a href="/%E5%9B%BD%E9%99%85/" class="modeless " title="国际时事">国际</a>
                                                                            
                                                                                    </li>
                                                                                                            <li>
                                            

                                                                                                                                                                                                                                                                                                                                                                                                                                                                    
                                                                                    <a href="/%E4%BA%BA%E6%9D%83/" class="modeless " title="人权时事">人权</a>
                                                                            
                                                                                    </li>
                                                                                                            <li>
                                            

                                                                                                                                                                                                                                                                                                                                                                                                                                                                    
                                                                                    <a href="/%E6%94%BF%E6%B2%BB/" class="modeless " title="政治时事">政治</a>
                                                                            
                                                                                    </li>
                                                                                                            <li>
                                            

                                                                                                                                                                                                                                                                                                                                                                                                                                                                    
                                                                                    <a href="/%E7%BB%8F%E8%B4%B8/" class="modeless " title="经济时事">经贸</a>
                                                                            
                                                                                    </li>
                                                                                                            <li>
                                            

                                                                                                                                                                                                                                                                                                                                                                                                                                                                    
                                                                                    <a href="/%E7%A4%BE%E4%BC%9A/" class="modeless " title="社会时事">社会</a>
                                                                            
                                                                                    </li>
                                                                                                            <li>
                                            

                                                                                                                                                                                                                                                                                                                                                                                                                                                                    
                                                                                    <a href="/%E7%94%9F%E6%80%81/" class="modeless " title="生态与环境时事">生态</a>
                                                                            
                                                                                    </li>
                                                                                                            <li>
                                            

                                                                                                                                                                                                                                                                                                                                                                                                                                                                    
                                                                                    <a href="/%E7%A7%91%E6%8A%80%E4%B8%8E%E6%96%87%E5%8C%96/" class="modeless " title="文化与科技时事">科技与文化</a>
                                                                            
                                                                                    </li>
                                                                                                            <li>
                                                                    <span>法新社</span>
                                                                                        <ul>
                                                                                                                    <li>
                                            

                                                                                                                                                                                                                                                                                                                                                                                                                                                                    
                                                                                    <a href="/wire/%E6%9C%80%E6%96%B0%E6%B6%88%E6%81%AF/" class="modeless " title="最新消息时事">最新消息</a>
                                                                            
                                                                                    </li>
                                                                                                            <li>
                                            

                                                                                                                                                                                                                                                                                                                                                                                                                                                                    
                                                                                    <a href="/wire/%E5%9B%BD%E9%99%85/" class="modeless " title="国际时事">国际</a>
                                                                            
                                                                                    </li>
                                                                                                            <li>
                                            

                                                                                                                                                                                                                                                                                                                                                                                                                                                                    
                                                                                    <a href="/wire/%E7%BB%8F%E6%B5%8E/" class="modeless " title="经济时事">经济</a>
                                                                            
                                                                                    </li>
                                                                                                            <li>
                                            

                                                                                                                                                                                                                                                                                                                                                                                                                                                                    
                                                                                    <a href="/wire/%E4%BD%93%E8%82%B2/" class="modeless " title="体育时事">体育</a>
                                                                            
                                                                                    </li>
                                                                                                            <li>
                                            

                                                                                                                                                                                                                                                                                                                                                                                                                                                                    
                                                                                    <a href="/wire/%E5%81%A5%E5%BA%B7/" class="modeless " title="健康时事">健康</a>
                                                                            
                                                                                    </li>
                                                                                                            <li>
                                            

                                                                                                                                                                                                                                                                                                                                                                                                                                                                    
                                                                                    <a href="/wire/%E5%90%8D%E6%B5%81/" class="modeless " title="名流时事">名流</a>
                                                                            
                                                                                    </li>
                        </ul>

                                                            </li>
                                                                                                                                                <li>
                                            

                                                                                                                                                                                                                                                                                                                                                                                                                                                                    
                                                                                    <a href="/%E4%B8%93%E6%A0%8F%E6%A3%80%E7%B4%A2/" class="modeless alt" title="法广节目表">专栏检索</a>
                                                                            
                                                                                    </li>
                        </ul>

                                            </nav>
                    <dialog class="h-search-bar">
                                                    <form name="Search" method="get" action="/search/" id="sinequa-search-form"><div><label for="Search_term" class="required">主题</label><input type="text" id="Search_term" name="Search[term]" required="required" /></div><input type="hidden" id="Search_page" name="Search[page]" value="1" /><div><button type="submit">开始搜寻</button></div><div><label class="required">Filters</label><div id="Search_filters"></div></div></form>
                                            </dialog>
                                                <div>
                    <ul class="h-menu">
                                                                                                                                                                                                                                                                                                                                                                                                                        <li >
                                                    <a  class="rfi-langue-francaise" title="学法语" href="http://savoirs.rfi.fr/cn/apprendre-enseigner" target="_blank">学法语</a>
                                                                    </li>
                                                                                                                                                                                                                                                                                                                                                                                                                        <li >
                                                    <a  class="rfi-musique" title="法广音乐" href="http://musique.rfi.fr" target="_blank">法广音乐</a>
                                                                    </li>
                                                                                                                                                                                                                                                                                                                                                                    <li >
                                                    <a  class="h-search" title="搜索" href="#">搜索</a>
                                                                    </li>
                                                                                                                                                                                                                                                                                                                                                                                                                <li  id="fmm-sites">
                                                    <a  title="France Médias Monde" href="#">France Médias Monde</a>
                                                                                                                                                                                                                                                                    <ul  class="h-fmm-sites">
                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                    <li >
                                                                                    <a  title="France 24" href="http://www.france24.com/fr/" target="_blank">France 24</a>
                                                                            </li>
                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                    <li >
                                                                                    <a  title="Monte Carlo Doualiya" href="http://www.mc-doualiya.com/" target="_blank">Monte Carlo Doualiya</a>
                                                                            </li>
                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                    <li >
                                                                                    <a  title="Les Observateurs" href="http://observers.france24.com/fr" target="_blank">Les Observateurs</a>
                                                                            </li>
                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                    <li >
                                                                                    <a  title="Académie" href="http://academie.france24-mcd-rfi.com/fr" target="_blank">Académie</a>
                                                                            </li>
                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                    <li >
                                                                                    <a  title="France Médias Monde" href="http://www.francemediasmonde.com/" target="_blank">France Médias Monde</a>
                                                                            </li>
                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                    <li >
                                                                                    <a  title="Atelier des médias" href="http://atelier.rfi.fr/" target="_blank">Atelier des médias</a>
                                                                            </li>
                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                    <li >
                                                                                    <a  title="Mondoblog" href="http://mondoblog.org/" target="_blank">Mondoblog</a>
                                                                            </li>
                                                            </ul>
                                            </li>
                                                                                                                                                                                                                                                                                                                                                                                                                        <li >
                                                    <a  class="modeless" title="电邮新闻" id="newsletter" href="/简讯">电邮新闻</a>
                                                                    </li>
                                                                                                                                                                                                                                                                                                                                                                    <li >
                                                    <a  title="低宽带" id="lowres" href="http://m.cn.rfi.fr">低宽带</a>
                                                                    </li>
                                                                                                                                                                                                                                                                                                                <li >
                                                    <a  title="简" href="http://trad.cn.rfi.fr/">繁</a>
                                                                    </li>
                            </ul>
        
                
                                                                                                                                                                                                                                                                                        <div  class="h-langs">
                <a  class="modeless" title="法广十五种语言" href="/语种">法广十五种语言</a>
            </div>
            </div>

                    
                                            <div id="player">
                            <!-- div id="main-player" style="height: 0px" class="bsplayer-container"></div -->

    
<div class="pl-first-part">

        <div class="pl-categories">
        <ul>
                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                    <li  data-title="点击收听网上电台" data-translate="RFI en chinois" data-stream="chinois">
                    <a  titre="网上电台" data-translate="RFI en chinois" href="#">网上电台</a>
                                    </li>
                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                    <li  class="pl-journaux">
                    <a  class="modeless" title="新闻" data-translate="Journaux">新闻</a>
                                            <ul>
                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                    <li  data-title="最新节目" data-translate="Journal en chinois" data-stream="dernier_journal_cn"><a  title="最新节目" data-translate="Journal en chinois" href="#">最新节目</a></li>
                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                <li ><a  class="modeless" href="/所有广播新闻/">新闻</a></li>
                                                    </ul>
                                    </li>
                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                    <li  data-title="法语节目" data-translate="RFI monde" data-stream="monde">
                    <a  titre="法语节目" data-translate="RFI monde" href="#">法语节目</a>
                                    </li>
                    </ul>
    </div>


    <div class="pl-sound">
    <div class="pl-volume">
        <div id="volume">
            <div id="volume-range"></div>
        </div>
    </div>
    <div class="pl-playing">
        <img src="/bundles/aefhermesrfi/img/player_off.png?version=20171011171259" />
    </div>
</div>

<div class="pl-current-block">
    <p id="amount">&nbsp;</p>
    <div class="pl-current-seek">
        <div class="pl-current">

            <div class="pl-pause">
                <a href="#">Play</a>
            </div>

            <strong>
                收听
            </strong>
            <span id="current_program_infos">
                                    广播新闻
                            </span>
        </div>
        <div class="clear-both"></div>
        <div id="seek-range"></div>
    </div>
</div>
                                    
            <a href="#" title="显示阅读器" class="pl-expand">Expand Player</a>
    </div>

        <div class="pl-second-part">
                                                                                                                                                                                                                                                                                                                                                                            
            <script type="text/javascript">
    window.BSPlayer = window.BSPlayer || { items: {} };
    window.BSPlayer.items['guest-WB260175-RFI-ZH-HANS-20171030'] = {"medias":{"media":{"type":"audio","media_sources":{"media_source":[{"streaming_type":{"platforms":{"platform":["flash","html5"]},"mime_type":"audio\/mpeg","type":"audio"},"is_default":0,"source":"http:\/\/telechargement.rfi.fr\/rfi\/chinois\/audio\/modules\/actu\/201710\/1ere_tranche_291017_nuit.mp3"}]},"title":"","is_active":1,"labels":{"now":"EN CE MOMENT"},"comscore":{"baseMeasurementURL":"fr.sitestat.com\/aef\/f24-mcd-rfi\/s?","labels":{"ns_st_ci":"WB260175-RFI-ZH-HANS-20171030","ns_st_ep":"\u6cd5\u5e7f 2017\u5e7410\u670830\u65e5\u7b2c\u4e00\u6b21\u64ad\u97f3\uff08\u4e00\u5c0f\u65f6\uff09\u5317\u4eac\u65f6\u95f4 6:00\u70b9-7:00\u70b9","ns_st_pr":"\u7b2c\u4e00\u6b21\u64ad\u97f3( \u4e00\u5c0f\u65f6) \u5317\u4eac\u65f6\u95f46:00-7:00","ns_st_ty":"audio","ns_st_st":"rfi_chinois","ns_st_pl":"rfi_chinois","ns_st_el":0,"ns_st_ub":0,"ns_st_cn":1,"ns_st_cl":"","ns_st_tp":1,"ns_st_pn":"1","ns_st_dt":"2017-10-30","aef_streamtype_2":"od","aef_rep_global":"\u9996\u9875","aef_thema":"\u9996\u9875,chronique,1\u00e8re tranche manuelle","aef_type_page1":"chine.defaut.defaut","aef_type_contenu1":"audio","aef_section1":"\u9996\u9875","aef_section2":"\u7b2c\u4e00\u6b21\u64ad\u97f3(-\u4e00\u5c0f\u65f6)-\u5317\u4eac\u65f6\u95f46:00-7:00","aef_auteur":"rfi","aef_dpubli":"2017-10-30","aef_hpubli":"03:00","ns_st_li":0,"aef_marque":"rfi","name":"chine.defaut.defaut","aef_type_environnement":"site","aef_plateforme":"ordinateur","aef_nom_environnement":"rfi_site","aef_version_environnement":"v2.46.9","aef_perimetre_diffusion":"interne","aef_url_provenance":"http:\/\/cn.rfi.fr\/%E4%B8%AD%E5%9B%BD\/all\/?page=1","aef_page_provenance":"\/%E4%B8%AD%E5%9B%BD\/all\/","aef_langue":"francais","aef_acces":"gratuit","aef_user_connection":"visiteur","aef_user_id":""}}}}};
</script>

                                                    <div class="pl-channel">
                                                                                    <a class="modeless" id="player_listen_again"
                       data-stream="guest-WB260175-RFI-ZH-HANS-20171030"
                       data-title="第一次播音( 一小时) 北京时间6:00-7:00"
                       href="http://cn.rfi.fr/%E9%A6%96%E9%A1%B5/20171030-%E6%B3%95%E5%B9%BF-2017%E5%B9%B410%E6%9C%8830%E6%97%A5%E7%AC%AC%E4%B8%80%E6%AC%A1%E6%92%AD%E9%9F%B3%E4%B8%80%E5%B0%8F%E6%97%B6%E5%8C%97%E4%BA%AC%E6%97%B6%E9%97%B4-600%E7%82%B9-700%E7%82%B9"
                       title="法广 2017年10月30日第一次播音（一小时）北京时间 6:00点-7:00点">再次收听
                    </a>
                                                <div class="clear-both"></div>
                <div class="pl-texts">
                                            <div class="title-emission">第一次播音( 一小时) 北京时间6:00-7:00</div>
                                                                                                                                                                                                <a class="modeless"
                           data-stream="guest-WB260175-RFI-ZH-HANS-20171030"
                           data-title="第一次播音( 一小时) 北京时间6:00-7:00"
                           href="http://cn.rfi.fr/%E9%A6%96%E9%A1%B5/20171030-%E6%B3%95%E5%B9%BF-2017%E5%B9%B410%E6%9C%8830%E6%97%A5%E7%AC%AC%E4%B8%80%E6%AC%A1%E6%92%AD%E9%9F%B3%E4%B8%80%E5%B0%8F%E6%97%B6%E5%8C%97%E4%BA%AC%E6%97%B6%E9%97%B4-600%E7%82%B9-700%E7%82%B9"
                           title="法广 2017年10月30日第一次播音（一小时）北京时间 6:00点-7:00点">法广 2017年10月30日第一次播音（一小时）北京时间 6:00点-7:00点
                        </a>
                                    </div>
                <div class="center-cropped" data-image="http://scd.cn.rfi.fr/sites/chinese.filesrfi/imagecache/hermes_infographie_vignette_home/sites/images.rfi.fr/files/aef_image/micro%20studio%20issy_0.jpg" data-width="105" data-height="60">
                    <img src="http://scd.cn.rfi.fr/sites/chinese.filesrfi/imagecache/hermes_infographie_vignette_home/sites/images.rfi.fr/files/aef_image/micro%20studio%20issy_0.jpg" alt="">
                </div>
            </div>
            
    </div>
    
    
    <script type="text/javascript">
    window.BSPlayer = window.BSPlayer || { items: {} };
    window.BSPlayer.items['chinois'] = {"medias":{"media":{"type":"audio","media_sources":{"media_source":[{"streaming_type":{"platforms":{"platform":["flash","html5"]},"mime_type":"audio\/mpeg","type":"audio"},"is_default":0,"source":"http:\/\/live02.rfi.fr\/rfienchinois-64.mp3"}]},"title":"\u7f51\u4e0a\u7535\u53f0","is_live":0,"is_active":1,"labels":{"now":""},"comscore":{"baseMeasurementURL":"fr.sitestat.com\/aef\/f24-mcd-rfi\/s?","labels":{"ns_st_ci":"chinois","ns_st_ep":"chinois","ns_st_pr":"chinois","ns_st_ty":"audio","ns_st_st":"rfi_chinois","ns_st_pl":"rfi_chinois","ns_st_el":0,"ns_st_ub":0,"ns_st_cn":1,"ns_st_cl":0,"ns_st_dt":"2017-10-30","aef_streamtype_2":"live","aef_rep_global":"live","aef_type_page1":"player","aef_type_contenu1":"video","aef_section1":"live","aef_auteur":"rfi","aef_dpubli":"2017-10-30","aef_hpubli":"13:00","ns_st_li":1,"aef_marque":"rfi","name":"chine.defaut.defaut","aef_type_environnement":"site","aef_plateforme":"ordinateur","aef_nom_environnement":"rfi_site","aef_version_environnement":"v2.46.9","aef_perimetre_diffusion":"interne","aef_url_provenance":"http:\/\/cn.rfi.fr\/%E4%B8%AD%E5%9B%BD\/all\/?page=1","aef_page_provenance":"\/%E4%B8%AD%E5%9B%BD\/all\/","aef_langue":"francais","aef_acces":"gratuit","aef_user_connection":"visiteur","aef_user_id":""}}}}};
</script>

    
    <script type="text/javascript">
    window.BSPlayer = window.BSPlayer || { items: {} };
    window.BSPlayer.items['dernier_journal_cn'] = {"medias":{"media":{"type":"audio","media_sources":{"media_source":[{"streaming_type":{"platforms":{"platform":["flash","html5"]},"mime_type":"audio\/mpeg","type":"audio"},"is_default":0,"source":"http:\/\/telechargement.rfi.fr\/rfi\/mandarin\/audio\/last\/RFI_Chinois_1_1.mp3"}]},"title":"\u6700\u65b0\u8282\u76ee","is_live":0,"is_active":1,"labels":{"now":""},"comscore":{"baseMeasurementURL":"fr.sitestat.com\/aef\/f24-mcd-rfi\/s?","labels":{"ns_st_ci":"dernier_journal_cn","ns_st_ep":"dernier_journal_cn","ns_st_pr":"dernier_journal_cn","ns_st_ty":"audio","ns_st_st":"rfi_chinois","ns_st_pl":"rfi_chinois","ns_st_el":0,"ns_st_ub":0,"ns_st_cn":1,"ns_st_cl":0,"ns_st_dt":"2017-10-30","aef_streamtype_2":"live","aef_rep_global":"live","aef_type_page1":"player","aef_type_contenu1":"video","aef_section1":"live","aef_auteur":"rfi","aef_dpubli":"2017-10-30","aef_hpubli":"13:00","ns_st_li":1,"aef_marque":"rfi","name":"chine.defaut.defaut","aef_type_environnement":"site","aef_plateforme":"ordinateur","aef_nom_environnement":"rfi_site","aef_version_environnement":"v2.46.9","aef_perimetre_diffusion":"interne","aef_url_provenance":"http:\/\/cn.rfi.fr\/%E4%B8%AD%E5%9B%BD\/all\/?page=1","aef_page_provenance":"\/%E4%B8%AD%E5%9B%BD\/all\/","aef_langue":"francais","aef_acces":"gratuit","aef_user_connection":"visiteur","aef_user_id":""}}}}};
</script>

    
    <script type="text/javascript">
    window.BSPlayer = window.BSPlayer || { items: {} };
    window.BSPlayer.items['monde'] = {"medias":{"media":{"type":"audio","media_sources":{"media_source":[{"streaming_type":{"platforms":{"platform":["flash","html5"]},"mime_type":"audio\/mpeg","type":"audio"},"is_default":0,"source":"http:\/\/live02.rfi.fr\/rfimonde-64.mp3"}]},"title":"\u6cd5\u8bed\u8282\u76ee","is_live":1,"is_active":1,"labels":{"now":""},"comscore":{"baseMeasurementURL":"fr.sitestat.com\/aef\/f24-mcd-rfi\/s?","labels":{"ns_st_ci":"monde","ns_st_ep":"monde","ns_st_pr":"live","ns_st_ty":"audio","ns_st_st":"rfi_chinois","ns_st_pl":"rfi_chinois","ns_st_el":0,"ns_st_ub":0,"ns_st_cn":1,"ns_st_cl":0,"ns_st_dt":"2017-10-30","aef_streamtype_2":"live","aef_rep_global":"live","aef_type_page1":"player","aef_type_contenu1":"video","aef_section1":"live","aef_auteur":"rfi","aef_dpubli":"2017-10-30","aef_hpubli":"13:00","ns_st_li":1,"aef_marque":"rfi","name":"chine.defaut.defaut","aef_type_environnement":"site","aef_plateforme":"ordinateur","aef_nom_environnement":"rfi_site","aef_version_environnement":"v2.46.9","aef_perimetre_diffusion":"interne","aef_url_provenance":"http:\/\/cn.rfi.fr\/%E4%B8%AD%E5%9B%BD\/all\/?page=1","aef_page_provenance":"\/%E4%B8%AD%E5%9B%BD\/all\/","aef_langue":"francais","aef_acces":"gratuit","aef_user_connection":"visiteur","aef_user_id":""}}}}};
</script>


    <div class="pl-wrapper">
        <div class="pl-playbac">
            <div id="playbac">
    </div>
<div class="img-player">&nbsp;</div>

        </div>
                    <div class="pl-tabs pl-tabs-large pl-tabs-lower">
                <div class="pl-tab active">
                                                        
<div class="pl-past-i-btn-labels">
    <span class="i-play-label">收听</span>
        <span class="i-download-label">下载</span>
    <span class="i-podcast-label">播客</span>
</div>
<div class="pl-past-programs pl-past-play">
                                                                                <div id="pl-programs-list-1" class="pl-programs-list active" >
        <ul class="i-list">
                                                        
                <script type="text/javascript">
    window.BSPlayer = window.BSPlayer || { items: {} };
    window.BSPlayer.items['listenCAF0008F-C57C-4462-BA1F-5176578BCE6F'] = {"medias":{"media":{"type":"audio","media_sources":{"media_source":[{"streaming_type":{"platforms":{"platform":["flash","html5"]},"mime_type":"audio\/mpeg","type":"audio"},"is_default":0,"source":"http:\/\/telechargement.rfi.fr\/rfi\/chinois\/audio\/modules\/actu\/201710\/2e_tranche20171029.mp3"}]},"title":"","is_active":1,"labels":{"now":"EN CE MOMENT"},"comscore":{"baseMeasurementURL":"fr.sitestat.com\/aef\/f24-mcd-rfi\/s?","labels":{"ns_st_ci":"CAF0008F-C57C-4462-BA1F-5176578BCE6F","ns_st_ep":"\u7b2c\u4e8c\u6b21\u64ad\u97f3\uff08\u4e00\u5c0f\u65f6\uff092017\u5e7410\u670829\u65e5 \u5317\u4eac\u65f6\u95f419h00\u81f320h00","ns_st_pr":"\u7b2c\u4e8c\u6b21\u64ad\u97f3\uff08\u4e00\u5c0f\u65f6\uff09  \u5317\u4eac\u65f6\u95f4  19:00-20:00","ns_st_ty":"audio","ns_st_st":"rfi_chinois","ns_st_pl":"rfi_chinois","ns_st_el":0,"ns_st_ub":0,"ns_st_cn":1,"ns_st_cl":"","ns_st_tp":1,"ns_st_pn":"1","ns_st_dt":"2017-10-29","aef_streamtype_2":"od","aef_rep_global":"\u9996\u9875","aef_thema":"\u9996\u9875,\u6cd5\u5e7f,chronique,2e tranche manuelle","aef_type_page1":"chine.defaut.defaut","aef_type_contenu1":"audio","aef_section1":"\u9996\u9875","aef_section2":"\u7b2c\u4e8c\u6b21\u64ad\u97f3\uff08\u4e00\u5c0f\u65f6\uff09-\u5317\u4eac\u65f6\u95f4-19:00-20:00","aef_auteur":"\u6cd5\u5e7f","aef_dpubli":"2017-10-29","aef_hpubli":"03:00","ns_st_li":0,"aef_marque":"rfi","name":"chine.defaut.defaut","aef_type_environnement":"site","aef_plateforme":"ordinateur","aef_nom_environnement":"rfi_site","aef_version_environnement":"v2.46.9","aef_perimetre_diffusion":"interne","aef_url_provenance":"http:\/\/cn.rfi.fr\/%E4%B8%AD%E5%9B%BD\/all\/?page=1","aef_page_provenance":"\/%E4%B8%AD%E5%9B%BD\/all\/","aef_langue":"francais","aef_acces":"gratuit","aef_user_connection":"visiteur","aef_user_id":""}}}}};
</script>

                <li data-bo-type="edition" data-bo-nid="CAF0008F-C57C-4462-BA1F-5176578BCE6F">
                    <strong>第二次播音（一小时）  北京时间  19:00-20:00</strong><div class="news-block-title"> 第二次播音（一小时）2017年10月29日 北京时间19h00至20h00</div>
                    <ul class="i-actions actions">
                        <li class="audio">
                            <a href="#" class="i-play" data-header="true" data-label-class="pl-past-i-btn-labels" data-title="&#x7B2C;&#x4E8C;&#x6B21;&#x64AD;&#x97F3;&#xFF08;&#x4E00;&#x5C0F;&#x65F6;&#xFF09;2017&#x5E74;10&#x6708;29&#x65E5;&#x20;&#x5317;&#x4EAC;&#x65F6;&#x95F4;19h00&#x81F3;20h00" data-stream="listenCAF0008F-C57C-4462-BA1F-5176578BCE6F">阅读</a>
                        </li>
                        <li class="fav">
                            <a href="http://telechargement.rfi.fr/rfi/chinois/audio/modules/actu/201710/2e_tranche20171029.mp3" class="i-download" data-header="true" data-label-class="pl-past-i-btn-labels" target="_blank">录制</a>
                        </li>

                                                    <li class="podcast">
                                <a href="http://www.rfi.fr/radiofr/podcast/Podcast_CN_TRANCHE3.xml" class="i-podcast" data-header="true" data-label-class="pl-past-i-btn-labels" target="_blank">录制</a>
                            </li>
                                            </ul>
                </li>
                                            
                <script type="text/javascript">
    window.BSPlayer = window.BSPlayer || { items: {} };
    window.BSPlayer.items['listenWB260054-RFI-ZH-HANS-20171028'] = {"medias":{"media":{"type":"audio","media_sources":{"media_source":[{"streaming_type":{"platforms":{"platform":["flash","html5"]},"mime_type":"audio\/mpeg","type":"audio"},"is_default":0,"source":"http:\/\/telechargement.rfi.fr\/rfi\/mandarin\/audio\/magazines\/r001\/19_00_-_19_15_20171028.mp3"}]},"title":"","is_active":1,"labels":{"now":"EN CE MOMENT"},"comscore":{"baseMeasurementURL":"fr.sitestat.com\/aef\/f24-mcd-rfi\/s?","labels":{"ns_st_ci":"WB260054-RFI-ZH-HANS-20171028","ns_st_ep":"\u65b0\u95fb\u8282\u76ee 28\/10 11h00 GMT","ns_st_pr":"\u7b2c\u4e8c\u6b21\u64ad\u97f3\uff08\u65b0\u95fb\uff0919\uff1a00 - 19\uff1a15\uff08\u5317\u4eac\u65f6\u95f4 \uff09","ns_st_ty":"audio","ns_st_st":"rfi_chinois","ns_st_pl":"rfi_chinois","ns_st_el":0,"ns_st_ub":0,"ns_st_cn":1,"ns_st_cl":"","ns_st_tp":1,"ns_st_pn":"1","ns_st_dt":"2017-10-28","aef_streamtype_2":"od","aef_rep_global":"20171028-\u65b0\u95fb\u8282\u76ee-2810-11h00-gmt","aef_thema":"journal,m,lngmandaviol110000111500","aef_type_page1":"chine.defaut.defaut","aef_type_contenu1":"audio","aef_section1":"20171028-\u65b0\u95fb\u8282\u76ee-2810-11h00-gmt","aef_section2":"emission-mandarin-11h00-11h15-tu","aef_auteur":"rfi","aef_dpubli":"2017-10-28","aef_hpubli":"13:00","ns_st_li":0,"aef_marque":"rfi","name":"chine.defaut.defaut","aef_type_environnement":"site","aef_plateforme":"ordinateur","aef_nom_environnement":"rfi_site","aef_version_environnement":"v2.46.9","aef_perimetre_diffusion":"interne","aef_url_provenance":"http:\/\/cn.rfi.fr\/%E4%B8%AD%E5%9B%BD\/all\/?page=1","aef_page_provenance":"\/%E4%B8%AD%E5%9B%BD\/all\/","aef_langue":"francais","aef_acces":"gratuit","aef_user_connection":"visiteur","aef_user_id":""}}}}};
</script>

                <li data-bo-type="edition" data-bo-nid="WB260054-RFI-ZH-HANS-20171028">
                    <strong>第二次播音（新闻）19：00 - 19：15（北京时间 ）</strong><div class="news-block-title"> 新闻节目 28/10 11h00 GMT</div>
                    <ul class="i-actions actions">
                        <li class="audio">
                            <a href="#" class="i-play" data-header="true" data-label-class="pl-past-i-btn-labels" data-title="&#x65B0;&#x95FB;&#x8282;&#x76EE;&#x20;28&#x2F;10&#x20;11h00&#x20;GMT" data-stream="listenWB260054-RFI-ZH-HANS-20171028">阅读</a>
                        </li>
                        <li class="fav">
                            <a href="http://telechargement.rfi.fr/rfi/mandarin/audio/magazines/r001/19_00_-_19_15_20171028.mp3" class="i-download" data-header="true" data-label-class="pl-past-i-btn-labels" target="_blank">录制</a>
                        </li>

                                                    <li class="podcast">
                                <a href="http://cn.rfi.fr/%E4%B8%93%E6%A0%8F%E6%A3%80%E7%B4%A2/emission-mandarin-11h00-11h15-tu/podcast" class="i-podcast" data-header="true" data-label-class="pl-past-i-btn-labels" target="_blank">录制</a>
                            </li>
                                            </ul>
                </li>
                                            
                <script type="text/javascript">
    window.BSPlayer = window.BSPlayer || { items: {} };
    window.BSPlayer.items['listenWB260060-RFI-ZH-HANS-20171028'] = {"medias":{"media":{"type":"audio","media_sources":{"media_source":[{"streaming_type":{"platforms":{"platform":["flash","html5"]},"mime_type":"audio\/mpeg","type":"audio"},"is_default":0,"source":"http:\/\/telechargement.rfi.fr\/rfi\/mandarin\/audio\/magazines\/r001\/19_15_-_20_00_20171028.mp3"}]},"title":"","is_active":1,"labels":{"now":"EN CE MOMENT"},"comscore":{"baseMeasurementURL":"fr.sitestat.com\/aef\/f24-mcd-rfi\/s?","labels":{"ns_st_ci":"WB260060-RFI-ZH-HANS-20171028","ns_st_ep":"\u5176\u5b83\u8282\u76ee 28\/10 11h15 GMT","ns_st_pr":"\u7b2c\u4e8c\u6b21\u64ad\u97f3\uff08\u65f6\u4e8b\u4e0e\u4e13\u9898\uff0919\uff1a15 - 20\uff1a00\uff08\u5317\u4eac\u65f6\u95f4\uff09","ns_st_ty":"audio","ns_st_st":"rfi_chinois","ns_st_pl":"rfi_chinois","ns_st_el":0,"ns_st_ub":0,"ns_st_cn":1,"ns_st_cl":"","ns_st_tp":1,"ns_st_pn":"1","ns_st_dt":"2017-10-28","aef_streamtype_2":"od","aef_rep_global":"20171028-\u5176\u5b83\u8282\u76ee-2810-11h15-gmt","aef_thema":"tranche d'information,m,lngmandaviol111500120000","aef_type_page1":"chine.defaut.defaut","aef_type_contenu1":"audio","aef_section1":"20171028-\u5176\u5b83\u8282\u76ee-2810-11h15-gmt","aef_section2":"emission-mandarin-11h15-12h00-tu","aef_auteur":"rfi","aef_dpubli":"2017-10-28","aef_hpubli":"13:15","ns_st_li":0,"aef_marque":"rfi","name":"chine.defaut.defaut","aef_type_environnement":"site","aef_plateforme":"ordinateur","aef_nom_environnement":"rfi_site","aef_version_environnement":"v2.46.9","aef_perimetre_diffusion":"interne","aef_url_provenance":"http:\/\/cn.rfi.fr\/%E4%B8%AD%E5%9B%BD\/all\/?page=1","aef_page_provenance":"\/%E4%B8%AD%E5%9B%BD\/all\/","aef_langue":"francais","aef_acces":"gratuit","aef_user_connection":"visiteur","aef_user_id":""}}}}};
</script>

                <li data-bo-type="edition" data-bo-nid="WB260060-RFI-ZH-HANS-20171028">
                    <strong>第二次播音（时事与专题）19：15 - 20：00（北京时间）</strong><div class="news-block-title"> 其它节目 28/10 11h15 GMT</div>
                    <ul class="i-actions actions">
                        <li class="audio">
                            <a href="#" class="i-play" data-header="true" data-label-class="pl-past-i-btn-labels" data-title="&#x5176;&#x5B83;&#x8282;&#x76EE;&#x20;28&#x2F;10&#x20;11h15&#x20;GMT" data-stream="listenWB260060-RFI-ZH-HANS-20171028">阅读</a>
                        </li>
                        <li class="fav">
                            <a href="http://telechargement.rfi.fr/rfi/mandarin/audio/magazines/r001/19_15_-_20_00_20171028.mp3" class="i-download" data-header="true" data-label-class="pl-past-i-btn-labels" target="_blank">录制</a>
                        </li>

                                                    <li class="podcast">
                                <a href="http://cn.rfi.fr/%E4%B8%93%E6%A0%8F%E6%A3%80%E7%B4%A2/emission-mandarin-11h15-12h00-tu/podcast" class="i-podcast" data-header="true" data-label-class="pl-past-i-btn-labels" target="_blank">录制</a>
                            </li>
                                            </ul>
                </li>
                                            
                <script type="text/javascript">
    window.BSPlayer = window.BSPlayer || { items: {} };
    window.BSPlayer.items['listenWB260175-RFI-ZH-HANS-20171030'] = {"medias":{"media":{"type":"audio","media_sources":{"media_source":[{"streaming_type":{"platforms":{"platform":["flash","html5"]},"mime_type":"audio\/mpeg","type":"audio"},"is_default":0,"source":"http:\/\/telechargement.rfi.fr\/rfi\/chinois\/audio\/modules\/actu\/201710\/1ere_tranche_291017_nuit.mp3"}]},"title":"","is_active":1,"labels":{"now":"EN CE MOMENT"},"comscore":{"baseMeasurementURL":"fr.sitestat.com\/aef\/f24-mcd-rfi\/s?","labels":{"ns_st_ci":"WB260175-RFI-ZH-HANS-20171030","ns_st_ep":"\u6cd5\u5e7f 2017\u5e7410\u670830\u65e5\u7b2c\u4e00\u6b21\u64ad\u97f3\uff08\u4e00\u5c0f\u65f6\uff09\u5317\u4eac\u65f6\u95f4 6:00\u70b9-7:00\u70b9","ns_st_pr":"\u7b2c\u4e00\u6b21\u64ad\u97f3( \u4e00\u5c0f\u65f6) \u5317\u4eac\u65f6\u95f46:00-7:00","ns_st_ty":"audio","ns_st_st":"rfi_chinois","ns_st_pl":"rfi_chinois","ns_st_el":0,"ns_st_ub":0,"ns_st_cn":1,"ns_st_cl":"","ns_st_tp":1,"ns_st_pn":"1","ns_st_dt":"2017-10-30","aef_streamtype_2":"od","aef_rep_global":"\u9996\u9875","aef_thema":"\u9996\u9875,chronique,1\u00e8re tranche manuelle","aef_type_page1":"chine.defaut.defaut","aef_type_contenu1":"audio","aef_section1":"\u9996\u9875","aef_section2":"\u7b2c\u4e00\u6b21\u64ad\u97f3(-\u4e00\u5c0f\u65f6)-\u5317\u4eac\u65f6\u95f46:00-7:00","aef_auteur":"rfi","aef_dpubli":"2017-10-30","aef_hpubli":"03:00","ns_st_li":0,"aef_marque":"rfi","name":"chine.defaut.defaut","aef_type_environnement":"site","aef_plateforme":"ordinateur","aef_nom_environnement":"rfi_site","aef_version_environnement":"v2.46.9","aef_perimetre_diffusion":"interne","aef_url_provenance":"http:\/\/cn.rfi.fr\/%E4%B8%AD%E5%9B%BD\/all\/?page=1","aef_page_provenance":"\/%E4%B8%AD%E5%9B%BD\/all\/","aef_langue":"francais","aef_acces":"gratuit","aef_user_connection":"visiteur","aef_user_id":""}}}}};
</script>

                <li data-bo-type="edition" data-bo-nid="WB260175-RFI-ZH-HANS-20171030">
                    <strong>第一次播音( 一小时) 北京时间6:00-7:00</strong><div class="news-block-title"> 法广 2017年10月30日第一次播音（一小时）北京时间 6:00点-7:00点</div>
                    <ul class="i-actions actions">
                        <li class="audio">
                            <a href="#" class="i-play" data-header="true" data-label-class="pl-past-i-btn-labels" data-title="&#x6CD5;&#x5E7F;&#x20;2017&#x5E74;10&#x6708;30&#x65E5;&#x7B2C;&#x4E00;&#x6B21;&#x64AD;&#x97F3;&#xFF08;&#x4E00;&#x5C0F;&#x65F6;&#xFF09;&#x5317;&#x4EAC;&#x65F6;&#x95F4;&#x20;6&#x3A;00&#x70B9;-7&#x3A;00&#x70B9;" data-stream="listenWB260175-RFI-ZH-HANS-20171030">阅读</a>
                        </li>
                        <li class="fav">
                            <a href="http://telechargement.rfi.fr/rfi/chinois/audio/modules/actu/201710/1ere_tranche_291017_nuit.mp3" class="i-download" data-header="true" data-label-class="pl-past-i-btn-labels" target="_blank">录制</a>
                        </li>

                                                    <li class="podcast">
                                <a href="http://cn.rfi.fr/%E4%B8%93%E6%A0%8F%E6%A3%80%E7%B4%A2/%E7%AC%AC%E4%B8%80%E6%AC%A1%E6%92%AD%E9%9F%B3%28-%E4%B8%80%E5%B0%8F%E6%97%B6%29-%E5%8C%97%E4%BA%AC%E6%97%B6%E9%97%B46:00-7:00/podcast" class="i-podcast" data-header="true" data-label-class="pl-past-i-btn-labels" target="_blank">录制</a>
                            </li>
                                            </ul>
                </li>
                                </ul>
    </div>


</div>
    
                            
                </div>
            </div>
                <div class="pl-recommended">
            
    <div class="title-recommended-player">最新专题</div>
    <ul>
                                                            
            <script type="text/javascript">
    window.BSPlayer = window.BSPlayer || { items: {} };
    window.BSPlayer.items['articleWB260215-RFI-ZH-HANS-20171030'] = {"medias":{"media":{"type":"audio","media_sources":{"media_source":[{"streaming_type":{"platforms":{"platform":["flash","html5"]},"mime_type":"audio\/mpeg","type":"audio"},"is_default":0,"source":"http:\/\/telechargement.rfi.fr\/rfi\/chinois\/audio\/modules\/actu\/201710\/chronique_USA_30-10-17_SEM44.mp3"}]},"photo_url":"\/bundles\/aefhermesrfi\/img\/image_generique_player_big.jpg?version=20171011171259","title":"","is_active":1,"labels":{"now":"EN CE MOMENT"},"comscore":{"baseMeasurementURL":"fr.sitestat.com\/aef\/f24-mcd-rfi\/s?","labels":{"ns_st_ci":"WB260215-RFI-ZH-HANS-20171030","ns_st_ep":"\u62c9\u65af\u7ef4\u52a0\u65af\u67aa\u51fb\u6848\u4e00\u4e2a\u6708\uff0c\u5df2\u542c\u4e0d\u5230\u63a7\u67aa\u58f0\u97f3\uff0c59\u540d\u9047\u96be\u8005\u53c8\u767d\u6b7b\u4e86","ns_st_pr":"\u7f8e\u56fd\u4e13\u680f","ns_st_ty":"audio","ns_st_st":"rfi_chinois","ns_st_pl":"rfi_chinois","ns_st_el":0,"ns_st_ub":0,"ns_st_cn":1,"ns_st_cl":"","ns_st_tp":1,"ns_st_pn":"1","ns_st_dt":"2017-10-30","aef_streamtype_2":"od","aef_rep_global":"\u653f\u6cbb","aef_thema":"\u653f\u6cbb,\u793e\u4f1a,\u7f8e\u6d32,\u7f8e\u56fd,\u793e\u4f1a,\u653f\u6cbb,\u65e7\u91d1\u5c71\u7279\u7ea6\u8bb0\u8005 \u738b\u5c71,magazine,\u7f8e\u56fd\u4e13\u680f","aef_type_page1":"chine.defaut.defaut","aef_type_contenu1":"audio","aef_section1":"\u653f\u6cbb","aef_section2":"\u7f8e\u56fd\u4e13\u680f","aef_auteur":"\u65e7\u91d1\u5c71\u7279\u7ea6\u8bb0\u8005 \u738b\u5c71","aef_dpubli":"2017-10-30","aef_hpubli":"03:00","ns_st_li":0,"aef_marque":"rfi","name":"chine.defaut.defaut","aef_type_environnement":"site","aef_plateforme":"ordinateur","aef_nom_environnement":"rfi_site","aef_version_environnement":"v2.46.9","aef_perimetre_diffusion":"interne","aef_url_provenance":"http:\/\/cn.rfi.fr\/%E4%B8%AD%E5%9B%BD\/all\/?page=1","aef_page_provenance":"\/%E4%B8%AD%E5%9B%BD\/all\/","aef_langue":"francais","aef_acces":"gratuit","aef_user_connection":"visiteur","aef_user_id":""}}}}};
</script>

            <li data-bo-type="edition" data-bo-nid="WB260215-RFI-ZH-HANS-20171030">
                                                                                                                                                                                                                                                                                                  <a href="#" class="media-play media" data-title="美国专栏"
                   data-stream="articleWB260215-RFI-ZH-HANS-20171030" data-player="main-player">
                                            <img src="http://scd.cn.rfi.fr/sites/chinese.filesrfi/dynimagecache/0/134/768/378/177/87/sites/images.rfi.fr/files/aef_image/063_8565204461_0.jpg" alt="media" width="150" height="85" />
                                        <div class="media-play-img"></div>
                </a>
                <div class="meta">
                    <time datetime="17-10-30">10/30/17</time>
                                        <span>美国专栏</span>
                </div>
                <div class="title-emission"><a class="modeless" href="/%E6%94%BF%E6%B2%BB/20171030-%E6%8B%89%E6%96%AF%E7%BB%B4%E5%8A%A0%E6%96%AF%E6%9E%AA%E5%87%BB%E6%A1%88%E4%B8%80%E4%B8%AA%E6%9C%88%EF%BC%8C%E5%B7%B2%E5%90%AC%E4%B8%8D%E5%88%B0%E6%8E%A7%E6%9E%AA%E5%A3%B0%E9%9F%B3%EF%BC%8C59%E5%90%8D%E9%81%87%E9%9A%BE%E8%80%85%E5%8F%88%E7%99%BD%E6%AD%BB%E4%BA%86">拉斯维加斯枪击案一个月，已听不到控枪声音，59名遇难者又白死了</a></div>
            </li>
                                                        
            <script type="text/javascript">
    window.BSPlayer = window.BSPlayer || { items: {} };
    window.BSPlayer.items['articleA16F8CD1-07EE-4527-A242-A62E98109367'] = {"medias":{"media":{"type":"audio","media_sources":{"media_source":[{"streaming_type":{"platforms":{"platform":["flash","html5"]},"mime_type":"audio\/mpeg","type":"audio"},"is_default":0,"source":"http:\/\/telechargement.rfi.fr\/rfi\/chinois\/audio\/modules\/actu\/201710\/Chr_Bangkok_29-10-17_SEM43.mp3"}]},"photo_url":"\/bundles\/aefhermesrfi\/img\/image_generique_player_big.jpg?version=20171011171259","title":"","is_active":1,"labels":{"now":"EN CE MOMENT"},"comscore":{"baseMeasurementURL":"fr.sitestat.com\/aef\/f24-mcd-rfi\/s?","labels":{"ns_st_ci":"A16F8CD1-07EE-4527-A242-A62E98109367","ns_st_ep":"\u674e\u663e\u9f99\u8bbf\u7f8e \u7f8e\u56fd\u4e9a\u6d32\u653f\u7b56\u8d8b\u660e\u6717","ns_st_pr":"\u66fc\u8c37\u4e13\u680f","ns_st_ty":"audio","ns_st_st":"rfi_chinois","ns_st_pl":"rfi_chinois","ns_st_el":0,"ns_st_ub":0,"ns_st_cn":1,"ns_st_cl":"","ns_st_tp":1,"ns_st_pn":"1","ns_st_dt":"2017-10-29","aef_streamtype_2":"od","aef_rep_global":"\u4e9a\u6d32","aef_thema":"\u4e9a\u6d32,\u65b0\u52a0\u5761,\u7f8e\u56fd,\u4e9a\u6d32,\u653f\u6cbb,\u66fc\u8c37\u7279\u7ea6\u8bb0\u8005 \u6c5f\u67ab,magazine,\u66fc\u8c37\u4e13\u680f","aef_type_page1":"chine.defaut.defaut","aef_type_contenu1":"audio","aef_section1":"\u4e9a\u6d32","aef_section2":"\u66fc\u8c37\u4e13\u680f","aef_auteur":"\u66fc\u8c37\u7279\u7ea6\u8bb0\u8005 \u6c5f\u67ab","aef_dpubli":"2017-10-29","aef_hpubli":"03:00","ns_st_li":0,"aef_marque":"rfi","name":"chine.defaut.defaut","aef_type_environnement":"site","aef_plateforme":"ordinateur","aef_nom_environnement":"rfi_site","aef_version_environnement":"v2.46.9","aef_perimetre_diffusion":"interne","aef_url_provenance":"http:\/\/cn.rfi.fr\/%E4%B8%AD%E5%9B%BD\/all\/?page=1","aef_page_provenance":"\/%E4%B8%AD%E5%9B%BD\/all\/","aef_langue":"francais","aef_acces":"gratuit","aef_user_connection":"visiteur","aef_user_id":""}}}}};
</script>

            <li data-bo-type="edition" data-bo-nid="A16F8CD1-07EE-4527-A242-A62E98109367">
                                                                                                                                                                                                                                                                                                  <a href="#" class="media-play media" data-title="曼谷专栏"
                   data-stream="articleA16F8CD1-07EE-4527-A242-A62E98109367" data-player="main-player">
                                            <img src="http://scd.cn.rfi.fr/sites/chinese.filesrfi/dynimagecache/0/245/3500/1720/177/87/sites/images.rfi.fr/files/aef_image/2017-10-23t184449z_2076997793_rc1f6d8fc280_rtrmadp_3_usa-singapore.jpg" alt="media" width="150" height="85" />
                                        <div class="media-play-img"></div>
                </a>
                <div class="meta">
                    <time datetime="17-10-29">10/29/17</time>
                                        <span>曼谷专栏</span>
                </div>
                <div class="title-emission"><a class="modeless" href="/%E4%BA%9A%E6%B4%B2/20171029-%E6%9D%8E%E6%98%BE%E9%BE%99%E8%AE%BF%E7%BE%8E-%E7%BE%8E%E5%9B%BD%E4%BA%9A%E6%B4%B2%E6%94%BF%E7%AD%96%E8%B6%8B%E6%98%8E%E6%9C%97">李显龙访美 美国亚洲政策趋明朗</a></div>
            </li>
                                                        
            <script type="text/javascript">
    window.BSPlayer = window.BSPlayer || { items: {} };
    window.BSPlayer.items['articleWB260051-RFI-ZH-HANS-20171028'] = {"medias":{"media":{"type":"audio","media_sources":{"media_source":[{"streaming_type":{"platforms":{"platform":["flash","html5"]},"mime_type":"audio\/mpeg","type":"audio"},"is_default":0,"source":"http:\/\/telechargement.rfi.fr\/rfi\/chinois\/audio\/modules\/actu\/201710\/Chr_Taipeh_28-10-17_SEM43.mp3"}]},"photo_url":"\/bundles\/aefhermesrfi\/img\/image_generique_player_big.jpg?version=20171011171259","title":"","is_active":1,"labels":{"now":"EN CE MOMENT"},"comscore":{"baseMeasurementURL":"fr.sitestat.com\/aef\/f24-mcd-rfi\/s?","labels":{"ns_st_ci":"WB260051-RFI-ZH-HANS-20171028","ns_st_ep":"\u56fd\u9645\u60b2\u89c2\u770b\u5f85\u4e24\u5cb8\u5bf9\u4e5d\u4e8c\u5171\u8bc6\u7684\u8ba4\u540c\u843d\u5dee","ns_st_pr":"\u53f0\u5317\u4e00\u5468","ns_st_ty":"audio","ns_st_st":"rfi_chinois","ns_st_pl":"rfi_chinois","ns_st_el":0,"ns_st_ub":0,"ns_st_cn":1,"ns_st_cl":"","ns_st_tp":1,"ns_st_pn":"1","ns_st_dt":"2017-10-28","aef_streamtype_2":"od","aef_rep_global":"\u6e2f\u6fb3\u53f0","aef_thema":"\u6e2f\u6fb3\u53f0,\u53f0\u6e7e,\u653f\u6cbb,\u53f0\u5317\u7279\u7ea6\u8bb0\u8005 \u9648\u6c11\u5cf0,magazine,\u53f0\u5317\u4e00\u5468","aef_type_page1":"chine.defaut.defaut","aef_type_contenu1":"audio","aef_section1":"\u6e2f\u6fb3\u53f0","aef_section2":"\u53f0\u5317\u4e00\u5468","aef_auteur":"\u53f0\u5317\u7279\u7ea6\u8bb0\u8005 \u9648\u6c11\u5cf0","aef_dpubli":"2017-10-28","aef_hpubli":"04:00","ns_st_li":0,"aef_marque":"rfi","name":"chine.defaut.defaut","aef_type_environnement":"site","aef_plateforme":"ordinateur","aef_nom_environnement":"rfi_site","aef_version_environnement":"v2.46.9","aef_perimetre_diffusion":"interne","aef_url_provenance":"http:\/\/cn.rfi.fr\/%E4%B8%AD%E5%9B%BD\/all\/?page=1","aef_page_provenance":"\/%E4%B8%AD%E5%9B%BD\/all\/","aef_langue":"francais","aef_acces":"gratuit","aef_user_connection":"visiteur","aef_user_id":""}}}}};
</script>

            <li data-bo-type="edition" data-bo-nid="WB260051-RFI-ZH-HANS-20171028">
                                                                                                                                                                                                                                                                                                  <a href="#" class="media-play media" data-title="台北一周"
                   data-stream="articleWB260051-RFI-ZH-HANS-20171028" data-player="main-player">
                                            <img src="http://scd.cn.rfi.fr/sites/chinese.filesrfi/dynimagecache/0/116/1000/492/177/87/sites/images.rfi.fr/files/aef_image/101_0_0.jpg" alt="media" width="150" height="85" />
                                        <div class="media-play-img"></div>
                </a>
                <div class="meta">
                    <time datetime="17-10-28">10/28/17</time>
                                        <span>台北一周</span>
                </div>
                <div class="title-emission"><a class="modeless" href="/%E6%B8%AF%E6%BE%B3%E5%8F%B0/20171028-%E5%9B%BD%E9%99%85%E6%82%B2%E8%A7%82%E7%9C%8B%E5%BE%85%E4%B8%A4%E5%B2%B8%E5%AF%B9%E4%B9%9D%E4%BA%8C%E5%85%B1%E8%AF%86%E7%9A%84%E8%AE%A4%E5%90%8C%E8%90%BD%E5%B7%AE">国际悲观看待两岸对九二共识的认同落差</a></div>
            </li>
                                                        
            <script type="text/javascript">
    window.BSPlayer = window.BSPlayer || { items: {} };
    window.BSPlayer.items['articleWB260052-RFI-ZH-HANS-20171028'] = {"medias":{"media":{"type":"audio","media_sources":{"media_source":[{"streaming_type":{"platforms":{"platform":["flash","html5"]},"mime_type":"audio\/mpeg","type":"audio"},"is_default":0,"source":"http:\/\/telechargement.rfi.fr\/rfi\/chinois\/audio\/modules\/actu\/201710\/Asia_weekly_28-10-17_SEM43.mp3"}]},"photo_url":"\/bundles\/aefhermesrfi\/img\/image_generique_player_big.jpg?version=20171011171259","title":"","is_active":1,"labels":{"now":"EN CE MOMENT"},"comscore":{"baseMeasurementURL":"fr.sitestat.com\/aef\/f24-mcd-rfi\/s?","labels":{"ns_st_ci":"WB260052-RFI-ZH-HANS-20171028","ns_st_ep":"\u4e60\u8fd1\u5e73\u542f\u52a8\u65b0\u65f6\u4ee3 \u5f3a\u52bf\u9886\u5bfc\u5341\u4e5d\u5927\u6743\u529b\u6d17\u724c","ns_st_pr":"\u4e9a\u6d32\u5468\u520a","ns_st_ty":"audio","ns_st_st":"rfi_chinois","ns_st_pl":"rfi_chinois","ns_st_el":0,"ns_st_ub":0,"ns_st_cn":1,"ns_st_cl":"","ns_st_tp":1,"ns_st_pn":"1","ns_st_dt":"2017-10-28","aef_streamtype_2":"od","aef_rep_global":"\u4e2d\u56fd","aef_thema":"\u4e2d\u56fd,\u4e9a\u6d32,\u653f\u6cbb,\u4e2d\u56fd,\u300a\u4e9a\u6d32\u5468\u520a\u300b,magazine,\u4e9a\u6d32\u5468\u520a","aef_type_page1":"chine.defaut.defaut","aef_type_contenu1":"audio","aef_section1":"\u4e2d\u56fd","aef_section2":"\u4e9a\u6d32\u5468\u520a","aef_auteur":"\u300a\u4e9a\u6d32\u5468\u520a\u300b","aef_dpubli":"2017-10-28","aef_hpubli":"04:00","ns_st_li":0,"aef_marque":"rfi","name":"chine.defaut.defaut","aef_type_environnement":"site","aef_plateforme":"ordinateur","aef_nom_environnement":"rfi_site","aef_version_environnement":"v2.46.9","aef_perimetre_diffusion":"interne","aef_url_provenance":"http:\/\/cn.rfi.fr\/%E4%B8%AD%E5%9B%BD\/all\/?page=1","aef_page_provenance":"\/%E4%B8%AD%E5%9B%BD\/all\/","aef_langue":"francais","aef_acces":"gratuit","aef_user_connection":"visiteur","aef_user_id":""}}}}};
</script>

            <li data-bo-type="edition" data-bo-nid="WB260052-RFI-ZH-HANS-20171028">
                                                                                                                                                                                                                                                                                                  <a href="#" class="media-play media" data-title="亚洲周刊"
                   data-stream="articleWB260052-RFI-ZH-HANS-20171028" data-player="main-player">
                                            <img src="http://scd.cn.rfi.fr/sites/chinese.filesrfi/imagecache/hermes_infographie_carroussel_dossiers/sites/images.rfi.fr/files/aef_image/2017-10-25t052140z_1135549227_rc1d42457010_rtrmadp_3_china-congress.jpg" alt="media" width="150" height="85" />
                                        <div class="media-play-img"></div>
                </a>
                <div class="meta">
                    <time datetime="17-10-28">10/28/17</time>
                                        <span>亚洲周刊</span>
                </div>
                <div class="title-emission"><a class="modeless" href="/%E4%B8%AD%E5%9B%BD/20171028-%E4%B9%A0%E8%BF%91%E5%B9%B3%E5%90%AF%E5%8A%A8%E6%96%B0%E6%97%B6%E4%BB%A3-%E5%BC%BA%E5%8A%BF%E9%A2%86%E5%AF%BC%E5%8D%81%E4%B9%9D%E5%A4%A7%E6%9D%83%E5%8A%9B%E6%B4%97%E7%89%8C">习近平启动新时代 强势领导十九大权力洗牌</a></div>
            </li>
                                                        
            <script type="text/javascript">
    window.BSPlayer = window.BSPlayer || { items: {} };
    window.BSPlayer.items['articleWB260053-RFI-ZH-HANS-20171027'] = {"medias":{"media":{"type":"audio","media_sources":{"media_source":[{"streaming_type":{"platforms":{"platform":["flash","html5"]},"mime_type":"audio\/mpeg","type":"audio"},"is_default":0,"source":"http:\/\/telechargement.rfi.fr\/rfi\/chinois\/audio\/modules\/actu\/201710\/DEV_DURABLE_27-10-17_Pollution_Paris_Prod_12_10_2017.mp3"}]},"photo_url":"\/bundles\/aefhermesrfi\/img\/image_generique_player_big.jpg?version=20171011171259","title":"","is_active":1,"labels":{"now":"EN CE MOMENT"},"comscore":{"baseMeasurementURL":"fr.sitestat.com\/aef\/f24-mcd-rfi\/s?","labels":{"ns_st_ci":"WB260053-RFI-ZH-HANS-20171027","ns_st_ep":"\u7a7a\u6c14\u6c61\u67d3\u5bfc\u81f4\u6b27\u6d32\u4eba\u65e9\u901d \u5df4\u9ece\u52a0\u5927\u63a7\u5236\u6c7d\u8f66\u529b\u5ea6","ns_st_pr":"\u73af\u5883\u4e0e\u53d1\u5c55","ns_st_ty":"audio","ns_st_st":"rfi_chinois","ns_st_pl":"rfi_chinois","ns_st_el":0,"ns_st_ub":0,"ns_st_cn":1,"ns_st_cl":"","ns_st_tp":1,"ns_st_pn":"1","ns_st_dt":"2017-10-27","aef_streamtype_2":"od","aef_rep_global":"\u6cd5\u56fd","aef_thema":"\u6cd5\u56fd,\u73af\u4fdd,\u6c61\u67d3,\u7f57\u62c9,magazine,\u73af\u5883\u4e0e\u53d1\u5c55","aef_type_page1":"chine.defaut.defaut","aef_type_contenu1":"audio","aef_section1":"\u6cd5\u56fd","aef_section2":"\u73af\u5883\u4e0e\u53d1\u5c55","aef_auteur":"\u7f57\u62c9","aef_dpubli":"2017-10-27","aef_hpubli":"04:00","ns_st_li":0,"aef_marque":"rfi","name":"chine.defaut.defaut","aef_type_environnement":"site","aef_plateforme":"ordinateur","aef_nom_environnement":"rfi_site","aef_version_environnement":"v2.46.9","aef_perimetre_diffusion":"interne","aef_url_provenance":"http:\/\/cn.rfi.fr\/%E4%B8%AD%E5%9B%BD\/all\/?page=1","aef_page_provenance":"\/%E4%B8%AD%E5%9B%BD\/all\/","aef_langue":"francais","aef_acces":"gratuit","aef_user_connection":"visiteur","aef_user_id":""}}}}};
</script>

            <li data-bo-type="edition" data-bo-nid="WB260053-RFI-ZH-HANS-20171027">
                                                                                                                                                                                                                                                                                                  <a href="#" class="media-play media" data-title="环境与发展"
                   data-stream="articleWB260053-RFI-ZH-HANS-20171027" data-player="main-player">
                                            <img src="http://scd.cn.rfi.fr/sites/chinese.filesrfi/imagecache/hermes_infographie_carroussel_dossiers/sites/images.rfi.fr/files/aef_image/000_ir6co_0.jpg" alt="media" width="150" height="85" />
                                        <div class="media-play-img"></div>
                </a>
                <div class="meta">
                    <time datetime="17-10-28">10/28/17</time>
                                        <span>环境与发展</span>
                </div>
                <div class="title-emission"><a class="modeless" href="/%E6%B3%95%E5%9B%BD/20171027-%E7%A9%BA%E6%B0%94%E6%B1%A1%E6%9F%93%E5%AF%BC%E8%87%B4%E6%AC%A7%E6%B4%B2%E4%BA%BA%E6%97%A9%E9%80%9D-%E5%B7%B4%E9%BB%8E%E5%8A%A0%E5%A4%A7%E6%8E%A7%E5%88%B6%E6%B1%BD%E8%BD%A6%E5%8A%9B%E5%BA%A6">空气污染导致欧洲人早逝 巴黎加大控制汽车力度</a></div>
            </li>
                </ul>

        </div>
    </div>

                        </div>
                                    </div>
                <div class="error_msg_block">
    <noscript>
        <span class="error_msg" id="error_msg_js">
            为了更好浏览RFI网站，您的浏览器需要启动JavaScript
        </span>
    </noscript>
    <span class="error_msg" id="error_msg_flash">
        为了更好浏览多媒体内容，您的浏览器需要安装Flash插件
    </span>
    <span class="error_msg" id="error_msg_cookies">
        若要连接，您需要启用您的浏览器上设置的cookie。
    </span>
    <span class="error_msg" id="error_msg_browser">
        为了更好浏览，RFI网站与以下浏览器兼容： Internet Explorer 8 et +, Firefox 10 et +, Safari 3 et +, Chrome 17 et +
    </span>
</div>

            </header>
        
                    
            <div class="content">

                
 <div id="loading" class="">
    <div id="squaresWaveG">
        <div id="squaresWaveG_1" class="squaresWaveG">
        </div>
        <div id="squaresWaveG_2" class="squaresWaveG">
        </div>
        <div id="squaresWaveG_3" class="squaresWaveG">
        </div>
        <div id="squaresWaveG_4" class="squaresWaveG">
        </div>
        <div id="squaresWaveG_5" class="squaresWaveG">
        </div>
        <div id="squaresWaveG_6" class="squaresWaveG">
        </div>
        <div id="squaresWaveG_7" class="squaresWaveG">
        </div>
        <div id="squaresWaveG_8" class="squaresWaveG">
        </div>
    </div>

</div>

                <div class="content-slider">
                    <div class="content-slide">

                                                                                                                                                                                                                                                                                    
                            
                        
    <div class="tms-block"
         data-pos="1"
         data-type="gigaban"
         data-location="top"
         data-expand="true"
         data-loaded="false">
    </div>

                        
                                                                                                            <div id="latest-info-wrapper" data-special-event-boolean="false" data-special-event-id="">
                                

                            </div>
                        
                                                    <div id="sections">

                                                                        
                                
                                <div class="page">
                                            <div class="page-inner">
                <section id="news">
                                                <div id="page_inner_header_title">
                        <h1 class="floatLeft">中国</h1>
                                                                                    <a class="ico-rss floatRight" title="RSS&#x805A;&#x5408;&#x65B0;&#x95FB;" href="/%E4%B8%AD%E5%9B%BD/rss" target="_blank">
        <span class="invisible">RSS聚合新闻</span>
    </a>


                    </div>
                                                                                        <header class="intro">
                                        

                    </header>
                                
                <ul id='articleList' class="list">
                                                                                                  
                                                                                                        
                                                                        
                                                                                                                                                                                                                                                                                                                 <li data-bo-type="article" data-bo-nid="WB260209-RFI-ZH-HANS-20171030">
                                                                                                                                <a href="/%E4%B8%AD%E5%9B%BD/20171030-%E4%B8%AD%E5%9B%BD%E5%A4%8D%E6%98%9F%E6%94%B6%E8%B4%AD%E6%B3%95%E5%9B%BD%E8%8D%AF%E5%93%81%E5%88%86%E9%94%80%E5%85%AC%E5%8F%B8-tridem" title="中国复星收购法国药品分销公司 Tridem" class="media center-cropped modeless" target="_self" data-image="http://scd.cn.rfi.fr/sites/chinese.filesrfi/imagecache/hermes_infographie_vignette_home/sites/images.rfi.fr/files/aef_image/fx.jpg" data-width="187" data-height="103">
                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                <img height="103" width="187" src="http://scd.cn.rfi.fr/sites/chinese.filesrfi/imagecache/hermes_infographie_vignette_home/sites/images.rfi.fr/files/aef_image/fx.jpg" alt="media">
                                    </a>
                                                                                                                    <div class="meta">
                                                                    <time datetime="17-10-30">30/10/2017</time>
                                                                                                        <span class="tag">
                                                                                                        <a class="modeless no-decoration" href="/tag/%E4%B8%AD%E5%9B%BD/">中国</a>
                                                </span>
                                <span class="tag">
                                                                                                        <a class="modeless no-decoration" href="/tag/%E6%B3%95%E5%9B%BD/">法国</a>
                                                </span>
                        
                            </div>

                                                                                        <h3 class=" ">
                                    <a href="/%E4%B8%AD%E5%9B%BD/20171030-%E4%B8%AD%E5%9B%BD%E5%A4%8D%E6%98%9F%E6%94%B6%E8%B4%AD%E6%B3%95%E5%9B%BD%E8%8D%AF%E5%93%81%E5%88%86%E9%94%80%E5%85%AC%E5%8F%B8-tridem" title="&#x4E2D;&#x56FD;&#x590D;&#x661F;&#x6536;&#x8D2D;&#x6CD5;&#x56FD;&#x836F;&#x54C1;&#x5206;&#x9500;&#x516C;&#x53F8;&#x20;Tridem" target="_self" class="modeless">中国复星收购法国药品分销公司 Tridem</a>
                                </h3>
                                                                                        <p>中国复星与法国药品分销公司Tridem在10月27日达成协议，复星的子公司以6300万欧元收购这家法国药品分销商。复星医药周日10月29日向香港交易所提交了有关文件，也显示复星加快国际发展步伐。
</p>
                                                                                </li>
                                                                                                                                                                                                                                                                                                                                                     <li data-bo-type="article" data-bo-nid="WB260190-RFI-ZH-HANS-20171030">
                                                                                                                                <a href="/%E4%B8%AD%E5%9B%BD/20171030-%E4%B8%AD%E7%BA%AA%E5%A7%94%E5%AE%9A%E6%80%A7%E5%AD%99%E6%94%BF%E6%89%8D%E4%B8%BA%E9%87%8E%E5%BF%83%E5%AE%B6-%E5%9D%9A%E5%86%B3%E9%93%B2%E9%99%A4" title="中纪委定性孙政才为野心家 坚决铲除" class="media center-cropped modeless" target="_self" data-image="http://scd.cn.rfi.fr/sites/chinese.filesrfi/imagecache/hermes_infographie_vignette_home/sites/images.rfi.fr/files/aef_image/chine_nid500565884_4.jpg" data-width="187" data-height="103">
                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                    <img height="103" width="187" src="http://scd.cn.rfi.fr/sites/chinese.filesrfi/imagecache/hermes_infographie_vignette_home/sites/images.rfi.fr/files/aef_image/chine_nid500565884_4.jpg" alt="media">
                                    </a>
                                                                                                                    <div class="meta">
                                                                    <time datetime="17-10-30">30/10/2017</time>
                                                                                                        <span class="tag">
                                                                                                        <a class="modeless no-decoration" href="/tag/%E4%B8%AD%E5%9B%BD/">中国</a>
                                                </span>
                                <span class="tag">
                                                                                                        <a class="modeless no-decoration" href="/tag/%E6%94%BF%E6%B2%BB/">政治</a>
                                                </span>
                        
                            </div>

                                                                                        <h3 class=" ">
                                    <a href="/%E4%B8%AD%E5%9B%BD/20171030-%E4%B8%AD%E7%BA%AA%E5%A7%94%E5%AE%9A%E6%80%A7%E5%AD%99%E6%94%BF%E6%89%8D%E4%B8%BA%E9%87%8E%E5%BF%83%E5%AE%B6-%E5%9D%9A%E5%86%B3%E9%93%B2%E9%99%A4" title="&#x4E2D;&#x7EAA;&#x59D4;&#x5B9A;&#x6027;&#x5B59;&#x653F;&#x624D;&#x4E3A;&#x91CE;&#x5FC3;&#x5BB6;&#x20;&#x575A;&#x51B3;&#x94F2;&#x9664;" target="_self" class="modeless">中纪委定性孙政才为野心家 坚决铲除</a>
                                </h3>
                                                                                        <p>中央纪律检查委员会在向中共十九大提交的工作报告中，直斥前政治局常委周永康、中共「第六代接班人选」之一的孙政才及前中共中央办公厅主任令计划等人为「野心家、阴谋家」，党坚决铲除，「消除重大政治隐患」。这是中共自林彪等人后具体点名党内野心家。中纪委报告又指，日后将重点查处结成利益集团的 &hellip;</p>
                                                                                </li>
                                                                                                                                                                                                                                                                                                                                                     <li data-bo-type="article" data-bo-nid="WB260189-RFI-ZH-HANS-20171030">
                                                                                                                                <a href="/%E4%B8%AD%E5%9B%BD/20171030-%E4%B8%AD%E5%9B%BD%E5%AE%98%E5%91%98%E4%BC%B8%E6%89%8B%E9%A6%99%E6%B8%AF%E6%95%99%E8%82%B2-%E4%B8%AD%E5%8F%B2%E5%BF%A7%E6%88%90%E6%B4%97%E8%84%91%E6%95%99%E8%82%B2" title="中国官员伸手香港教育 中史忧成洗脑教育" class="media center-cropped modeless" target="_self" data-image="http://scd.cn.rfi.fr/sites/chinese.filesrfi/imagecache/hermes_infographie_vignette_home/sites/images.rfi.fr/files/aef_image/2017-07-02t074754z_1110487828_rc14272bb230_rtrmadp_3_hongkong-anniversary_0.jpg" data-width="187" data-height="103">
                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                            <img height="103" width="187" src="http://scd.cn.rfi.fr/sites/chinese.filesrfi/imagecache/hermes_infographie_vignette_home/sites/images.rfi.fr/files/aef_image/2017-07-02t074754z_1110487828_rc14272bb230_rtrmadp_3_hongkong-anniversary_0.jpg" alt="media">
                                    </a>
                                                                                                                    <div class="meta">
                                                                    <time datetime="17-10-30">30/10/2017</time>
                                                                                                        <span class="tag">
                                                                                                        <a class="modeless no-decoration" href="/tag/%E4%B8%AD%E5%9B%BD/">中国</a>
                                                </span>
                                <span class="tag">
                                                                                                        <a class="modeless no-decoration" href="/tag/%E9%A6%99%E6%B8%AF/">香港</a>
                                                </span>
                                <span class="tag">
                                                                                                        <a class="modeless no-decoration" href="/tag/%E6%94%BF%E6%B2%BB/">政治</a>
                                                </span>
                                <span class="tag">
                                                                                                        <a class="modeless no-decoration" href="/tag/%E6%95%99%E8%82%B2/">教育</a>
                                                </span>
                        
                            </div>

                                                                                        <h3 class=" ">
                                    <a href="/%E4%B8%AD%E5%9B%BD/20171030-%E4%B8%AD%E5%9B%BD%E5%AE%98%E5%91%98%E4%BC%B8%E6%89%8B%E9%A6%99%E6%B8%AF%E6%95%99%E8%82%B2-%E4%B8%AD%E5%8F%B2%E5%BF%A7%E6%88%90%E6%B4%97%E8%84%91%E6%95%99%E8%82%B2" title="&#x4E2D;&#x56FD;&#x5B98;&#x5458;&#x4F38;&#x624B;&#x9999;&#x6E2F;&#x6559;&#x80B2;&#x20;&#x4E2D;&#x53F2;&#x5FE7;&#x6210;&#x6D17;&#x8111;&#x6559;&#x80B2;" target="_self" class="modeless">中国官员伸手香港教育 中史忧成洗脑教育</a>
                                </h3>
                                                                                        <p>声称对香港拥有「全面管治权」的中国北京政府，其驻港代表机构据称约见香港的校长和教师，谈谈香港的中国历史课程。属于泛民主派的立法会教育界议员叶建源忧虑，若中方官员的约谈不是纯粹了解，而是介入，那便是干预香港内部事务，违反基本法。
</p>
                                                                                </li>
                                                                                                                                                                                                                                                                                                                                                     <li data-bo-type="article" data-bo-nid="WB260173-RFI-ZH-HANS-20171030">
                                                                                                                                <a href="/%E4%B8%AD%E5%9B%BD/20171030-%E7%8B%AC%E7%AB%8B%E4%B8%AD%E6%96%87%E7%AC%94%E4%BC%9A%E5%91%BC%E5%90%81%E4%B8%AD%E5%9B%BD%E5%BD%93%E5%B1%80%E8%BF%98%E4%BA%8E%E6%A1%82%E6%B0%91%E6%B5%B7%E8%87%AA%E7%94%B1" title="桂民海获释 独立中文笔会呼吁中国当局恢复其自由" class="media center-cropped modeless" target="_self" data-image="http://scd.cn.rfi.fr/sites/chinese.filesrfi/imagecache/hermes_infographie_vignette_home/sites/images.rfi.fr/files/aef_image/bkn-20151114171043185-1114_00822_001_01b.jpg" data-width="187" data-height="103">
                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                    <img height="103" width="187" src="http://scd.cn.rfi.fr/sites/chinese.filesrfi/imagecache/hermes_infographie_vignette_home/sites/images.rfi.fr/files/aef_image/bkn-20151114171043185-1114_00822_001_01b.jpg" alt="media">
                                    </a>
                                                                                                                    <div class="meta">
                                                                    <time datetime="17-10-30">30/10/2017</time>
                                                                                                        <span class="tag">
                                                                                                        <a class="modeless no-decoration" href="/tag/%E9%A6%99%E6%B8%AF/">香港</a>
                                                </span>
                                <span class="tag">
                                                                                                        <a class="modeless no-decoration" href="/tag/%E4%B8%AD%E5%9B%BD/">中国</a>
                                                </span>
                                <span class="tag">
                                                                                                        <a class="modeless no-decoration" href="/tag/%E6%94%BF%E6%B2%BB/">政治</a>
                                                </span>
                                <span class="tag">
                                                                                                        <a class="modeless no-decoration" href="/tag/%E7%A4%BE%E4%BC%9A/">社会</a>
                                                </span>
                                <span class="tag">
                                                                                                        <a class="modeless no-decoration" href="/tag/%E5%8F%B8%E6%B3%95/">司法</a>
                                                </span>
                                <span class="tag">
                                                                                                        <a class="modeless no-decoration" href="/tag/%E7%91%9E%E5%85%B8/">瑞典</a>
                                                </span>
                        
                            </div>

                                                                                        <h3 class=" ">
                                    <a href="/%E4%B8%AD%E5%9B%BD/20171030-%E7%8B%AC%E7%AB%8B%E4%B8%AD%E6%96%87%E7%AC%94%E4%BC%9A%E5%91%BC%E5%90%81%E4%B8%AD%E5%9B%BD%E5%BD%93%E5%B1%80%E8%BF%98%E4%BA%8E%E6%A1%82%E6%B0%91%E6%B5%B7%E8%87%AA%E7%94%B1" title="&#x6842;&#x6C11;&#x6D77;&#x83B7;&#x91CA;&#x20;&#x72EC;&#x7ACB;&#x4E2D;&#x6587;&#x7B14;&#x4F1A;&#x547C;&#x5401;&#x4E2D;&#x56FD;&#x5F53;&#x5C40;&#x6062;&#x590D;&#x5176;&#x81EA;&#x7531;" target="_self" class="modeless">桂民海获释 独立中文笔会呼吁中国当局恢复其自由</a>
                                </h3>
                                                                                        <p>日前经多方消息证实，在香港&ldquo;铜锣湾书店&rdquo;事件中被失踪的瑞典公民桂民海在近日得到释放。他本人现已在浙江宁波老家的一所公寓里与他德国籍的妻子团聚。对此，独立中文笔会在周日发表声明呼吁中国当局立即恢复桂民海的人身自由，并宣称他的出行和与外界的联系都受到了&ldquo;相当程度的控制&rdquo;。
</p>
                                                                                </li>
                                                                                                                                                                                                                                                                                                                                                     <li data-bo-type="article" data-bo-nid="C4507A4A-4578-41A0-8C48-7A5DABA5252D">
                                                                                                                                <a href="/%E4%B8%AD%E5%9B%BD/20171029-%E5%AD%94%E9%93%89%E4%BD%91%E8%AE%BF%E6%97%A5%E4%B8%BA%E6%9D%8E%E5%85%8B%E5%BC%BA%E8%AE%BF%E6%97%A5%E9%93%BA%E8%B7%AF" title="孔铉佑访日为李克强访日铺路" class="media center-cropped modeless" target="_self" data-image="http://scd.cn.rfi.fr/sites/chinese.filesrfi/dynimagecache/0/56/553/305/187/103/sites/images.rfi.fr/files/aef_image/2011-11-23T105521Z_1121082965_GM1E7BN1GQW01_RTRMADP_2_JAPAN-CHINA.JPG" data-width="187" data-height="103">
                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                    <img height="103" width="187" src="http://scd.cn.rfi.fr/sites/chinese.filesrfi/dynimagecache/0/56/553/305/187/103/sites/images.rfi.fr/files/aef_image/2011-11-23T105521Z_1121082965_GM1E7BN1GQW01_RTRMADP_2_JAPAN-CHINA.JPG" alt="media">
                                    </a>
                                                                                                                    <div class="meta">
                                                                    <time datetime="17-10-29">29/10/2017</time>
                                                                                                        <span class="tag">
                                                                                                        <a class="modeless no-decoration" href="/tag/%E4%B8%AD%E6%97%A5%E5%85%B3%E7%B3%BB/">中日关系</a>
                                                </span>
                                <span class="tag">
                                                                                                        <a class="modeless no-decoration" href="/tag/%E6%94%BF%E6%B2%BB/">政治</a>
                                                </span>
                        
                            </div>

                                                                                        <h3 class=" ">
                                    <a href="/%E4%B8%AD%E5%9B%BD/20171029-%E5%AD%94%E9%93%89%E4%BD%91%E8%AE%BF%E6%97%A5%E4%B8%BA%E6%9D%8E%E5%85%8B%E5%BC%BA%E8%AE%BF%E6%97%A5%E9%93%BA%E8%B7%AF" title="&#x5B54;&#x94C9;&#x4F51;&#x8BBF;&#x65E5;&#x4E3A;&#x674E;&#x514B;&#x5F3A;&#x8BBF;&#x65E5;&#x94FA;&#x8DEF;" target="_self" class="modeless">孔铉佑访日为李克强访日铺路</a>
                                </h3>
                                                                                        <p>日本外务省外务审议官秋叶刚男10月28日与中国外交部部长助理兼朝鲜半岛事务特别代表孔铉佑在东京举行非正式会谈，围绕在今年年内举行由日本担任轮值主席国的日中韩首脑会谈进行了磋商。为争取实现预计出席会议的中国国务院总理李克强首次访日，日中加快了协调工作，正在进行具体沟通和日程的调整。 &hellip;</p>
                                                                                </li>
                                                                                                                                                                                                                                                                                                                                                     <li data-bo-type="article" data-bo-nid="5F21FCEF-6E3D-4D0D-9255-C6BE9D8AE065">
                                                                                                                                <a href="/%E4%B8%AD%E5%9B%BD/20171029-%E9%98%B2%E8%8C%83%E6%9A%97%E6%9D%80%E7%AF%A1%E5%85%9A%E5%A4%BA%E6%9D%83%E4%BC%A0%E5%BD%93%E5%B1%80%E4%B8%A5%E6%9F%A5%E4%B8%AD%E5%8D%97%E6%B5%B7%E4%BF%9D%E9%95%96%E8%AD%A6%E5%8D%AB%E5%8F%B8%E6%9C%BA%E8%83%8C%E6%99%AF" title="防范暗杀篡党夺权传当局严查中南海保镖警卫司机背景" class="media center-cropped modeless" target="_self" data-image="http://scd.cn.rfi.fr/sites/chinese.filesrfi/imagecache/hermes_infographie_vignette_home/sites/images.rfi.fr/files/aef_image/onhiem_01.jpg" data-width="187" data-height="103">
                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                <img height="103" width="187" src="http://scd.cn.rfi.fr/sites/chinese.filesrfi/imagecache/hermes_infographie_vignette_home/sites/images.rfi.fr/files/aef_image/onhiem_01.jpg" alt="media">
                                    </a>
                                                                                                                    <div class="meta">
                                                                    <time datetime="17-10-29">29/10/2017</time>
                                                                                                        <span class="tag">
                                                                                                        <a class="modeless no-decoration" href="/tag/%E4%B8%AD%E5%9B%BD/">中国</a>
                                                </span>
                                <span class="tag">
                                                                                                        <a class="modeless no-decoration" href="/tag/%E6%94%BF%E6%B2%BB/">政治</a>
                                                </span>
                        
                            </div>

                                                                                        <h3 class=" ">
                                    <a href="/%E4%B8%AD%E5%9B%BD/20171029-%E9%98%B2%E8%8C%83%E6%9A%97%E6%9D%80%E7%AF%A1%E5%85%9A%E5%A4%BA%E6%9D%83%E4%BC%A0%E5%BD%93%E5%B1%80%E4%B8%A5%E6%9F%A5%E4%B8%AD%E5%8D%97%E6%B5%B7%E4%BF%9D%E9%95%96%E8%AD%A6%E5%8D%AB%E5%8F%B8%E6%9C%BA%E8%83%8C%E6%99%AF" title="&#x9632;&#x8303;&#x6697;&#x6740;&#x7BE1;&#x515A;&#x593A;&#x6743;&#x4F20;&#x5F53;&#x5C40;&#x4E25;&#x67E5;&#x4E2D;&#x5357;&#x6D77;&#x4FDD;&#x9556;&#x8B66;&#x536B;&#x53F8;&#x673A;&#x80CC;&#x666F;" target="_self" class="modeless">防范暗杀篡党夺权传当局严查中南海保镖警卫司机背景</a>
                                </h3>
                                                                                        <p>据海外中文网站博闻社报道，中共为防内鬼、独狼（lone wolf），从保镳到警衞、从司机到秘书均需重新进行背景审查。&ldquo;独狼&rdquo;是指没有组织背景只是因为不满现状而触发恐怖活动的个人。
</p>
                                                                                </li>
                                                                                                                                                                                                                                                                                                                                                     <li data-bo-type="article" data-bo-nid="68612BFD-C23C-4C6A-9744-3AC14653E202">
                                                                                                                                <a href="/%E4%B8%AD%E5%9B%BD/20171029-%E4%B9%A0%E5%AE%B6%E5%86%9B%E6%94%BF%E6%B2%BB%E5%B1%80%E6%96%B0%E8%B4%B5%E6%9D%8E%E5%BC%BA%E4%B8%BB%E6%94%BF%E4%B8%8A%E6%B5%B7" title="“习家军”政治局新贵李强主政上海" class="media center-cropped modeless" target="_self" data-image="http://scd.cn.rfi.fr/sites/chinese.filesrfi/imagecache/hermes_infographie_vignette_home/sites/images.rfi.fr/files/aef_image/2017-10-24t041218z_368141803_rc1d95ba4a80_rtrmadp_3_china-congress.jpg" data-width="187" data-height="103">
                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                    <img height="103" width="187" src="http://scd.cn.rfi.fr/sites/chinese.filesrfi/imagecache/hermes_infographie_vignette_home/sites/images.rfi.fr/files/aef_image/2017-10-24t041218z_368141803_rc1d95ba4a80_rtrmadp_3_china-congress.jpg" alt="media">
                                    </a>
                                                                                                                    <div class="meta">
                                                                    <time datetime="17-10-29">29/10/2017</time>
                                                                                                        <span class="tag">
                                                                                                        <a class="modeless no-decoration" href="/tag/%E4%B8%AD%E5%9B%BD%E9%AB%98%E5%B1%82%E4%BA%BA%E4%BA%8B/">中国高层人事</a>
                                                </span>
                                <span class="tag">
                                                                                                        <a class="modeless no-decoration" href="/tag/%E6%94%BF%E6%B2%BB/">政治</a>
                                                </span>
                                <span class="tag">
                                                                                                        <a class="modeless no-decoration" href="/tag/%E5%8D%81%E4%B9%9D%E5%A4%A7/">十九大</a>
                                                </span>
                        
                            </div>

                                                                                        <h3 class=" ">
                                    <a href="/%E4%B8%AD%E5%9B%BD/20171029-%E4%B9%A0%E5%AE%B6%E5%86%9B%E6%94%BF%E6%B2%BB%E5%B1%80%E6%96%B0%E8%B4%B5%E6%9D%8E%E5%BC%BA%E4%B8%BB%E6%94%BF%E4%B8%8A%E6%B5%B7" title="&#x201C;&#x4E60;&#x5BB6;&#x519B;&#x201D;&#x653F;&#x6CBB;&#x5C40;&#x65B0;&#x8D35;&#x674E;&#x5F3A;&#x4E3B;&#x653F;&#x4E0A;&#x6D77;" target="_self" class="modeless">&ldquo;习家军&rdquo;政治局新贵李强主政上海</a>
                                </h3>
                                                                                        <p>十九大闭幕之后，中共政坛即出现人事大搬风，继辽宁省委书记李希调任全国最富裕省份之一的广东省第一把手之后，新华社29日报道，现年58岁出身自浙江省的政治局新贵李强，出任上海市委书记。
</p>
                                                                                </li>
                                                                                                                                                                                                                                                                                                                                                     <li data-bo-type="article" data-bo-nid="709CABF8-DA2D-4032-B009-5B4071DCE910">
                                                                                                                                <a href="/%E4%B8%AD%E5%9B%BD/20171029-%E6%94%BF%E6%B2%BB%E5%B1%80%E6%94%B9%E4%B8%BA%E6%AF%8F%E5%B9%B4%E8%A6%81%E5%90%91%E4%B9%A0%E8%BF%91%E5%B9%B3%E8%BF%B0%E8%81%8C%E6%84%8F%E5%91%B3%E6%9E%B6%E7%A9%BA%E5%B8%B8%E5%A7%94%E9%9B%86%E4%BD%93%E9%A2%86%E5%AF%BC" title="政治局改为每年要向习近平述职意味架空常委集体领导" class="media center-cropped modeless" target="_self" data-image="http://scd.cn.rfi.fr/sites/chinese.filesrfi/dynimagecache/0/5/3500/1925/187/103/sites/images.rfi.fr/files/aef_image/2017-10-18t014526z_478131504_rc1c70817b10_rtrmadp_3_china-congress.jpg" data-width="187" data-height="103">
                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                <img height="103" width="187" src="http://scd.cn.rfi.fr/sites/chinese.filesrfi/dynimagecache/0/5/3500/1925/187/103/sites/images.rfi.fr/files/aef_image/2017-10-18t014526z_478131504_rc1c70817b10_rtrmadp_3_china-congress.jpg" alt="media">
                                    </a>
                                                                                                                    <div class="meta">
                                                                    <time datetime="17-10-29">29/10/2017</time>
                                                                                                        <span class="tag">
                                                                                                        <a class="modeless no-decoration" href="/tag/%E4%B8%AD%E5%9B%BD/">中国</a>
                                                </span>
                                <span class="tag">
                                                                                                        <a class="modeless no-decoration" href="/tag/%E6%94%BF%E6%B2%BB/">政治</a>
                                                </span>
                        
                            </div>

                                                                                        <h3 class=" ">
                                    <a href="/%E4%B8%AD%E5%9B%BD/20171029-%E6%94%BF%E6%B2%BB%E5%B1%80%E6%94%B9%E4%B8%BA%E6%AF%8F%E5%B9%B4%E8%A6%81%E5%90%91%E4%B9%A0%E8%BF%91%E5%B9%B3%E8%BF%B0%E8%81%8C%E6%84%8F%E5%91%B3%E6%9E%B6%E7%A9%BA%E5%B8%B8%E5%A7%94%E9%9B%86%E4%BD%93%E9%A2%86%E5%AF%BC" title="&#x653F;&#x6CBB;&#x5C40;&#x6539;&#x4E3A;&#x6BCF;&#x5E74;&#x8981;&#x5411;&#x4E60;&#x8FD1;&#x5E73;&#x8FF0;&#x804C;&#x610F;&#x5473;&#x67B6;&#x7A7A;&#x5E38;&#x59D4;&#x96C6;&#x4F53;&#x9886;&#x5BFC;" target="_self" class="modeless">政治局改为每年要向习近平述职意味架空常委集体领导</a>
                                </h3>
                                                                                        <p>十九大一中全会刚闭幕不久，新一届的政治局日前在北京即召开会议，会上一致同意关于加强和维护，党中央集中统一领导的有关规定。有学者认为，新规定要求政治局委员每年要向总书记作书面述职，是习近平进一步集权的表现。
</p>
                                                                                </li>
                                                                                                                                                                                                                                                                                                                                                     <li data-bo-type="article" data-bo-nid="FE001A5A-18CC-4ADC-9142-15733A072CE6">
                                                                                                                                <a href="/%E4%B8%AD%E5%9B%BD/20171028-%E7%89%B9%E6%9C%97%E6%99%AE%E8%AE%BF%E5%8D%8E%E5%89%8D%E7%BE%8E%E5%95%86%E5%8A%A1%E9%83%A8%E5%88%9D%E8%A3%81%E4%B8%AD%E5%9B%BD%E9%93%9D%E7%AE%94%E5%80%BE%E9%94%80" title="特朗普访华前美商务部初裁中国铝箔倾销" class="media center-cropped modeless" target="_self" data-image="http://scd.cn.rfi.fr/sites/chinese.filesrfi/imagecache/hermes_infographie_vignette_home/sites/images.rfi.fr/files/aef_image/zmmy.jpg" data-width="187" data-height="103">
                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                        <img height="103" width="187" src="http://scd.cn.rfi.fr/sites/chinese.filesrfi/imagecache/hermes_infographie_vignette_home/sites/images.rfi.fr/files/aef_image/zmmy.jpg" alt="media">
                                    </a>
                                                                                                                    <div class="meta">
                                                                    <time datetime="17-10-28">28/10/2017</time>
                                                                                                        <span class="tag">
                                                                                                        <a class="modeless no-decoration" href="/tag/%E4%B8%AD%E5%9B%BD/">中国</a>
                                                </span>
                        
                            </div>

                                                                                        <h3 class=" ">
                                    <a href="/%E4%B8%AD%E5%9B%BD/20171028-%E7%89%B9%E6%9C%97%E6%99%AE%E8%AE%BF%E5%8D%8E%E5%89%8D%E7%BE%8E%E5%95%86%E5%8A%A1%E9%83%A8%E5%88%9D%E8%A3%81%E4%B8%AD%E5%9B%BD%E9%93%9D%E7%AE%94%E5%80%BE%E9%94%80" title="&#x7279;&#x6717;&#x666E;&#x8BBF;&#x534E;&#x524D;&#x7F8E;&#x5546;&#x52A1;&#x90E8;&#x521D;&#x88C1;&#x4E2D;&#x56FD;&#x94DD;&#x7B94;&#x503E;&#x9500;" target="_self" class="modeless">特朗普访华前美商务部初裁中国铝箔倾销</a>
                                </h3>
                                                                                        <p>美国商务部28日发出的信息说，美国商务部长威尔伯&middot;罗斯宣布在反倾销调查中发现，来自中国的铝箔出口商销售铝箔的价格导致存在幅度从96.81%到162.24%的倾销，这些都是基于各利益方使用美国商务部非市场经济体倾销方法得出的实际证据。美国商务部公布对中国铝箔产品反倾销调查初步裁定。 &hellip;</p>
                                                                                </li>
                                                                                                                                                                                                                                                                                                                                                     <li data-bo-type="article" data-bo-nid="7219A10A-6601-43EC-9704-7392EA1D4338">
                                                                                                                                <a href="/%E4%B8%AD%E5%9B%BD/20171028-%E5%8D%97%E4%BA%AC%E5%A4%A7%E5%B1%A0%E6%9D%80%E9%81%87%E9%9A%BE%E5%90%8C%E8%83%9E%E7%BA%AA%E5%BF%B5%E9%A6%86%E9%A6%86%E9%95%BF%E5%90%81%E5%AE%89%E5%80%8D%E5%8F%82%E8%A7%82" title="南京大屠杀遇难同胞纪念馆馆长吁安倍参观" class="media center-cropped modeless" target="_self" data-image="http://scd.cn.rfi.fr/sites/chinese.filesrfi/dynimagecache/0/474/4992/2745/187/103/sites/images.rfi.fr/files/aef_image/000_rl1ci.jpg" data-width="187" data-height="103">
                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                        <img height="103" width="187" src="http://scd.cn.rfi.fr/sites/chinese.filesrfi/dynimagecache/0/474/4992/2745/187/103/sites/images.rfi.fr/files/aef_image/000_rl1ci.jpg" alt="media">
                                    </a>
                                                                                                                    <div class="meta">
                                                                    <time datetime="17-10-28">28/10/2017</time>
                                                                                                        <span class="tag">
                                                                                                        <a class="modeless no-decoration" href="/tag/%E4%B8%AD%E5%9B%BD/">中国</a>
                                                </span>
                                <span class="tag">
                                                                                                        <a class="modeless no-decoration" href="/tag/%E6%97%A5%E6%9C%AC/">日本</a>
                                                </span>
                        
                            </div>

                                                                                        <h3 class=" ">
                                    <a href="/%E4%B8%AD%E5%9B%BD/20171028-%E5%8D%97%E4%BA%AC%E5%A4%A7%E5%B1%A0%E6%9D%80%E9%81%87%E9%9A%BE%E5%90%8C%E8%83%9E%E7%BA%AA%E5%BF%B5%E9%A6%86%E9%A6%86%E9%95%BF%E5%90%81%E5%AE%89%E5%80%8D%E5%8F%82%E8%A7%82" title="&#x5357;&#x4EAC;&#x5927;&#x5C60;&#x6740;&#x9047;&#x96BE;&#x540C;&#x80DE;&#x7EAA;&#x5FF5;&#x9986;&#x9986;&#x957F;&#x5401;&#x5B89;&#x500D;&#x53C2;&#x89C2;" target="_self" class="modeless">南京大屠杀遇难同胞纪念馆馆长吁安倍参观</a>
                                </h3>
                                                                                        <p>今年12月是日本皇军在南京大量杀害中国人80周年。南京侵华日军南京大屠杀遇难同胞纪念馆馆长张建军首次接受日媒采访，他敦促日本首相安倍晋三访问南京。当年大屠杀的幸存者仅剩100人。
</p>
                                                                                </li>
                                                                                                                                                                                                                                                                                                                                                     <li data-bo-type="article" data-bo-nid="972C58DF-3993-466C-BE70-A9333EE88567">
                                                                                                                                <a href="/%E4%B8%AD%E5%9B%BD/20171028-%E8%83%A1%E6%98%A5%E5%8D%8E%E8%B0%83%E7%A6%BB%E5%B9%BF%E4%B8%9C%E5%8E%BB%E5%90%91%E4%B8%8D%E6%98%8E%E5%8F%97%E5%85%B3%E6%B3%A8" title="胡春华调离广东去向不明受关注" class="media center-cropped modeless" target="_self" data-image="http://scd.cn.rfi.fr/sites/chinese.filesrfi/imagecache/hermes_infographie_vignette_home/sites/images.rfi.fr/files/aef_image/000_tn9pt.jpg" data-width="187" data-height="103">
                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                        <img height="103" width="187" src="http://scd.cn.rfi.fr/sites/chinese.filesrfi/imagecache/hermes_infographie_vignette_home/sites/images.rfi.fr/files/aef_image/000_tn9pt.jpg" alt="media">
                                    </a>
                                                                                                                    <div class="meta">
                                                                    <time datetime="17-10-28">28/10/2017</time>
                                                                                                        <span class="tag">
                                                                                                        <a class="modeless no-decoration" href="/tag/%E4%B8%AD%E5%9B%BD/">中国</a>
                                                </span>
                                <span class="tag">
                                                                                                        <a class="modeless no-decoration" href="/tag/%E4%B8%AD%E5%9B%BD%E9%AB%98%E5%B1%82%E4%BA%BA%E4%BA%8B/">中国高层人事</a>
                                                </span>
                        
                            </div>

                                                                                        <h3 class=" ">
                                    <a href="/%E4%B8%AD%E5%9B%BD/20171028-%E8%83%A1%E6%98%A5%E5%8D%8E%E8%B0%83%E7%A6%BB%E5%B9%BF%E4%B8%9C%E5%8E%BB%E5%90%91%E4%B8%8D%E6%98%8E%E5%8F%97%E5%85%B3%E6%B3%A8" title="&#x80E1;&#x6625;&#x534E;&#x8C03;&#x79BB;&#x5E7F;&#x4E1C;&#x53BB;&#x5411;&#x4E0D;&#x660E;&#x53D7;&#x5173;&#x6CE8;" target="_self" class="modeless">胡春华调离广东去向不明受关注</a>
                                </h3>
                                                                                        <p>中共60后领导人胡春华被调离广东，但他的去向没有被透露，也未获&ldquo;另有任用&rdquo;的标签。胡春华和今年9月被&ldquo;双开&rdquo;的前重庆领导人孙政才曾是中共60后双子接班人选。胡春华在孙政才倒台后，一枝独秀，却未能进入中共19届政治局常委。
</p>
                                                                                </li>
                                                                                                                                                                                                                                                                                                                                                     <li data-bo-type="article" data-bo-nid="WB260066-RFI-ZH-HANS-20171028">
                                                                                                                                <a href="/%E4%B8%AD%E5%9B%BD/20171028-%E8%94%A1%E8%8B%B1%E6%96%87%E8%BF%87%E5%A2%83%E7%BE%8E%E5%9B%BD-%E5%8C%97%E4%BA%AC%E2%80%9C%E4%B8%A5%E6%AD%A3%E4%BA%A4%E6%B6%89%E2%80%9D" title="蔡英文过境美国 北京“严正交涉”" class="media center-cropped modeless" target="_self" data-image="http://scd.cn.rfi.fr/sites/chinese.filesrfi/imagecache/hermes_infographie_vignette_home/sites/images.rfi.fr/files/aef_image/000_t90tk.jpg" data-width="187" data-height="103">
                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                        <img height="103" width="187" src="http://scd.cn.rfi.fr/sites/chinese.filesrfi/imagecache/hermes_infographie_vignette_home/sites/images.rfi.fr/files/aef_image/000_t90tk.jpg" alt="media">
                                    </a>
                                                                                                                    <div class="meta">
                                                                    <time datetime="17-10-28">28/10/2017</time>
                                                                                                        <span class="tag">
                                                                                                        <a class="modeless no-decoration" href="/tag/%E4%B8%AD%E5%9B%BD/">中国</a>
                                                </span>
                                <span class="tag">
                                                                                                        <a class="modeless no-decoration" href="/tag/%E7%BE%8E%E5%9B%BD/">美国</a>
                                                </span>
                                <span class="tag">
                                                                                                        <a class="modeless no-decoration" href="/tag/%E5%8F%B0%E6%B9%BE/">台湾</a>
                                                </span>
                        
                            </div>

                                                                                        <h3 class=" ">
                                    <a href="/%E4%B8%AD%E5%9B%BD/20171028-%E8%94%A1%E8%8B%B1%E6%96%87%E8%BF%87%E5%A2%83%E7%BE%8E%E5%9B%BD-%E5%8C%97%E4%BA%AC%E2%80%9C%E4%B8%A5%E6%AD%A3%E4%BA%A4%E6%B6%89%E2%80%9D" title="&#x8521;&#x82F1;&#x6587;&#x8FC7;&#x5883;&#x7F8E;&#x56FD;&#x20;&#x5317;&#x4EAC;&#x201C;&#x4E25;&#x6B63;&#x4EA4;&#x6D89;&#x201D;" target="_self" class="modeless">蔡英文过境美国 北京&ldquo;严正交涉&rdquo;</a>
                                </h3>
                                                                                        <p>台湾总统蔡英文10月28日出访太平洋3个邦交国。北京向华盛顿提出&ldquo;严正交涉&rdquo;，要求美方拒绝蔡英文过境美国。中美这个裂痕出现在美国总统特朗普到访中国之前。
</p>
                                                                                </li>
                                                                                                                                                                                                                                                                                                                                                     <li data-bo-type="article" data-bo-nid="B37127B7-B34D-47CA-B5DC-0D464DB24AF8">
                                                                                                                                <a href="/%E4%B8%AD%E5%9B%BD/20171028-19%E5%90%8D%E5%8F%B0%E6%B9%BE%E4%BA%BA%E5%9C%A8%E6%9F%AC%E6%B6%89%E7%94%B5%E4%BF%A1%E8%AF%88%E9%AA%97%E8%A2%AB%E9%81%A3%E9%80%81%E4%B8%AD%E5%9B%BD%E5%A4%A7%E9%99%86%E5%8F%B0%E6%B9%BE%E6%8A%97%E8%AE%AE" title="19名台湾人在柬涉电信诈骗被遣送中国大陆台湾抗议" class="media center-cropped modeless" target="_self" data-image="http://scd.cn.rfi.fr/sites/chinese.filesrfi/imagecache/hermes_infographie_vignette_home/sites/images.rfi.fr/files/aef_image/000_cc0e2.jpg" data-width="187" data-height="103">
                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                    <img height="103" width="187" src="http://scd.cn.rfi.fr/sites/chinese.filesrfi/imagecache/hermes_infographie_vignette_home/sites/images.rfi.fr/files/aef_image/000_cc0e2.jpg" alt="media">
                                    </a>
                                                                                                                    <div class="meta">
                                                                    <time datetime="17-10-28">28/10/2017</time>
                                                                                                        <span class="tag">
                                                                                                        <a class="modeless no-decoration" href="/tag/%E5%8F%B0%E6%B9%BE/">台湾</a>
                                                </span>
                                <span class="tag">
                                                                                                        <a class="modeless no-decoration" href="/tag/%E4%B8%AD%E5%9B%BD/">中国</a>
                                                </span>
                                <span class="tag">
                                                                                                        <a class="modeless no-decoration" href="/tag/%E6%9F%AC%E5%9F%94%E5%AF%A8/">柬埔寨</a>
                                                </span>
                        
                            </div>

                                                                                        <h3 class=" ">
                                    <a href="/%E4%B8%AD%E5%9B%BD/20171028-19%E5%90%8D%E5%8F%B0%E6%B9%BE%E4%BA%BA%E5%9C%A8%E6%9F%AC%E6%B6%89%E7%94%B5%E4%BF%A1%E8%AF%88%E9%AA%97%E8%A2%AB%E9%81%A3%E9%80%81%E4%B8%AD%E5%9B%BD%E5%A4%A7%E9%99%86%E5%8F%B0%E6%B9%BE%E6%8A%97%E8%AE%AE" title="19&#x540D;&#x53F0;&#x6E7E;&#x4EBA;&#x5728;&#x67EC;&#x6D89;&#x7535;&#x4FE1;&#x8BC8;&#x9A97;&#x88AB;&#x9063;&#x9001;&#x4E2D;&#x56FD;&#x5927;&#x9646;&#x53F0;&#x6E7E;&#x6297;&#x8BAE;" target="_self" class="modeless">19名台湾人在柬涉电信诈骗被遣送中国大陆台湾抗议</a>
                                </h3>
                                                                                        <p>19名台湾人在柬埔寨涉电信诈骗被强行遣送到中国大陆。台湾陆委会提出抗议，表示，陆方的作法无助于两岸合作打击跨境电信诈骗犯罪，更不利两岸关系的良性发展。
</p>
                                                                                </li>
                                                                                                                                                                                                                                                                                                                                                     <li data-bo-type="article" data-bo-nid="WB260036-RFI-ZH-HANS-20171028">
                                                                                                                                <a href="/%E4%B8%AD%E5%9B%BD/20171028-%E9%87%91%E8%9E%8D%E6%97%B6%E6%8A%A5%E6%8F%AD%E5%BC%80%E7%BB%9F%E6%88%98%E9%83%A8%E7%A5%9E%E7%A7%98%E9%9D%A2%E7%BA%B1%E8%A7%A3%E6%9E%90%E4%B8%AD%E5%9B%BD%E8%BD%AF%E5%AE%9E%E5%8A%9B%E7%9A%84%E6%B3%95%E5%AE%9D" title="金融时报揭开统战部神秘面纱解析中国软实力的法宝" class="media center-cropped modeless" target="_self" data-image="http://scd.cn.rfi.fr/sites/chinese.filesrfi/imagecache/hermes_infographie_vignette_home/sites/images.rfi.fr/files/aef_image/2017-10-24t041218z_368141803_rc1d95ba4a80_rtrmadp_3_china-congress.jpg" data-width="187" data-height="103">
                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                <img height="103" width="187" src="http://scd.cn.rfi.fr/sites/chinese.filesrfi/imagecache/hermes_infographie_vignette_home/sites/images.rfi.fr/files/aef_image/2017-10-24t041218z_368141803_rc1d95ba4a80_rtrmadp_3_china-congress.jpg" alt="media">
                                    </a>
                                                                                                                    <div class="meta">
                                                                    <time datetime="17-10-28">28/10/2017</time>
                                                                                                        <span class="tag">
                                                                                                        <a class="modeless no-decoration" href="/tag/%E4%B8%AD%E5%9B%BD/">中国</a>
                                                </span>
                                <span class="tag">
                                                                                                        <a class="modeless no-decoration" href="/tag/%E6%94%BF%E6%B2%BB/">政治</a>
                                                </span>
                        
                            </div>

                                                                                        <h3 class=" ">
                                    <a href="/%E4%B8%AD%E5%9B%BD/20171028-%E9%87%91%E8%9E%8D%E6%97%B6%E6%8A%A5%E6%8F%AD%E5%BC%80%E7%BB%9F%E6%88%98%E9%83%A8%E7%A5%9E%E7%A7%98%E9%9D%A2%E7%BA%B1%E8%A7%A3%E6%9E%90%E4%B8%AD%E5%9B%BD%E8%BD%AF%E5%AE%9E%E5%8A%9B%E7%9A%84%E6%B3%95%E5%AE%9D" title="&#x91D1;&#x878D;&#x65F6;&#x62A5;&#x63ED;&#x5F00;&#x7EDF;&#x6218;&#x90E8;&#x795E;&#x79D8;&#x9762;&#x7EB1;&#x89E3;&#x6790;&#x4E2D;&#x56FD;&#x8F6F;&#x5B9E;&#x529B;&#x7684;&#x6CD5;&#x5B9D;" target="_self" class="modeless">金融时报揭开统战部神秘面纱解析中国软实力的法宝</a>
                                </h3>
                                                                                        <p>英国金融时报刊登一篇长文，详细介绍和分析中共中央统战部在总书记习近平的督促下，如何为中国扩大国际影响力所承担的任务和角色，文章还引述统战部常务副部长张裔炯日前在十九大召开期间的记者会上所言，统战工作&ldquo;发挥了重要的法宝作用&rdquo;。报道同时又披露了统战部一共有9个局，各司其职，对本国和全 &hellip;</p>
                                                                                </li>
                                                                                                                                                                                                                                                                                                                                                     <li data-bo-type="article" data-bo-nid="WB260035-RFI-ZH-HANS-20171028">
                                                                                                                                <a href="/%E4%B8%AD%E5%9B%BD/20171028-%E4%B9%A0%E6%80%BB%E5%85%A8%E9%9D%A2%E5%AF%B9%E9%A6%99%E6%B8%AF%E7%AE%A1%E6%B2%BB%E6%9D%83%E5%8E%9F%E6%9D%A5%E5%8F%AA%E9%92%88%E5%AF%B9%E6%9E%81%E5%B0%91%E6%95%B0%E4%BA%BA" title="习总“全面对香港管治权”原来只针对“极少数”人" class="media center-cropped modeless" target="_self" data-image="http://scd.cn.rfi.fr/sites/chinese.filesrfi/dynimagecache/0/180/3500/1925/187/103/sites/images.rfi.fr/files/aef_image/2017-10-18t014526z_478131504_rc1c70817b10_rtrmadp_3_china-congress.jpg" data-width="187" data-height="103">
                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                <img height="103" width="187" src="http://scd.cn.rfi.fr/sites/chinese.filesrfi/dynimagecache/0/180/3500/1925/187/103/sites/images.rfi.fr/files/aef_image/2017-10-18t014526z_478131504_rc1c70817b10_rtrmadp_3_china-congress.jpg" alt="media">
                                    </a>
                                                                                                                    <div class="meta">
                                                                    <time datetime="17-10-28">28/10/2017</time>
                                                                                                        <span class="tag">
                                                                                                        <a class="modeless no-decoration" href="/tag/%E4%B8%AD%E5%9B%BD/">中国</a>
                                                </span>
                                <span class="tag">
                                                                                                        <a class="modeless no-decoration" href="/tag/%E6%94%BF%E6%B2%BB/">政治</a>
                                                </span>
                        
                            </div>

                                                                                        <h3 class=" ">
                                    <a href="/%E4%B8%AD%E5%9B%BD/20171028-%E4%B9%A0%E6%80%BB%E5%85%A8%E9%9D%A2%E5%AF%B9%E9%A6%99%E6%B8%AF%E7%AE%A1%E6%B2%BB%E6%9D%83%E5%8E%9F%E6%9D%A5%E5%8F%AA%E9%92%88%E5%AF%B9%E6%9E%81%E5%B0%91%E6%95%B0%E4%BA%BA" title="&#x4E60;&#x603B;&#x201C;&#x5168;&#x9762;&#x5BF9;&#x9999;&#x6E2F;&#x7BA1;&#x6CBB;&#x6743;&#x201D;&#x539F;&#x6765;&#x53EA;&#x9488;&#x5BF9;&#x201C;&#x6781;&#x5C11;&#x6570;&#x201D;&#x4EBA;" target="_self" class="modeless">习总&ldquo;全面对香港管治权&rdquo;原来只针对&ldquo;极少数&rdquo;人</a>
                                </h3>
                                                                                        <p>刚在不久前闭幕的十九大上从候补晋升中共中央委员的港澳办主任张晓明，在官网撰文，为习近平在十九大报告中提到的中央对港有&ldquo;全面管治权&rdquo;作出辩解，声称此论引起担心会影响香港的高度自治，但认为这种担心是不必要的。
</p>
                                                                                </li>
                                                            


                </ul>

                                                                                                                                
                                                                <a href="/%E4%B8%AD%E5%9B%BD/all/?page=2" class="btn-load-more alt more-loader"
                           data-div-id='articleList'
                           data-href='/%E4%B8%AD%E5%9B%BD/all/?page=2'
                           data-itemsperpage="15"
                           data-globalcount="29323"
                           data-next-level='2'>
                            更多文章
                        </a>
                                    
            
        </section>

                <aside>
                                        <div class="banner first" data-bo-type="em" data-bo-nid="55FBBB39-B0F6-4EA5-BE85-91A5D1A8298A">
                    
    <div class="slider-rfi-auto-ad">
    <ul class="slides autopromo-mask">
                                                                                <li>
                            <a target="_blank"
                                href="http://cn.rfi.fr/%E4%BA%BA%E6%9D%83/20170713-%E5%88%98%E6%99%93%E6%B3%A2%EF%BC%8819551228%EF%BC%8D2017713%EF%BC%89"
                                title="刘晓波">
                                <img src="http://scd.cn.rfi.fr/sites/chinese.filesrfi/imagecache/aef_image_original_format/sites/images.rfi.fr/files/aef_image/denrmwnw0aaplvk.jpg" alt="刘晓波" width="300" height="135">
                            </a>
                        </li>
                                            <li>
                            <a target="_blank"
                                href="http://cn.rfi.fr/%E4%B8%AD%E5%9B%BD/20170628-%E8%AF%BA%E8%B4%9D%E5%B0%94%E5%A5%96%E5%92%8C%E5%B9%B3%E5%A5%96%E5%BE%97%E4%B8%BB%E5%88%98%E6%99%93%E6%B3%A2"
                                title="刘晓波和妻子刘霞">
                                <img src="http://scd.cn.rfi.fr/sites/chinese.filesrfi/imagecache/aef_image_original_format/sites/images.rfi.fr/files/aef_image/2010-11p28yu.jpg" alt="刘晓波和妻子刘霞" width="300" height="135">
                            </a>
                        </li>
                                            <li>
                            <a target="_blank"
                                href="http://cn.rfi.fr/%E4%B8%93%E6%A0%8F%E6%A3%80%E7%B4%A2/%E6%B3%95%E5%9B%BD%E6%80%9D%E6%83%B3%E9%95%BF%E5%BB%8A"
                                title="罗丹雕塑思想者">
                                <img src="http://scd.cn.rfi.fr/sites/chinese.filesrfi/imagecache/aef_image_original_format/sites/images.rfi.fr/files/aef_image/luodansixiangzhediaosuyishu_6702595.jpg" alt="罗丹雕塑思想者" width="300" height="135">
                            </a>
                        </li>
                                            <li>
                            <a target="_blank"
                                href="http://cn.rfi.fr/%E6%B3%95%E5%9B%BD/20170607-2017%E6%B3%95%E5%9B%BD%E7%AB%8B%E6%B3%95%E9%80%89%E4%B8%BE"
                                title="2017法国立法选举">
                                <img src="http://scd.cn.rfi.fr/sites/chinese.filesrfi/imagecache/aef_image_original_format/sites/images.rfi.fr/files/aef_image/habillage-rfi_elec-legislatives_cn.jpg" alt="2017法国立法选举" width="300" height="135">
                            </a>
                        </li>
                                                            </ul>
</div>




    </div>


    <div class="banner">
                    
    


                        
    <div class="tms-block"
         data-pos="1"
         data-type="pave"
         data-location="sidebar"
         data-expand="true"
         data-loaded="false">
    </div>





    </div>

    <section class="forum">
                                            
            <div class="h2">大家评说</div>
        <ul>
                                                                                                                                        <li data-bo-type="article" data-bo-nid="F5D4C454-D8F7-4900-96F6-654B70CD16D8">
                    <div class="meta">
                        <time datetime="17-08-23">23/08/2017</time>
                        <span class="author" rel="author">
                                                            <a class="modeless" href="/%E4%B8%AD%E5%9B%BD/20170823-%E6%AF%9B%E6%80%9D%E6%83%B3%E4%B9%A0%E6%80%9D%E6%83%B3%E4%B8%AD%E5%9B%BD%E9%9C%80%E8%A6%81%E4%BB%80%E4%B9%88%E6%80%9D%E6%83%B3" title="&#x6BDB;&#x601D;&#x60F3;&#x4E60;&#x601D;&#x60F3;&#x4E2D;&#x56FD;&#x9700;&#x8981;&#x4EC0;&#x4E48;&#x601D;&#x60F3;">
                                    毛思想习思想中国需要什么思想
                                </a>
                                                                                </span>
                    </div>
                                            <span class="h3">
                        <a class="modeless" href="/%E4%B8%AD%E5%9B%BD/20170823-%E6%AF%9B%E6%80%9D%E6%83%B3%E4%B9%A0%E6%80%9D%E6%83%B3%E4%B8%AD%E5%9B%BD%E9%9C%80%E8%A6%81%E4%BB%80%E4%B9%88%E6%80%9D%E6%83%B3" title="&#x6BDB;&#x601D;&#x60F3;&#x4E60;&#x601D;&#x60F3;&#x4E2D;&#x56FD;&#x9700;&#x8981;&#x4EC0;&#x4E48;&#x601D;&#x60F3;">现在说&ldquo;习近平思想&rdquo;，有点像以前某个阶段说&ldquo;毛泽东思想&rdquo;，炙手可热。&ldquo;毛思想&rdquo;的核心大约是&ldquo;无产阶级专政下的继续革命&rdquo;，搞&ldquo;阶级斗争&rdquo;，结果&nbsp;&hellip;</a>
                    </span>
                                            <span class="disqus-comment-count"
      data-disqus-identifier="20170823-毛思想习思想中国需要什么思想"
      data-disqus-url="/%E4%B8%AD%E5%9B%BD/20170823-%E6%AF%9B%E6%80%9D%E6%83%B3%E4%B9%A0%E6%80%9D%E6%83%B3%E4%B8%AD%E5%9B%BD%E9%9C%80%E8%A6%81%E4%BB%80%E4%B9%88%E6%80%9D%E6%83%B3"
>&nbsp;</span>
                                                            </li>
                                                                                                                                <li data-bo-type="article" data-bo-nid="DE9F2133-6A0A-42E9-AD64-9B316B68536C">
                    <div class="meta">
                        <time datetime="17-09-19">19/09/2017</time>
                        <span class="author" rel="author">
                                                            <a class="modeless" href="/%E4%B8%AD%E5%9B%BD/20170919-%E8%B0%81%E9%83%BD%E5%8F%AF%E8%83%BD%E4%BC%9A%E6%B2%A6%E4%B8%BA%E6%B0%94%E5%80%99%E9%9A%BE%E6%B0%91" title="&#x8C01;&#x90FD;&#x53EF;&#x80FD;&#x4F1A;&#x6CA6;&#x4E3A;&#x6C14;&#x5019;&#x96BE;&#x6C11;&#xFF1F;">
                                    谁都可能会沦为气候难民？
                                </a>
                                                                                </span>
                    </div>
                                            <span class="h3">
                        <a class="modeless" href="/%E4%B8%AD%E5%9B%BD/20170919-%E8%B0%81%E9%83%BD%E5%8F%AF%E8%83%BD%E4%BC%9A%E6%B2%A6%E4%B8%BA%E6%B0%94%E5%80%99%E9%9A%BE%E6%B0%91" title="&#x8C01;&#x90FD;&#x53EF;&#x80FD;&#x4F1A;&#x6CA6;&#x4E3A;&#x6C14;&#x5019;&#x96BE;&#x6C11;&#xFF1F;">几周来袭击美国、袭击加勒比海法国海外省的飓风，造成的后果相当严重，飓风过后，满目疮痍。
</a>
                    </span>
                                            <span class="disqus-comment-count"
      data-disqus-identifier="20170919-谁都可能会沦为气候难民"
      data-disqus-url="/%E4%B8%AD%E5%9B%BD/20170919-%E8%B0%81%E9%83%BD%E5%8F%AF%E8%83%BD%E4%BC%9A%E6%B2%A6%E4%B8%BA%E6%B0%94%E5%80%99%E9%9A%BE%E6%B0%91"
>&nbsp;</span>
                                                            </li>
                            </ul>
                <a href="/%E4%B8%AD%E5%9B%BD/20130503-%E5%A4%A7%E5%AE%B6%E8%AF%84%E8%AF%B4" class="btn-more">更多"大家评说"</a>
    
    </section>

    <section>
        <div class="em-twitter orientation-center">
            <span class="side-block">推特</span>
             <a class="twitter-timeline"  href="https://twitter.com/RFI_Cn"
height="400"
width="300"
data-widget-id="642018444867727361"
data-tweet-limit="1"
data-link-color='#E20000'
data-chrome="noheader nofooter noborders transparent"
lang="zh-cn">Tweets by @RFI_Cn</a>
</div>

    </section>


    <section>
        <div class="em-flash aside">
                        <span class="side-block">脸书</span>
                <iframe src="//www.facebook.com/plugins/likebox.php?href=https%3A%2F%2Fwww.facebook.com%2Fpages%2F%25E6%25B3%2595%25E5%259B%25BD%25E5%259B%25BD%25E9%2599%2585%25E5%25B9%25BF%25E6%2592%25AD%25E7%2594%25B5%25E5%258F%25B0%2F155677885272&amp;width=300&amp;height=230&amp;colorscheme=light&amp;show_faces=true&amp;stream=false&amp;header=false&amp;locale=zh_CN&amp;show_border=false&amp;appId=113191652055439" scrolling="no" frameborder="0" style="border:none; overflow:hidden; width:300px; height:212px;" allowTransparency="true"></iframe>
    </div>

    </section>


    <section>
                    
                
                            
                                
            <div class="h2">更多中国新闻</div>
                    <ul>
                            <li data-bo-type="article" data-bo-nid="FE001A5A-18CC-4ADC-9142-15733A072CE6">
                    <div class="meta">
                        <time datetime="17-10-28">28/10/2017</time>
                                                                <span class="tag">
                                                                                                        <a class="modeless no-decoration" href="/tag/%E4%B8%AD%E5%9B%BD/">中国</a>
                                                </span>
                        
                    </div>
                    <span class="h3">
                                                    <a class="modeless" href="/%E4%B8%AD%E5%9B%BD/20171028-%E7%89%B9%E6%9C%97%E6%99%AE%E8%AE%BF%E5%8D%8E%E5%89%8D%E7%BE%8E%E5%95%86%E5%8A%A1%E9%83%A8%E5%88%9D%E8%A3%81%E4%B8%AD%E5%9B%BD%E9%93%9D%E7%AE%94%E5%80%BE%E9%94%80" title="&#x7279;&#x6717;&#x666E;&#x8BBF;&#x534E;&#x524D;&#x7F8E;&#x5546;&#x52A1;&#x90E8;&#x521D;&#x88C1;&#x4E2D;&#x56FD;&#x94DD;&#x7B94;&#x503E;&#x9500;">特朗普访华前美商务部初裁中国铝箔倾销</a>
                                            </span>
                </li>
                            <li data-bo-type="article" data-bo-nid="7219A10A-6601-43EC-9704-7392EA1D4338">
                    <div class="meta">
                        <time datetime="17-10-28">28/10/2017</time>
                                                                <span class="tag">
                                                                                                        <a class="modeless no-decoration" href="/tag/%E4%B8%AD%E5%9B%BD/">中国</a>
                                                </span>
                                <span class="tag">
                                                                                                        <a class="modeless no-decoration" href="/tag/%E6%97%A5%E6%9C%AC/">日本</a>
                                                </span>
                        
                    </div>
                    <span class="h3">
                                                    <a class="modeless" href="/%E4%B8%AD%E5%9B%BD/20171028-%E5%8D%97%E4%BA%AC%E5%A4%A7%E5%B1%A0%E6%9D%80%E9%81%87%E9%9A%BE%E5%90%8C%E8%83%9E%E7%BA%AA%E5%BF%B5%E9%A6%86%E9%A6%86%E9%95%BF%E5%90%81%E5%AE%89%E5%80%8D%E5%8F%82%E8%A7%82" title="&#x5357;&#x4EAC;&#x5927;&#x5C60;&#x6740;&#x9047;&#x96BE;&#x540C;&#x80DE;&#x7EAA;&#x5FF5;&#x9986;&#x9986;&#x957F;&#x5401;&#x5B89;&#x500D;&#x53C2;&#x89C2;">南京大屠杀遇难同胞纪念馆馆长吁安倍参观</a>
                                            </span>
                </li>
                            <li data-bo-type="article" data-bo-nid="972C58DF-3993-466C-BE70-A9333EE88567">
                    <div class="meta">
                        <time datetime="17-10-28">28/10/2017</time>
                                                                <span class="tag">
                                                                                                        <a class="modeless no-decoration" href="/tag/%E4%B8%AD%E5%9B%BD/">中国</a>
                                                </span>
                                <span class="tag">
                                                                                                        <a class="modeless no-decoration" href="/tag/%E4%B8%AD%E5%9B%BD%E9%AB%98%E5%B1%82%E4%BA%BA%E4%BA%8B/">中国高层人事</a>
                                                </span>
                        
                    </div>
                    <span class="h3">
                                                    <a class="modeless" href="/%E4%B8%AD%E5%9B%BD/20171028-%E8%83%A1%E6%98%A5%E5%8D%8E%E8%B0%83%E7%A6%BB%E5%B9%BF%E4%B8%9C%E5%8E%BB%E5%90%91%E4%B8%8D%E6%98%8E%E5%8F%97%E5%85%B3%E6%B3%A8" title="&#x80E1;&#x6625;&#x534E;&#x8C03;&#x79BB;&#x5E7F;&#x4E1C;&#x53BB;&#x5411;&#x4E0D;&#x660E;&#x53D7;&#x5173;&#x6CE8;">胡春华调离广东去向不明受关注</a>
                                            </span>
                </li>
                        </ul>
                            

    </section>

<section>
    <div class="wide-angle">
            <div class="hd">
        <span class="side-block">法新社</span>
    </div>
    <div class="bd">
        <ul class="wa-list slides">
                                                                    <li data-bo-type="depeche" data-bo-nid="B1CCBA5C-0F7B-4F14-ADD7-888A6B084CEA">
                                        <p class="media"><img src="http://scd.cn.rfi.fr/sites/chinese.filesrfi/imagecache/aef_ct_wire_image_620/images/afp/int0019b.171030185002.jpg" alt="" /></p>

                    <div class="copy">
                                                                        <h4 class="title">美国堪萨斯州州长选举刮起青少年参选风</h4>
                    </div>

                                                            
                    <p class="default-read-more">
                        <a rel="nofollow" title="美国堪萨斯州州长选举刮起青少年参选风" href="http://cn.rfi.fr/wire/20171030-%E7%BE%8E%E5%9B%BD%E5%A0%AA%E8%90%A8%E6%96%AF%E5%B7%9E%E5%B7%9E%E9%95%BF%E9%80%89%E4%B8%BE%E5%88%AE%E8%B5%B7%E9%9D%92%E5%B0%91%E5%B9%B4%E5%8F%82%E9%80%89%E9%A3%8E" class="modeless" ></a>
                    </p>
                </li>
                            <li data-bo-type="depeche" data-bo-nid="3C145A01-B398-495A-A52F-F4C6CB9B935B">
                                        <p class="media"><img src="http://scd.cn.rfi.fr/sites/chinese.filesrfi/imagecache/aef_ct_wire_image_620/images/afp/int0018b.171030180501.jpg" alt="" /></p>

                    <div class="copy">
                                                                        <h4 class="title">肯亚总统大选重新投票  结果还得等等</h4>
                    </div>

                                                            
                    <p class="default-read-more">
                        <a rel="nofollow" title="肯亚总统大选重新投票  结果还得等等" href="http://cn.rfi.fr/wire/20171030-%E8%82%AF%E4%BA%9A%E6%80%BB%E7%BB%9F%E5%A4%A7%E9%80%89%E9%87%8D%E6%96%B0%E6%8A%95%E7%A5%A8-%E7%BB%93%E6%9E%9C%E8%BF%98%E5%BE%97%E7%AD%89%E7%AD%89" class="modeless" ></a>
                    </p>
                </li>
                            <li data-bo-type="depeche" data-bo-nid="6C764692-E013-47A4-AF37-75C4F2FC684F">
                                        <p class="media"><img src="http://scd.cn.rfi.fr/sites/chinese.filesrfi/imagecache/aef_ct_wire_image_620/images/afp/eco0002b.171030182006.jpg" alt="" /></p>

                    <div class="copy">
                                                                        <h4 class="title">亚洲业绩旺 汇丰第3季获利狂翻5倍</h4>
                    </div>

                                                            
                    <p class="default-read-more">
                        <a rel="nofollow" title="亚洲业绩旺 汇丰第3季获利狂翻5倍" href="http://cn.rfi.fr/wire/20171030-%E4%BA%9A%E6%B4%B2%E4%B8%9A%E7%BB%A9%E6%97%BA-%E6%B1%87%E4%B8%B0%E7%AC%AC3%E5%AD%A3%E8%8E%B7%E5%88%A9%E7%8B%82%E7%BF%BB5%E5%80%8D" class="modeless" ></a>
                    </p>
                </li>
                            <li data-bo-type="depeche" data-bo-nid="431814EE-B992-4072-8912-68F1534908BE">
                                        <p class="media"><img src="http://scd.cn.rfi.fr/sites/chinese.filesrfi/imagecache/aef_ct_wire_image_620/images/afp/int0017b.171030163502.jpg" alt="" /></p>

                    <div class="copy">
                                                                        <h4 class="title">洛兴雅孩童饱受创伤 小丑耍宝抚慰他们</h4>
                    </div>

                                                            
                    <p class="default-read-more">
                        <a rel="nofollow" title="洛兴雅孩童饱受创伤 小丑耍宝抚慰他们" href="http://cn.rfi.fr/wire/20171030-%E6%B4%9B%E5%85%B4%E9%9B%85%E5%AD%A9%E7%AB%A5%E9%A5%B1%E5%8F%97%E5%88%9B%E4%BC%A4-%E5%B0%8F%E4%B8%91%E8%80%8D%E5%AE%9D%E6%8A%9A%E6%85%B0%E4%BB%96%E4%BB%AC" class="modeless" ></a>
                    </p>
                </li>
                            <li data-bo-type="depeche" data-bo-nid="9B0D2E5F-9002-4A53-9642-097D699E5CC8">
                                        <p class="media"><img src="http://scd.cn.rfi.fr/sites/chinese.filesrfi/imagecache/aef_ct_wire_image_620/images/afp/health0001b.171030163504.jpg" alt="" /></p>

                    <div class="copy">
                                                                        <h4 class="title">参加气候会谈争公平 美方官员任务艰困</h4>
                    </div>

                                                            
                    <p class="default-read-more">
                        <a rel="nofollow" title="参加气候会谈争公平 美方官员任务艰困" href="http://cn.rfi.fr/wire/20171030-%E5%8F%82%E5%8A%A0%E6%B0%94%E5%80%99%E4%BC%9A%E8%B0%88%E4%BA%89%E5%85%AC%E5%B9%B3-%E7%BE%8E%E6%96%B9%E5%AE%98%E5%91%98%E4%BB%BB%E5%8A%A1%E8%89%B0%E5%9B%B0" class="modeless" ></a>
                    </p>
                </li>
                            <li data-bo-type="depeche" data-bo-nid="0B5076FD-359C-4794-83E3-81E545DDCF09">
                                        <p class="media"><img src="http://scd.cn.rfi.fr/sites/chinese.filesrfi/imagecache/aef_ct_wire_image_620/images/afp/eco0001b.171030163503.jpg" alt="" /></p>

                    <div class="copy">
                                                                        <h4 class="title">日股收盘近乎持平 续创21年高点</h4>
                    </div>

                                                            
                    <p class="default-read-more">
                        <a rel="nofollow" title="日股收盘近乎持平 续创21年高点" href="http://cn.rfi.fr/wire/20171030-%E6%97%A5%E8%82%A1%E6%94%B6%E7%9B%98%E8%BF%91%E4%B9%8E%E6%8C%81%E5%B9%B3-%E7%BB%AD%E5%88%9B21%E5%B9%B4%E9%AB%98%E7%82%B9" class="modeless" ></a>
                    </p>
                </li>
                            <li data-bo-type="depeche" data-bo-nid="0E7F12E1-B504-47FB-A710-269D2924513A">
                                        <p class="media"><img src="http://scd.cn.rfi.fr/sites/chinese.filesrfi/imagecache/aef_ct_wire_image_620/images/afp/top0005b.171030160502.jpg" alt="" /></p>

                    <div class="copy">
                                                                        <h4 class="title">瑞穗金融大裁员 10年内拟削减1/3人力</h4>
                    </div>

                                                            
                    <p class="default-read-more">
                        <a rel="nofollow" title="瑞穗金融大裁员 10年内拟削减1/3人力" href="http://cn.rfi.fr/wire/20171030-%E7%91%9E%E7%A9%97%E9%87%91%E8%9E%8D%E5%A4%A7%E8%A3%81%E5%91%98-10%E5%B9%B4%E5%86%85%E6%8B%9F%E5%89%8A%E5%87%8F13%E4%BA%BA%E5%8A%9B" class="modeless" ></a>
                    </p>
                </li>
                            <li data-bo-type="depeche" data-bo-nid="8059EE93-3E19-4052-927F-C16080C85B01">
                                        <p class="media"><img src="http://scd.cn.rfi.fr/sites/chinese.filesrfi/imagecache/aef_ct_wire_image_620/images/afp/int0014b.171030153506.jpg" alt="" /></p>

                    <div class="copy">
                                                                        <h4 class="title">大权独立的侦探 历年还有这些特别检察官</h4>
                    </div>

                                                            
                    <p class="default-read-more">
                        <a rel="nofollow" title="大权独立的侦探 历年还有这些特别检察官" href="http://cn.rfi.fr/wire/20171030-%E5%A4%A7%E6%9D%83%E7%8B%AC%E7%AB%8B%E7%9A%84%E4%BE%A6%E6%8E%A2-%E5%8E%86%E5%B9%B4%E8%BF%98%E6%9C%89%E8%BF%99%E4%BA%9B%E7%89%B9%E5%88%AB%E6%A3%80%E5%AF%9F%E5%AE%98" class="modeless" ></a>
                    </p>
                </li>
                            <li data-bo-type="depeche" data-bo-nid="4809D329-F18F-40BA-B8A1-781224925D70">
                                        <p class="media"><img src="http://scd.cn.rfi.fr/sites/chinese.filesrfi/imagecache/aef_ct_wire_image_620/images/afp/int0015b.171030155001.jpg" alt="" /></p>

                    <div class="copy">
                                                                        <h4 class="title">「＃我也是」运动走出网路 法女性挺身反性骚</h4>
                    </div>

                                                            
                    <p class="default-read-more">
                        <a rel="nofollow" title="「＃我也是」运动走出网路 法女性挺身反性骚" href="http://cn.rfi.fr/wire/20171030-%EF%BC%83%E6%88%91%E4%B9%9F%E6%98%AF%E8%BF%90%E5%8A%A8%E8%B5%B0%E5%87%BA%E7%BD%91%E8%B7%AF-%E6%B3%95%E5%A5%B3%E6%80%A7%E6%8C%BA%E8%BA%AB%E5%8F%8D%E6%80%A7%E9%AA%9A" class="modeless" ></a>
                    </p>
                </li>
                            <li data-bo-type="depeche" data-bo-nid="E038C405-6F68-401C-BDC3-378BA24522BA">
                                        <p class="media"><img src="http://scd.cn.rfi.fr/sites/chinese.filesrfi/imagecache/aef_ct_wire_image_620/images/afp/int0011b.171030153502.jpg" alt="" /></p>

                    <div class="copy">
                                                                        <h4 class="title">北约秘书长访日本 称北韩是全球威胁</h4>
                    </div>

                                                            
                    <p class="default-read-more">
                        <a rel="nofollow" title="北约秘书长访日本 称北韩是全球威胁" href="http://cn.rfi.fr/wire/20171030-%E5%8C%97%E7%BA%A6%E7%A7%98%E4%B9%A6%E9%95%BF%E8%AE%BF%E6%97%A5%E6%9C%AC-%E7%A7%B0%E5%8C%97%E9%9F%A9%E6%98%AF%E5%85%A8%E7%90%83%E5%A8%81%E8%83%81" class="modeless" ></a>
                    </p>
                </li>
                            <li data-bo-type="depeche" data-bo-nid="E96093E3-3FED-4200-A478-A4A97CB542D1">
                                        <p class="media"><img src="http://scd.cn.rfi.fr/sites/chinese.filesrfi/imagecache/aef_ct_wire_image_620/images/afp/int0012b.171030153503.jpg" alt="" /></p>

                    <div class="copy">
                                                                        <h4 class="title">冰岛不沾锅 连串丑闻打不倒贝尼狄克逊</h4>
                    </div>

                                                            
                    <p class="default-read-more">
                        <a rel="nofollow" title="冰岛不沾锅 连串丑闻打不倒贝尼狄克逊" href="http://cn.rfi.fr/wire/20171030-%E5%86%B0%E5%B2%9B%E4%B8%8D%E6%B2%BE%E9%94%85-%E8%BF%9E%E4%B8%B2%E4%B8%91%E9%97%BB%E6%89%93%E4%B8%8D%E5%80%92%E8%B4%9D%E5%B0%BC%E7%8B%84%E5%85%8B%E9%80%8A" class="modeless" ></a>
                    </p>
                </li>
                            <li data-bo-type="depeche" data-bo-nid="7F8B199F-50CD-40A6-9B9B-25D14E6E623B">
                                        <p class="media"><img src="http://scd.cn.rfi.fr/sites/chinese.filesrfi/imagecache/aef_ct_wire_image_620/images/afp/int0013b.171030153504.jpg" alt="" /></p>

                    <div class="copy">
                                                                        <h4 class="title">遭波湾4国制裁 卡达国王提阴谋论</h4>
                    </div>

                                                            
                    <p class="default-read-more">
                        <a rel="nofollow" title="遭波湾4国制裁 卡达国王提阴谋论" href="http://cn.rfi.fr/wire/20171030-%E9%81%AD%E6%B3%A2%E6%B9%BE4%E5%9B%BD%E5%88%B6%E8%A3%81-%E5%8D%A1%E8%BE%BE%E5%9B%BD%E7%8E%8B%E6%8F%90%E9%98%B4%E8%B0%8B%E8%AE%BA" class="modeless" ></a>
                    </p>
                </li>
                    </ul>
    </div>

    </div>
</section>

    <section>
                    
                
                            
                                
            <div class="h2">法广专访</div>
                    <ul>
                            <li data-bo-type="edition" data-bo-nid="4711454D-DF48-4A1F-A08E-9DFAA6145975">
                    <div class="meta">
                        <time datetime="17-08-19">19/08/2017</time>
                                                                <span class="tag">
                                                                                                        <a class="modeless no-decoration" href="/tag/%E4%B8%AD%E5%9B%BD/">中国</a>
                                                </span>
                                <span class="tag">
                                                                                                        <a class="modeless no-decoration" href="/tag/%E9%A6%99%E6%B8%AF/">香港</a>
                                                </span>
                                <span class="tag">
                                                                                                        <a class="modeless no-decoration" href="/tag/%E6%94%BF%E6%B2%BB/">政治</a>
                                                </span>
                                <span class="tag">
                                                                                                        <a class="modeless no-decoration" href="/tag/%E7%A4%BE%E4%BC%9A/">社会</a>
                                                </span>
                        
                    </div>
                    <span class="h3">
                                                    <a class="modeless" href="/%E6%94%BF%E6%B2%BB/20170819-%E9%A6%99%E6%B8%AF%E4%B8%BB%E6%9D%83%E5%9B%9E%E5%BD%92%EF%BC%92%EF%BC%90%E5%91%A8%E5%B9%B4%E9%9D%92%E5%B9%B4%E8%AE%BF%E8%B0%88%E4%B9%8B%E4%BA%8C%E6%B8%AF%E4%BA%BA%E7%9F%9B%E7%9B%BE%E7%9A%84%E4%B8%AD%E5%9B%BD%E6%83%85%E7%BB%93" title="&#x9999;&#x6E2F;&#x4E3B;&#x6743;&#x56DE;&#x5F52;20&#x5468;&#x5E74;&#x9752;&#x5E74;&#x8BBF;&#x8C08;&#x4E4B;&#x4E8C;&#xFF1A;&#x6E2F;&#x4EBA;&#x77DB;&#x76FE;&#x7684;&#x4E2D;&#x56FD;&#x60C5;&#x7ED3;">香港主权回归20周年青年访谈之二：港人矛盾的中国情结</a>
                                            </span>
                </li>
                            <li data-bo-type="edition" data-bo-nid="0C22A9A6-B69B-47C9-8A2D-08C574DC000A">
                    <div class="meta">
                        <time datetime="17-08-01">01/08/2017</time>
                                                                <span class="tag">
                                                                                                        <a class="modeless no-decoration" href="/tag/%E6%B8%AF%E6%BE%B3/">港澳</a>
                                                </span>
                                <span class="tag">
                                                                                                        <a class="modeless no-decoration" href="/tag/%E6%94%BF%E6%B2%BB/">政治</a>
                                                </span>
                                <span class="tag">
                                                                                                        <a class="modeless no-decoration" href="/tag/%E7%A4%BE%E4%BC%9A/">社会</a>
                                                </span>
                        
                    </div>
                    <span class="h3">
                                                    <a class="modeless" href="/%E6%B8%AF%E6%BE%B3%E5%8F%B0/20170801-%E9%A6%99%E6%B8%AF%E4%B8%BB%E6%9D%83%E5%9B%9E%E5%BD%9220%E5%91%A8%E5%B9%B4%E9%9D%92%E5%B9%B4%E8%AE%BF%E8%B0%88%E4%B9%8B%E4%B8%80" title="&#x9999;&#x6E2F;&#x4E3B;&#x6743;&#x56DE;&#x5F52;20&#x5468;&#x5E74;&#x9752;&#x5E74;&#x8BBF;&#x8C08;&#x4E4B;&#x4E00;&#xFF1A;&#x81EA;&#x7531;&#x8868;&#x8FBE;&#x7684;&#x6743;&#x5229;&#x662F;&#x9999;&#x6E2F;&#x7E41;&#x8363;&#x7684;&#x57FA;&#x77F3;">香港主权回归20周年青年访谈之一：自由表达的权利是香港繁荣的基石</a>
                                            </span>
                </li>
                            <li data-bo-type="edition" data-bo-nid="72DD0791-407D-408B-9930-CCDBB63F21CF">
                    <div class="meta">
                        <time datetime="17-07-18">18/07/2017</time>
                                                                <span class="tag">
                                                                                                        <a class="modeless no-decoration" href="/tag/%E4%B8%AD%E5%9B%BD/">中国</a>
                                                </span>
                                <span class="tag">
                                                                                                        <a class="modeless no-decoration" href="/tag/%E6%94%BF%E6%B2%BB/">政治</a>
                                                </span>
                                <span class="tag">
                                                                                                        <a class="modeless no-decoration" href="/tag/%E5%88%98%E6%99%93%E6%B3%A2/">刘晓波</a>
                                                </span>
                        
                    </div>
                    <span class="h3">
                                                    <a class="modeless" href="/%E4%B8%AD%E5%9B%BD/20170718-%E5%BE%90%E5%8F%8B%E6%B8%94%EF%BC%9A%E5%AE%AA%E6%94%BF%E6%B0%91%E4%B8%BB%E4%B8%8E%E5%92%8C%E5%B9%B3%E7%90%86%E6%80%A7%E6%98%AF%E5%88%98%E6%99%93%E6%B3%A2%E9%87%8D%E8%A6%81%E7%B2%BE%E7%A5%9E%E9%81%97%E4%BA%A7" title="&#x5F90;&#x53CB;&#x6E14;&#xFF1A;&#x5BAA;&#x653F;&#x6C11;&#x4E3B;&#x4E0E;&#x548C;&#x5E73;&#x7406;&#x6027;&#x662F;&#x5218;&#x6653;&#x6CE2;&#x91CD;&#x8981;&#x7CBE;&#x795E;&#x9057;&#x4EA7;">徐友渔：宪政民主与和平理性是刘晓波重要精神遗产</a>
                                            </span>
                </li>
                        </ul>
                            

    </section>

<section>
                
                
                            
                                
            <div class="h2">争鸣/来稿/论坛</div>
                    <ul>
                            <li data-bo-type="article" data-bo-nid="10021D71-3B27-4E44-9D79-CBEA7348BA69">
                    <div class="meta">
                        <time datetime="17-07-12">12/07/2017</time>
                                                                <span class="tag">
                                                                                                        <a class="modeless no-decoration" href="/tag/%E7%BD%91%E6%96%87%E9%80%89%E5%88%8A/">网文选刊</a>
                                                </span>
                        
                    </div>
                    <span class="h3">
                                                    <a class="modeless" href="/%E9%A6%96%E9%A1%B5/20170712-%E4%BD%99%E6%9D%B0%EF%BC%9A%E5%88%98%E9%9C%9E%E2%80%94%E2%80%94%E4%BD%9C%E4%B8%BA%E5%88%98%E6%99%93%E6%B3%A2%E7%9A%84%E4%BA%BA%E8%B4%A8" title="&#x4F59;&#x6770;&#xFF1A;&#x5218;&#x971E;&#x2014;&#x2014;&#x4F5C;&#x4E3A;&#x5218;&#x6653;&#x6CE2;&#x7684;&#x4EBA;&#x8D28;">余杰：刘霞——作为刘晓波的人质</a>
                                            </span>
                </li>
                            <li data-bo-type="article" data-bo-nid="5E44090D-40BD-494A-967E-12129377DE23">
                    <div class="meta">
                        <time datetime="17-07-07">07/07/2017</time>
                                                                <span class="tag">
                                                                                                        <a class="modeless no-decoration" href="/tag/%E5%88%98%E6%99%93%E6%B3%A2/">刘晓波</a>
                                                </span>
                                <span class="tag">
                                                                                                        <a class="modeless no-decoration" href="/tag/%E7%BD%91%E6%96%87%E9%80%89%E5%88%8A/">网文选刊</a>
                                                </span>
                        
                    </div>
                    <span class="h3">
                                                    <a class="modeless" href="/%E9%A6%96%E9%A1%B5/20170707-%E5%88%98%E6%99%93%E6%B3%A2%E7%97%85%E6%83%85%E5%8A%A0%E9%87%8D%EF%BC%8C%E6%88%91%E4%BB%AC%E5%BA%94%E8%AF%A5%E6%80%8E%E4%B9%88%E5%81%9A%EF%BC%9F" title="&#x5218;&#x6653;&#x6CE2;&#x75C5;&#x60C5;&#x52A0;&#x91CD;&#xFF0C;&#x6211;&#x4EEC;&#x5E94;&#x8BE5;&#x600E;&#x4E48;&#x505A;&#xFF1F;">刘晓波病情加重，我们应该怎么做？</a>
                                            </span>
                </li>
                        </ul>
                                    <a href="/tag/%E7%BD%91%E6%96%87%E9%80%89%E5%88%8A/" class="btn-more">更多</a>
    

</section>



                    </aside>

                        <section class="slider slider-broadcast next-prev-top">
                    
                
                                                    
    <div class="h2">时事分析与报摘</div>

                    <ul>
                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                        
                    <li data-bo-type="edition" data-bo-nid="WB260212-RFI-ZH-HANS-20171030">
                        <a href="/%E4%B8%AD%E5%9B%BD/20171030-%E4%B8%AD%E5%85%B1%E5%8A%A0%E5%BC%BA%E5%AF%B9%E4%BC%81%E4%B8%9A%E9%A2%86%E5%AF%BC" title="&#x4E2D;&#x5171;&#x52A0;&#x5F3A;&#x5BF9;&#x4F01;&#x4E1A;&#x9886;&#x5BFC;"
                                                        class="media center-cropped modeless lazy-loaded"
                            data-image="http://scd.cn.rfi.fr/sites/chinese.filesrfi/imagecache/rfi_169_small/sites/images.rfi.fr/files/aef_image/2017-10-18t064704z_883700935_rc1a865fcb00_rtrmadp_3_china-congress.jpg" data-width="202" data-height="114"
                        >
                                                            <noscript>
                                    <img src="http://scd.cn.rfi.fr/sites/chinese.filesrfi/imagecache/rfi_169_small/sites/images.rfi.fr/files/aef_image/2017-10-18t064704z_883700935_rc1a865fcb00_rtrmadp_3_china-congress.jpg" alt="video" />
                                </noscript>
                                                    </a>
                                                    <a class="modeless title" href="/%E4%B8%AD%E5%9B%BD/20171030-%E4%B8%AD%E5%85%B1%E5%8A%A0%E5%BC%BA%E5%AF%B9%E4%BC%81%E4%B8%9A%E9%A2%86%E5%AF%BC" title="&#x4E2D;&#x5171;&#x52A0;&#x5F3A;&#x5BF9;&#x4F01;&#x4E1A;&#x9886;&#x5BFC;">
                                要闻解说
                            </a>
                                                                                                    <div class="h3">
                            <a href="/%E4%B8%AD%E5%9B%BD/20171030-%E4%B8%AD%E5%85%B1%E5%8A%A0%E5%BC%BA%E5%AF%B9%E4%BC%81%E4%B8%9A%E9%A2%86%E5%AF%BC" title="&#x4E2D;&#x5171;&#x52A0;&#x5F3A;&#x5BF9;&#x4F01;&#x4E1A;&#x9886;&#x5BFC;"
                                class="modeless"                            >
                                                                    中共加强对企业领导
                                                            </a>
                        </div>
                                            </li>
                                                                                                                                                                                                                                                                                                                                                                                                                                
                    <li data-bo-type="edition" data-bo-nid="WB260208-RFI-ZH-HANS-20171029">
                        <a href="/%E4%B8%AD%E5%9B%BD/20171029-%E9%82%93%E5%B0%8F%E5%B9%B3%E6%97%B6%E4%BB%A3%E4%B8%8D%E5%AD%98%E5%9C%A8-%E6%94%B9%E9%9D%A9%E5%BC%80%E6%94%BE%E6%80%BB%E8%AE%BE%E8%AE%A1%E5%B8%88%E6%98%AF%E5%81%87%E5%86%92" title="&#x201C;&#x9093;&#x5C0F;&#x5E73;&#x65F6;&#x4EE3;&#x201D;&#x4E0D;&#x5B58;&#x5728;&#x20;&#x6539;&#x9769;&#x5F00;&#x653E;&#x201C;&#x603B;&#x8BBE;&#x8BA1;&#x5E08;&#x201D;&#x662F;&#x5047;&#x5192;"
                                                        class="media center-cropped modeless lazy-loaded"
                            data-image="http://scd.cn.rfi.fr/sites/chinese.filesrfi/dynimagecache/0/97/551/274/195/97/sites/images.rfi.fr/files/aef_image/wai_can_90qi_feng_mian__0.jpg" data-width="202" data-height="114"
                        >
                                                            <noscript>
                                    <img src="http://scd.cn.rfi.fr/sites/chinese.filesrfi/dynimagecache/0/97/551/274/195/97/sites/images.rfi.fr/files/aef_image/wai_can_90qi_feng_mian__0.jpg" alt="video" />
                                </noscript>
                                                    </a>
                                                    <a class="modeless title" href="/%E4%B8%AD%E5%9B%BD/20171029-%E9%82%93%E5%B0%8F%E5%B9%B3%E6%97%B6%E4%BB%A3%E4%B8%8D%E5%AD%98%E5%9C%A8-%E6%94%B9%E9%9D%A9%E5%BC%80%E6%94%BE%E6%80%BB%E8%AE%BE%E8%AE%A1%E5%B8%88%E6%98%AF%E5%81%87%E5%86%92" title="&#x201C;&#x9093;&#x5C0F;&#x5E73;&#x65F6;&#x4EE3;&#x201D;&#x4E0D;&#x5B58;&#x5728;&#x20;&#x6539;&#x9769;&#x5F00;&#x653E;&#x201C;&#x603B;&#x8BBE;&#x8BA1;&#x5E08;&#x201D;&#x662F;&#x5047;&#x5192;">
                                明镜书刊
                            </a>
                                                                                                    <div class="h3">
                            <a href="/%E4%B8%AD%E5%9B%BD/20171029-%E9%82%93%E5%B0%8F%E5%B9%B3%E6%97%B6%E4%BB%A3%E4%B8%8D%E5%AD%98%E5%9C%A8-%E6%94%B9%E9%9D%A9%E5%BC%80%E6%94%BE%E6%80%BB%E8%AE%BE%E8%AE%A1%E5%B8%88%E6%98%AF%E5%81%87%E5%86%92" title="&#x201C;&#x9093;&#x5C0F;&#x5E73;&#x65F6;&#x4EE3;&#x201D;&#x4E0D;&#x5B58;&#x5728;&#x20;&#x6539;&#x9769;&#x5F00;&#x653E;&#x201C;&#x603B;&#x8BBE;&#x8BA1;&#x5E08;&#x201D;&#x662F;&#x5047;&#x5192;"
                                class="modeless"                            >
                                                                    &ldquo;邓小平时代&rdquo;不存在 改革开放&ldquo;总设计师&rdquo;是假冒
                                                            </a>
                        </div>
                                            </li>
                                                                                                                                                                                                                                                                                                                                                                                                                                
                    <li data-bo-type="edition" data-bo-nid="D696E5E4-DF7F-46D7-AE0B-2C97D55E07A6">
                        <a href="/%E4%B8%AD%E5%9B%BD/20171029-%E6%98%9F%E6%9C%9F%E6%97%A5%E6%8A%A5%E5%9B%BE%E5%8D%A2%E5%85%B9%E6%9C%BA%E5%9C%BA%E4%B8%AD%E5%9B%BD%E8%82%A1%E4%B8%9C%E9%A6%96%E6%AC%A1%E8%87%AA%E7%99%BD" title="&#x300A;&#x661F;&#x671F;&#x65E5;&#x62A5;&#x300B;&#xFF1A;&#x56FE;&#x5362;&#x5179;&#x673A;&#x573A;&#x4E2D;&#x56FD;&#x80A1;&#x4E1C;&#x9996;&#x6B21;&#x81EA;&#x767D;"
                                                        class="media center-cropped modeless lazy-loaded"
                            data-image="http://scd.cn.rfi.fr/sites/chinese.filesrfi/imagecache/rfi_169_small/sites/images.rfi.fr/files/aef_image/presse-2.jpg.gif" data-width="202" data-height="114"
                        >
                                                            <noscript>
                                    <img src="http://scd.cn.rfi.fr/sites/chinese.filesrfi/imagecache/rfi_169_small/sites/images.rfi.fr/files/aef_image/presse-2.jpg.gif" alt="video" />
                                </noscript>
                                                    </a>
                                                    <a class="modeless title" href="/%E4%B8%AD%E5%9B%BD/20171029-%E6%98%9F%E6%9C%9F%E6%97%A5%E6%8A%A5%E5%9B%BE%E5%8D%A2%E5%85%B9%E6%9C%BA%E5%9C%BA%E4%B8%AD%E5%9B%BD%E8%82%A1%E4%B8%9C%E9%A6%96%E6%AC%A1%E8%87%AA%E7%99%BD" title="&#x300A;&#x661F;&#x671F;&#x65E5;&#x62A5;&#x300B;&#xFF1A;&#x56FE;&#x5362;&#x5179;&#x673A;&#x573A;&#x4E2D;&#x56FD;&#x80A1;&#x4E1C;&#x9996;&#x6B21;&#x81EA;&#x767D;">
                                法国报纸摘要
                            </a>
                                                                                                    <div class="h3">
                            <a href="/%E4%B8%AD%E5%9B%BD/20171029-%E6%98%9F%E6%9C%9F%E6%97%A5%E6%8A%A5%E5%9B%BE%E5%8D%A2%E5%85%B9%E6%9C%BA%E5%9C%BA%E4%B8%AD%E5%9B%BD%E8%82%A1%E4%B8%9C%E9%A6%96%E6%AC%A1%E8%87%AA%E7%99%BD" title="&#x300A;&#x661F;&#x671F;&#x65E5;&#x62A5;&#x300B;&#xFF1A;&#x56FE;&#x5362;&#x5179;&#x673A;&#x573A;&#x4E2D;&#x56FD;&#x80A1;&#x4E1C;&#x9996;&#x6B21;&#x81EA;&#x767D;"
                                class="modeless"                            >
                                                                    《星期日报》：图卢兹机场中国股东首次自白
                                                            </a>
                        </div>
                                            </li>
                                                                                                                                                                                                                                                                                                                                                                                                                                
                    <li data-bo-type="edition" data-bo-nid="WB260097-RFI-ZH-HANS-20171029">
                        <a href="/%E4%B8%AD%E5%9B%BD/20171029-%E8%94%A1%E8%8B%B1%E6%96%87%E5%87%BA%E8%AE%BF%E5%8D%97%E5%A4%AA%E5%B9%B3%E6%B4%8B3%E5%9B%BD-%E5%AF%B9%E7%BE%8E%E8%BF%87%E5%A2%83%E5%A4%96%E4%BA%A4%E5%86%8D%E6%88%90%E7%84%A6%E7%82%B9" title="&#x8521;&#x82F1;&#x6587;&#x51FA;&#x8BBF;&#x5357;&#x592A;&#x5E73;&#x6D0B;3&#x56FD;&#x20;&#x5BF9;&#x7F8E;&#x201C;&#x8FC7;&#x5883;&#x5916;&#x4EA4;&#x201D;&#x518D;&#x6210;&#x7126;&#x70B9;"
                                                        class="media center-cropped modeless lazy-loaded"
                            data-image="http://scd.cn.rfi.fr/sites/chinese.filesrfi/dynimagecache/0/21/500/249/195/97/sites/images.rfi.fr/files/aef_image/capture_44_1.png" data-width="202" data-height="114"
                        >
                                                            <noscript>
                                    <img src="http://scd.cn.rfi.fr/sites/chinese.filesrfi/dynimagecache/0/21/500/249/195/97/sites/images.rfi.fr/files/aef_image/capture_44_1.png" alt="video" />
                                </noscript>
                                                    </a>
                                                    <a class="modeless title" href="/%E4%B8%AD%E5%9B%BD/20171029-%E8%94%A1%E8%8B%B1%E6%96%87%E5%87%BA%E8%AE%BF%E5%8D%97%E5%A4%AA%E5%B9%B3%E6%B4%8B3%E5%9B%BD-%E5%AF%B9%E7%BE%8E%E8%BF%87%E5%A2%83%E5%A4%96%E4%BA%A4%E5%86%8D%E6%88%90%E7%84%A6%E7%82%B9" title="&#x8521;&#x82F1;&#x6587;&#x51FA;&#x8BBF;&#x5357;&#x592A;&#x5E73;&#x6D0B;3&#x56FD;&#x20;&#x5BF9;&#x7F8E;&#x201C;&#x8FC7;&#x5883;&#x5916;&#x4EA4;&#x201D;&#x518D;&#x6210;&#x7126;&#x70B9;">
                                要闻分析
                            </a>
                                                                                                    <div class="h3">
                            <a href="/%E4%B8%AD%E5%9B%BD/20171029-%E8%94%A1%E8%8B%B1%E6%96%87%E5%87%BA%E8%AE%BF%E5%8D%97%E5%A4%AA%E5%B9%B3%E6%B4%8B3%E5%9B%BD-%E5%AF%B9%E7%BE%8E%E8%BF%87%E5%A2%83%E5%A4%96%E4%BA%A4%E5%86%8D%E6%88%90%E7%84%A6%E7%82%B9" title="&#x8521;&#x82F1;&#x6587;&#x51FA;&#x8BBF;&#x5357;&#x592A;&#x5E73;&#x6D0B;3&#x56FD;&#x20;&#x5BF9;&#x7F8E;&#x201C;&#x8FC7;&#x5883;&#x5916;&#x4EA4;&#x201D;&#x518D;&#x6210;&#x7126;&#x70B9;"
                                class="modeless"                            >
                                                                    蔡英文出访南太平洋3国 对美&ldquo;过境外交&rdquo;再成焦点
                                                            </a>
                        </div>
                                            </li>
                                                                                                                                                                                                                                                                                                                                                                                                                                
                    <li data-bo-type="edition" data-bo-nid="23F7DB6C-5136-4EE7-94AF-54C3ECD12362">
                        <a href="/%E6%AC%A7%E6%B4%B2/20171027-%E5%8A%A0%E6%B3%B0%E7%BD%97%E5%B0%BC%E4%BA%9A%E6%AD%A3%E5%9C%A8%E6%AF%85%E7%84%B6%E5%86%B3%E7%84%B6%E7%9A%84%E8%B5%B0%E5%90%91%E7%8B%AC%E7%AB%8B" title="&#x52A0;&#x6CF0;&#x7F57;&#x5C3C;&#x4E9A;&#x6B63;&#x5728;&#x6BC5;&#x7136;&#x51B3;&#x7136;&#x7684;&#x8D70;&#x5411;&#x72EC;&#x7ACB;"
                                                        class="media center-cropped modeless lazy-loaded"
                            data-image="http://scd.cn.rfi.fr/sites/chinese.filesrfi/imagecache/rfi_169_small/sites/images.rfi.fr/files/aef_image/4%20la%20Une%20du%20monde.jpg" data-width="202" data-height="114"
                        >
                                                            <noscript>
                                    <img src="http://scd.cn.rfi.fr/sites/chinese.filesrfi/imagecache/rfi_169_small/sites/images.rfi.fr/files/aef_image/4%20la%20Une%20du%20monde.jpg" alt="video" />
                                </noscript>
                                                    </a>
                                                    <a class="modeless title" href="/%E6%AC%A7%E6%B4%B2/20171027-%E5%8A%A0%E6%B3%B0%E7%BD%97%E5%B0%BC%E4%BA%9A%E6%AD%A3%E5%9C%A8%E6%AF%85%E7%84%B6%E5%86%B3%E7%84%B6%E7%9A%84%E8%B5%B0%E5%90%91%E7%8B%AC%E7%AB%8B" title="&#x52A0;&#x6CF0;&#x7F57;&#x5C3C;&#x4E9A;&#x6B63;&#x5728;&#x6BC5;&#x7136;&#x51B3;&#x7136;&#x7684;&#x8D70;&#x5411;&#x72EC;&#x7ACB;">
                                法国世界报
                            </a>
                                                                                                    <div class="h3">
                            <a href="/%E6%AC%A7%E6%B4%B2/20171027-%E5%8A%A0%E6%B3%B0%E7%BD%97%E5%B0%BC%E4%BA%9A%E6%AD%A3%E5%9C%A8%E6%AF%85%E7%84%B6%E5%86%B3%E7%84%B6%E7%9A%84%E8%B5%B0%E5%90%91%E7%8B%AC%E7%AB%8B" title="&#x52A0;&#x6CF0;&#x7F57;&#x5C3C;&#x4E9A;&#x6B63;&#x5728;&#x6BC5;&#x7136;&#x51B3;&#x7136;&#x7684;&#x8D70;&#x5411;&#x72EC;&#x7ACB;"
                                class="modeless"                            >
                                                                    加泰罗尼亚正在毅然决然的走向独立
                                                            </a>
                        </div>
                                            </li>
                                                                                                                                                                                                                                                                                                                                                                                                                                
                    <li data-bo-type="edition" data-bo-nid="A8BF4A56-BF6B-4BF7-85C0-DEEDC87C2078">
                        <a href="/%E7%BE%8E%E6%B4%B2/20171027-%E7%89%B9%E6%9C%97%E6%99%AE%E7%A8%8E%E6%94%B6%E6%94%B9%E9%9D%A9%E5%BE%88%E5%8F%AF%E8%83%BD%E6%8F%90%E5%8D%87%E6%8A%95%E8%B5%84%E5%9B%9E%E6%8A%A5%E6%81%B6%E5%8C%96%E5%8A%B3%E5%8A%A8%E5%8A%9B%E5%9B%9E%E6%8A%A5" title="&#x7279;&#x6717;&#x666E;&#x7A0E;&#x6536;&#x6539;&#x9769;&#x5F88;&#x53EF;&#x80FD;&#x63D0;&#x5347;&#x6295;&#x8D44;&#x56DE;&#x62A5;&#x6076;&#x5316;&#x52B3;&#x52A8;&#x529B;&#x56DE;&#x62A5;"
                                                        class="media center-cropped modeless lazy-loaded"
                            data-image="http://scd.cn.rfi.fr/sites/chinese.filesrfi/imagecache/rfi_169_small/sites/images.rfi.fr/files/aef_image/05-economie-d-aujourd-hui.png" data-width="202" data-height="114"
                        >
                                                            <noscript>
                                    <img src="http://scd.cn.rfi.fr/sites/chinese.filesrfi/imagecache/rfi_169_small/sites/images.rfi.fr/files/aef_image/05-economie-d-aujourd-hui.png" alt="video" />
                                </noscript>
                                                    </a>
                                                    <a class="modeless title" href="/%E7%BE%8E%E6%B4%B2/20171027-%E7%89%B9%E6%9C%97%E6%99%AE%E7%A8%8E%E6%94%B6%E6%94%B9%E9%9D%A9%E5%BE%88%E5%8F%AF%E8%83%BD%E6%8F%90%E5%8D%87%E6%8A%95%E8%B5%84%E5%9B%9E%E6%8A%A5%E6%81%B6%E5%8C%96%E5%8A%B3%E5%8A%A8%E5%8A%9B%E5%9B%9E%E6%8A%A5" title="&#x7279;&#x6717;&#x666E;&#x7A0E;&#x6536;&#x6539;&#x9769;&#x5F88;&#x53EF;&#x80FD;&#x63D0;&#x5347;&#x6295;&#x8D44;&#x56DE;&#x62A5;&#x6076;&#x5316;&#x52B3;&#x52A8;&#x529B;&#x56DE;&#x62A5;">
                                今日经济
                            </a>
                                                                                                    <div class="h3">
                            <a href="/%E7%BE%8E%E6%B4%B2/20171027-%E7%89%B9%E6%9C%97%E6%99%AE%E7%A8%8E%E6%94%B6%E6%94%B9%E9%9D%A9%E5%BE%88%E5%8F%AF%E8%83%BD%E6%8F%90%E5%8D%87%E6%8A%95%E8%B5%84%E5%9B%9E%E6%8A%A5%E6%81%B6%E5%8C%96%E5%8A%B3%E5%8A%A8%E5%8A%9B%E5%9B%9E%E6%8A%A5" title="&#x7279;&#x6717;&#x666E;&#x7A0E;&#x6536;&#x6539;&#x9769;&#x5F88;&#x53EF;&#x80FD;&#x63D0;&#x5347;&#x6295;&#x8D44;&#x56DE;&#x62A5;&#x6076;&#x5316;&#x52B3;&#x52A8;&#x529B;&#x56DE;&#x62A5;"
                                class="modeless"                            >
                                                                    特朗普税收改革很可能提升投资回报恶化劳动力回报
                                                            </a>
                        </div>
                                            </li>
                                        </ul>



    </section>

<section class="slider slider-broadcast next-prev-top">
                
                
                                                    
    <div class="h2">热点新闻</div>

                                        <a href="/%E7%89%B9%E5%88%AB%E4%B8%93%E9%A2%98/" class="btn-more modeless">更多热点新闻</a>
                            <ul>
                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                        
                    <li data-bo-type="pagecompos" data-bo-nid="3C2376C7-F5EB-4AE1-AEC0-3EF59834E5D0">
                        <a href="/%E4%BA%BA%E6%9D%83/20170713-%E5%88%98%E6%99%93%E6%B3%A219551228%EF%BC%8D2017713" title="&#x5218;&#x6653;&#x6CE2;&#x4E4B;&#x6B7B;"
                                                        class="media center-cropped modeless lazy-loaded"
                            data-image="http://scd.cn.rfi.fr/sites/chinese.filesrfi/dynimagecache/0/25/432/215/195/97/sites/images.rfi.fr/files/aef_image/denrmwnw0aaplvk.jpg" data-width="202" data-height="114"
                        >
                                                            <noscript>
                                    <img src="http://scd.cn.rfi.fr/sites/chinese.filesrfi/dynimagecache/0/25/432/215/195/97/sites/images.rfi.fr/files/aef_image/denrmwnw0aaplvk.jpg" alt="video" />
                                </noscript>
                                                    </a>
                                                                        <div class="h3">
                            <a href="/%E4%BA%BA%E6%9D%83/20170713-%E5%88%98%E6%99%93%E6%B3%A219551228%EF%BC%8D2017713" title="&#x5218;&#x6653;&#x6CE2;&#x4E4B;&#x6B7B;"
                                class="modeless"                            >
                                                                    刘晓波之死
                                                            </a>
                        </div>
                                            </li>
                                                                                                                                                                                                                                                                                                                                                                                                                                
                    <li data-bo-type="pagecompos" data-bo-nid="E4897E27-628D-4529-BAFF-43EC0052F975">
                        <a href="/%E6%B3%95%E5%9B%BD/20170607-2017%E6%B3%95%E5%9B%BD%E7%AB%8B%E6%B3%95%E9%80%89%E4%B8%BE" title="2017&#x6CD5;&#x56FD;&#x7ACB;&#x6CD5;&#x9009;&#x4E3E;"
                                                        class="media center-cropped modeless lazy-loaded"
                            data-image="http://scd.cn.rfi.fr/sites/chinese.filesrfi/imagecache/rfi_169_small/sites/images.rfi.fr/files/aef_image/162.jpg" data-width="202" data-height="114"
                        >
                                                            <noscript>
                                    <img src="http://scd.cn.rfi.fr/sites/chinese.filesrfi/imagecache/rfi_169_small/sites/images.rfi.fr/files/aef_image/162.jpg" alt="video" />
                                </noscript>
                                                    </a>
                                                                        <div class="h3">
                            <a href="/%E6%B3%95%E5%9B%BD/20170607-2017%E6%B3%95%E5%9B%BD%E7%AB%8B%E6%B3%95%E9%80%89%E4%B8%BE" title="2017&#x6CD5;&#x56FD;&#x7ACB;&#x6CD5;&#x9009;&#x4E3E;"
                                class="modeless"                            >
                                                                    2017法国立法选举
                                                            </a>
                        </div>
                                            </li>
                                                                                                                                                                                                                                                                                                                                                                                                                                
                    <li data-bo-type="pagecompos" data-bo-nid="F22995E4-BDE4-4AD6-9B18-04BDCE7A1E5C">
                        <a href="/%E6%B3%95%E5%9B%BD/20170511-%E6%88%9B%E7%BA%B3%E5%9B%BD%E9%99%85%E7%94%B5%E5%BD%B1%E8%8A%822017%E7%89%B9%E5%88%AB%E8%8A%82%E7%9B%AE" title="2017&#x621B;&#x7EB3;&#x56FD;&#x9645;&#x7535;&#x5F71;&#x8282;"
                                                        class="media center-cropped modeless lazy-loaded"
                            data-image="http://scd.cn.rfi.fr/sites/chinese.filesrfi/imagecache/rfi_169_small/sites/images.rfi.fr/files/aef_image/main-image-cannes-1024.png" data-width="202" data-height="114"
                        >
                                                            <noscript>
                                    <img src="http://scd.cn.rfi.fr/sites/chinese.filesrfi/imagecache/rfi_169_small/sites/images.rfi.fr/files/aef_image/main-image-cannes-1024.png" alt="video" />
                                </noscript>
                                                    </a>
                                                                        <div class="h3">
                            <a href="/%E6%B3%95%E5%9B%BD/20170511-%E6%88%9B%E7%BA%B3%E5%9B%BD%E9%99%85%E7%94%B5%E5%BD%B1%E8%8A%822017%E7%89%B9%E5%88%AB%E8%8A%82%E7%9B%AE" title="2017&#x621B;&#x7EB3;&#x56FD;&#x9645;&#x7535;&#x5F71;&#x8282;"
                                class="modeless"                            >
                                                                    2017戛纳国际电影节
                                                            </a>
                        </div>
                                            </li>
                                                                                                                                                                                                                                                                                                                                                                                                                                
                    <li data-bo-type="pagecompos" data-bo-nid="D66120F8-EBE8-4124-A100-515ADA94A41C">
                        <a href="/%E6%94%BF%E6%B2%BB/20170307-2017%E6%B3%95%E5%9B%BD%E6%80%BB%E7%BB%9F%E5%A4%A7%E9%80%89" title="&#x6CD5;&#x56FD;2017&#x603B;&#x7EDF;&#x5927;&#x9009;"
                                                        class="media center-cropped modeless lazy-loaded"
                            data-image="http://scd.cn.rfi.fr/sites/chinese.filesrfi/imagecache/rfi_169_small/sites/images.rfi.fr/files/aef_image/2017-03-18t105333z_1912742804_rc1acb0a48b0_rtrmadp_3_france-election-candidates_0_0.jpg" data-width="202" data-height="114"
                        >
                                                            <noscript>
                                    <img src="http://scd.cn.rfi.fr/sites/chinese.filesrfi/imagecache/rfi_169_small/sites/images.rfi.fr/files/aef_image/2017-03-18t105333z_1912742804_rc1acb0a48b0_rtrmadp_3_france-election-candidates_0_0.jpg" alt="video" />
                                </noscript>
                                                    </a>
                                                                        <div class="h3">
                            <a href="/%E6%94%BF%E6%B2%BB/20170307-2017%E6%B3%95%E5%9B%BD%E6%80%BB%E7%BB%9F%E5%A4%A7%E9%80%89" title="&#x6CD5;&#x56FD;2017&#x603B;&#x7EDF;&#x5927;&#x9009;"
                                class="modeless"                            >
                                                                    法国2017总统大选
                                                            </a>
                        </div>
                                            </li>
                                                                                                                                                                                                                                                                                                                                                                                                                                
                    <li data-bo-type="pagecompos" data-bo-nid="508D9ACB-EF9A-4B9E-A421-825901EB599D">
                        <a href="/%E6%94%BF%E6%B2%BB/20170216-%E6%B3%95%E5%B9%BF%E5%8D%8E%E8%AF%AD%E8%A7%86%E9%A2%91" title="&#x6CD5;&#x5E7F;&#x534E;&#x8BED;&#x89C6;&#x9891;"
                                                        class="media center-cropped modeless lazy-loaded"
                            data-image="http://scd.cn.rfi.fr/sites/chinese.filesrfi/imagecache/rfi_169_small/sites/images.rfi.fr/files/aef_image/video-marketing.png" data-width="202" data-height="114"
                        >
                                                            <noscript>
                                    <img src="http://scd.cn.rfi.fr/sites/chinese.filesrfi/imagecache/rfi_169_small/sites/images.rfi.fr/files/aef_image/video-marketing.png" alt="video" />
                                </noscript>
                                                    </a>
                                                                        <div class="h3">
                            <a href="/%E6%94%BF%E6%B2%BB/20170216-%E6%B3%95%E5%B9%BF%E5%8D%8E%E8%AF%AD%E8%A7%86%E9%A2%91" title="&#x6CD5;&#x5E7F;&#x534E;&#x8BED;&#x89C6;&#x9891;"
                                class="modeless"                            >
                                                                    法广华语视频
                                                            </a>
                        </div>
                                            </li>
                                                                                                                                                                                                                                                                                                                                                                                                                                
                    <li data-bo-type="pagecompos" data-bo-nid="90829F49-7FF4-464D-8F89-9A2D2271AE51">
                        <a href="/%E7%A7%91%E6%8A%80%E4%B8%8E%E6%96%87%E5%8C%96/20170112-%E6%B3%95%E5%9B%BD%E6%80%9D%E6%83%B3%E9%95%BF%E5%BB%8A" title="&#x6CD5;&#x56FD;&#x601D;&#x60F3;&#x957F;&#x5ECA;&#x20;"
                                                        class="media center-cropped modeless lazy-loaded"
                            data-image="http://scd.cn.rfi.fr/sites/chinese.filesrfi/imagecache/rfi_169_small/sites/images.rfi.fr/files/aef_image/luodansixiangzhediaosuyishu_6702595.jpg" data-width="202" data-height="114"
                        >
                                                            <noscript>
                                    <img src="http://scd.cn.rfi.fr/sites/chinese.filesrfi/imagecache/rfi_169_small/sites/images.rfi.fr/files/aef_image/luodansixiangzhediaosuyishu_6702595.jpg" alt="video" />
                                </noscript>
                                                    </a>
                                                                        <div class="h3">
                            <a href="/%E7%A7%91%E6%8A%80%E4%B8%8E%E6%96%87%E5%8C%96/20170112-%E6%B3%95%E5%9B%BD%E6%80%9D%E6%83%B3%E9%95%BF%E5%BB%8A" title="&#x6CD5;&#x56FD;&#x601D;&#x60F3;&#x957F;&#x5ECA;&#x20;"
                                class="modeless"                            >
                                                                    法国思想长廊 
                                                            </a>
                        </div>
                                            </li>
                                                                                                                                                                                                                                                                                                                                                                                                                                
                    <li data-bo-type="pagecompos" data-bo-nid="678C7716-CBEF-41BC-8CB5-5EB8552F951A">
                        <a href="/%E4%B8%AD%E5%9B%BD/20161109-%E7%89%B9%E6%9C%97%E6%99%AE%E6%84%8F%E5%A4%96%E5%BD%93%E9%80%89%E7%BE%8E%E5%9B%BD%E6%80%BB%E7%BB%9F" title="&#x7279;&#x6717;&#x666E;&#x610F;&#x5916;&#x5F53;&#x9009;&#x7F8E;&#x56FD;&#x603B;&#x7EDF;"
                                                        class="media center-cropped modeless lazy-loaded"
                            data-image="http://scd.cn.rfi.fr/sites/chinese.filesrfi/dynimagecache/0/274/3500/1738/195/97/sites/images.rfi.fr/files/aef_image/donald_trump_elu_45e_president_des_etats-unis_0.jpg" data-width="202" data-height="114"
                        >
                                                            <noscript>
                                    <img src="http://scd.cn.rfi.fr/sites/chinese.filesrfi/dynimagecache/0/274/3500/1738/195/97/sites/images.rfi.fr/files/aef_image/donald_trump_elu_45e_president_des_etats-unis_0.jpg" alt="video" />
                                </noscript>
                                                    </a>
                                                                        <div class="h3">
                            <a href="/%E4%B8%AD%E5%9B%BD/20161109-%E7%89%B9%E6%9C%97%E6%99%AE%E6%84%8F%E5%A4%96%E5%BD%93%E9%80%89%E7%BE%8E%E5%9B%BD%E6%80%BB%E7%BB%9F" title="&#x7279;&#x6717;&#x666E;&#x610F;&#x5916;&#x5F53;&#x9009;&#x7F8E;&#x56FD;&#x603B;&#x7EDF;"
                                class="modeless"                            >
                                                                    特朗普意外当选美国总统
                                                            </a>
                        </div>
                                            </li>
                                                                                                                                                                                                                                                                                                                                                                                                                                
                    <li data-bo-type="pagecompos" data-bo-nid="C63D94C3-2E15-494E-BCAA-1B555F731E9A">
                        <a href="/%E5%9B%BD%E9%99%85/20161013-2016%E5%B9%B4%E8%AF%BA%E8%B4%9D%E5%B0%94%E5%A5%96" title="2016&#x5E74;&#x8BFA;&#x8D1D;&#x5C14;&#x5956;"
                                                        class="media center-cropped modeless lazy-loaded"
                            data-image="http://scd.cn.rfi.fr/sites/chinese.filesrfi/imagecache/rfi_169_small/sites/images.rfi.fr/files/aef_image/NOBEL.gif" data-width="202" data-height="114"
                        >
                                                            <noscript>
                                    <img src="http://scd.cn.rfi.fr/sites/chinese.filesrfi/imagecache/rfi_169_small/sites/images.rfi.fr/files/aef_image/NOBEL.gif" alt="video" />
                                </noscript>
                                                    </a>
                                                                        <div class="h3">
                            <a href="/%E5%9B%BD%E9%99%85/20161013-2016%E5%B9%B4%E8%AF%BA%E8%B4%9D%E5%B0%94%E5%A5%96" title="2016&#x5E74;&#x8BFA;&#x8D1D;&#x5C14;&#x5956;"
                                class="modeless"                            >
                                                                    2016年诺贝尔奖
                                                            </a>
                        </div>
                                            </li>
                                                                                                                                                                                                                                                                                                                                                                                                                                
                    <li data-bo-type="pagecompos" data-bo-nid="B7F40807-C453-4F3B-97EF-2088DC917E22">
                        <a href="/%E5%9B%BD%E9%99%85/20160813-%E9%87%8C%E7%BA%A62016%E5%A5%A5%E8%BF%90" title="&#x91CC;&#x7EA6;2016&#x5965;&#x8FD0;"
                                                        class="media center-cropped modeless lazy-loaded"
                            data-image="http://scd.cn.rfi.fr/sites/chinese.filesrfi/imagecache/rfi_169_small/sites/images.rfi.fr/files/aef_image/2016-08-12t205332z_1421340728_rioec8c1m0tgb_rtrmadp_3_olympics-rio-judo-m-heavy.jpg" data-width="202" data-height="114"
                        >
                                                            <noscript>
                                    <img src="http://scd.cn.rfi.fr/sites/chinese.filesrfi/imagecache/rfi_169_small/sites/images.rfi.fr/files/aef_image/2016-08-12t205332z_1421340728_rioec8c1m0tgb_rtrmadp_3_olympics-rio-judo-m-heavy.jpg" alt="video" />
                                </noscript>
                                                    </a>
                                                                        <div class="h3">
                            <a href="/%E5%9B%BD%E9%99%85/20160813-%E9%87%8C%E7%BA%A62016%E5%A5%A5%E8%BF%90" title="&#x91CC;&#x7EA6;2016&#x5965;&#x8FD0;"
                                class="modeless"                            >
                                                                    里约2016奥运
                                                            </a>
                        </div>
                                            </li>
                                                                                                                                                                                                                                                                                                                                                                                                                                
                    <li data-bo-type="pagecompos" data-bo-nid="C0065945-B966-4651-8A49-A67E48715AF8">
                        <a href="/%E4%B8%AD%E5%9B%BD/20160714-%E5%8D%97%E6%B5%B7%E4%BB%B2%E8%A3%81%E6%A1%88" title="&#x5357;&#x6D77;&#x4EF2;&#x88C1;&#x6848;"
                                                        class="media center-cropped modeless lazy-loaded"
                            data-image="http://scd.cn.rfi.fr/sites/chinese.filesrfi/imagecache/rfi_169_small/sites/images.rfi.fr/files/aef_image/zbj.jpg" data-width="202" data-height="114"
                        >
                                                            <noscript>
                                    <img src="http://scd.cn.rfi.fr/sites/chinese.filesrfi/imagecache/rfi_169_small/sites/images.rfi.fr/files/aef_image/zbj.jpg" alt="video" />
                                </noscript>
                                                    </a>
                                                                        <div class="h3">
                            <a href="/%E4%B8%AD%E5%9B%BD/20160714-%E5%8D%97%E6%B5%B7%E4%BB%B2%E8%A3%81%E6%A1%88" title="&#x5357;&#x6D77;&#x4EF2;&#x88C1;&#x6848;"
                                class="modeless"                            >
                                                                    南海仲裁案
                                                            </a>
                        </div>
                                            </li>
                                        </ul>



</section>

    <section class="slider slider-broadcast next-prev-top">
                    
                
                                                    
    <div class="h2">专栏检索</div>

                    <ul>
                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                        
                    <li data-bo-type="edition" data-bo-nid="WB260215-RFI-ZH-HANS-20171030">
                        <a href="/%E6%94%BF%E6%B2%BB/20171030-%E6%8B%89%E6%96%AF%E7%BB%B4%E5%8A%A0%E6%96%AF%E6%9E%AA%E5%87%BB%E6%A1%88%E4%B8%80%E4%B8%AA%E6%9C%88%EF%BC%8C%E5%B7%B2%E5%90%AC%E4%B8%8D%E5%88%B0%E6%8E%A7%E6%9E%AA%E5%A3%B0%E9%9F%B3%EF%BC%8C59%E5%90%8D%E9%81%87%E9%9A%BE%E8%80%85%E5%8F%88%E7%99%BD%E6%AD%BB%E4%BA%86" title="&#x62C9;&#x65AF;&#x7EF4;&#x52A0;&#x65AF;&#x67AA;&#x51FB;&#x6848;&#x4E00;&#x4E2A;&#x6708;&#xFF0C;&#x5DF2;&#x542C;&#x4E0D;&#x5230;&#x63A7;&#x67AA;&#x58F0;&#x97F3;&#xFF0C;59&#x540D;&#x9047;&#x96BE;&#x8005;&#x53C8;&#x767D;&#x6B7B;&#x4E86;"
                                                        class="media center-cropped modeless lazy-loaded"
                            data-image="http://scd.cn.rfi.fr/sites/chinese.filesrfi/dynimagecache/0/130/766/382/195/97/sites/images.rfi.fr/files/aef_image/063_8565204461_0.jpg" data-width="202" data-height="114"
                        >
                                                            <noscript>
                                    <img src="http://scd.cn.rfi.fr/sites/chinese.filesrfi/dynimagecache/0/130/766/382/195/97/sites/images.rfi.fr/files/aef_image/063_8565204461_0.jpg" alt="video" />
                                </noscript>
                                                    </a>
                                                    <a class="modeless title" href="/%E6%94%BF%E6%B2%BB/20171030-%E6%8B%89%E6%96%AF%E7%BB%B4%E5%8A%A0%E6%96%AF%E6%9E%AA%E5%87%BB%E6%A1%88%E4%B8%80%E4%B8%AA%E6%9C%88%EF%BC%8C%E5%B7%B2%E5%90%AC%E4%B8%8D%E5%88%B0%E6%8E%A7%E6%9E%AA%E5%A3%B0%E9%9F%B3%EF%BC%8C59%E5%90%8D%E9%81%87%E9%9A%BE%E8%80%85%E5%8F%88%E7%99%BD%E6%AD%BB%E4%BA%86" title="&#x62C9;&#x65AF;&#x7EF4;&#x52A0;&#x65AF;&#x67AA;&#x51FB;&#x6848;&#x4E00;&#x4E2A;&#x6708;&#xFF0C;&#x5DF2;&#x542C;&#x4E0D;&#x5230;&#x63A7;&#x67AA;&#x58F0;&#x97F3;&#xFF0C;59&#x540D;&#x9047;&#x96BE;&#x8005;&#x53C8;&#x767D;&#x6B7B;&#x4E86;">
                                美国专栏
                            </a>
                                                                                                    <div class="h3">
                            <a href="/%E6%94%BF%E6%B2%BB/20171030-%E6%8B%89%E6%96%AF%E7%BB%B4%E5%8A%A0%E6%96%AF%E6%9E%AA%E5%87%BB%E6%A1%88%E4%B8%80%E4%B8%AA%E6%9C%88%EF%BC%8C%E5%B7%B2%E5%90%AC%E4%B8%8D%E5%88%B0%E6%8E%A7%E6%9E%AA%E5%A3%B0%E9%9F%B3%EF%BC%8C59%E5%90%8D%E9%81%87%E9%9A%BE%E8%80%85%E5%8F%88%E7%99%BD%E6%AD%BB%E4%BA%86" title="&#x62C9;&#x65AF;&#x7EF4;&#x52A0;&#x65AF;&#x67AA;&#x51FB;&#x6848;&#x4E00;&#x4E2A;&#x6708;&#xFF0C;&#x5DF2;&#x542C;&#x4E0D;&#x5230;&#x63A7;&#x67AA;&#x58F0;&#x97F3;&#xFF0C;59&#x540D;&#x9047;&#x96BE;&#x8005;&#x53C8;&#x767D;&#x6B7B;&#x4E86;"
                                class="modeless"                            >
                                                                    拉斯维加斯枪击案一个月，已听不到控枪声音，59名遇难者又白死了
                                                            </a>
                        </div>
                                            </li>
                                                                                                                                                                                                                                                                                                                                                                                                                                
                    <li data-bo-type="edition" data-bo-nid="A16F8CD1-07EE-4527-A242-A62E98109367">
                        <a href="/%E4%BA%9A%E6%B4%B2/20171029-%E6%9D%8E%E6%98%BE%E9%BE%99%E8%AE%BF%E7%BE%8E-%E7%BE%8E%E5%9B%BD%E4%BA%9A%E6%B4%B2%E6%94%BF%E7%AD%96%E8%B6%8B%E6%98%8E%E6%9C%97" title="&#x674E;&#x663E;&#x9F99;&#x8BBF;&#x7F8E;&#x20;&#x7F8E;&#x56FD;&#x4E9A;&#x6D32;&#x653F;&#x7B56;&#x8D8B;&#x660E;&#x6717;"
                                                        class="media center-cropped modeless lazy-loaded"
                            data-image="http://scd.cn.rfi.fr/sites/chinese.filesrfi/dynimagecache/0/151/3500/1739/195/97/sites/images.rfi.fr/files/aef_image/2017-10-23t184449z_2076997793_rc1f6d8fc280_rtrmadp_3_usa-singapore.jpg" data-width="202" data-height="114"
                        >
                                                            <noscript>
                                    <img src="http://scd.cn.rfi.fr/sites/chinese.filesrfi/dynimagecache/0/151/3500/1739/195/97/sites/images.rfi.fr/files/aef_image/2017-10-23t184449z_2076997793_rc1f6d8fc280_rtrmadp_3_usa-singapore.jpg" alt="video" />
                                </noscript>
                                                    </a>
                                                    <a class="modeless title" href="/%E4%BA%9A%E6%B4%B2/20171029-%E6%9D%8E%E6%98%BE%E9%BE%99%E8%AE%BF%E7%BE%8E-%E7%BE%8E%E5%9B%BD%E4%BA%9A%E6%B4%B2%E6%94%BF%E7%AD%96%E8%B6%8B%E6%98%8E%E6%9C%97" title="&#x674E;&#x663E;&#x9F99;&#x8BBF;&#x7F8E;&#x20;&#x7F8E;&#x56FD;&#x4E9A;&#x6D32;&#x653F;&#x7B56;&#x8D8B;&#x660E;&#x6717;">
                                曼谷专栏
                            </a>
                                                                                                    <div class="h3">
                            <a href="/%E4%BA%9A%E6%B4%B2/20171029-%E6%9D%8E%E6%98%BE%E9%BE%99%E8%AE%BF%E7%BE%8E-%E7%BE%8E%E5%9B%BD%E4%BA%9A%E6%B4%B2%E6%94%BF%E7%AD%96%E8%B6%8B%E6%98%8E%E6%9C%97" title="&#x674E;&#x663E;&#x9F99;&#x8BBF;&#x7F8E;&#x20;&#x7F8E;&#x56FD;&#x4E9A;&#x6D32;&#x653F;&#x7B56;&#x8D8B;&#x660E;&#x6717;"
                                class="modeless"                            >
                                                                    李显龙访美 美国亚洲政策趋明朗
                                                            </a>
                        </div>
                                            </li>
                                                                                                                                                                                                                                                                                                                                                                                                                                
                    <li data-bo-type="edition" data-bo-nid="WB260052-RFI-ZH-HANS-20171028">
                        <a href="/%E4%B8%AD%E5%9B%BD/20171028-%E4%B9%A0%E8%BF%91%E5%B9%B3%E5%90%AF%E5%8A%A8%E6%96%B0%E6%97%B6%E4%BB%A3-%E5%BC%BA%E5%8A%BF%E9%A2%86%E5%AF%BC%E5%8D%81%E4%B9%9D%E5%A4%A7%E6%9D%83%E5%8A%9B%E6%B4%97%E7%89%8C" title="&#x4E60;&#x8FD1;&#x5E73;&#x542F;&#x52A8;&#x65B0;&#x65F6;&#x4EE3;&#x20;&#x5F3A;&#x52BF;&#x9886;&#x5BFC;&#x5341;&#x4E5D;&#x5927;&#x6743;&#x529B;&#x6D17;&#x724C;"
                                                        class="media center-cropped modeless lazy-loaded"
                            data-image="http://scd.cn.rfi.fr/sites/chinese.filesrfi/imagecache/rfi_169_small/sites/images.rfi.fr/files/aef_image/2017-10-25t052140z_1135549227_rc1d42457010_rtrmadp_3_china-congress.jpg" data-width="202" data-height="114"
                        >
                                                            <noscript>
                                    <img src="http://scd.cn.rfi.fr/sites/chinese.filesrfi/imagecache/rfi_169_small/sites/images.rfi.fr/files/aef_image/2017-10-25t052140z_1135549227_rc1d42457010_rtrmadp_3_china-congress.jpg" alt="video" />
                                </noscript>
                                                    </a>
                                                    <a class="modeless title" href="/%E4%B8%AD%E5%9B%BD/20171028-%E4%B9%A0%E8%BF%91%E5%B9%B3%E5%90%AF%E5%8A%A8%E6%96%B0%E6%97%B6%E4%BB%A3-%E5%BC%BA%E5%8A%BF%E9%A2%86%E5%AF%BC%E5%8D%81%E4%B9%9D%E5%A4%A7%E6%9D%83%E5%8A%9B%E6%B4%97%E7%89%8C" title="&#x4E60;&#x8FD1;&#x5E73;&#x542F;&#x52A8;&#x65B0;&#x65F6;&#x4EE3;&#x20;&#x5F3A;&#x52BF;&#x9886;&#x5BFC;&#x5341;&#x4E5D;&#x5927;&#x6743;&#x529B;&#x6D17;&#x724C;">
                                亚洲周刊
                            </a>
                                                                                                    <div class="h3">
                            <a href="/%E4%B8%AD%E5%9B%BD/20171028-%E4%B9%A0%E8%BF%91%E5%B9%B3%E5%90%AF%E5%8A%A8%E6%96%B0%E6%97%B6%E4%BB%A3-%E5%BC%BA%E5%8A%BF%E9%A2%86%E5%AF%BC%E5%8D%81%E4%B9%9D%E5%A4%A7%E6%9D%83%E5%8A%9B%E6%B4%97%E7%89%8C" title="&#x4E60;&#x8FD1;&#x5E73;&#x542F;&#x52A8;&#x65B0;&#x65F6;&#x4EE3;&#x20;&#x5F3A;&#x52BF;&#x9886;&#x5BFC;&#x5341;&#x4E5D;&#x5927;&#x6743;&#x529B;&#x6D17;&#x724C;"
                                class="modeless"                            >
                                                                    习近平启动新时代 强势领导十九大权力洗牌
                                                            </a>
                        </div>
                                            </li>
                                                                                                                                                                                                                                                                                                                                                                                                                                
                    <li data-bo-type="edition" data-bo-nid="WB260051-RFI-ZH-HANS-20171028">
                        <a href="/%E6%B8%AF%E6%BE%B3%E5%8F%B0/20171028-%E5%9B%BD%E9%99%85%E6%82%B2%E8%A7%82%E7%9C%8B%E5%BE%85%E4%B8%A4%E5%B2%B8%E5%AF%B9%E4%B9%9D%E4%BA%8C%E5%85%B1%E8%AF%86%E7%9A%84%E8%AE%A4%E5%90%8C%E8%90%BD%E5%B7%AE" title="&#x56FD;&#x9645;&#x60B2;&#x89C2;&#x770B;&#x5F85;&#x4E24;&#x5CB8;&#x5BF9;&#x4E5D;&#x4E8C;&#x5171;&#x8BC6;&#x7684;&#x8BA4;&#x540C;&#x843D;&#x5DEE;"
                                                        class="media center-cropped modeless lazy-loaded"
                            data-image="http://scd.cn.rfi.fr/sites/chinese.filesrfi/imagecache/rfi_169_small/sites/images.rfi.fr/files/aef_image/101_0_0.jpg" data-width="202" data-height="114"
                        >
                                                            <noscript>
                                    <img src="http://scd.cn.rfi.fr/sites/chinese.filesrfi/imagecache/rfi_169_small/sites/images.rfi.fr/files/aef_image/101_0_0.jpg" alt="video" />
                                </noscript>
                                                    </a>
                                                    <a class="modeless title" href="/%E6%B8%AF%E6%BE%B3%E5%8F%B0/20171028-%E5%9B%BD%E9%99%85%E6%82%B2%E8%A7%82%E7%9C%8B%E5%BE%85%E4%B8%A4%E5%B2%B8%E5%AF%B9%E4%B9%9D%E4%BA%8C%E5%85%B1%E8%AF%86%E7%9A%84%E8%AE%A4%E5%90%8C%E8%90%BD%E5%B7%AE" title="&#x56FD;&#x9645;&#x60B2;&#x89C2;&#x770B;&#x5F85;&#x4E24;&#x5CB8;&#x5BF9;&#x4E5D;&#x4E8C;&#x5171;&#x8BC6;&#x7684;&#x8BA4;&#x540C;&#x843D;&#x5DEE;">
                                台北一周
                            </a>
                                                                                                    <div class="h3">
                            <a href="/%E6%B8%AF%E6%BE%B3%E5%8F%B0/20171028-%E5%9B%BD%E9%99%85%E6%82%B2%E8%A7%82%E7%9C%8B%E5%BE%85%E4%B8%A4%E5%B2%B8%E5%AF%B9%E4%B9%9D%E4%BA%8C%E5%85%B1%E8%AF%86%E7%9A%84%E8%AE%A4%E5%90%8C%E8%90%BD%E5%B7%AE" title="&#x56FD;&#x9645;&#x60B2;&#x89C2;&#x770B;&#x5F85;&#x4E24;&#x5CB8;&#x5BF9;&#x4E5D;&#x4E8C;&#x5171;&#x8BC6;&#x7684;&#x8BA4;&#x540C;&#x843D;&#x5DEE;"
                                class="modeless"                            >
                                                                    国际悲观看待两岸对九二共识的认同落差
                                                            </a>
                        </div>
                                            </li>
                                                                                                                                                                                                                                                                                                                                                                                                                                
                    <li data-bo-type="edition" data-bo-nid="WB260053-RFI-ZH-HANS-20171027">
                        <a href="/%E6%B3%95%E5%9B%BD/20171027-%E7%A9%BA%E6%B0%94%E6%B1%A1%E6%9F%93%E5%AF%BC%E8%87%B4%E6%AC%A7%E6%B4%B2%E4%BA%BA%E6%97%A9%E9%80%9D-%E5%B7%B4%E9%BB%8E%E5%8A%A0%E5%A4%A7%E6%8E%A7%E5%88%B6%E6%B1%BD%E8%BD%A6%E5%8A%9B%E5%BA%A6" title="&#x7A7A;&#x6C14;&#x6C61;&#x67D3;&#x5BFC;&#x81F4;&#x6B27;&#x6D32;&#x4EBA;&#x65E9;&#x901D;&#x20;&#x5DF4;&#x9ECE;&#x52A0;&#x5927;&#x63A7;&#x5236;&#x6C7D;&#x8F66;&#x529B;&#x5EA6;"
                                                        class="media center-cropped modeless lazy-loaded"
                            data-image="http://scd.cn.rfi.fr/sites/chinese.filesrfi/imagecache/rfi_169_small/sites/images.rfi.fr/files/aef_image/000_ir6co_0.jpg" data-width="202" data-height="114"
                        >
                                                            <noscript>
                                    <img src="http://scd.cn.rfi.fr/sites/chinese.filesrfi/imagecache/rfi_169_small/sites/images.rfi.fr/files/aef_image/000_ir6co_0.jpg" alt="video" />
                                </noscript>
                                                    </a>
                                                    <a class="modeless title" href="/%E6%B3%95%E5%9B%BD/20171027-%E7%A9%BA%E6%B0%94%E6%B1%A1%E6%9F%93%E5%AF%BC%E8%87%B4%E6%AC%A7%E6%B4%B2%E4%BA%BA%E6%97%A9%E9%80%9D-%E5%B7%B4%E9%BB%8E%E5%8A%A0%E5%A4%A7%E6%8E%A7%E5%88%B6%E6%B1%BD%E8%BD%A6%E5%8A%9B%E5%BA%A6" title="&#x7A7A;&#x6C14;&#x6C61;&#x67D3;&#x5BFC;&#x81F4;&#x6B27;&#x6D32;&#x4EBA;&#x65E9;&#x901D;&#x20;&#x5DF4;&#x9ECE;&#x52A0;&#x5927;&#x63A7;&#x5236;&#x6C7D;&#x8F66;&#x529B;&#x5EA6;">
                                环境与发展
                            </a>
                                                                                                    <div class="h3">
                            <a href="/%E6%B3%95%E5%9B%BD/20171027-%E7%A9%BA%E6%B0%94%E6%B1%A1%E6%9F%93%E5%AF%BC%E8%87%B4%E6%AC%A7%E6%B4%B2%E4%BA%BA%E6%97%A9%E9%80%9D-%E5%B7%B4%E9%BB%8E%E5%8A%A0%E5%A4%A7%E6%8E%A7%E5%88%B6%E6%B1%BD%E8%BD%A6%E5%8A%9B%E5%BA%A6" title="&#x7A7A;&#x6C14;&#x6C61;&#x67D3;&#x5BFC;&#x81F4;&#x6B27;&#x6D32;&#x4EBA;&#x65E9;&#x901D;&#x20;&#x5DF4;&#x9ECE;&#x52A0;&#x5927;&#x63A7;&#x5236;&#x6C7D;&#x8F66;&#x529B;&#x5EA6;"
                                class="modeless"                            >
                                                                    空气污染导致欧洲人早逝 巴黎加大控制汽车力度
                                                            </a>
                        </div>
                                            </li>
                                                                                                                                                                                                                                                                                                                                                                                                                                
                    <li data-bo-type="edition" data-bo-nid="WB259981-RFI-ZH-HANS-20171027">
                        <a href="/%E4%B8%AD%E5%9B%BD/20171027-%E4%BB%8E%E5%85%9A%E6%8A%A5%E7%89%88%E9%9D%A2%E7%9C%8B%E4%B9%A0%E8%BF%91%E5%B9%B3%E7%9A%84%E5%8E%8B%E5%80%92%E6%80%A7%E5%9C%B0%E4%BD%8D" title="&#x4ECE;&#x515A;&#x62A5;&#x7248;&#x9762;&#x770B;&#x4E60;&#x8FD1;&#x5E73;&#x7684;&#x538B;&#x5012;&#x6027;&#x5730;&#x4F4D;"
                                                        class="media center-cropped modeless lazy-loaded"
                            data-image="http://scd.cn.rfi.fr/sites/chinese.filesrfi/imagecache/rfi_169_small/sites/images.rfi.fr/files/aef_image/2017-10-26t105114z_664418173_rc1e276722a0_rtrmadp_3_china-congress-media.jpg" data-width="202" data-height="114"
                        >
                                                            <noscript>
                                    <img src="http://scd.cn.rfi.fr/sites/chinese.filesrfi/imagecache/rfi_169_small/sites/images.rfi.fr/files/aef_image/2017-10-26t105114z_664418173_rc1e276722a0_rtrmadp_3_china-congress-media.jpg" alt="video" />
                                </noscript>
                                                    </a>
                                                    <a class="modeless title" href="/%E4%B8%AD%E5%9B%BD/20171027-%E4%BB%8E%E5%85%9A%E6%8A%A5%E7%89%88%E9%9D%A2%E7%9C%8B%E4%B9%A0%E8%BF%91%E5%B9%B3%E7%9A%84%E5%8E%8B%E5%80%92%E6%80%A7%E5%9C%B0%E4%BD%8D" title="&#x4ECE;&#x515A;&#x62A5;&#x7248;&#x9762;&#x770B;&#x4E60;&#x8FD1;&#x5E73;&#x7684;&#x538B;&#x5012;&#x6027;&#x5730;&#x4F4D;">
                                上海视窗
                            </a>
                                                                                                    <div class="h3">
                            <a href="/%E4%B8%AD%E5%9B%BD/20171027-%E4%BB%8E%E5%85%9A%E6%8A%A5%E7%89%88%E9%9D%A2%E7%9C%8B%E4%B9%A0%E8%BF%91%E5%B9%B3%E7%9A%84%E5%8E%8B%E5%80%92%E6%80%A7%E5%9C%B0%E4%BD%8D" title="&#x4ECE;&#x515A;&#x62A5;&#x7248;&#x9762;&#x770B;&#x4E60;&#x8FD1;&#x5E73;&#x7684;&#x538B;&#x5012;&#x6027;&#x5730;&#x4F4D;"
                                class="modeless"                            >
                                                                    从党报版面看习近平的压倒性地位
                                                            </a>
                        </div>
                                            </li>
                                                                                                                                                                                                                                                                                                                                                                                                                                
                    <li data-bo-type="edition" data-bo-nid="WB259957-RFI-ZH-HANS-20171027">
                        <a href="/%E6%B3%95%E5%9B%BD/20171027-%E6%B3%95%E5%9B%BD%E9%BB%84%E6%B2%B9%E5%8D%B1%E6%9C%BA%E8%BF%98%E4%BC%9A%E6%8C%81%E7%BB%AD%E5%A4%9A%E4%B9%85" title="&#x6CD5;&#x56FD;&#x9EC4;&#x6CB9;&#x5371;&#x673A;&#x8FD8;&#x4F1A;&#x6301;&#x7EED;&#x591A;&#x4E45;&#xFF1F;"
                                                        class="media center-cropped modeless lazy-loaded"
                            data-image="http://scd.cn.rfi.fr/sites/chinese.filesrfi/imagecache/rfi_169_small/sites/images.rfi.fr/files/aef_image/_france-food_0.jpg" data-width="202" data-height="114"
                        >
                                                            <noscript>
                                    <img src="http://scd.cn.rfi.fr/sites/chinese.filesrfi/imagecache/rfi_169_small/sites/images.rfi.fr/files/aef_image/_france-food_0.jpg" alt="video" />
                                </noscript>
                                                    </a>
                                                    <a class="modeless title" href="/%E6%B3%95%E5%9B%BD/20171027-%E6%B3%95%E5%9B%BD%E9%BB%84%E6%B2%B9%E5%8D%B1%E6%9C%BA%E8%BF%98%E4%BC%9A%E6%8C%81%E7%BB%AD%E5%A4%9A%E4%B9%85" title="&#x6CD5;&#x56FD;&#x9EC4;&#x6CB9;&#x5371;&#x673A;&#x8FD8;&#x4F1A;&#x6301;&#x7EED;&#x591A;&#x4E45;&#xFF1F;">
                                法国美食
                            </a>
                                                                                                    <div class="h3">
                            <a href="/%E6%B3%95%E5%9B%BD/20171027-%E6%B3%95%E5%9B%BD%E9%BB%84%E6%B2%B9%E5%8D%B1%E6%9C%BA%E8%BF%98%E4%BC%9A%E6%8C%81%E7%BB%AD%E5%A4%9A%E4%B9%85" title="&#x6CD5;&#x56FD;&#x9EC4;&#x6CB9;&#x5371;&#x673A;&#x8FD8;&#x4F1A;&#x6301;&#x7EED;&#x591A;&#x4E45;&#xFF1F;"
                                class="modeless"                            >
                                                                    法国黄油危机还会持续多久？
                                                            </a>
                        </div>
                                            </li>
                                                                                                                                                                                                                                                                                                                                                                                                                                
                    <li data-bo-type="edition" data-bo-nid="13F55129-1DED-49DA-B430-4B87BA4692A8">
                        <a href="/%E4%B8%AD%E5%9B%BD/20171026-%E5%A4%96%E7%95%8C%E4%B8%80%E4%BA%9B%E8%A7%A3%E8%AF%BB%E8%AE%A4%E4%B8%BA%EF%BC%8C%E4%B9%A0%E8%BF%91%E5%B9%B3%E5%B0%86%E4%BC%9A%E6%88%90%E4%B8%BA%E7%AC%AC%E4%BA%8C%E4%B8%AA%E6%AF%9B%E6%B3%BD%E4%B8%9C" title="&#x5916;&#x754C;&#x89E3;&#x8BFB;&#xFF1A;&#x4E60;&#x8FD1;&#x5E73;&#x5C06;&#x4F1A;&#x6210;&#x4E3A;&#x7B2C;&#x4E8C;&#x4E2A;&#x6BDB;&#x6CFD;&#x4E1C;"
                                                        class="media center-cropped modeless lazy-loaded"
                            data-image="http://scd.cn.rfi.fr/sites/chinese.filesrfi/dynimagecache/0/157/3500/1738/195/97/sites/images.rfi.fr/files/aef_image/2017-10-25t105004z_1064940964_rc13f3943c70_rtrmadp_3_china-congress_1.jpg" data-width="202" data-height="114"
                        >
                                                            <noscript>
                                    <img src="http://scd.cn.rfi.fr/sites/chinese.filesrfi/dynimagecache/0/157/3500/1738/195/97/sites/images.rfi.fr/files/aef_image/2017-10-25t105004z_1064940964_rc13f3943c70_rtrmadp_3_china-congress_1.jpg" alt="video" />
                                </noscript>
                                                    </a>
                                                    <a class="modeless title" href="/%E4%B8%AD%E5%9B%BD/20171026-%E5%A4%96%E7%95%8C%E4%B8%80%E4%BA%9B%E8%A7%A3%E8%AF%BB%E8%AE%A4%E4%B8%BA%EF%BC%8C%E4%B9%A0%E8%BF%91%E5%B9%B3%E5%B0%86%E4%BC%9A%E6%88%90%E4%B8%BA%E7%AC%AC%E4%BA%8C%E4%B8%AA%E6%AF%9B%E6%B3%BD%E4%B8%9C" title="&#x5916;&#x754C;&#x89E3;&#x8BFB;&#xFF1A;&#x4E60;&#x8FD1;&#x5E73;&#x5C06;&#x4F1A;&#x6210;&#x4E3A;&#x7B2C;&#x4E8C;&#x4E2A;&#x6BDB;&#x6CFD;&#x4E1C;">
                                观察中国
                            </a>
                                                                                                    <div class="h3">
                            <a href="/%E4%B8%AD%E5%9B%BD/20171026-%E5%A4%96%E7%95%8C%E4%B8%80%E4%BA%9B%E8%A7%A3%E8%AF%BB%E8%AE%A4%E4%B8%BA%EF%BC%8C%E4%B9%A0%E8%BF%91%E5%B9%B3%E5%B0%86%E4%BC%9A%E6%88%90%E4%B8%BA%E7%AC%AC%E4%BA%8C%E4%B8%AA%E6%AF%9B%E6%B3%BD%E4%B8%9C" title="&#x5916;&#x754C;&#x89E3;&#x8BFB;&#xFF1A;&#x4E60;&#x8FD1;&#x5E73;&#x5C06;&#x4F1A;&#x6210;&#x4E3A;&#x7B2C;&#x4E8C;&#x4E2A;&#x6BDB;&#x6CFD;&#x4E1C;"
                                class="modeless"                            >
                                                                    外界解读：习近平将会成为第二个毛泽东
                                                            </a>
                        </div>
                                            </li>
                                                                                                                                                                                                                                                                                                                                                                                                                                
                    <li data-bo-type="edition" data-bo-nid="WB259710-RFI-ZH-HANS-20171025">
                        <a href="/%E4%B8%AD%E5%9B%BD/20171025-%E5%AE%89%E5%80%8D%E5%A4%A7%E9%80%89%E8%8E%B7%E8%83%9C%E5%90%8E%E5%B0%86%E7%BB%A7%E7%BB%AD%E6%94%B9%E5%96%84%E6%97%A5%E4%B8%AD%E5%85%B3%E7%B3%BB" title="&#x5B89;&#x500D;&#x5927;&#x9009;&#x83B7;&#x80DC;&#x540E;&#x5C06;&#x7EE7;&#x7EED;&#x6539;&#x5584;&#x65E5;&#x4E2D;&#x5173;&#x7CFB;"
                                                        class="media center-cropped modeless lazy-loaded"
                            data-image="http://scd.cn.rfi.fr/sites/chinese.filesrfi/imagecache/rfi_169_small/sites/images.rfi.fr/files/aef_image/sino_jap_1.jpg" data-width="202" data-height="114"
                        >
                                                            <noscript>
                                    <img src="http://scd.cn.rfi.fr/sites/chinese.filesrfi/imagecache/rfi_169_small/sites/images.rfi.fr/files/aef_image/sino_jap_1.jpg" alt="video" />
                                </noscript>
                                                    </a>
                                                    <a class="modeless title" href="/%E4%B8%AD%E5%9B%BD/20171025-%E5%AE%89%E5%80%8D%E5%A4%A7%E9%80%89%E8%8E%B7%E8%83%9C%E5%90%8E%E5%B0%86%E7%BB%A7%E7%BB%AD%E6%94%B9%E5%96%84%E6%97%A5%E4%B8%AD%E5%85%B3%E7%B3%BB" title="&#x5B89;&#x500D;&#x5927;&#x9009;&#x83B7;&#x80DC;&#x540E;&#x5C06;&#x7EE7;&#x7EED;&#x6539;&#x5584;&#x65E5;&#x4E2D;&#x5173;&#x7CFB;">
                                东京专栏
                            </a>
                                                                                                    <div class="h3">
                            <a href="/%E4%B8%AD%E5%9B%BD/20171025-%E5%AE%89%E5%80%8D%E5%A4%A7%E9%80%89%E8%8E%B7%E8%83%9C%E5%90%8E%E5%B0%86%E7%BB%A7%E7%BB%AD%E6%94%B9%E5%96%84%E6%97%A5%E4%B8%AD%E5%85%B3%E7%B3%BB" title="&#x5B89;&#x500D;&#x5927;&#x9009;&#x83B7;&#x80DC;&#x540E;&#x5C06;&#x7EE7;&#x7EED;&#x6539;&#x5584;&#x65E5;&#x4E2D;&#x5173;&#x7CFB;"
                                class="modeless"                            >
                                                                    安倍大选获胜后将继续改善日中关系
                                                            </a>
                        </div>
                                            </li>
                                                                                                                                                                                                                                                                                                                                                                                                                                
                    <li data-bo-type="edition" data-bo-nid="WB259582-RFI-ZH-HANS-20171024">
                        <a href="/%E4%B8%AD%E5%9B%BD/20171024-%E5%95%86%E6%8A%A5%E5%B9%BF%E5%BC%80%E8%A8%80%E8%B7%AF%E6%89%8D%E6%98%AF%E7%A4%BE%E4%BC%9A%E8%B5%B0%E5%90%91%E6%AD%A3%E7%A1%AE%E6%96%B9%E5%90%91%E7%9A%84%E9%92%A5%E5%8C%99" title="&#x300A;&#x5546;&#x62A5;&#x300B;&#xFF1A;&#x5E7F;&#x5F00;&#x8A00;&#x8DEF;&#x624D;&#x662F;&#x793E;&#x4F1A;&#x8D70;&#x5411;&#x6B63;&#x786E;&#x65B9;&#x5411;&#x7684;&#x94A5;&#x5319;"
                                                        class="media center-cropped modeless lazy-loaded"
                            data-image="http://scd.cn.rfi.fr/sites/chinese.filesrfi/imagecache/rfi_169_small/sites/images.rfi.fr/files/aef_image/2017-10-18t065642z_2066245830_rc15a671e290_rtrmadp_3_china-congress.jpg" data-width="202" data-height="114"
                        >
                                                            <noscript>
                                    <img src="http://scd.cn.rfi.fr/sites/chinese.filesrfi/imagecache/rfi_169_small/sites/images.rfi.fr/files/aef_image/2017-10-18t065642z_2066245830_rc15a671e290_rtrmadp_3_china-congress.jpg" alt="video" />
                                </noscript>
                                                    </a>
                                                    <a class="modeless title" href="/%E4%B8%AD%E5%9B%BD/20171024-%E5%95%86%E6%8A%A5%E5%B9%BF%E5%BC%80%E8%A8%80%E8%B7%AF%E6%89%8D%E6%98%AF%E7%A4%BE%E4%BC%9A%E8%B5%B0%E5%90%91%E6%AD%A3%E7%A1%AE%E6%96%B9%E5%90%91%E7%9A%84%E9%92%A5%E5%8C%99" title="&#x300A;&#x5546;&#x62A5;&#x300B;&#xFF1A;&#x5E7F;&#x5F00;&#x8A00;&#x8DEF;&#x624D;&#x662F;&#x793E;&#x4F1A;&#x8D70;&#x5411;&#x6B63;&#x786E;&#x65B9;&#x5411;&#x7684;&#x94A5;&#x5319;">
                                柏林飞鸿
                            </a>
                                                                                                    <div class="h3">
                            <a href="/%E4%B8%AD%E5%9B%BD/20171024-%E5%95%86%E6%8A%A5%E5%B9%BF%E5%BC%80%E8%A8%80%E8%B7%AF%E6%89%8D%E6%98%AF%E7%A4%BE%E4%BC%9A%E8%B5%B0%E5%90%91%E6%AD%A3%E7%A1%AE%E6%96%B9%E5%90%91%E7%9A%84%E9%92%A5%E5%8C%99" title="&#x300A;&#x5546;&#x62A5;&#x300B;&#xFF1A;&#x5E7F;&#x5F00;&#x8A00;&#x8DEF;&#x624D;&#x662F;&#x793E;&#x4F1A;&#x8D70;&#x5411;&#x6B63;&#x786E;&#x65B9;&#x5411;&#x7684;&#x94A5;&#x5319;"
                                class="modeless"                            >
                                                                    《商报》：广开言路才是社会走向正确方向的钥匙
                                                            </a>
                        </div>
                                            </li>
                                        </ul>



    </section>

                                        
                                        
                                        
                                                
                                        
                                                                
            </div>

        
                                </div>
                            </div>                                                                                                                                                                        
                        
                        
    <div class="tms-block"
         data-pos="2"
         data-type="gigaban"
         data-location="bottom"
         data-expand="true"
         data-loaded="false">
    </div>


                    </div>
                </div>

                                            </div>
        
                                    <footer>
                <div class="footer-main">
        <div class="f-col">
            <div class="f-list">
                                <img src="/bundles/aefhermesrfi/img/logo_rfi_big.png?version=20171011171259" alt="法广" />
                                                    <div class="f-first-list">
                                                    <div class="h4">广播节目</div>
                            <ul>
                                                                                                                                                    
                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                    <li><a  class="modeless" href="/专栏检索/" title="专栏检索" data-translate="Emissions">专栏检索</a></li>
                                                                                                                                                                                        
                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                    <li><a  class="modeless" href="/所有广播新闻/" title="所有广播新闻" data-translate="Tous les journaux">所有广播新闻</a></li>
                                                                                                </ul>
                                                    <div class="h4">法广简介</div>
                            <ul>
                                                                                                                                                    
                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                    <li><a  href="/关于法广" class="modeless" title="关于法广" data-translate="À propos de RFI">关于法广</a></li>
                                                                                                </ul>
                                                    <div class="h4">服务</div>
                            <ul>
                                                                                                                                                    
                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                    <li><a  class="grid-programs" title="节目表" data-translate="Grille des programmes" style="cursor: pointer">节目表</a></li>
                                                                                                                                                                                        
                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                    <li><a  href="/手机与平板电脑" class="modeless" title="手机与平板电脑" data-translate="Mobile / Tablette">手机与平板电脑</a></li>
                                                                                                                                                                                        
                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                    <li><a  href="/销售法广产品" class="modeless" title="销售法广产品" data-translate="Vente de contenus">销售法广产品</a></li>
                                                                                                </ul>
                                                    <div class="h4">法广货架</div>
                            <ul>
                                                                                                                                                    
                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                    <li><a  href="http://www.rfi.fr/talent/cd/" class="modeless" title="唱碟" data-translate="CD">唱碟</a></li>
                                                                                                                                                                                        
                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                    <li><a  href="http://www.rfi.fr/talent/livres/" class="modeless" title="书籍" data-translate="LIVRES">书籍</a></li>
                                                                                                                                                                                        
                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                    <li><a  href="http://www.rfi.fr/talent/archives/" class="modeless" title="音频存档" data-translate="ARCHIVES">音频存档</a></li>
                                                                                                </ul>
                                            </div>
                            </div>
        </div>
        <div class="f-col">
            <div class="f-col">
                                    <div class="f-col f-list">
                                                    <div class="h4">语种</div>
                            <ul>
                                                                                                                                                    
                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                    <li><a  href="http://www.rfi.fr" title="法语" data-translate="RFI FR" target="_blank">法语</a></li>
                                                                                                                                                                                        
                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                    <li><a  href="http://en.rfi.fr" title="英语" data-translate="RFI english" target="_blank">英语</a></li>
                                                                                                                                                                                        
                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                    <li><a  href="http://br.rfi.fr/" title="巴西葡萄牙语" data-translate="Bresilien" target="_blank">巴西葡萄牙语</a></li>
                                                                                                                                                                                        
                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                    <li><a  href="http://pt.rfi.fr" title="葡萄牙语" data-translate="RFI portugues" target="_blank">葡萄牙语</a></li>
                                                                                                                                                                                        
                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                    <li><a  href="http://km.rfi.fr" title="柬埔寨语" data-translate="RFI khmer" target="_blank">柬埔寨语</a></li>
                                                                                                                                                                                        
                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                    <li><a  href="http://es.rfi.fr" title="西班牙语" data-translate="RFI espanol" target="_blank">西班牙语</a></li>
                                                                                                                                                                                        
                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                    <li><a  href="http://ha.rfi.fr" title="豪萨语" data-translate="RFI hausa" target="_blank">豪萨语</a></li>
                                                                                                                                                                                        
                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                    <li><a  href="http://ma.rfi.fr" title="曼丁哥语" data-translate="RFI Mandenkan" target="_blank">曼丁哥语</a></li>
                                                                                                                                                                                        
                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                    <li><a  href="http://sw.rfi.fr" title="斯瓦希里语" data-translate="RFI kiswahili" target="_blank">斯瓦希里语</a></li>
                                                                                                                                                                                        
                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                    <li><a  href="http://fa.rfi.fr" title="波斯语" data-translate="RFI persian" target="_blank">波斯语</a></li>
                                                                                                                                                                                        
                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                    <li><a  href="http://ru.rfi.fr" title="俄语" data-translate="RFI RU" target="_blank">俄语</a></li>
                                                                                                                                                                                        
                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                    <li><a  href="http://vi.rfi.fr" title="越语" data-translate="RFI VI" target="_blank">越语</a></li>
                                                                                                                                                                                        
                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                    <li><a  href="http://www.rfi.ro" title="罗马尼亚语" data-translate="RFI RO" target="_blank">罗马尼亚语</a></li>
                                                                                                </ul>
                                                    <div class="h4">FMM集团其他网站</div>
                            <ul>
                                                                                                                                                    
                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                    <li><a  href="https://savoirs.rfi.fr/cn" title="学法语" data-translate="Langue française" target="_blank">学法语</a></li>
                                                                                                                                                                                        
                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                    <li><a  href="http://musique.rfi.fr" title="法广音乐" data-translate="RFI Musique" target="_blank">法广音乐</a></li>
                                                                                                                                                                                        
                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                    <li><a  href="http://www.rfiplaneteradio.org/" title="RFI Planète Radio" data-translate="RFI Planète Radio" target="_blank">RFI Planète Radio</a></li>
                                                                                                                                                                                        
                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                    <li><a  href="http://www.france24.com/" title="法国24电视台" data-translate="France 24" target="_blank">法国24电视台</a></li>
                                                                                                                                                                                        
                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                    <li><a  href="http://www.mc-doualiya.com/" title="阿拉伯语" data-translate="mc-doualiya" target="_blank">阿拉伯语</a></li>
                                                                                                                                                                                        
                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                    <li><a  href="http://www.rfi-instrumental.com/" title="法广音乐库" data-translate="rfi-instrumental" target="_blank">法广音乐库</a></li>
                                                                                                                                                                                        
                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                    <li><a  href="http://academie.france24-mcd-rfi.com/fr/" title="新闻学部" data-translate="Académie" target="_blank">新闻学部</a></li>
                                                                                                </ul>
                                            </div>
                                <div class="f-col">
                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                        <div class="map">
                            <a  href="/如何收听法广" class="modeless" title="如何收听法广" data-translate="Comment recevoir RFI ?">如何收听法广</a>
                        </div>
                                                                                                                                                                                    
                    
                        
    <div class="banner tms-block"
         data-pos="1"
         data-type="pave"
         data-location="footer"
         data-expand="false"
         data-loaded="false">
    </div>

                </div>
            </div>
            <div class="f-row">
                                    <div class="social-networks">
                                                                                                                                                            
                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                    <a  class="join-community" title="加入社区" data-translate="Rejoignez la communauté" style="cursor: pointer">加入社区</a>
                                                                                                                                        <ul>
                                                                                                                                                    
                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                    <li><a  href="https://www.facebook.com/pages/法国国际广播电台/155677885272" class="fb" title="RFI sur Facebook" data-translate="RFI sur Facebook" target="_blank">Facebook</a></li>
                                                                                                                                                                                        
                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                    <li><a  href="https://twitter.com/RFI_Cn" class="tw" title="RFI sur Twitter" data-translate="RFI sur Twitter" target="_blank">Twitter</a></li>
                                                                                                                                                                                        
                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                    <li><a  href="https://plus.google.com/+RFIcn" class="go" title="RFI sur Google+" data-translate="RFI sur Google+" target="_blank" rel="publisher">Google +</a></li>
                                                                                                                                                                                        
                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                    <li><a  href="http://instagram.com/rfi.fr" class="is" title="RFI sur Instagram" data-translate="RFI sur Instagram" target="_blank">Instagram</a></li>
                                                                                                                                                                                        
                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                    <li><a  href="http://www.dailymotion.com/rfi" class="dm" title="RFI sur Dailymotion" data-translate="RFI sur Dailymotion" target="_blank">Dailymotion</a></li>
                                                                                                                                                                                        
                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                    <li><a  href="http://www.youtube.com/RFIcn" class="yt" title="RFI sur Youtube" data-translate="RFI sur Youtube" target="_blank">Youtube</a></li>
                                                                                                                                                                                        
                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                    <li><a  href="https://soundcloud.com/RadioFranceInternationale" class="sc" title="RFI sur SoundCloud" data-translate="RFI sur SoundCloud" target="_blank">Soundcloud</a></li>
                                                                                                </ul>
                                            </div>
                            </div>
        </div>
    </div>
            <nav>
            <ul>
                                                                                    
                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                    <li><a  href="/关于法广" class="modeless" title="关于法广" data-translate="A propos de RFI">关于法广</a></li>
                                                                                                        
                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                    <li><a  href="/与法广联系" class="modeless" title="与法广联系" data-translate="Nous écrire">与法广联系</a></li>
                                                                                                        
                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                    <li><a  href="http://partenariat.rfi.fr" title="如何与法广合作" data-translate="RFI Radios Partenaires" target="_blank">如何与法广合作</a></li>
                                                                                                        
                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                    <li><a  href="/广告部" class="modeless" title="广告部" data-translate="Régie publicitaire">广告部</a></li>
                                                                                                        
                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                    <li><a  href="/版本说明" class="modeless" title="版本说明" data-translate="Mentions légales">版本说明</a></li>
                                                </ul>
        </nav>
    
                <ul class="partners">
            <li><a href="/" class="modeless" title="法国国际广播电台"><img src="/bundles/aefhermesrfi/img/rfi-logo.png?version=20171011171259" alt=""></a></li>
            <li><a href="http://www.france24.com/" target="_blank" title="法国24电视台"><img src="/bundles/aefhermesrfi/img/france24-logo.png?version=20171011171259" alt=""></a></li>
            <li><a href="http://www.mc-doualiya.com/" target="_blank" title="蒙特卡洛中东电台"><img src="/bundles/aefhermesrfi/img/mcd-logo.png?version=20171011171259" alt=""></a></li>
            <li><a href="http://www.francemediasmonde.com/" target="_blank" title="法国世界媒体集团 "><img src="/bundles/aefhermesrfi/img/fmm-logo.png?version=20171011171259" alt=""></a></li>
        </ul>
                <div class="copy">
            © 2017 RFI – 版权所有版权所有<br>
            法广对非本网站内容不承担责任<br>
            <a href="http://www.acpm.fr/Marque/marque-rfi" target="_blank" rel="nofollow" class="ojd">通过OJD认证</a>
        </div>
    </footer>

                                        <div id="main-player-wrapper">
                    <div id="main-player" style="height: 0px" class="bsplayer-container"></div>
                </div>
                                        <div id="common-overlay">&nbsp;</div>
                    
                    <!-- // placeholder RFI CN // -->
<style>
.sharetext-box .shareable-text .opening-quote {margin-right: 15px !important;}
.shareable-text {line-height: 1.1 !important;}
.lang-cn nav#nav-main a, .lang-cn nav#nav-main span {margin-right: 25px;}
.h-menu > li:last-child {
font-size: 16px;
}
.emmision_article-container article > .intro {clear: left;float: none;}
</style>
<script type="text/javascript">
if (document.location.toString().match(/\/preview\//)!=null) {
if (document.getElementById('comments'))
document.getElementById('comments').remove();
if (document.getElementsByTagName('article')) {
if (document.getElementsByTagName('article').item(0)) {
if (document.getElementsByTagName('article').item(0).children[0]) {
document.getElementsByTagName('article').item(0).children[0].remove();
}
}
}
}
</script>

        
                                
        
                
                            <div id='errorsArea' class='error-area'>
    <div>抱歉，链接期限已过</div>
</div>
                <script type="text/javascript" src="//nexus.ensighten.com/francemm/rfi/Bootstrap.js"></script>
    </body>
</html>

'''

datetime_t = str(datetime.date.today()).split('-')  # 对日期进行拆分，返回一个['2017', '10', '09']形式的列表


#
#
def ans0():
    liebie_dic = {'中国':'%E4%B8%AD%E5%9B%BD','港澳台':'%E6%B8%AF%E6%BE%B3%E5%8F%B0', '国际':'%E5%9B%BD%E9%99%85', '人权':'%E4%BA%BA%E6%9D%83', '政治':'%E6%94%BF%E6%B2%BB', '经贸':'%E7%BB%8F%E8%B4%B8', '社会':'%E7%A4%BE%E4%BC%9A', '生态':'%E7%94%9F%E6%80%81', '科技与文化':'%E7%A7%91%E6%8A%80%E4%B8%8E%E6%96%87%E5%8C%96'}
    print(liebie_dic['中国'])
    liebie_list = ['中国','港澳台']
    for lan in liebie_list:
        url_prefix = 'http://cn.rfi.fr'
        url_list = []
        vol_tl = lan + '时事'
        for nu in range(1,3):
            vol_ul = 'http://cn.rfi.fr/' + liebie_dic[lan] + '/all/?page=' + str(nu)
            url_list.append(vol_ul)

        print(url_list)
        print(vol_tl)
    soup = BeautifulSoup(''.join(html))
    article_link = []
    artiultag = soup.find('ul', attrs = {'class':'list'})
    for li in artiultag.findAll('li'):
        #print(li)

        find_today = re.compile('(\d\d)/(\d\d)/(\d\d\d\d)</time>')
        month = find_today.search(str(li))  # 把上面构建的表达式作用于findAll找出来的内容
        # try/except结构主要是用于正则表达式查找，如果不用这个结构，在部分标签当中查找不到内容的时候，下面引用查找结果group()就会报错，造成崩溃。
        try:
            #print(month.group())
            d1 = datetime.date.today()  # 获取今天的日期
            d2 = datetime.date(int(month.group(3)), int(month.group(2)), int(month.group(1)))  # 获取新闻的日期
            days_betwen = (d1 - d2).days  # 获取时间差，结果为整数
            #print(days_betwen)
            if days_betwen <= 1:  # 限定抓取几天内的新闻，当天的则为days_betwen == 0
                article_link.append(str(li))  # 注意要转换为字符串，beautifusoup不接受列表和其他类型的数据
        except:
            pass

    #print(article_link)
    soup2 = BeautifulSoup(''.join(article_link))

    #下面的for循环在上面找出指定日期范围内的正文链接当中提取url链接，并配合'http://www.jxta.gov.cn/'形成最终的正文链接
    for link in soup2.findAll('a'):
        imagelink = re.compile(r'src="')
        ilinkfind = imagelink.findall(str(link))
        if ilinkfind:
            continue
        if '/tag/' in link['href']:
            continue
        # print(link)
        print(url_prefix + link['href'])
        # title_find = re.compile(r'<.*><span>.*</span>(.*)</a>')
        # title_search = title_find.search(str(link))
        #print(link['href'])
        print(link.contents[0].strip())
#
ans0()

