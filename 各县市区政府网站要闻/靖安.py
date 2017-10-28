# coding=utf-8

from BeautifulSoup import BeautifulSoup
import datetime, re

doc = """

<!DOCTYPE html PUBLIC "-//W3C//DTD XHTML 1.0 Transitional//EN" "http://www.w3.org/TR/xhtml1/DTD/xhtml1-transitional.dtd">
<html xmlns="http://www.w3.org/1999/xhtml">
<head>
    <meta http-equiv="Content-Type" content="text/html; charset=utf-8" />
<meta content="" name="Keywords" />
<meta content="" name="Description"/>
<title>政务要闻-靖安县人民政府网站</title>
 
    <link href="/Template/Default/Skin/ja/style.css" rel="stylesheet" type="text/css" />
    <link href="/Template/Default/Skin/ja/default2016.css" rel="stylesheet" type="text/css" />
    <link href="/Template/Default/Skin/ja/article_page2016.css" rel="stylesheet" type="text/css" />
    <link href="/Template/Default/Skin/ja/navcss.css" rel="stylesheet" type="text/css" />
    <link href="/Template/Default/Skin/ja/module2016.css" rel="stylesheet" type="text/css" />
  
    <link href="/Template/Default/Skin/ja/page_bs2016.css" rel="stylesheet" type="text/css" />
      
<script src="/Template/Default/Skin/ja/jquery.pack.js"></script>
<script src="/Template/Default/Skin/ja/scFa.js"></script>
<script src="/Template/Default/Skin/ja/jquery.SuperSlide.2.1.1.js"></script>
<script src="/Template/Default/Skin/ja/jquery.pack.js"></script>
<script src="/Template/Default/Skin/ja/scFa.js"></script>
<script src="/Template/Default/Skin/ja/jquery.SuperSlide.2.1.1.js"></script>
<script type="text/javascript" src="/js/jquery.bcat.bgswitcher.js"></script>
<script src="/JsC/require.js" upload="true"></script>
    <script src="/JsC/public.js"></script>
    <script type="text/javascript" src="/JsC/wcmjslib1.2.js"></script>
    <script src="/JsC/zwgk_global.js"></script>
    <script type="text/javascript" src="/JsC/Hj.easyRead.Mask.js"></script>
    <script type="text/javascript" src="/JsC/Hj.easyRead.main.js"></script>
    <script type="text/javascript" src="/JsC/Hj.easyRead.load.js"></script>
    <script type="text/javascript" src="/JsC/jquery-powerFloat-min.js"></script>
    <script type="text/javascript" src="/JsC/jquery.hotkeys.js"></script>
    <script type="text/javascript" src="/JsC/soundmanager2-nodebug-jsmin.js"></script>
    <script type="text/javascript" src="/JsC/Hj.easyRead.panel.js"></script>
    <script type="text/javascript" src="/JsC/Hj.easyRead.line.js"></script>
    <script type="text/javascript" src="/JsC/Hj.easyRead.ui.js"></script>
    <script type="text/javascript" src="/JsC/Hj.easyRead.light.js"></script>
    <script type="text/javascript" src="/JsC/Hj.easyRead.refresh.js"></script>
    <script type="text/javascript" src="/JsC/Hj.easyRead.Init.js"></script>
    <script type="text/javascript" src="/JsC/Hj.easyRead.history.js"></script>
    <script type="text/javascript" src="/JsC/Hj.easyRead.correction.js"></script>
    <link rel="stylesheet" type="text/css" href="/JsC/Hj.easyRead.css">
<link href="/Template/Default/Skin/ja/default2016.css" rel="stylesheet" type="text/css" />
 <link href="/Template/Default/Skin/ja/module2016.css" rel="stylesheet" type="text/css" />
      <link href="/Template/Default/Skin/ja/page_bs2016.css" rel="stylesheet" type="text/css" />

<style>
  .smooth dt, .smooth dd {
margin: 0 4px;
overflow: hidden;
padding-top: 2px;
height: 15px;
line-height: 15px;
}
.float, .fl, .smooth-lf, .smooth, .smooth dt, .smooth dd, .logo-box, .header-rg, .menu li {
float: left;
display: inline;
overflow: hidden;
}
.Hj-easyRead-smoothTips, .smoothTips
{
    height: 28px;
}
.w980
{
    margin: 0 auto;
    padding: 0;
    width: 980px;
}
.smooth-box
{
    float: right;
    display: inline;
    overflow: hidden;
    text-align: right;
    padding-top: 7px;
}
.smooth-lf
{
    width: 3px;
    padding-top: 2px;
}

Inherited from div.smooth-box .smooth-box
{
    text-align: right;
}
.smooth
{
    width: 657px;
}
.smooth dd a {
display: inline;
}
.smooth dd img {
vertical-align: middle;
margin-right: 5px;
}
  </style>

<script>
$(function(){
	$(".tabbox .tab a").mouseover(function(){
		$(this).addClass('on').siblings().removeClass('on');
		var index = $(this).index();
		number = index;
		$('.tabbox .content li').hide();
		$('.tabbox .content li:eq('+index+')').show();
	});
	
	var auto = 0;  //等于1则自动切换，其他任意数字则不自动切换
	if(auto ==1){
		var number = 0;
		var maxNumber = $('.tabbox .tab a').length;
		function autotab(){
			number++;
			number == maxNumber? number = 0 : number;
			$('.tabbox .tab a:eq('+number+')').addClass('on').siblings().removeClass('on');
			$('.tabbox .content ul li:eq('+number+')').show().siblings().hide();
		}
		var tabChange = setInterval(autotab,3000);
		//鼠标悬停暂停切换
		$('.tabbox').mouseover(function(){
			clearInterval(tabChange);
		});
		$('.tabbox').mouseout(function(){
			tabChange = setInterval(autotab,3000);
		});
	  }
});
</script>

<script type="text/javascript">
            $(function () {
                function tabs(tabTit, on, tabCon) {
                    $(tabCon).each(function () {
                        $(this).children().eq(0).show();
                    });
                    $(tabTit).each(function () {
                        $(this).children().eq(0).addClass(on);
                    });
                    $(tabTit).children().click(function () {//鼠标“click”的效果
                        $(this).addClass(on).siblings().removeClass(on);
                        var index = $(tabTit).children().index(this);
                        $(tabCon).children().eq(index).show().siblings().hide();
                    });
                }
	 
		tabs(".tab-hd1", "active", ".tab-bd1");
                tabs(".tab-hd", "active", ".tab-bd");
		tabs(".tab-hd3", "active", ".tab-bd3");
                tabs(".tab-hd2", "active", ".tab-bd2");
		tabs(".tab-hd4", "active", ".tab-bd4");
            });
        </script>
<script type="text/javascript">
function MM_jumpMenu(targ,selObj,restore){ //v3.0
  eval(targ+".location='"+selObj.options[selObj.selectedIndex].value+"'");
  if (restore) selObj.selectedIndex=0;
}

$(function(){
    $(".J_tabBox").slide({mainCell:".J_tabContent", titCell:".J_tabHandler>*"});
})

<!-- 
/*tab切换脚本*/ 
function setTab(name,cursel,n){ 
for(i=1;i<=n;i++){ 
var menu=document.getElementById(name+i); 
var con=document.getElementById("con_"+name+"_"+i); 
menu.className=i==cursel?"hover":""; 
con.style.display=i==cursel?"block":"none"; 
} 
} 
//--> 

</script>
</head>
<body>
<!--top start -->
 

 

  
    <!--top start -->
    <div class="fullSlide" id="bg-body">
      
    </div>
    <script type="text/javascript">
        $(".fullSlide").slide({ mainCell: "ul", effect: "fold", autoPlay: true, mouseOverStop: false, interTime: 6000 });
    </script>
 

<script type="text/javascript">
    var srcBgArray = ["/Template/Default/Skin/images/bg-005.jpg", "/Template/Default/Skin/images/bg-006.jpg", "/Template/Default/Skin/images/bg-007.jpg", "/Template/Default/Skin/images/bg-008.jpg", "/Template/Default/Skin/images/bg-004.jpg"];

    $(document).ready(function () {
        $('#bg-body').bcatBGSwitcher({
            urls: srcBgArray,
            alt: 'Full screen background image'
        });
    });
</script>

    <div class="gnqwarp">
        <div class="gnq w1002">
            <p>
                中国<span>·</span>江西省<span>·</span>靖安县人民政府门户网站欢迎您！</p>
            <ul>
                <li><a href="javascript:void(0);" onclick="SetHome(this,'');">设为首页</a></li>
               <li> <a href="javascript:;" class="fav" target="_self" id="smoothBegin2">
                <voice class="Hj-EasyRead-Pointer-Label"><voice class="Hj-EasyRead-Pointer-Label">无障碍浏览</voice></voice></a></li>
 <li><a href="/Category_493/Index.aspx" >RSS订阅</a></li>
                  <li>  <a href="javascript:void(0);" onclick="AddFavorite('靖安县政府门户','')">
                        收藏本站</a></li><li><a href="http://www.jxjaxzf.gov.cn/">手机网站</a></li><li><a href="/Category_485/Index.aspx">
                            网站导航</a></li></ul>
        </div>
    </div>
    <div class="header w1002">
        <div class="logo fl">
           <a href="/"><img src="/Template/Default/Skin/images/logo.png" alt=""  style=" height: 100px;"></a></div>
        <div class="search">
            <form action="/search.aspx" class="searchform" target="_blank">
           
            <input type="text" class="keyword" autocomplete="off" name="keyword" id="skeyword"
                placeholder="请输入搜索关键字">
            <input type="submit" class="submit" value=" " id="sbutton"></form>
            <script type="text/javascript">
                                                                                                                                                                                                                                                                                                                     var holder = $(this).find(".keyword").attr("placeholder"),
              keyword = $.trim($(this).find(".keyword").val()),
              searchType = $(this).find(".searchType").val();
        	                                                                                                                                                                                                                                                                                                         }
        	                                                                                                                                                                                                                                                                                                                          })(jQuery);
            </script>
            <div class="synotice">
                <ul>

            <li><a href="/Item/24071.aspx" target="_blank">宝峰禅意养生乐园10KV毗炉线改迁工程中标结…</a></li><li><a href="/Item/24062.aspx" target="_blank">靖安县城南市民健身公园设计项目中标公示</a></li><li><a href="/Item/24055.aspx" target="_blank">靖安县春秋盛苑住宅小区建设工程项目监理中…</a></li><li><a href="/Item/24048.aspx" target="_blank">水口乡哲里至熊家三级公路拓宽改建工程施工…</a></li><li><a href="/Item/24045.aspx" target="_blank">靖安县仁首镇防洪堤硬化、绿化、亮化工程 招…</a></li><li><a href="/Item/24044.aspx" target="_blank">靖安县罗湾乡塘埠村等2个乡镇5个村土地整理…</a></li><li><a href="/Item/24043.aspx" target="_blank">靖安县交警大队车辆管理所附属工程招标公告</a></li><li><a href="/Item/24032.aspx" target="_blank">靖安县水口乡桃源村土门中桥工程招标公告</a></li>
          
                  
                </ul>
            </div>
            <script type="text/javascript">
                jQuery(".synotice").slide({ mainCell: "ul", effect: "top", autoPlay: true, vis: 1, mouseOverStop: false, interTime: 2000 });
            </script>
        </div>
        <div class="clear">
        </div>
    </div>
    <div class="nav w1002">
        <ul>
            <li class="navqhnma asd" id="m1"><a href="/Default.aspx" class="na asd1">网站首页 </a></li>
            <li class="navqhnma nb" id="m2"><a class="nb" href="/Category_108/Index.aspx">县情浏览 </a>
                <div class="sub"  style=" border:3px solid #0D7DCA;">

                <div class="col-1">
                <div class="col-11"><img src="/Template/Default/Skin/img/con2.png" /><h3>走进靖安</h3></div>
                <ul>
                <li><a href="/Category_124/Index.aspx">地理气候</a></li>
                <li><a href="/Category_121/Index.aspx">自然资源</a></li>
                <li><a href="/Category_126/Index.aspx">历史渊源</a></li>
                <li><a href="/Category_119/Index.aspx">名胜古迹</a></li>
                <li><a href="/Category_118/Index.aspx">历史名人</a></li>
                </ul>
                
                </div>
                <div class="line"><img src="/Template/Default/Skin/img/line.png" /></div>
                
                <div class="col-2">
               <div class="col-22"><img src="/Template/Default/Skin/img/con3.png" /><h3>靖安情况</h3></div>
               <div class="xmap"> <img src="/Template/Default/Skin/img/about.jpg" /> <span style="text-indent:2em;">靖安县地处赣西北，总面积1377平方公里，辖5镇6乡，人口15万，经昌铜高速到南昌37公里，到省行政中心仅半小时，距昌北国际机场56公里，属国家长江中游城市群、南昌大都市区、昌铜高速生态经济带三大规划区内。</span></div>

                <div class="xmaptext">2016年，财政总收入完成8.67亿元，同比增长3.9%；规模以上工业增加值完成16.5亿元，同比增长9.6%；固定资产投资预计完成50.96亿元，同比增长17.7%。靖安是全省首个国家级生态县、全国休闲农业和乡村旅游示范县、全国生态文明示范工程试点县、全国河湖管护体制机制创新试点县、全国森林可持续经营试点县、全省绿色低碳转型试点县、全省生态文明先行示范县...<a href="/Category_114/Index.aspx">更多》</a> </div>
                </div>


             
                       <div class="line"><img src="/Template/Default/Skin/img/line.png" /></div>
                       
               <div class="col-3">
                <div class="col-33"><img src="/Template/Default/Skin/img/con4.png" /><h3>旅游靖安</h3></div>
                <ul>
                <li><a href="/Category_110/Index.aspx">旅游景点</a></li>
                <li><a href="/Category_340/Index.aspx">精品路线</a></li>
                <li><a href="/Category_348/Index.aspx">靖安风光</a></li>
                <li><a href="/Category_208/Index.aspx">靖安民俗</a></li>
                <li><a href="/Category_209/Index.aspx">靖安故事</a></li>               
                 <li><a href="/Category_211/Index.aspx">文化古迹</a></li>         
       </ul>   
       
       
                 <div class="col-34"><img src="/Template/Default/Skin/img/con5.png" /><h3>投资靖安</h3></div>
                <ul>
                <li><a href="/Category_43/Index.aspx">招商项目</a></li>
                <li><a href="/Category_45/Index.aspx">投资环境</a></li>
                <li><a href="/Category_339/Index.aspx">公开承诺</a></li>
                <li><a href="/Category_44/Index.aspx">优惠政策</a></li>   
       </ul>   
               </div>     
        </div>
            </li>
            <li class="navqhnma" id="m3"><a class="nc" href="/Category_111/Index.aspx">政务公开 </a>
                <div class="sub" style=" border:3px solid #0D7DCA;">
                    <div class="col-1">
                        <div class="m-gkdh">
                            <ul>
                                <li class="lbox l1"><a href="/Category_313/Index.aspx">领导风范</a></li>
                                <li class="lbox l2"><a href="http://xxgk.jxjaxzf.gov.cn/zgja/zfxxgk_38041/ysqgkxx_38043/">财政公开</a></li>
                            </ul>
                            <div class="l3">
                               
                               <a href="http://xxgk.jxjaxzf.gov.cn/zgja/zfxxgk_38041/gkzn_38042/">政府信息公开指南</a>
                                <a href="/Category_598/Index.aspx">政府信息公开年报</a>
                                  <a href="http://xxgk.jxjaxzf.gov.cn/zgja/zfxxgk_38041/">政府信息公开目录</a>
                                   <a href="http://xxgk.jxjaxzf.gov.cn/zgja/zfxxgk_38041/">政府信息公开规定</a>
                                   
                            </div>
                        </div>
                        <div class="m-news box J_tabBox">
                            <div class="hd">
                                <ul class="tab J_tabHandler">
                                    <li class="on"><a href="/Category_133/Index.aspx">政务要闻 </a></li>
                                    <li><a href="/Category_320/Index.aspx">乡镇动态</a></li>
                                    <li><a href="/Category_134/Index.aspx">部门动态</a></li>
                                </ul>
                            </div>
                            <div class="bd J_tabContent">
                                <ul class="infoList infoListA">
                              
            <li><span class="date">10-20</span><a href="/Item/24067.aspx" target="_blank">我县保障性住房公开摇号、405户中低收入…</a></li><li><span class="date">10-20</span><a href="/Item/24066.aspx" target="_blank">广西天等县考察团到我县考察精准扶贫工作</a></li><li><span class="date">10-19</span><a href="/Item/24064.aspx" target="_blank">我县广大干部群众收听收看十九大开幕式盛况</a></li><li><span class="date">10-18</span><a href="/Item/24063.aspx" target="_blank">我县开展2017年扶贫日电商扶贫体验活动</a></li><li><span class="date">10-17</span><a href="/Item/24059.aspx" target="_blank">我县获评2016年度市县科学发展综合考核评…</a></li><li><span class="date">10-16</span><a href="/Item/24054.aspx" target="_blank">县人大开展城区备用水源调研工作</a></li><li><span class="date">10-16</span><a href="/Item/24053.aspx" target="_blank">“田野牧歌•仁首老家”在周末大舞台精彩…</a></li><li><span class="date">10-13</span><a href="/Item/24050.aspx" target="_blank">市委常委、组织部长蔡清平到我县督查安全…</a></li><li><span class="date">10-12</span><a href="/Item/24047.aspx" target="_blank">全县当前重点工作调度会召开</a></li><li><span class="date">10-11</span><a href="/Item/24039.aspx" target="_blank">县政府召开第十一次常务会议</a></li>
          
                                </ul>
                                <ul class="infoList infoListA hide">
                                    
            <li><span class="date">10-20</span><a href="/Item/24069.aspx" target="_blank">双溪镇联合人社局、工业园管委会举办“降…</a></li><li><span class="date">10-16</span><a href="/Item/24056.aspx" target="_blank">罗湾乡强化管理，确保收获季节“不冒烟”</a></li><li><span class="date">10-13</span><a href="/Item/24051.aspx" target="_blank">双溪镇大桥村党员协力打造“高颜值”家园…</a></li><li><span class="date">10-12</span><a href="/Item/24049.aspx" target="_blank">三爪仑百花蜜进军2017中国（江西）红色旅…</a></li><li><span class="date">10-11</span><a href="/Item/24041.aspx" target="_blank">高湖镇“个性化认领订制”富农民</a></li><li><span class="date">10-09</span><a href="/Item/24035.aspx" target="_blank">高湖商会与高湖中学举办共商教育发展座谈会</a></li><li><span class="date">10-09</span><a href="/Item/24034.aspx" target="_blank">中源乡召开第十次支部书记例会暨“国省干…</a></li><li><span class="date">09-30</span><a href="/Item/24028.aspx" target="_blank">双溪镇举办综治干部暨网格员业务培训班</a></li><li><span class="date">09-29</span><a href="/Item/24024.aspx" target="_blank">罗湾乡严把“三关”确保廉洁过“双节”</a></li><li><span class="date">09-28</span><a href="/Item/24021.aspx" target="_blank">中源乡三步走推进“路长制”工作</a></li>
          
                                </ul>
                                <ul class="infoList infoListA hide">
                                   
            <li><span class="date">10-20</span><a href="/Item/24070.aspx" target="_blank">县公安局组织民警观看“十九大”开幕盛会</a></li><li><span class="date">10-20</span><a href="/Item/24068.aspx" target="_blank">县统计局组织党员干部集中收看十九大开幕式</a></li><li><span class="date">10-18</span><a href="/Item/24061.aspx" target="_blank">我县建立首家省武术太极拳培训基地</a></li><li><span class="date">10-16</span><a href="/Item/24057.aspx" target="_blank">县国土局:四举措做好批而未用土地消化工作</a></li><li><span class="date">10-13</span><a href="/Item/24052.aspx" target="_blank">县国土资源局形势多样学习黄大年先进事迹</a></li><li><span class="date">10-11</span><a href="/Item/24042.aspx" target="_blank">县检察院召开2017年度检察理论研究年会</a></li><li><span class="date">10-09</span><a href="/Item/24033.aspx" target="_blank">县公路分局“十一”假期加紧施工为国庆献礼</a></li><li><span class="date">09-29</span><a href="/Item/24025.aspx" target="_blank">县国土局:举行朗诵比赛、喜迎十九大</a></li><li><span class="date">09-28</span><a href="/Item/24017.aspx" target="_blank">县公安局全力优化治安环境</a></li><li><span class="date">09-27</span><a href="/Item/24014.aspx" target="_blank">县畜牧水产局开展环境卫生大整治行动</a></li>
          
                                </ul>
                            </div>
                        </div>
                    </div>
                    <div class="col-2">
                        <div class="m-tzgg">
                            <h3>
                                通知公告</h3>
                            <ul class="infoList">
                                 
            <li><a href="/Item/24071.aspx" target="_blank">宝峰禅意养生乐园10KV毗炉线改迁工…</a></li><li><a href="/Item/24062.aspx" target="_blank">靖安县城南市民健身公园设计项目中…</a></li><li><a href="/Item/24055.aspx" target="_blank">靖安县春秋盛苑住宅小区建设工程项…</a></li>
          
                        </div>
                        <div class="m-menu">
                            <h3>
                                重点领域信息公开</h3> 
                            <ul>
                                <li class="li1 first"><a title="行政权力清单"  target="_blank" href="http://ycja.jxzwfww.gov.cn/jazwfw/ygzwNew.jspx">行政权力清单</a></li>
                                <li class="li2"><a title="部门责任清单" target="_blank" href="http://ycja.jxzwfww.gov.cn/jazwfw/ygzw_bmzrNew.jspx" >部门责任清单</a></li>
                              <li class="li2"><a title="市场准入清单" target="_blank" href="http://ycja.jxzwfww.gov.cn/jazwfw/ygzw_sczrNew.jspx" >市场准入清单</a></li>
 
                              <li class="li2"><a title="行政事业性收费清单"  target="_blank" href="http://ycja.jxzwfww.gov.cn/jazwfw/ygzw_xzsyNew.jspx">行政事业性收费清单</a></li>
                              <li class="li2"><a title="财政资金信息" href="/Category_245/Index.aspx">财政资金信息</a></li>
                              <li class="li2"><a title="公共服务信息" href="/Category_652/Index.aspx">公共服务信息</a></li>
                              <li class="li2"><a title="重大项目建设" href="/Category_291/Index.aspx">重大项目建设</a></li>
                            </ul>
                        </div>
                    </div>
                </div>
            </li>
            <li class="navqhnma" id="m4"><a class="nd" href="/Category_137/Index.aspx">办事服务 </a>
                <div class="sub" style=" border:3px solid #0D7DCA;">
                    <div class="col-1">
                    <div class="col-11"><h4><a href="/Category_425/Index.aspx">场景导航</a></h4></div>
                    <div class="clear"></div>
                    <ul>
                     <li><a href="/Category_425/Index.aspx">婚姻生育</a></li>
<li><a href="/Category_426/Index.aspx">上学服务</a></li>
<li><a href="/Category_427/Index.aspx">户籍服务</a></li>
<li><a href="/Category_428/Index.aspx">驾驶员办事</a></li>
<li><a href="/Category_429/Index.aspx">我要创业</a></li>
                    </ul>
                     <div class="clear"></div>
                        <div class="col-11"><h4>绿色通道</h4></div>
                    <div class="clear"></div>
                    <ul>
                   <li><a href="/Category_165/Index.aspx">军人</a></li>
                    <li><a href="/Category_161/Index.aspx">下岗工人</a></li>
                    <li><a href="/Category_163/Index.aspx">妇女</a></li>
                    <li><a href="/Category_160/Index.aspx">老年人</a></li>
                    <li><a href="/Category_142/Index.aspx">农民</a></li>
                    <li><a href="/Category_162/Index.aspx">残疾人</a></li>
                    </ul>
                    </div>
                    
                    <div class="line"><img src="/Template/Default/Skin/img/line.png" /></div>
                    <div class="tab4" style="width: 417px;">
            <ul class="tab-hd4">
<li>个人办事 </li><li>法人办事 </li><li>行政审批</li>
                      </ul>
                 
                      <ul class="tab-bd4">
                <li>
              <a   href="http://ycja.jxzwfww.gov.cn/jazwfw/grbs_list.jspx?zhuti=婚姻&amp;zhutiorbumentext=婚　　姻&amp;service_object=0"
                    title="婚　　姻">婚 姻</a>
                <a   href="http://ycja.jxzwfww.gov.cn/jazwfw/grbs_list.jspx?zhuti=生育收养&amp;zhutiorbumentext=生育收养&amp;service_object=0"
                    title="生育收养">生育收养</a>
                <a   href="http://ycja.jxzwfww.gov.cn/jazwfw/grbs_list.jspx?zhuti=退休&amp;zhutiorbumentext=退　　休&amp;service_object=0"
                    title="退　　休">退 休</a>
                <a  href="http://ycja.jxzwfww.gov.cn/jazwfw/grbs_list.jspx?zhuti=公安&amp;zhutiorbumentext=公　　安&amp;service_object=0"
                    title="公　　安">公 安</a>
                <a  href="http://ycja.jxzwfww.gov.cn/jazwfw/grbs_list.jspx?zhuti=兵役&amp;zhutiorbumentext=兵　　役&amp;service_object=0"
                    title="兵　　役">兵 役</a>
                <a  href="http://ycja.jxzwfww.gov.cn/jazwfw/grbs_list.jspx?zhuti=环境气象&amp;zhutiorbumentext=环境气象&amp;service_object=0"
                    title="环境气象">环境气象</a>
                <a  href="http://ycja.jxzwfww.gov.cn/jazwfw/grbs_list.jspx?zhuti=司法公证&amp;zhutiorbumentext=司法公证&amp;service_object=0"
                    title="司法公证">司法公证</a>
                <a  href="http://ycja.jxzwfww.gov.cn/jazwfw/grbs_list.jspx?zhuti=消费维权&amp;zhutiorbumentext=消费维权&amp;service_object=0"
                    title="消费维权">消费维权</a>
                <a  href="http://ycja.jxzwfww.gov.cn/jazwfw/grbs_list.jspx?zhuti=知识产权&amp;zhutiorbumentext=知识产权&amp;service_object=0"
                    title="知识产权">知识产权</a>
                <a  href="http://ycja.jxzwfww.gov.cn/jazwfw/grbs_list.jspx?zhuti=职业资格&amp;zhutiorbumentext=职业资格&amp;service_object=0"
                    title="职业资格">职业资格</a>
                <a  href="http://ycja.jxzwfww.gov.cn/jazwfw/grbs_list.jspx?zhuti=纳税缴费&amp;zhutiorbumentext=纳税缴费&amp;service_object=0"
                    title="纳税缴费">纳税缴费</a>
                <a  href="http://ycja.jxzwfww.gov.cn/jazwfw/grbs_list.jspx?zhuti=出境入境&amp;zhutiorbumentext=出境入境&amp;service_object=0"
                    title="出境入境">出境入境</a>
                <a  href="http://ycja.jxzwfww.gov.cn/jazwfw/grbs_list.jspx?zhuti=医疗卫生&amp;zhutiorbumentext=医疗卫生&amp;service_object=0"
                    title="医疗卫生">医疗卫生</a>
                <a  href="http://ycja.jxzwfww.gov.cn/jazwfw/grbs_list.jspx?zhuti=住房&amp;zhutiorbumentext=住　　房&amp;service_object=0"
                    title="住　　房">住 房</a>
                <a  href="http://ycja.jxzwfww.gov.cn/jazwfw/grbs_list.jspx?zhuti=教育科研&amp;zhutiorbumentext=教育科研&amp;service_object=0"
                    title="教育科研">教育科研</a>
                <a  href="http://ycja.jxzwfww.gov.cn/jazwfw/grbs_list.jspx?zhuti=死亡殡葬&amp;zhutiorbumentext=死亡殡葬&amp;service_object=0"
                    title="死亡殡葬">死亡殡葬</a>
                <a  href="http://ycja.jxzwfww.gov.cn/jazwfw/grbs_list.jspx?zhuti=社保救助&amp;zhutiorbumentext=社保救助&amp;service_object=0"
                    title="社保救助">社保救助</a>
                <a  href="http://ycja.jxzwfww.gov.cn/jazwfw/grbs_list.jspx?zhuti=证件证明&amp;zhutiorbumentext=证件证明&amp;service_object=0"
                    title="证件证明">证件证明</a>
                <a  href="http://ycja.jxzwfww.gov.cn/jazwfw/grbs_list.jspx?zhuti=其他&amp;zhutiorbumentext=其　　他&amp;service_object=0"
                    title="其　　他">其 他</a>

                
                
                <div style=" clear:both;"></div>
                
                </li>
                
                
                <li>    <a  href="http://ycja.jxzwfww.gov.cn/jazwfw/grbs_list.jspx?zhuti=设立变更&amp;zhutiorbumentext=设立变更&amp;service_object=1"
                    title="设立变更">设立变更</a>
                <a  href="http://ycja.jxzwfww.gov.cn/jazwfw/grbs_list.jspx?zhuti=准营准办&amp;zhutiorbumentext=准营准办&amp;service_object=1"
                    title="准营准办">准营准办</a>
                <a  href="http://ycja.jxzwfww.gov.cn/jazwfw/grbs_list.jspx?zhuti=投资审批&amp;zhutiorbumentext=投资审批&amp;service_object=1"
                    title="投资审批">投资审批</a>
                <a  href="http://ycja.jxzwfww.gov.cn/jazwfw/grbs_list.jspx?zhuti=资质认证&amp;zhutiorbumentext=资质认证&amp;service_object=1"
                    title="资质认证">资质认证</a>
                <a  href="http://ycja.jxzwfww.gov.cn/jazwfw/grbs_list.jspx?zhuti=年检延续&amp;zhutiorbumentext=年检延续&amp;service_object=1"
                    title="年检延续">年检延续</a>
                <a  href="http://ycja.jxzwfww.gov.cn/jazwfw/grbs_list.jspx?zhuti=人力社保&amp;zhutiorbumentext=人力社保&amp;service_object=1"
                    title="人力社保">人力社保</a>
                <a  href="http://ycja.jxzwfww.gov.cn/jazwfw/grbs_list.jspx?zhuti=医药卫生&amp;zhutiorbumentext=医药卫生&amp;service_object=1"
                    title="医药卫生">医药卫生</a>
                <a  href="http://ycja.jxzwfww.gov.cn/jazwfw/grbs_list.jspx?zhuti=教育科技&amp;zhutiorbumentext=教育科技&amp;service_object=1"
                    title="教育科技">教育科技</a>
                <a  href="http://ycja.jxzwfww.gov.cn/jazwfw/grbs_list.jspx?zhuti=文化体育&amp;zhutiorbumentext=文化体育&amp;service_object=1"
                    title="文化体育">文化体育</a>
                <a  href="http://ycja.jxzwfww.gov.cn/jazwfw/grbs_list.jspx?zhuti=出版广电&amp;zhutiorbumentext=出版广电&amp;service_object=1"
                    title="出版广电">出版广电</a>
                <a  href="http://ycja.jxzwfww.gov.cn/jazwfw/grbs_list.jspx?zhuti=文物保护&amp;zhutiorbumentext=文物保护&amp;service_object=1"
                    title="文物保护">文物保护</a>
                <a  href="http://ycja.jxzwfww.gov.cn/jazwfw/grbs_list.jspx?zhuti=交通运输&amp;zhutiorbumentext=交通运输&amp;service_object=1"
                    title="交通运输">交通运输</a>
                <a  href="http://ycja.jxzwfww.gov.cn/jazwfw/grbs_list.jspx?zhuti=环保绿化&amp;zhutiorbumentext=环保绿化&amp;service_object=1"
                    title="环保绿化">环保绿化</a>
                <a  href="http://ycja.jxzwfww.gov.cn/jazwfw/grbs_list.jspx?zhuti=国土建设&amp;zhutiorbumentext=国土建设&amp;service_object=1"
                    title="国土建设">国土建设</a>
                <a  href="http://ycja.jxzwfww.gov.cn/jazwfw/grbs_list.jspx?zhuti=工业生产&amp;zhutiorbumentext=工业生产&amp;service_object=1"
                    title="工业生产">工业生产</a>
                <a  href="http://ycja.jxzwfww.gov.cn/jazwfw/grbs_list.jspx?zhuti=信息产业&amp;zhutiorbumentext=信息产业&amp;service_object=1"
                    title="信息产业">信息产业</a>
                <a  href="http://ycja.jxzwfww.gov.cn/jazwfw/grbs_list.jspx?zhuti=知识产权&amp;zhutiorbumentext=知识产权&amp;service_object=1"
                    title="知识产权">知识产权</a>
                <a  href="http://ycja.jxzwfww.gov.cn/jazwfw/grbs_list.jspx?zhuti=税费财务&amp;zhutiorbumentext=税费财务&amp;service_object=1"
                    title="税费财务">税费财务</a>
                <a  href="http://ycja.jxzwfww.gov.cn/jazwfw/grbs_list.jspx?zhuti=安全防护&amp;zhutiorbumentext=安全防护&amp;service_object=1"
                    title="安全防护">安全防护</a>
                <a  href="http://ycja.jxzwfww.gov.cn/jazwfw/grbs_list.jspx?zhuti=质量标准&amp;zhutiorbumentext=质量标准&amp;service_object=1"
                    title="质量标准">质量标准</a>
                <a  href="http://ycja.jxzwfww.gov.cn/jazwfw/grbs_list.jspx?zhuti=公安消防&amp;zhutiorbumentext=公安消防&amp;service_object=1"
                    title="公安消防">公安消防</a>
                <a  href="http://ycja.jxzwfww.gov.cn/jazwfw/grbs_list.jspx?zhuti=司法公证&amp;zhutiorbumentext=司法公证&amp;service_object=1"
                    title="司法公证">司法公证</a>
                <a  href="http://ycja.jxzwfww.gov.cn/jazwfw/grbs_list.jspx?zhuti=涉外服务&amp;zhutiorbumentext=涉外服务&amp;service_object=1"
                    title="涉外服务">涉外服务</a>
                <a  href="http://ycja.jxzwfww.gov.cn/jazwfw/grbs_list.jspx?zhuti=民族宗教&amp;zhutiorbumentext=民族宗教&amp;service_object=1"
                    title="民族宗教">民族宗教</a>
                <a  href="http://ycja.jxzwfww.gov.cn/jazwfw/grbs_list.jspx?zhuti=农林牧渔&amp;zhutiorbumentext=农林牧渔&amp;service_object=1"
                    title="农林牧渔">农林牧渔</a>
                <a  href="http://ycja.jxzwfww.gov.cn/jazwfw/grbs_list.jspx?zhuti=水利水务&amp;zhutiorbumentext=水利水务&amp;service_object=1"
                    title="水利水务">水利水务</a>
                <a  href="http://ycja.jxzwfww.gov.cn/jazwfw/grbs_list.jspx?zhuti=其他&amp;zhutiorbumentext=其　　他&amp;service_object=1"
                    title="其　　他">其 他</a>

                
                <div style=" clear:both;"></div></li>
                
                
                <li>    <a  href="http://ycja.jxzwfww.gov.cn/jazwfw/grbs_list.jspx?bumen=360925000201020000&amp;zhutiorbumentext=县物价局&amp;service_object=2"
                        title="靖安县物价局">县物价局</a>
                    <a  href="http://ycja.jxzwfww.gov.cn/jazwfw/grbs_list.jspx?bumen=360925000602032002&amp;zhutiorbumentext=县交警大队&amp;service_object=2"
                        title="靖安县交警大队">县交警大队</a>
                    <a  href="http://ycja.jxzwfww.gov.cn/jazwfw/grbs_list.jspx?bumen=360925000602050000&amp;zhutiorbumentext=县中行&amp;service_object=2"
                        title="中国人民银行靖安县支行">县中行</a>
                    <a  href="http://ycja.jxzwfww.gov.cn/jazwfw/grbs_list.jspx?bumen=360925000201018000&amp;zhutiorbumentext=县水产局&amp;service_object=2"
                        title="靖安县畜牧水产局">县水产局</a>
                    <a  href="http://ycja.jxzwfww.gov.cn/jazwfw/grbs_list.jspx?bumen=360925000201026000&amp;zhutiorbumentext=县城建局&amp;service_object=2"
                        title="靖安县规划建设局">县城建局</a>
                    <a  href="http://ycja.jxzwfww.gov.cn/jazwfw/grbs_list.jspx?bumen=360925000602053000&amp;zhutiorbumentext=县服务业办&amp;service_object=2"
                        title="靖安县服务业办">县服务业办</a>
                    <a  href="http://ycja.jxzwfww.gov.cn/jazwfw/grbs_list.jspx?bumen=360925000201004000&amp;zhutiorbumentext=县市监局&amp;service_object=2"
                        title="靖安县质量技术监督局">县市监局</a>
                    <a  href="http://ycja.jxzwfww.gov.cn/jazwfw/grbs_list.jspx?bumen=360925000602056000&amp;zhutiorbumentext=县农机局&amp;service_object=2"
                        title="靖安县农业机械管理局">县农机局</a>
                    <a  href="http://ycja.jxzwfww.gov.cn/jazwfw/grbs_list.jspx?bumen=360925000201030000&amp;zhutiorbumentext=县地税局&amp;service_object=2"
                        title="靖安县地方税务局">县地税局</a>
                    <a  href="http://ycja.jxzwfww.gov.cn/jazwfw/grbs_list.jspx?bumen=360925000201025000&amp;zhutiorbumentext=县水务局&amp;service_object=2"
                        title="靖安县水利局">县水务局</a>
                    <a  href="http://ycja.jxzwfww.gov.cn/jazwfw/grbs_list.jspx?bumen=360925000201010000&amp;zhutiorbumentext=县安监局&amp;service_object=2"
                        title="靖安县安全生产监督管理局">县安监局</a>
                    <a  href="http://ycja.jxzwfww.gov.cn/jazwfw/grbs_list.jspx?bumen=360925000602024000&amp;zhutiorbumentext=县人防办&amp;service_object=2"
                        title="靖安县政府人民防空办公室">县人防办</a>
                    <a  href="http://ycja.jxzwfww.gov.cn/jazwfw/grbs_list.jspx?bumen=360925000459043000&amp;zhutiorbumentext=县石油公司&amp;service_object=2"
                        title="靖安县石油公司">县石油公司</a>
                    <a  href="http://ycja.jxzwfww.gov.cn/jazwfw/grbs_list.jspx?bumen=360925000602001000&amp;zhutiorbumentext=县服务中心&amp;service_object=2"
                        title="靖安县行政服务中心">县服务中心</a>
                    <a  href="http://ycja.jxzwfww.gov.cn/jazwfw/grbs_list.jspx?bumen=360925000602023000&amp;zhutiorbumentext=县防减局&amp;service_object=2"
                        title="靖安县防震减灾局">县防减局</a>
                    <a  href="http://ycja.jxzwfww.gov.cn/jazwfw/grbs_list.jspx?bumen=360925000201007000&amp;zhutiorbumentext=县卫计委&amp;service_object=2"
                        title="靖安县卫生和计划生育委员会">县卫计委</a>
                     
                    <a  href="http://ycja.jxzwfww.gov.cn/jazwfw/grbs_list.jspx?bumen=360925000602029000&amp;zhutiorbumentext=县残联&amp;service_object=2"
                        title="靖安县残疾人联合会">县残联</a>
                    <a  href="http://ycja.jxzwfww.gov.cn/jazwfw/grbs_list.jspx?bumen=360925000459041000&amp;zhutiorbumentext=县供电公司&amp;service_object=2"
                        title="靖安县供电公司">县供电公司</a>
                    <a  href="http://ycja.jxzwfww.gov.cn/jazwfw/grbs_list.jspx?bumen=360925000201009000&amp;zhutiorbumentext=县房管局&amp;service_object=2"
                        title="靖安县房管局">县房管局</a>
                    <a  href="http://ycja.jxzwfww.gov.cn/jazwfw/grbs_list.jspx?bumen=360925000101038000&amp;zhutiorbumentext=县农工部&amp;service_object=2"
                        title="靖安县农村工作部">县农工部</a>
                    <a  href="http://ycja.jxzwfww.gov.cn/jazwfw/grbs_list.jspx?bumen=360925000201012000&amp;zhutiorbumentext=县教育局&amp;service_object=2"
                        title="靖安县教育局">县教育局</a>
                    <a  href="http://ycja.jxzwfww.gov.cn/jazwfw/grbs_list.jspx?bumen=360925000201034000&amp;zhutiorbumentext=县文广新局&amp;service_object=2"
                        title="靖安县文化广电新闻出版局">县文广新局</a>
                    <a  href="http://ycja.jxzwfww.gov.cn/jazwfw/grbs_list.jspx?bumen=360925000201006000&amp;zhutiorbumentext=县交通局&amp;service_object=2"
                        title="靖安县交通运输局">县交通局</a>
                    <a  href="http://ycja.jxzwfww.gov.cn/jazwfw/grbs_list.jspx?bumen=360925000459048000&amp;zhutiorbumentext=县联通&amp;service_object=2"
                        title="联通靖安分公司">县联通</a>
                    <a  href="http://ycja.jxzwfww.gov.cn/jazwfw/grbs_list.jspx?bumen=360925000201005000&amp;zhutiorbumentext=县环保局&amp;service_object=2"
                        title="靖安县环境保护局">县环保局</a>
                    <a  href="http://ycja.jxzwfww.gov.cn/jazwfw/grbs_list.jspx?bumen=360925000602049000&amp;zhutiorbumentext=县民宗局&amp;service_object=2"
                        title="靖安县民族宗教事务局">县民宗局</a>
                    <a  href="http://ycja.jxzwfww.gov.cn/jazwfw/grbs_list.jspx?bumen=360925000602032001&amp;zhutiorbumentext=县消防大队&amp;service_object=2"
                        title="靖安县消防大队">县消防大队</a>
                    <a  href="http://ycja.jxzwfww.gov.cn/jazwfw/grbs_list.jspx?bumen=360925000602015000&amp;zhutiorbumentext=县气象局&amp;service_object=2"
                        title="靖安县气象局">县气象局</a>
                    <a  href="http://ycja.jxzwfww.gov.cn/jazwfw/grbs_list.jspx?bumen=360925000602036000&amp;zhutiorbumentext=县旅发委&amp;service_object=2"
                        title="靖安县旅游发展委员会">县旅发委</a>
                    <a  href="http://ycja.jxzwfww.gov.cn/jazwfw/grbs_list.jspx?bumen=360925000201032000&amp;zhutiorbumentext=县公安局&amp;service_object=2"
                        title="靖安县公安局">县公安局</a>
                    <a  href="http://ycja.jxzwfww.gov.cn/jazwfw/grbs_list.jspx?bumen=360925000201017000&amp;zhutiorbumentext=县农业局&amp;service_object=2"
                        title="靖安县农业局">县农业局</a>
                    <a  href="http://ycja.jxzwfww.gov.cn/jazwfw/grbs_list.jspx?bumen=360925000459046000&amp;zhutiorbumentext=县电信公司&amp;service_object=2"
                        title="电信靖安分公司">县电信公司</a>
                    <a  href="http://ycja.jxzwfww.gov.cn/jazwfw/grbs_list.jspx?bumen=360925000201014000&amp;zhutiorbumentext=县人保局&amp;service_object=2"
                        title="靖安县人力资源和社会保障局">县人保局</a>
                    <a  href="http://ycja.jxzwfww.gov.cn/jazwfw/grbs_list.jspx?bumen=360925000201027000&amp;zhutiorbumentext=县工信委&amp;service_object=2"
                        title="靖安县工业和信息化委员会">县工信委</a>
                    <a  href="http://ycja.jxzwfww.gov.cn/jazwfw/grbs_list.jspx?bumen=360925000201011000&amp;zhutiorbumentext=县国土局&amp;service_object=2"
                        title="靖安县国土资源局">县国土局</a>
                    <a  href="http://ycja.jxzwfww.gov.cn/jazwfw/grbs_list.jspx?bumen=360925000201003000&amp;zhutiorbumentext=县发改委&amp;service_object=2"
                        title="靖安县发展和改革委员会">县发改委</a>
                    <a  href="http://ycja.jxzwfww.gov.cn/jazwfw/grbs_list.jspx?bumen=360925000201016000&amp;zhutiorbumentext=县民政局&amp;service_object=2"
                        title="靖安县民政局">县民政局</a>
                    <a  href="http://ycja.jxzwfww.gov.cn/jazwfw/grbs_list.jspx?bumen=360925000201019000&amp;zhutiorbumentext=县粮食局&amp;service_object=2"
                        title="靖安县粮食局">县粮食局</a>
                    <a  href="http://ycja.jxzwfww.gov.cn/jazwfw/grbs_list.jspx?bumen=360925000201021000&amp;zhutiorbumentext=县财政局&amp;service_object=2"
                        title="靖安县财政局">县财政局</a>
                    <a  href="http://ycja.jxzwfww.gov.cn/jazwfw/grbs_list.jspx?bumen=360925000602044000&amp;zhutiorbumentext=县公路局&amp;service_object=2"
                        title="靖安县公路管理局">县公路局</a>
                    <a  href="http://ycja.jxzwfww.gov.cn/jazwfw/grbs_list.jspx?bumen=360925000501013000&amp;zhutiorbumentext=县城管局&amp;service_object=2"
                        title="靖安县城市管理综合行政执法局">县城管局</a>
                    <a  href="http://ycja.jxzwfww.gov.cn/jazwfw/grbs_list.jspx?bumen=360925000602033000&amp;zhutiorbumentext=县商务局&amp;service_object=2"
                        title="靖安县商务局">县商务局</a>

                
                <div style=" clear:both;"></div></li>
                
                
                
          </ul>
               
                      </div>
                      
                            <div class="line"><img src="/Template/Default/Skin/img/line.png" /></div>
                            
                       <div class="xol-2">
                       	 <div class="xol-21"><img src="/Template/Default/Skin/img/con4.png" /><h4>办件公示</h4></div>
                  		<div class="xol-22">
                  			<span>受理事件</span><span>办件状态</span>
                  		<div class="xol-22-left">
                  			<ul>
                  				 <li><a href="&#xD;&#xA;							/Government/Letter/LetterView.aspx?LetterId=691" title="举报仁首团结村棚二组刘贤梅大肆侵占基本农田大肆建房和填埋">举报仁首团结村棚二…</a></li>
<li><a href="&#xD;&#xA;							/Government/Letter/LetterView.aspx?LetterId=687" title="投诉举报函">投诉举报函</a></li>
<li><a href="&#xD;&#xA;							/Government/Letter/LetterView.aspx?LetterId=678" title="为县政府大力治理商城周边非法占道经营点赞">为县政府大力治理商…</a></li>
<li><a href="&#xD;&#xA;							/Government/Letter/LetterView.aspx?LetterId=672" title="关于昌铜高速靖安至南昌西和昌北机场往返免费通行">关于昌铜高速靖安至…</a></li>
                  			</ul>
                  		</div>
                  			<div class="xol-22-right">
                  			<ul>
                  				<li>
						已处理完
					</li>
<li>
						已处理完
					</li>
<li>
						已处理完
					</li>
<li>
						已处理完
					</li>
                  			</ul>
                  	</div>
                  		</div>
                       	
                       	 <div class="xol-23"><img src="/Template/Default/Skin/img/con4.png" /><h4>办件统计</h4></div>
                       	<div class="xol-23-1"><span>本月收件：6件</span><span>本月办结：0件</span></div>
<div class="xol-23-1"><span>累计收件：491件</span><span>累计办结：447件</span></div>
                       	 
                       	   	 <div class="xol-23-2"><span><a target="_blank" href="http://ycja.jxzwfww.gov.cn/jazwfw/ygzwNew.jspx">行政权力清单</a></span>
                             <span><a target="_blank" href="http://ycja.jxzwfww.gov.cn/jazwfw/ygzw_bmzrNew.jspx">部门责任清单</a></span> </div>
                       	 <div class="xol-23-2"><span> <a target="_blank" href="http://ycja.jxzwfww.gov.cn/jazwfw/ygzw_sczrNew.jspx">市场准入清单</a></span>
                         <span> <a target="_blank" href="http://ycja.jxzwfww.gov.cn/jazwfw/ygzw_xzsyNew.jspx">行政事业性收费清单</a></span> </div>
                       </div>     
                          <div class="line"><img src="/Template/Default/Skin/img/line.png" /></div>
                          
                     <div class="xol-3">
                     	<ul>
                     		<li><a href="/Category_236/Index.aspx">通知公告</a></li>
                     		<li><a target="_blank" href="http://www.jxzwfww.gov.cn/bmfw/">热门服务</a></li>
                     		<li><a target="_blank" href="http://www.jxzwfww.gov.cn/qa/">智能问答</a></li>
                     		<li><a target="_blank" href="http://www.jxzwfww.gov.cn/zx/">我要咨询</a></li>
                     		<li><a target="_blank" href="http://www.jxzwfww.gov.cn/wycx/">我要查询</a></li>
                     		<li><a target="_blank" href="http://www.jxzwfww.gov.cn/ts/">我要投诉</a></li>
                     		
                     	</ul>
                     	
                     </div>
                </div>
            </li>
            <li class="navqhnma" id="m5"><a class="ne" href="/Category_14/Index.aspx">政民互动 </a>
                <div class="sub"  style=" border:3px solid #0D7DCA;">
                    <div class="col-1">
                        <div class="z-zjxd">
                            <div class="hd">
                                <h3>
                                    信件选登</h3>
                            </div>
                            <div class="bd">
                                <ul class="navLetterList">
<li class="th"><span class="sp_1">标题</span><span class="sp_2">信件状态</span><span class="sp_3">信件日期</span></li>
<li class="tr"><span class="date">2017-08-22</span><span class="title"><a href="/Government/Letter/LetterView.aspx?LetterId=691" title="举报仁首团结村棚二组刘贤梅大肆侵占基本农田大肆建房和填埋">举报仁首团结村棚二组刘贤梅大肆侵占基本农田大肆建…</a></span><span class="state"><i class="s1" style="font-style: normal;">
                       已处理完
                    </i></span></li>
<li class="tr"><span class="date">2017-08-15</span><span class="title"><a href="/Government/Letter/LetterView.aspx?LetterId=687" title="投诉举报函">投诉举报函</a></span><span class="state"><i class="s1" style="font-style: normal;">
                       已处理完
                    </i></span></li>
<li class="tr"><span class="date">2017-07-18</span><span class="title"><a href="/Government/Letter/LetterView.aspx?LetterId=678" title="为县政府大力治理商城周边非法占道经营点赞">为县政府大力治理商城周边非法占道经营点赞</a></span><span class="state"><i class="s1" style="font-style: normal;">
                       已处理完
                    </i></span></li>
<li class="tr"><span class="date">2017-06-25</span><span class="title"><a href="/Government/Letter/LetterView.aspx?LetterId=672" title="关于昌铜高速靖安至南昌西和昌北机场往返免费通行">关于昌铜高速靖安至南昌西和昌北机场往返免费通行</a></span><span class="state"><i class="s1" style="font-style: normal;">
                       已处理完
                    </i></span></li>
<li class="tr"><span class="date">2017-06-20</span><span class="title"><a href="/Government/Letter/LetterView.aspx?LetterId=670" title="解决村民喝水问题">解决村民喝水问题</a></span><span class="state"><i class="s1" style="font-style: normal;">
                       已处理完
                    </i></span></li>
<li class="tr"><span class="date">2017-06-15</span><span class="title"><a href="/Government/Letter/LetterView.aspx?LetterId=666" title="无房证明开具资料">无房证明开具资料</a></span><span class="state"><i class="s1" style="font-style: normal;">
                       已处理完
                    </i></span></li>
<li class="tr"><span class="date">2017-05-30</span><span class="title"><a href="/Government/Letter/LetterView.aspx?LetterId=663" title="请问2017年公租房何时开始申请">请问2017年公租房何时开始申请</a></span><span class="state"><i class="s1" style="font-style: normal;">
                       已处理完
                    </i></span></li>
<li class="tr"><span class="date">2017-05-26</span><span class="title"><a href="/Government/Letter/LetterView.aspx?LetterId=661" title="商城大润发超市音响严重扰民">商城大润发超市音响严重扰民</a></span><span class="state"><i class="s1" style="font-style: normal;">
                       已处理完
                    </i></span></li>
                                   
                                </ul>
                            </div>
                        </div>
                        <div class="z-wyxx">
                            <ul>
                                <li class="a1"><a href="/government/letter/letterwriter.aspx?LetterTypeId=6&DepartmentId=220"
                                    target="_blank"><span></span>我要写信</a></li>
                                <li class="a2"><a href="/Government/Letter/LetterQuery.aspx"  target="_blank"><span></span>进度查询</a></li>
                                <li class="a3"><a href="/Category_312/Index.aspx" target="_blank"><span></span>民意征集</a></li>
                            </ul>
                        </div>
                    </div>
                    <div class="col-2">
                        <div class="z-zxft">
                            <div class="hd">
                                <h3>
                                    在线访谈</h3>
                            </div>
                            <div class="bd">
                                <ul>
 <li class="pic"><a href="&#xD;&#xA;								/Government/Interview/Interview.aspx?InterviewId=13">
<img src="/UploadFiles/2017/7/201707271752218964.jpg" border="0" width="275" height="195">
</a></li>
<li class="ft_li">
访谈主题：大众创业 万众创新</li>
<li class="ft_li">
访谈时间： 2017年07月27日 16时(星期四)
</li>

                                   
                                </ul>
                            </div>
                        </div>
                    </div>
                </div>
            </li>
             <li class="navqhnma"  ><a class="ne" href="/Category_655/Index.aspx">数据共享</a></li>
        </ul>
        <div class="tqyb">
            <iframe width="200" scrolling="no" height="60" frameborder="0" allowtransparency="true"
                src="http://i.tianqi.com/index.php?c=code&id=12&color=%230070C0&icon=3&py=jingan&num=5">
            </iframe>
        </div>
    </div>
    <!--top close -->

 
<!--top close -->

<!--main start -->
	

	<div id="contentpage">
		<div class="path">您当前位置<a href="http://www.jxjaxzf.gov.cn">靖安县人民政府网站</a>>>
    
    
    
    <a href="/Category_108/Index.aspx" target="_self">走进靖安</a>&gt;&gt;
    <a href="/Category_132/Index.aspx" target="_self">靖安新闻</a>&gt;&gt;
    <a href="/Category_133/Index.aspx" target="_self">政务要闻</a></div>
		<div id="mainpage">
			<div class="col-1">
				
		
		<div class="box mb10" id="box_menu">
			<div class="hd"><h3><a href="/Category_133/Index.aspx">政务要闻</a></h3></div>
			<div class="bd">
				 
   <ul id="mainNavType3Ver" class="mainNavType3Ver" />     
     

			</div>
		</div>
		<script type="text/javascript">
		    if( jQuery("#box_menu .bd li").size()==0 ){ jQuery("#box_menu").hide() }
        jQuery("#box_menu .bd .hasUl1>.h1").append("<a class='trigger'>+</a>");
        jQuery("#box_menu .trigger").click(function(){
            var sub = $(this).parent().next("ul");
            if (sub.is(":visible")) {
                sub.stop(1,1).slideUp(200);
                $(this).html("+");
            } else {
                sub.stop(1,1).slideDown(200);
                $(this).html("-");
            }
        })
		</script>


					<div class="sideBox" id="side_hot">
  <div class="hd">
    <h3 class="title">热门排行</h3>
  </div>
  <div class="bd">
    <ul class="infoList infoListA">
         
            <li><a href="/Item/24067.aspx" target="_blank">我县保障性住房公开摇号、405户中低收入家庭喜…</a></li><li><a href="/Item/24066.aspx" target="_blank">广西天等县考察团到我县考察精准扶贫工作</a></li><li><a href="/Item/24064.aspx" target="_blank">我县广大干部群众收听收看十九大开幕式盛况</a></li><li><a href="/Item/24063.aspx" target="_blank">我县开展2017年扶贫日电商扶贫体验活动</a></li><li><a href="/Item/24059.aspx" target="_blank">我县获评2016年度市县科学发展综合考核评价先…</a></li><li><a href="/Item/24054.aspx" target="_blank">县人大开展城区备用水源调研工作</a></li><li><a href="/Item/24053.aspx" target="_blank">“田野牧歌•仁首老家”在周末大舞台精彩演出</a></li><li><a href="/Item/24050.aspx" target="_blank">市委常委、组织部长蔡清平到我县督查安全生产…</a></li>
             
             
        </ul>
  </div>
</div>
			</div>
			<div class="col-2">
				<div id="mainCon">
					<div class="mHd">
						<h3 class="nodeName"><a href="/Category_133/Index.aspx">政务要闻</a></h3>
					</div>
					<div class="mBd">
						<!-- 正文内容 S -->
						<ul class="newsList infoListA">
	
            <li><span class="date">2017-10-20</span><a href="/Item/24067.aspx" target="_blank">我县保障性住房公开摇号、405户中低收入家庭喜圆住房梦</a></li><li><span class="date">2017-10-20</span><a href="/Item/24066.aspx" target="_blank">广西天等县考察团到我县考察精准扶贫工作</a></li><li><span class="date">2017-10-19</span><a href="/Item/24064.aspx" target="_blank">我县广大干部群众收听收看十九大开幕式盛况</a></li><li><span class="date">2017-10-18</span><a href="/Item/24063.aspx" target="_blank">我县开展2017年扶贫日电商扶贫体验活动</a></li><li class="split"></li><li><span class="date">2017-10-17</span><a href="/Item/24059.aspx" target="_blank">我县获评2016年度市县科学发展综合考核评价先进县称号</a></li><li><span class="date">2017-10-16</span><a href="/Item/24054.aspx" target="_blank">县人大开展城区备用水源调研工作</a></li><li><span class="date">2017-10-16</span><a href="/Item/24053.aspx" target="_blank">“田野牧歌•仁首老家”在周末大舞台精彩演出</a></li><li><span class="date">2017-10-13</span><a href="/Item/24050.aspx" target="_blank">市委常委、组织部长蔡清平到我县督查安全生产、社会稳…</a></li><li><span class="date">2017-10-12</span><a href="/Item/24047.aspx" target="_blank">全县当前重点工作调度会召开</a></li><li class="split"></li><li><span class="date">2017-10-11</span><a href="/Item/24039.aspx" target="_blank">县政府召开第十一次常务会议</a></li><li><span class="date">2017-10-10</span><a href="/Item/24037.aspx" target="_blank">我县成功入选“2017年度国家有机产品认证示范创建区”…</a></li><li><span class="date">2017-10-09</span><a href="/Item/24036.aspx" target="_blank">我县赵青、张远平夫妇荣登9月中国好人榜</a></li><li><span class="date">2017-10-09</span><a href="/Item/24031.aspx" target="_blank">省旅发委副主任陈晓平一行到我县开展双节期间旅游市场…</a></li><li><span class="date">2017-09-30</span><a href="/Item/24027.aspx" target="_blank">我县举行第四个全国烈士纪念日公祭活动</a></li><li class="split"></li><li><span class="date">2017-09-29</span><a href="/Item/24026.aspx" target="_blank">我县全面启动“国省干线路长制”建设</a></li><li><span class="date">2017-09-28</span><a href="/Item/24022.aspx" target="_blank">2017江西靖安第三届宝峰孝文化庙会即将启幕</a></li><li><span class="date">2017-09-28</span><a href="/Item/24016.aspx" target="_blank">我县义务教育均衡发展基本均衡顺利通过省级复查</a></li><li><span class="date">2017-09-27</span><a href="/Item/24013.aspx" target="_blank">我市对今年新上项目开展巡查</a></li><li><span class="date">2017-09-26</span><a href="/Item/24008.aspx" target="_blank">靖安(广州)精工制造（工程机械配套件）产业园专题招商…</a></li><li class="split"></li><li><span class="date">2017-09-25</span><a href="/Item/24005.aspx" target="_blank">全市安全生产工作电视电话会议召开</a></li>
          						
          
						</ul>
						<div class="page"><span id="pe100_page_通用信息列表_普通式列表" class="pagecss"><!--{pe.begin.pagination}--><style type="text/css">
/* Pager */
.pager { padding:3px; margin:3px;}
.pager A,.pager SPAN{display:block; float:left;margin-right:3px; height:20px; line-height:20px; }
.pager A,.pager A:active  {display:block; float:left;border:1px solid #c5c5c5; color:#1485ff; padding:0 6px;}
.pager A:hover {border:1px solid #0099FF; text-decoration:none; color:#c00;}
.pager SPAN.current {background:#1485ff; border:1px solid #1485ff; color:#fff; font-weight:bold; padding:0 6px; }
.pager SPAN.disabled {border:1px solid #c5c5c5;  padding:0 6px; color:#c0c0c0;}
</style>
<script type="text/javascript" language="javascript">
function listPage_Jumpto通用信息列表_普通式列表(e,ele){
e=e||event;
if(13==e.keyCode){
var i=Number(ele.value);
if(i<1||i>120){alert("你输入的页码超出范围。");}
switch(i){
case 1: break; case 2: location='Index_2.aspx';break; case 3: location='Index_3.aspx';break; case 4: location='Index_4.aspx';break; case 5: location='Index_5.aspx';break; case 6: location='Index_6.aspx';break; case 7: location='Index_7.aspx';break; case 8: location='Index_8.aspx';break; case 9: location='Index_9.aspx';break; case 10: location='Index_10.aspx';break; case 11: location='Index_11.aspx';break; case 12: location='Index_12.aspx';break; case 13: location='Index_13.aspx';break; case 14: location='Index_14.aspx';break; case 15: location='Index_15.aspx';break; case 16: location='Index_16.aspx';break; case 17: location='Index_17.aspx';break; case 18: location='Index_18.aspx';break; case 19: location='Index_19.aspx';break; case 20: location='Index_20.aspx';break; case 21: location='Index_21.aspx';break; case 22: location='Index_22.aspx';break; case 23: location='Index_23.aspx';break; case 24: location='Index_24.aspx';break; case 25: location='Index_25.aspx';break; case 26: location='Index_26.aspx';break; case 27: location='Index_27.aspx';break; case 28: location='Index_28.aspx';break; case 29: location='Index_29.aspx';break; case 30: location='Index_30.aspx';break; case 31: location='Index_31.aspx';break; case 32: location='Index_32.aspx';break; case 33: location='Index_33.aspx';break; case 34: location='Index_34.aspx';break; case 35: location='Index_35.aspx';break; case 36: location='Index_36.aspx';break; case 37: location='Index_37.aspx';break; case 38: location='Index_38.aspx';break; case 39: location='Index_39.aspx';break; case 40: location='Index_40.aspx';break; case 41: location='Index_41.aspx';break; case 42: location='Index_42.aspx';break; case 43: location='Index_43.aspx';break; case 44: location='Index_44.aspx';break; case 45: location='Index_45.aspx';break; case 46: location='Index_46.aspx';break; case 47: location='Index_47.aspx';break; case 48: location='Index_48.aspx';break; case 49: location='Index_49.aspx';break; case 50: location='Index_50.aspx';break; case 51: location='Index_51.aspx';break; case 52: location='Index_52.aspx';break; case 53: location='Index_53.aspx';break; case 54: location='Index_54.aspx';break; case 55: location='Index_55.aspx';break; case 56: location='Index_56.aspx';break; case 57: location='Index_57.aspx';break; case 58: location='Index_58.aspx';break; case 59: location='Index_59.aspx';break; case 60: location='Index_60.aspx';break; case 61: location='Index_61.aspx';break; case 62: location='Index_62.aspx';break; case 63: location='Index_63.aspx';break; case 64: location='Index_64.aspx';break; case 65: location='Index_65.aspx';break; case 66: location='Index_66.aspx';break; case 67: location='Index_67.aspx';break; case 68: location='Index_68.aspx';break; case 69: location='Index_69.aspx';break; case 70: location='Index_70.aspx';break; case 71: location='Index_71.aspx';break; case 72: location='Index_72.aspx';break; case 73: location='Index_73.aspx';break; case 74: location='Index_74.aspx';break; case 75: location='Index_75.aspx';break; case 76: location='Index_76.aspx';break; case 77: location='Index_77.aspx';break; case 78: location='Index_78.aspx';break; case 79: location='Index_79.aspx';break; case 80: location='Index_80.aspx';break; case 81: location='Index_81.aspx';break; case 82: location='Index_82.aspx';break; case 83: location='Index_83.aspx';break; case 84: location='Index_84.aspx';break; case 85: location='Index_85.aspx';break; case 86: location='Index_86.aspx';break; case 87: location='Index_87.aspx';break; case 88: location='Index_88.aspx';break; case 89: location='Index_89.aspx';break; case 90: location='Index_90.aspx';break; case 91: location='Index_91.aspx';break; case 92: location='Index_92.aspx';break; case 93: location='Index_93.aspx';break; case 94: location='Index_94.aspx';break; case 95: location='Index_95.aspx';break; case 96: location='Index_96.aspx';break; case 97: location='Index_97.aspx';break; case 98: location='Index_98.aspx';break; case 99: location='Index_99.aspx';break; case 100: location='Index_100.aspx';break; case 101: location='Index_101.aspx';break; case 102: location='Index_102.aspx';break; case 103: location='Index_103.aspx';break; case 104: location='Index_104.aspx';break; case 105: location='Index_105.aspx';break; case 106: location='Index_106.aspx';break; case 107: location='Index_107.aspx';break; case 108: location='Index_108.aspx';break; case 109: location='Index_109.aspx';break; case 110: location='Index_110.aspx';break; case 111: location='Index_111.aspx';break; case 112: location='Index_112.aspx';break; case 113: location='Index_113.aspx';break; case 114: location='Index_114.aspx';break; case 115: location='Index_115.aspx';break; case 116: location='Index_116.aspx';break; case 117: location='Index_117.aspx';break; case 118: location='Index_118.aspx';break; case 119: location='Index_119.aspx';break; case 120: location='Index_120.aspx';break; 
default: break;
}
}
}
</script>
<div class="pager">
 <a href="Index.aspx">首页</a>
 <a href="Index.aspx">上一页</a>
 <span class="current">1</span> <a href="Index_2.aspx">2</a> <a href="Index_3.aspx">3</a> <a href="Index_4.aspx">4</a> <a href="Index_5.aspx">5</a> <a href="Index_6.aspx">6</a> <a href="Index_7.aspx">7</a> 
<a href="Index_2.aspx">下一页</a>
 <a href="Index_120.aspx">尾页</a>
<input type="text" value="1" onkeydown="listPage_Jumpto通用信息列表_普通式列表(event,this)" size="3" title="输入数字，回车跳转" style="width:18px;float:left;margin-right:3px;"/>
<span class="disabled">共2397篇文章/共120页</span>
</div><!--{pe.end.pagination}--></span></div>
						<!-- 正文内容 E -->
					</div>
				</div>
			</div>
		</div>
				
	</div>
	<!-- /#content -->
<!--main close -->

<!--foot start -->
<script type="text/javascript" src='/IAA/201411/5.js'></script>
   <div id="footer">
        <div class="footLink">
            <div class="siteWidth">
                <a href="javascript:void(0);" onclick="SetHome(this,'');">设为首页</a>
                <span class="spe">|</span> <a href="javascript:void(0);" onclick="AddFavorite('靖安县政府门户','')">
                    收藏本站</a> <span class="spe">|</span> <a href="/Category_492/Index.aspx">联系我们</a> <span class="spe">
                        |</span> <a href="/Category_485/Index.aspx">网站地图</a> <span class="spe">
                        |</span><a href="/Category_490/Index.aspx" target="_blank"> 隐私条款</a> <span class="spe">|</span>
                <a href="/Category_491/Index.aspx" target="_blank">版权声明</a> 
            </div>
        </div>
        <div class="copyright">
            <div class="siteWidth">
              主办：靖安县人民政府   
承办：靖安县政府信息化工作办公室 联系电话：0795-4662252<br> 赣ICP备14008674号 赣公网安备36092502000005<br>
建议使用IE7以上版本、分辨率1024*768浏览，效果最佳<br>
                
            </div>
            <span id="_ideConac"><a href="http://bszs.conac.cn/sitename?method=show&id=294359A562C36296E053022819AC160F" target="_blank">
            <img id="imgConac" vspace="0" hspace="0" border="0" src="//dcs.conac.cn/image/red.png" data-bd-imgshare-binded="1"></a>
</span>
<span id="_span_jiucuo"><a href="http://pucha.kaipuyun.cn/exposure/jiucuo.html?site_code=3609250007&url=http%3A%2F%2Fwww.jxjaxzf.gov.cn%2FDefault.aspx" target="_blank"><img onclick="Link('4305000001')" style="margin: 0px; border: 0px; cursor: pointer; vertical-align: middle; 
                            padding-top: 10px;" src="http://pucha.kaipuyun.cn/exposure/images/jiucuo.png?v=4305000001"></a></span>
<span id="Span1"><a href="http://www.12377.cn/" target="_blank"><img  style="margin: 0px; border: 0px; cursor: pointer; vertical-align: middle; 
                            padding-top: 10px;" src="/Template/Default/Skin/ja/images/12377logo.png"></a></span>


        </div>
    </div>
    <script type="text/javascript" src="http://hnsa.hugedata.com.cn:18080/webtracker/ha/?siteid=1000000132&sinput=skeyword&sbutton=sbutton"
        charset="UTF-8"></script>
    <div style="display: none">
        <script type="text/javascript">            var cnzz_protocol = (("https:" == document.location.protocol) ? " https://" : " http://"); document.write(unescape("%3Cspan id='cnzz_stat_icon_1256314068'%3E%3C/span%3E%3Cscript src='" + cnzz_protocol + "s11.cnzz.com/z_stat.php%3Fid%3D1256314068' type='text/javascript'%3E%3C/script%3E"));</script>
    </div>
    <script type="text/javascript">
        $(function () {
            $("#_span_jiucuo img").css("vertical-align", "middle");
            $("#_span_jiucuo img").css("padding-top", "10px");
        });
    </script>
    <!--foot close -->
    <!--左侧漂浮 -->
    

<div id="Hj-EasyRead-Pop-Title" style="position: fixed; bottom: 0px; left: 0px;
        width: 100%; height: 106px; background-color: rgb(255, 255, 255); z-index: 200;
        text-align: center; font-size: 72px;  display:none">
        <div style="border: 3px solid #1877DF; height: 100px;">
            <span id="Hj-EasyRead-Pop-Title-t" style="line-height: 100px; color: #000;"></span>
            <span id="Hj-EasyRead-Pop-Title-c" style="line-height: 100px; color: #000;font-size: 40px;"></span></div>
    </div>

 
 


<!--foot close -->


<!--左侧漂浮 -->
 
<!--左侧漂浮 -->
</body>
</html>

"""

