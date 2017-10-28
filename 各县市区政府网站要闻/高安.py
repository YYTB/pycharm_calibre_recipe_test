# coding=utf-8

from BeautifulSoup import BeautifulSoup
import datetime, re

doc = """

<!DOCTYPE html PUBLIC "-//W3C//DTD XHTML 1.0 Transitional//EN" "http://www.w3.org/TR/xhtml1/DTD/xhtml1-transitional.dtd">
<html xmlns="http://www.w3.org/1999/xhtml">
<head>

<meta http-equiv="Content-Type" content="text/html; charset=gb2312" />
<meta name="keywords" content=""/>
<title>热点新闻</title>
<link href="/css/css.css" rel="stylesheet" type="text/css" />
<script src="/js/jQuery.js" type="text/javascript"></script>
<script language="javascript" src="http://www.jxnews.com.cn/first/js/function.js"></script>
</head>

<body>
<div class="warp">
<div class="topnav">　　欢迎访问高安新闻网　我们见证时代　我们记录高安　　　　　电话：07955210210　　邮箱：<a href="mailto:gawxb@126.com" target="_blank">gawxb@126.com</a> 　　　　　　　　　　　 　　网站简介　|　<a href="javascript:" onClick="javascript:this.style.behavior='url(#default#homepage)';this.setHomePage('http://www.gaxww.com/')">设为首页</a>　|　<a href=# tppabs=http://www.gaxww.com/ onClick="window.external.addFavorite('http://www.gaxww.com/','高安新闻网')" title=高安新闻网>加入收藏</a> </div>

<div class="ad"><img src="http://www.gaxww.com/images/ad21.jpg" width="1000" height="150" /></div>
<div class="top">
  <p><object classid="clsid:D27CDB6E-AE6D-11cf-96B8-444553540000" codebase="http://download.macromedia.com/pub/shockwave/cabs/flash/swflash.cab#version=7,0,19,0" width="1000" height="185">
      <param name="quality" value="high" />
      <param name="SRC" value="http://www.gaxww.com/images/top14.swf" />
      <embed src="http://www.gaxww.com/images/top.swf" width="1000" height="185" quality="high" pluginspage="http://www.macromedia.com/go/getflashplayer" type="application/x-shockwave-flash"></embed>
</object></p>
  <div class="navb"> 

<div class="time" id="time" style="background-image:url(images/nav_11.jpg); background-position:left 10px; background-repeat:no-repeat; padding-left:30px;"><script language=javascript>ShowTime();</script>
</div>


<div class="search">
  <table width="240" height="22" border="0" align="right" cellpadding="0" cellspacing="0">
  <script>
function txy()
{
if (form0.keywords.value!=""){
	//alert("457687878787");
	if (form0.channel_id.value=="jxnewstxy"){
	document.form0.action="http://adv.jxnews.com.cn/2006/tg/stgyx.php?sinput="+form0.keywords.value;
	}
}
}
            </script>
  <form name=form0 action='http://search.jxnews.com.cn:7001/m_fullsearch/utf8/full_search.jsp' method='post' target='_blank'  accept-charset='utf-8'>
    <tr>
    <td width="130">本站搜索</td>
      <td width="176" height="23" style="padding-left:2px"><div align="center">
        <input name=keywords class="input2" onFocus="this.select()" onBlur="if (value ==''){value='请输入关键字'}" onClick="if(this.value=='请输入关键字') this.value=''" onMouseOver="this.focus()" value="请输入关键字" size="12" maxlength=30 height="23" width="200" >
        </div></td>
      <td width="1"><input type=hidden name=channel_id value= "88000000" ></td>
      <td width="51"><input name="submit2" type="image" style="cursor:hand;" onClick="txy()" value="查询" src="http://www.gaxww.com/images/ga_09.jpg" width=46px;></td>
      <input type=hidden name=news_type_id value=1>
      </tr>
  </form> 
  </table>
  </div>
</div>
  <table width="100%" border="0" cellspacing="0" cellpadding="0">
    <tr>
      <td height="5" bgcolor="#a30000"></td>
    </tr>
  </table>
  <div class="nav">
  <div class="sy"><a href="http://www.gaxww.com/" target="_blank"><img src="http://www.gaxww.com/images/sy.jpg" border="0" /></a></div>
  <ul>
<li>
<a href="/hot/" target="_blank">热点新闻</a>&nbsp;&nbsp;<a href="/vedio/" target="_blank">视频新闻</a><br />
<a href="/media/" target="_blank">媒体聚焦</a>&nbsp;&nbsp;<a href="/jhkx/" target="_blank">锦河快讯</a></li>
<li>
<a href="/zsyz/" target="_blank">投资指南</a>&nbsp;&nbsp;<a href="/zdxm/" target="_blank">重大项目</a>&nbsp;&nbsp;<a href="/zwgk/rsxx/" target="_blank">人事任免</a>
<br />
<a href="/zdcy/" target="_blank">重点产业</a>&nbsp;&nbsp;<a href="/yqgk/" target="_blank">园区概况</a>&nbsp; <a href="/zwgk/zwgg/" target="_blank">公告通知</a></li>

<li>
<a href="/yljy/" target="_blank">医疗教育</a>&nbsp;<a href="/sfzj/" target="_blank">&nbsp;书法之乡</a><br />
<a href="/wxtd/" target="_blank">文学天地</a>&nbsp;&nbsp;<a href="/wgss/" target="_blank">五光十摄</a></li>

<li>
<a href="/szxx/" target="_blank">走进高安</a><br />
<a href="/mlxz/" target="_blank">魅力乡镇</a></li>

<li>
<a href="http://www.gaxww.com/zjga.shtml" target="_blank">高安微博</a><br />
<a href="/txyzj/" target="_blank">通讯员之家</a></li>
  </ul>
  </div>
  

  
  </div>
<!--enorth cms page [ enorth parse_date="2017/04/11 10:35:26.026", cost="5", server=":=$encp$=:3e98b31f2b1d13471120858011a74bd3", error_count="0"]-->
  <!--头部完-->
  
  <div class="contect">
    <div class="conn_left">
    <h5>
<!--enorth cms block start [ name="v5.position" ]-->
您当前的位置 ：
<a href=http://www.jxnews.com.cn/index.shtml>中国江西网首页</a>
&nbsp;&gt;&nbsp;
<a href=http://www.gaxww.com/index.shtml>中国高安网</a>
&nbsp;&gt;&nbsp;
<a href=http://www.gaxww.com/hot/index.shtml>热点新闻</a>
<!--enorth cms block end [ name="v5.position" cost="13"]--></h5>
    
    <div class="con_wz">

<!--enorth cms block start [ name="v5.latest" ]-->
<table width="100%" >
<tr> <td > <div class="newsmb"><dl>
<dt><strong>·</strong><a href="http://www.gaxww.com/system/2017/10/19/016478629.shtml" target="_blank" title="【时政】①宜春市政协到我市视察河长制工作">【时政】①宜春市政协到我市视察河长制工作</a></dt>
<dd><a class=amore href="http://www.gaxww.com/system/2017/10/19/016478629.shtml" target=_blank>查阅全文</a><font color="#BE0000">发表于：</font>2017/10/19</dd></dl>
</div> </td> </tr> <tr> <td > <div class="newsmb"><dl>
<dt><strong>·</strong><a href="http://www.gaxww.com/system/2017/10/18/016477784.shtml" target="_blank" title="【消灭劣Ⅴ类水】鲁伟深入肖江流域督查消灭劣Ⅴ类水工作">【消灭劣Ⅴ类水】鲁伟深入肖江流域督查消灭劣Ⅴ类水工作</a></dt>
<dd><a class=amore href="http://www.gaxww.com/system/2017/10/18/016477784.shtml" target=_blank>查阅全文</a><font color="#BE0000">发表于：</font>2017/10/18</dd></dl>
</div> </td> </tr> <tr> <td > <div class="newsmb"><dl>
<dt><strong>·</strong><a href="http://www.gaxww.com/system/2017/10/18/016477748.shtml" target="_blank" title="【喜迎十九大】我市欢送党的十九大代表付秀秀赴京参会">【喜迎十九大】我市欢送党的十九大代表付秀秀赴京参会</a></dt>
<dd><a class=amore href="http://www.gaxww.com/system/2017/10/18/016477748.shtml" target=_blank>查阅全文</a><font color="#BE0000">发表于：</font>2017/10/18</dd></dl>
</div> </td> </tr> <tr> <td > <div class="newsmb"><dl>
<dt><strong>·</strong><a href="http://www.gaxww.com/system/2017/10/18/016477731.shtml" target="_blank" title="【时政】我市举行第三届“泛高安”陶瓷采购节新闻发布会">【时政】我市举行第三届“泛高安”陶瓷采购节新闻发布会</a></dt>
<dd><a class=amore href="http://www.gaxww.com/system/2017/10/18/016477731.shtml" target=_blank>查阅全文</a><font color="#BE0000">发表于：</font>2017/10/18</dd></dl>
</div> </td> </tr> <tr> <td > <div class="newsmb"><dl>
<dt><strong>·</strong><a href="http://www.gaxww.com/system/2017/10/18/016477663.shtml" target="_blank" title="一分钟读懂党的十八届七中全会公报">一分钟读懂党的十八届七中全会公报</a></dt>
<dd><a class=amore href="http://www.gaxww.com/system/2017/10/18/016477663.shtml" target=_blank>查阅全文</a><font color="#BE0000">发表于：</font>2017/10/18</dd></dl>
</div> </td> </tr> <tr> <td > <div class="newsmb"><dl>
<dt><strong>·</strong><a href="http://www.gaxww.com/system/2017/10/18/016477629.shtml" target="_blank" title="众人划桨开大船 同舟共济搏急流_高安广电网络公司以实际行动迎接党的十九大">众人划桨开大船 同舟共济搏急流_高安广电网络公司以实际行动迎接党的十九大</a></dt>
<dd><a class=amore href="http://www.gaxww.com/system/2017/10/18/016477629.shtml" target=_blank>查阅全文</a><font color="#BE0000">发表于：</font>2017/10/18</dd></dl>
</div> </td> </tr> <tr> <td > <div class="newsmb"><dl>
<dt><strong>·</strong><a href="http://www.gaxww.com/system/2017/10/18/016477526.shtml" target="_blank" title="解读”高安卫计委惠民政策“，全市老百姓们，福利来了！">解读”高安卫计委惠民政策“，全市老百姓们，福利来了！</a></dt>
<dd><a class=amore href="http://www.gaxww.com/system/2017/10/18/016477526.shtml" target=_blank>查阅全文</a><font color="#BE0000">发表于：</font>2017/10/18</dd></dl>
</div> </td> </tr> <tr> <td > <div class="newsmb"><dl>
<dt><strong>·</strong><a href="http://www.gaxww.com/system/2017/10/18/016477520.shtml" target="_blank" title="消灭劣Ⅴ类水，高安在行动！">消灭劣Ⅴ类水，高安在行动！</a></dt>
<dd><a class=amore href="http://www.gaxww.com/system/2017/10/18/016477520.shtml" target=_blank>查阅全文</a><font color="#BE0000">发表于：</font>2017/10/18</dd></dl>
</div> </td> </tr> <tr> <td > <div class="newsmb"><dl>
<dt><strong>·</strong><a href="http://www.gaxww.com/system/2017/10/18/016477388.shtml" target="_blank" title="【人物故事】陈宏：一位基层司法所长的朴素情怀">【人物故事】陈宏：一位基层司法所长的朴素情怀</a></dt>
<dd><a class=amore href="http://www.gaxww.com/system/2017/10/18/016477388.shtml" target=_blank>查阅全文</a><font color="#BE0000">发表于：</font>2017/10/18</dd></dl>
</div> </td> </tr> <tr> <td > <div class="newsmb"><dl>
<dt><strong>·</strong><a href="http://www.gaxww.com/system/2017/10/18/016477184.shtml" target="_blank" title="【品读高安】谢季：山水洪城情">【品读高安】谢季：山水洪城情</a></dt>
<dd><a class=amore href="http://www.gaxww.com/system/2017/10/18/016477184.shtml" target=_blank>查阅全文</a><font color="#BE0000">发表于：</font>2017/10/18</dd></dl>
</div> </td> </tr> <tr> <td > <div class="newsmb"><dl>
<dt><strong>·</strong><a href="http://www.gaxww.com/system/2017/10/17/016474579.shtml" target="_blank" title="高安市民间融资登记服务中心有限公司 诚聘信息">高安市民间融资登记服务中心有限公司 诚聘信息</a></dt>
<dd><a class=amore href="http://www.gaxww.com/system/2017/10/17/016474579.shtml" target=_blank>查阅全文</a><font color="#BE0000">发表于：</font>2017/10/17</dd></dl>
</div> </td> </tr> <tr> <td > <div class="newsmb"><dl>
<dt><strong>·</strong><a href="http://www.gaxww.com/system/2017/10/12/016460891.shtml" target="_blank" title="【中国高安 巴夫洛田园综合体】扮靓新家园 开启新生活">【中国高安 巴夫洛田园综合体】扮靓新家园 开启新生活</a></dt>
<dd><a class=amore href="http://www.gaxww.com/system/2017/10/12/016460891.shtml" target=_blank>查阅全文</a><font color="#BE0000">发表于：</font>2017/10/12</dd></dl>
</div> </td> </tr>
</table>
<!--enorth cms block end [ name="v5.latest" cost="105"]-->	 <div>
<!--enorth cms block start [ name="v5.select_page" ]-->
<script src="http://www.gaxww.com/system/count/0088001/000000000000/count_page_list_0088001000000000000.js"></script><div id="pagetemple"></div>
<!--enorth cms block end [ name="v5.select_page" cost="2"]--></div>
    </div>
    </div>
    
<!--文章左侧-->
<div class="wz_right">

<div class="nav_name leader">
<h4>领导之窗</h4>
<ul>
<li><a href="http://www.gaxww.com/system/2011/12/22/011858883.shtml" target="_blank"><img src="/images/leader_01.jpg" border="0" /></a></li>
<li><a href="http://www.gaxww.com/system/2011/12/24/011860598.shtml" target="_blank"><img src="/images/leader_02.jpg" border="0" /></a></li>
<li><a href="http://www.gaxww.com/system/2011/12/24/011860600.shtml" target="_blank"><img src="/images/leader_03.jpg" border="0" /></a></li>
<li><a href="http://www.gaxww.com/system/2011/12/24/011860601.shtml" target="_blank"><img src="/images/leader_04.jpg" border="0" /></a></li>
	</ul>

  </div>
  <div class="nav_name">
    <h4><a href="/hot/" target="_blank" class="amore">更多>></a>热点新闻</h4>
    <ul>

<!--enorth cms block start [ name="v5.latest" ]-->
<li><a href="http://www.gaxww.com/system/2017/10/19/016478997.shtml" target="_blank" title="看直播，话感想！高安社会各界集中收看十九大开幕盛况">看直播，话感想！高安社会各界集中收看...</a></li> <li><a href="http://www.gaxww.com/system/2017/10/19/016478823.shtml" target="_blank" title="【消灭劣Ⅴ类水 高安在行动】市领导督查消灭劣Ⅴ类水整改情况">【消灭劣Ⅴ类水 高安在行动】市领导督查...</a></li> <li><a href="http://www.gaxww.com/system/2017/10/19/016478669.shtml" target="_blank" title="【时政】 ②潘劲松调研上湖珠湖村新农村">【时政】 ②潘劲松调研上湖珠湖村新农村</a></li> <li><a href="http://www.gaxww.com/system/2017/10/19/016478629.shtml" target="_blank" title="【时政】①宜春市政协到我市视察河长制工作">【时政】①宜春市政协到我市视察河长制工作</a></li> <li><a href="http://www.gaxww.com/system/2017/10/18/016477784.shtml" target="_blank" title="【消灭劣Ⅴ类水】鲁伟深入肖江流域督查消灭劣Ⅴ类水工作">【消灭劣Ⅴ类水】鲁伟深入肖江流域督查...</a></li> <li><a href="http://www.gaxww.com/system/2017/10/18/016477748.shtml" target="_blank" title="【喜迎十九大】我市欢送党的十九大代表付秀秀赴京参会">【喜迎十九大】我市欢送党的十九大代表...</a></li> <li><a href="http://www.gaxww.com/system/2017/10/18/016477731.shtml" target="_blank" title="【时政】我市举行第三届“泛高安”陶瓷采购节新闻发布会">【时政】我市举行第三届“泛高安”陶瓷...</a></li> <li><a href="http://www.gaxww.com/system/2017/10/18/016477663.shtml" target="_blank" title="一分钟读懂党的十八届七中全会公报">一分钟读懂党的十八届七中全会公报</a></li>
<!--enorth cms block end [ name="v5.latest" cost="32"]-->    </ul>
  </div>
  
  
<div class="nav_name">
<h4>图片新闻</h4>

<!--enorth cms block start [ name="ga_pic" ]-->
<p><a href="http://www.gaxww.com/system/2016/04/15/014833906.shtml" target="_blank" title="【高品高安】机关建起了读报栏"><img src="http://www.gaxww.com/att2014/000/135/912/00013591290_i1000124000084be_41dc42e6.jpg" border="0" /></a><span>近日，我市在各级党政机关办公楼建起了读报栏，每天把《人民日报》、《江西日报》和《...<a href="http://www.gaxww.com/system/2016/04/15/014833906.shtml" target="_blank">[详细]</a></span></p> <p><a href="http://www.gaxww.com/system/2016/04/15/014833701.shtml" target="_blank" title="【新闻速递】市公安局举办“平安高安与警同行”警营开放日活动"><img src="" border="0" /></a><span>为让市民朋友更好地了解公安工作，增进与群众沟通联系，着力营造“警爱民、民亲警、警...<a href="http://www.gaxww.com/system/2016/04/15/014833701.shtml" target="_blank">[详细]</a></span></p> <p><a href="http://www.gaxww.com/system/2016/04/11/014823316.shtml" target="_blank" title="聂智胜：变思路为举措 变要求为落实 变务虚为务实"><img src="" border="0" /></a><span>4月11日，我市召开市委理论学习中心组专题学习会，学习贯彻《省委书记强卫在宜春调研结...<a href="http://www.gaxww.com/system/2016/04/11/014823316.shtml" target="_blank">[详细]</a></span></p>
<!--enorth cms block end [ name="ga_pic" cost="121"]--></div>

<div class="nav_name spp">
    <h4><a href="/vedio/" target="_blank" class="amore">更多>></a>视频新闻</h4>
    <ul>

<!--enorth cms block start [ name="v5.latest" ]-->
<li><a href="http://www.gaxww.com/system/2017/09/21/016416538.shtml" target="_blank" title="2017年9月14日《高安新闻》">2017年9月14日《高安新闻》</a></li> <li><a href="http://www.gaxww.com/system/2017/09/21/016416530.shtml" target="_blank" title="2017年9月11日《高安新闻》">2017年9月11日《高安新闻》</a></li> <li><a href="http://www.gaxww.com/system/2017/09/21/016416518.shtml" target="_blank" title="2017年9月6日《高安新闻》">2017年9月6日《高安新闻》</a></li> <li><a href="http://www.gaxww.com/system/2017/09/06/016382995.shtml" target="_blank" title="2017年9月2日《高安新闻》">2017年9月2日《高安新闻》</a></li> <li><a href="http://www.gaxww.com/system/2017/09/06/016382984.shtml" target="_blank" title="2017年8月29日《高安新闻》">2017年8月29日《高安新闻》</a></li> <li><a href="http://www.gaxww.com/system/2017/08/30/016370374.shtml" target="_blank" title="2017年8月28日《高安新闻》">2017年8月28日《高安新闻》</a></li> <li><a href="http://www.gaxww.com/system/2017/08/28/016364527.shtml" target="_blank" title="2017年8月24日《高安新闻》">2017年8月24日《高安新闻》</a></li> <li><a href="http://www.gaxww.com/system/2017/08/25/016361957.shtml" target="_blank" title="2017年8月22日《高安新闻》">2017年8月22日《高安新闻》</a></li>
<!--enorth cms block end [ name="v5.latest" cost="62"]-->    </ul>
  </div>
    

</div>
<!--enorth cms page [ enorth parse_date="2017/10/21 00:26:29.029", cost="225", server="unkown host", error_count="0"]-->
  </div>
  <!--第一屏-->

<div class="foot"><p><a href="#" target="_blank">使用帮助</a>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;<a href="#" target="_blank">网站声明</a>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;<a href="#" target="_blank">常见问题</a>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;<a href="#" target="_blank">隐私声明</a>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;<a href="#" target="_blank">联系我们</a></p>


</div>
<div class="aq">
<ul>
<li><img src="http://www.gaxww.com/images/ga_220a.jpg" /></li>
<li>Copyright 2011 GaoAn China All Rights Reserved.<br />
高安新闻网版权所有webmaster@gaxww.com</li>
<li><img src="http://www.gaxww.com/images/ga_215.jpg" /></li>
<li><img src="http://www.gaxww.com/images/ga_217.jpg" align="absmiddle" /> 赣ICP备07004085号-1</li>
</ul>

</div>


<div id="bq">主办：中共高安市委宣传部
　承办：高安市外宣办</div>
<div align=center><script type="text/javascript">document.write(unescape("%3Cspan id='_ideConac' %3E%3C/span%3E%3Cscript  src='http://dcs.conac.cn/js/15/232/0887/60604359/CA152320887606043590001.js' type='text/javascript'%3E%3C/script%3E"));</script></div><!--<page cms="enorth webpublisher"  version="5.0.0 /2011101201" server_name="enorthProgram" parse_date="2015-12-24 15:43:10" cost="15" parse_result="0" input_mode="manual"></page>-->
<!--底部-->
</div>
</body>
</html>


<!--enorth cms page [ enorth parse_date="2017/10/21 00:26:29.029", cost="130", server="unkown host", error_count="0"]-->

"""

soup = BeautifulSoup(''.join(doc))

div = soup.find('div', {'class': 'conn_left'})

datetime_t = str(datetime.date.today()).split('-')
# print(datetime_t)


articles_link = []
for newsmb in div.findAll('div', {'class': 'newsmb'}):
    print(newsmb)

    find_today = re.compile(r'(\d\d\d\d)/(\d\d)/(\d\d)</dd>')  # 构建找到末尾发布日期的正则表达式
    month = find_today.search(str(newsmb))  # 把上面构建的表达式作用于findAll找出来的内容

    try:
        d1 = datetime.date.today()  # 获取今天的日期
        d2 = datetime.date(int(month.group(1)), int(month.group(2)), int(month.group(3)))  # 获取新闻的日期
        days_betwen = (d1 - d2).days  # 获取日期差
        if days_betwen <= 8:
            articles_link.append(str(newsmb))

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