soup = BeautifulSoup(''.join(doc))

ul = soup.find('ul', {'class': 'newsList infoListA'})

datetime_t = str(datetime.date.today()).split('-')
# print(datetime_t)


articles_link = []
for li in ul.findAll('li'):
    # print(tr)

    find_today = re.compile(r'(\d\d\d\d)-(\d\d)-(\d\d)</span>')  # 构建找到末尾发布日期的正则表达式
    month = find_today.search(str(li))  # 把上面构建的表达式作用于findAll找出来的内容

    try:
        d1 = datetime.date.today()  # 获取今天的日期
        d2 = datetime.date(int(month.group(1)), int(month.group(2)), int(month.group(3)))  # 获取新闻的日期
        days_betwen = (d1 - d2).days  # 获取日期差
        if days_betwen <= 3:
            articles_link.append(str(li))

        """
        if not int(datetime_t[2]) - int(month.group(2)) <= 2: #'14':#self.datetime[2]:  # 判断日期是否为当日
            continue
        if not month.group(1) == datetime_t[1]: #'10':#self.datetime[1]:  # 判断月份是否为当日
            continue
        articles_link.append(str(tr))  # 注意要转换为字符串，beautifusoup不接受列表和其他类型的数据
        print(month.group(2))
        """
    except:
        pass

print(articles_link)

soup3 = BeautifulSoup(''.join(articles_link))

for link in soup3.findAll('a'):
    print(link)
    print(link['href'])

"""
def link():
    for link in table.findAll('a'):
        print(link)


print('\n\n\nLINK\n')
link()


def linkhref():
    for link in table.findAll('a'):
        print(link['href'])


print('\n\n\nLINKHREF\n')
linkhref()


def linkcontent():
    for link in table.findAll('a'):
        print(link.contents[0])


print('\n\n\nLINKCONTENTS\n')
linkcontent()
"""