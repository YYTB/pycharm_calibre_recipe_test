# coding=utf-8
from BeautifulSoup import BeautifulSoup
import datetime,re  # 导入日期时间模块，各版面的url根据发行日期改变。

html = '''

<!DOCTYPE html PUBLIC "-//W3C//DTD XHTML 1.0 Transitional//EN" "http://www.w3.org/TR/xhtml1/DTD/xhtml1-transitional.dtd">
<html xmlns="http://www.w3.org/1999/xhtml" lang="utf-8">
<head>
<meta http-equiv="content-type" content="text/html;charset=utf-8" />
<meta http-equiv="content-language" content="utf-8" />
<meta name="robots" content="all" />
<meta name="author" content='' />
<meta name="copyright" content="" />
<meta name="description" content="" />
<meta name="keywords" content="" />
<META name='filetype' content='0'>
<META name='publishedtype' content='1'>
<META name='pagetype' content='2'>
<META name='catalogs' content='XTW_0009002'>
<link href="../../../tplimg/mulu_m1.css" type="text/css" rel="stylesheet" rev="stylesheet" media="all" />
<title>人民日报-人民网</title>
<script language="javascript">
function killErrors() {
    return true;
}
window.onerror = killErrors;
</script>
<SCRIPT language=Javascript src="../../../tplimg/prototype.js"></SCRIPT>
<SCRIPT language=Javascript src="../../../tplimg/mp.js"></SCRIPT>
<SCRIPT language=Javascript src="../../../tplimg/calendar2.js"></SCRIPT>
<SCRIPT language=Javascript src="../../../tplimg/range.js"></SCRIPT>
<SCRIPT language=Javascript src="../../../tplimg/lib.js"></SCRIPT>
<SCRIPT language=Javascript src="../../../tplimg/dzb.js"></SCRIPT>
<SCRIPT language=Javascript src="../../../tplimg/new.js"></SCRIPT>
<SCRIPT language=Javascript src="../../../tplimg/jspoints.js"></SCRIPT>
<style>
a.ared:link {
	font-size: 12px;
	color: #FF0000;
	text-decoration: none;
}
a.ared:visited {
	font-size: 12px;
	color: #FF0000;
	text-decoration: none;
}
a.ared:hover {
	font-size: 12px;
	color: #006699;
	text-decoration: none;
}
.un {
	color:#004677;
}
.right_title1 {

}
.right_title2 {

}
.right_title-name {
	padding:3px 5px 0px 5px;
	float:left;
	width:188px;
	line-height:24px;
}
.right_title-pdf {
	padding:5px 5px 0px 0px;
	float:right;
}
</style>
<style>
.head_c2{display:block;float:left;margin:0 15px 0 0;width:91px;color:#004873;height:21px;padding:0 2px 0 2px;background:#fff;border:1px solid #66B1EB;text-align:left;}
.head_c3{float:right; margin:2px 0 0 0;}
</style>
<script type="text/javascript">
function nTabs(tabObj,obj){
	var tabList = document.getElementById(tabObj).getElementsByTagName("li");
	for(i=0; i <tabList.length; i++)
	{
		if (tabList[i].id == obj.id)
		{
			document.getElementById(tabObj+"_Title"+i).className = "active";
    		document.getElementById(tabObj+"_Content"+i).style.display = "block";
		}else{
			document.getElementById(tabObj+"_Title"+i).className = "normal";
			document.getElementById(tabObj+"_Content"+i).style.display = "none";
		}
	}
}

function getStringLength(str)
{
	if (str == null || str == "")
		return 0;
	else
		return str.length;
}

function view(str)
{
 var len = 20;
 var ret = "";
str=str.replace(/<br>/gi," ");
 if(getStringLength(str) > len)
  ret = "<span title='" + str + "'>" + str.substring(0, len) + "...</span>";
 else
  ret = str;
 return ret;
}
function zoomIn() {
 newZoom= parseInt(ozoom.style.zoom)+10+'%'
 ozoom.style.zoom =newZoom;
 }
function zoomOut() {
 newZoom= parseInt(ozoom.style.zoom)-10+'%'
 ozoom.style.zoom =newZoom;
 }

 function submitCheck()
 {
 	 if(document.all("content1").value.length>1000){
	 alert("评论内容超过1000字！");
	 return false;
	 }
	 if(document.all("content1").value.indexOf("<script")!=-1 ||document.all("content1").value.indexOf("<\/")!=-1){
	 alert("评论内容含有特殊字符!");
	 return false;
	 }
	 if(document.all("content1").value == "")
	 {
	 alert("必须填写评论内容！");
	 return false;
	 }
	 document.commentform.paperdate.value = document.getElementById("paperdatediv").innerText.replace(/(^\s*)|(\s*$)/g, "");
	 document.commentform.nispagename.value = escape(document.getElementById("pageNameForJiaoHu").innerText.replace(/(^\s*)|(\s*$)/g, ""));
	var isnodecomment = document.commentform.isnodecomm.value;
	document.commentform.isGuest.value = document.commentform.isGuest.checked;
	document.commentform.rankRadio.value = document.commentform.rankRadio.checked;
	document.commentform.content.value=escape(document.commentform.content1.value);
	document.commentform.author.value=escape(document.commentform.author1.value);
	document.commentform.weburl.value=location.href;

	if (document.commentform.channelname1.value == "")
	{

		document.commentform.channelname1.value = document.commentform.channelname.value;
		document.commentform.nodename1.value = document.commentform.nodename.value;
		document.commentform.channelname.value=escape(document.commentform.channelname.value);
		document.commentform.nodename.value=escape(document.commentform.nodename.value);
	}
	else{

		document.commentform.channelname.value = document.commentform.channelname1.value;
		document.commentform.nodename.value = document.commentform.nodename1.value;
		document.commentform.channelname.value=escape(document.commentform.channelname.value);
		document.commentform.nodename.value=escape(document.commentform.nodename.value);
	}
 	document.commentform.submit();
 	alert("您的留言已经成功提交！");
 	document.commentform.content1.value="";
 }
 function viewComment(){
 		 document.viewform.paperdate.value = document.getElementById("paperdatediv").innerText.replace(/(^\s*)|(\s*$)/g, "");
		 document.viewform.nispagename.value = escape(document.getElementById("pageNameForJiaoHu").innerText.replace(/(^\s*)|(\s*$)/g, ""));
 	 if (document.viewform.channelname1.value =="")
	 {

				document.viewform.channelname1.value = document.viewform.channelname.value;
				document.viewform.nodename1.value = document.viewform.nodename.value;
				document.viewform.nodename.value=escape(document.viewform.nodename.value);
				document.viewform.channelname.value=escape(document.viewform.channelname.value);
		}else
		{

				document.viewform.channelname.value = document.viewform.channelname1.value;
				document.viewform.nodename.value = document.viewform.nodename1.value;
				document.viewform.nodename.value=escape(document.viewform.nodename.value);
				document.viewform.channelname.value=escape(document.viewform.channelname.value);
		}
		document.viewform.action="http://paperpost.people.com.cn/comment/nodeComment.jsp";
		document.viewform.target="";
		document.viewform.weburl.value=location.href;
 		 document.viewform.submit();
 	}

	 function showComment(){
 		document.viewform.paperdate.value = document.getElementById("paperdatediv").innerText.replace(/(^\s*)|(\s*$)/g, "");
 	 if (document.viewform.channelname1.value =="")
	 {

				document.viewform.channelname1.value = document.viewform.channelname.value;
				document.viewform.nodename1.value = document.viewform.nodename.value;
				document.viewform.nodename.value=escape(document.viewform.nodename.value);
				document.viewform.channelname.value=escape(document.viewform.channelname.value);
		}else
		{

				document.viewform.channelname.value = document.viewform.channelname1.value;
				document.viewform.nodename.value = document.viewform.nodename1.value;
				document.viewform.nodename.value=escape(document.viewform.nodename.value);
				document.viewform.channelname.value=escape(document.viewform.channelname.value);
		}
		 document.viewform.action="http://paperpost.people.com.cn/comment/nodeCommentList.jsp";
		 document.viewform.target="NodeCommentFrame";
 		 document.viewform.submit();

 	}

 function dohit(){
  if (document.readyState == 'complete' )
     {
  document.frames("hitClickIframe").document.hitform.url.value = location.href;
  if(document.commentform.isnodecomm.value == '1'){
  document.frames("hitClickIframe").document.hitform.nodeid.value = document.commentform.nodeid.value;
  }else{
  document.frames("hitClickIframe").document.hitform.articleid.value = document.commentform.articleid.value;
  }
  document.frames("hitClickIframe").document.hitform.submit();
  document.hitClickIframe.style.display="none";
  }else
  window.setTimeout("dohit()","300");
}
	function getDate()
	{
		  var url = window.location.pathname.split('/');
		  var length = url.length;
		  document.getElementById("newsIframe").src = "http://paperpost.people.com.cn/"+url[1]+"-"+url[length-3]+"-"+url[length-2]+".html";
	}
</script>
</head>
<SPAN id=leveldiv title=点击查看内容
style="BORDER-TOP-WIDTH: 0px; BORDER-LEFT-WIDTH: 0px; Z-INDEX: 100; LEFT: 233px; BORDER-BOTTOM-WIDTH: 0px; WIDTH: 210px; CURSOR: hand; POSITION: absolute; TOP: 123px; HEIGHT: 34px; BORDER-RIGHT-WIDTH: 0px"></SPAN>
<body onLoad="createStarsPage();getDate();initialize();initMPPage();loadWowi();dohit();showArtPics();">
<div class="div_bg"><div class="div_center">
  <!--左侧版面图部分-->
  <div class="left_c">
    <div class="ban">
      <div>
        <map name=PagePicMap><Area coords="397,31,397,2,204,2,204,31,204,111,397,111" shape="polygon" href="nw.D110000renmrb_20171016_1-01.htm"><Area coords="2,96,195,96,195,373,2,373" shape="polygon" href="nw.D110000renmrb_20171016_2-01.htm"><Area coords="204,119,397,119,397,284,204,284" shape="polygon" href="nw.D110000renmrb_20171016_3-01.htm"><Area coords="397,334,397,292,204,292,204,334,204,397,397,397" shape="polygon" href="nw.D110000renmrb_20171016_4-01.htm"><Area coords="2,403,397,403,397,567,2,567" shape="polygon" href="nw.D110000renmrb_20171016_5-01.htm"></map><img  width=400 height=575 src=../../../page/2017-10/16/01/rmrb2017101601_b.jpg border=0 USEMAP=#PagePicMap></div>
    </div>
    <div class="ban_t">
      <div>
        <ul>
          <li>
            01版:要闻
            &nbsp;
            <a href=../../../page/2017-10/16/01/rmrb2017101601.pdf><IMG src="../../../tplimg/ico4.gif" border=0></a>
            PDF版下载 <span>
              <a class=preart href="nbs.D110000renmrb_02.htm">下一版 <img src='../../../tplimg/right_ico.gif' border=0 /></a>
            </span></li>
        </ul>
      </div>
    </div>
    <div class="tool"><input type="image" onclick="javascript:window.open('http://ardownload.adobe.com/pub/adobe/reader/win/8.x/8.1/chs/AdbeRdr810_zh_CN.exe')" src="../../../tplimg/button.gif" name="" style="float:left;padding-left:40px"/><img src="../../../tplimg/button1.gif" style="display:none"/><img src="../../../tplimg/button2.gif"  style="display:none"/><a href="node_1921.htm"><img src="../../../tplimg/button3.gif" border="0" style="float:right;padding-right:40px" /></a></div>
  <!-- -->
  <!--版面打分-->
	<div class="title da_t" style="width:416px;margin-top:10px;margin-left:10px;float:none;margin-right:0px;">
      <div style="width:404px;">我给版面打分</div>
    </div>
    <div class="pai" style="width:396px;height:50px;border:1px solid #7DBCEF;padding-left:20px">
      <FORM id=pointsform name=pointsform action="" method=post
                  target=pointsIframe  style=" display:none;">
                  <INPUT type=hidden name=paperdate />
        <INPUT
                              type=hidden name=nodename1 />
        <INPUT type=hidden
                              name=channelname1 />
        <INPUT type=hidden name=title1 />
        <INPUT type=hidden value=2 name=attr />
        <!--attr 2 数字报刊 1 翔宇-->
        <INPUT type=hidden value=1
                              name=isnodecomm />
        <!--isnodecomm 2 文章评论 1 版面或栏目评论-->
        <INPUT
                              type=hidden value=2 name=pointtype />
        <!--pointtype 2 计算平均分（现阶段必须设为2） 1 统计类型-->
        <!--此列为插件生成的组件-->
        <input name="nodeid" type=hidden value="1922"><input name="nodename" type=hidden value="01"><input name="nodetype" type=hidden value="0"><input name="nodeurl" type=hidden value="null.htm"><input name="channelid" type=hidden value="1921"><input name="channelname" type=hidden value="人民日报">
        <div id="paperdatediv">
          2017-October-16
        </div>
      </FORM>
      <form name="pForm" id="pForm">
        <input type="radio" name="pointVal" value="1" onClick="pv(1)"/>
        1分&nbsp;&nbsp;
        <input type="radio" name="pointVal" value="2" onClick="pv(2)" />
        2分&nbsp;&nbsp;
        <input type="radio" name="pointVal" value="3" onClick="pv(3)" checked="checked" />
        3分&nbsp;&nbsp;
        <input type="radio" name="pointVal" value="4" onClick="pv(4)" />
        4分&nbsp;&nbsp;
        <input type="radio" name="pointVal" value="5" onClick="pv(5)" />
        5分 &nbsp; <img src="../../../tplimg/ti.gif"  alt="" border="0" style="cursor:hand " onclick="submitPoints(document.pForm.Input2.value);" />
        <!--<p>本版得分:<span>4.1分</span>(共有<span>19</span>位网友打分)</p>-->
        <input name="Input2" type="hidden" value="3" />
      </form>
      <iframe id="pointsIframe"
            name="pointsIframe" src="about:blank" frameborder=0 width=375
            scrolling=no height=30></iframe>
    </div>
    <div class="title"style="margin-top:10px">
      <div>新闻排行榜</div>
    </div>
    <div class="pai">
      <div>
        <!--
	    <span>1</span><a href="">我看到了你，也看到了我的种点</a><br />
		<span>2</span><a href="">我看到了你，也看到了我的种点</a><br />
		<span>3</span><a href="">我看到了你，也看到了我的种点</a><br />
		<span>4</span><a href="">我看到了你，也看到了我的种点</a><br />
		<span>5</span><a href="">我看到了你，也看到了我的种点</a><br />
		<span>6</span><a href="">我看到了你，也看到了我的种点</a><br />
		<span>7</span><a href="">我看到了你，也看到了我的种点</a><br />
		<span>8</span><a href="">我看到了你，也看到了我的种点</a><br />
		<span>9</span><a href="">我看到了你，也看到了我的种点</a><br />
		<span>10</span><a href="">我看到了你，也看到了我的种点</a><br />-->
        <iframe name="newsIframe" id="newsIframe" style="font-size:12px;" border="0" width="95%" height="240" frameborder="0" src=""></iframe>
        <br />
        <iframe name="hitClickIframe" style="font-size:12px;" id="hitClickIframe" height="0" width="0" border="0" frameborder="0" src="../../../tplimg/hitPost.htm"></iframe>
      </div>
    </div>
    <div class="title">
      <div id="bqsm">版权声明</div>
    </div>
    <div class="pai f_link" id="bqsm_nr" style="line-height:25px">　　《人民日报》（电子版）的一切内容(包括但不限于文字、图片、PDF、图表、标志、标识、商标、版面设计、专栏目录与名称、内容分类标准以及为读者提供的任何信息)仅供人民网读者阅读、学习研究使用，未经人民网股份有限公司及/或相关权利人书面授权，任何单位及个人不得将《人民日报》（电子版）所登载、发布的内容用于商业性目的，包括但不限于转载、复制、发行、制作光盘、数据库、触摸展示等行为方式，或将之在非本站所属的服务器上作镜像。否则，人民网股份有限公司将采取包括但不限于网上公示、向有关部门举报、诉讼等一切合法手段，追究侵权者的法律责任。</div><!-- -->  
  </div>
  <!--右侧目录部分-->
  <div class="right_c">
    <div style="margin:0 auto;width:530px;height:70px;text-align:right;padding:8px 0 0 20px;">
      <div style="height:70px;">
        <div style="float:left; width:390px;">
          <div style="height:23px; padding:10px 0px;">
            <div onMouseOver="document.getElementById('rmrbbx').style.display = 'block';" onMouseOut="document.getElementById('rmrbbx').style.display = 'none';" class="head_c2">
              <div style="float:left">日&nbsp;报</div>
              <div  class="head_c3"><img src="../../../tplimg/ico10.gif" border="0" alt="" /></div>
            </div>
            <div onMouseOver="document.getElementById('rmrbbx1').style.display = 'block';" onMouseOut="document.getElementById('rmrbbx1').style.display = 'none';" class="head_c2">
              <div style="float:left">周&nbsp;报</div>
              <div  class="head_c3"><img src="../../../tplimg/ico10.gif" border="0" alt="" /></div>
            </div>
            <div onMouseOver="document.getElementById('rmrbbx2').style.display = 'block';" onMouseOut="document.getElementById('rmrbbx2').style.display = 'none';" class="head_c2">
              <div style="float:left">杂&nbsp;志</div>
              <div  class="head_c3"><img src="../../../tplimg/ico10.gif" border="0" alt="" /></div>
            </div>
          </div>
          <div style="text-align:left;">
            <div style="float:left; width:370px;"><div id="riqi_"  style="float:left;">
            人民日报
            2017年10月16日 星期一
            </div><div id="peopledata" style="float:right; display:none" class="peopledata"></div>
		   <div style="float:left; color:#004773; display:none; padding-left:5px;" id="infowelcome">&nbsp;欢迎您：<span id="disname" class="un">用户ID名称</span></div></div>
         </div>
        </div>
        <div style="float:left;"><a href="http://www.people.com.cn"><img src="../../../tplimg/logo.jpg" border="0" alt="人民网" /></a></div>
      </div>
    </div>
    <div style="margin:0 auto; color:#004773; height:20px; width:525px; padding:8px 10px 10px 20px; text-align: left;float:left;">
      <div style="float:left; width:50px;">往期回顾</div>
      <div style="float:left; width:60px; padding-top:2px;"><a onClick="autoShowDate();" style="cursor:hand;" title="鼠标点击，显示日历牌"><img src="../../../tplimg/ico1.gif" border="0" alt="" /></a></div>
      <div style="float:left; width:80px;display:none" id="paperSearch"><a href="http://search.people.com.cn/rmw/GB/bkzzsearch/index.jsp" target="_blank">人民网检索</a></div>
      <div style="float:left; display:none; font-weight:bold;" id="usercenter"><a href="../../../notice/notice.htm" class="ared" target="_blank">《人民日报》数字报取消收费的通知</a></div>
      <div style="float:right; text-align:right;">&nbsp;<a href="#" onClick="goPrePeriod()">&lt;上一期</a>&nbsp;&nbsp;&nbsp;<a href="#" onClick="goNextPeriod()">下一期&gt;</a></div>
    </div>
    <div class="mobilepaper" id="mobilepaper"></div>
    <!--目录与标题-->
    <DIV id="ozoom" style="zoom:100%;">
      <div class="list_t">
        <!--新闻标题-->
        <div class="list_l">
          <div class="l_t">
            01版:要闻
          </div>
          <div class="l_b" id="titleImgUp"><a href="#"><img src="../../../tplimg/jiao1.gif" border="0" alt="" /></a></div>
          <div class="l_c">
            <div id="titleList"  style="height:440px;overflow:hidden;">
              <!-- list starting -->
              <ul>


<li>
<a href=nw.D110000renmrb_20171016_1-01.htm><script>document.write(view("《习近平关于社会主义文化建设论述摘编》出版发行  "))</script></a></li>
<li class="one">
 <a href=nw.D110000renmrb_20171016_2-01.htm><script>document.write(view("中共中央召开党外人士座谈会<br>征求对中共十九大报告的意见  "))</script></a></li>
<li>
<a href=nw.D110000renmrb_20171016_3-01.htm><script>document.write(view("党的十九大代表陆续抵京  "))</script></a></li>
<li class="one">
 <a href=nw.D110000renmrb_20171016_4-01.htm><script>document.write(view("砥砺奋进 铸就辉煌  "))</script></a></li>
<li>
<a href=nw.D110000renmrb_20171016_5-01.htm><script>document.write(view("党的十八大以来大事记  "))</script></a></li>

</ul><!-- list endding -->
            </div>
          </div>
          <div style="width:316px;height:10px;background:#D0EBFE;border-top:1px solid #94D5FF;text-align:center;padding:2px 0 0 0;" id="titleImgDown" align="center"><a href="#"><img src="../../../tplimg/jiao.gif" border="0" alt="" /></a></div>
        </div>
        <!--版面目录-->
        <div class="list_r">
          <div class="l_t l_t1">版面目录</div>
          <div class="l_b l_b1" id="pageImgUp"><a href="#"><img src="../../../tplimg/jiao1.gif" border="0" alt="" /></a></div>
          <div class="l_c l_c1">
            <div id="pageList" style="overflow:hidden;height:440px;">
              <!-- list starting -->
              <ul>
<div class="right_title1">
<div class="right_title-name"><a id=pageLink href=./nbs.D110000renmrb_01.htm>第01版：要闻</a></div>
<div class="right_title-pdf"><a href=../../../page/2017-10/16/01/rmrb2017101601.pdf><img src="../../../tplimg/ico3.gif" border=0 /></a></div>
</div>
<div class="right_title2">
<div class="right_title-name"><a id=pageLink href=nbs.D110000renmrb_02.htm>第02版：要闻</a></div>
<div class="right_title-pdf"><a href=../../../page/2017-10/16/02/rmrb2017101602.pdf><img src="../../../tplimg/ico3.gif" border=0 /></a></div>
</div>
<div class="right_title1">
<div class="right_title-name"><a id=pageLink href=nbs.D110000renmrb_03.htm>第03版：要闻</a></div>
<div class="right_title-pdf"><a href=../../../page/2017-10/16/03/rmrb2017101603.pdf><img src="../../../tplimg/ico3.gif" border=0 /></a></div>
</div>
<div class="right_title2">
<div class="right_title-name"><a id=pageLink href=nbs.D110000renmrb_04.htm>第04版：要闻</a></div>
<div class="right_title-pdf"><a href=../../../page/2017-10/16/04/rmrb2017101604.pdf><img src="../../../tplimg/ico3.gif" border=0 /></a></div>
</div>
<div class="right_title1">
<div class="right_title-name"><a id=pageLink href=nbs.D110000renmrb_05.htm>第05版：要闻</a></div>
<div class="right_title-pdf"><a href=../../../page/2017-10/16/05/rmrb2017101605.pdf><img src="../../../tplimg/ico3.gif" border=0 /></a></div>
</div>
<div class="right_title2">
<div class="right_title-name"><a id=pageLink href=nbs.D110000renmrb_06.htm>第06版：要闻</a></div>
<div class="right_title-pdf"><a href=../../../page/2017-10/16/06/rmrb2017101606.pdf><img src="../../../tplimg/ico3.gif" border=0 /></a></div>
</div>
<div class="right_title1">
<div class="right_title-name"><a id=pageLink href=nbs.D110000renmrb_07.htm>第07版：要闻</a></div>
<div class="right_title-pdf"><a href=../../../page/2017-10/16/07/rmrb2017101607.pdf><img src="../../../tplimg/ico3.gif" border=0 /></a></div>
</div>
<div class="right_title2">
<div class="right_title-name"><a id=pageLink href=nbs.D110000renmrb_08.htm>第08版：广告</a></div>
<div class="right_title-pdf"><a href=../../../page/2017-10/16/08/rmrb2017101608.pdf><img src="../../../tplimg/ico3.gif" border=0 /></a></div>
</div>
<div class="right_title1">
<div class="right_title-name"><a id=pageLink href=nbs.D110000renmrb_09.htm>第09版：砥砺奋进的5年·迎接党的十九大特别报道·历史性变革⑧</a></div>
<div class="right_title-pdf"><a href=../../../page/2017-10/16/09/rmrb2017101609.pdf><img src="../../../tplimg/ico3.gif" border=0 /></a></div>
</div>
<div class="right_title2">
<div class="right_title-name"><a id=pageLink href=nbs.D110000renmrb_10.htm>第10版：砥砺奋进的5年·迎接党的十九大特别报道·历史性变革</a></div>
<div class="right_title-pdf"><a href=../../../page/2017-10/16/10/rmrb2017101610.pdf><img src="../../../tplimg/ico3.gif" border=0 /></a></div>
</div>
<div class="right_title1">
<div class="right_title-name"><a id=pageLink href=nbs.D110000renmrb_11.htm>第11版：砥砺奋进的5年·迎接党的十九大特别报道·历史性变革</a></div>
<div class="right_title-pdf"><a href=../../../page/2017-10/16/11/rmrb2017101611.pdf><img src="../../../tplimg/ico3.gif" border=0 /></a></div>
</div>
<div class="right_title2">
<div class="right_title-name"><a id=pageLink href=nbs.D110000renmrb_12.htm>第12版：砥砺奋进的5年·迎接党的十九大特别报道·历史性变革</a></div>
<div class="right_title-pdf"><a href=../../../page/2017-10/16/12/rmrb2017101612.pdf><img src="../../../tplimg/ico3.gif" border=0 /></a></div>
</div>
<div class="right_title1">
<div class="right_title-name"><a id=pageLink href=nbs.D110000renmrb_13.htm>第13版：砥砺奋进的5年·迎接党的十九大特别报道·历史性变革</a></div>
<div class="right_title-pdf"><a href=../../../page/2017-10/16/13/rmrb2017101613.pdf><img src="../../../tplimg/ico3.gif" border=0 /></a></div>
</div>
<div class="right_title2">
<div class="right_title-name"><a id=pageLink href=nbs.D110000renmrb_14.htm>第14版：砥砺奋进的5年·迎接党的十九大特别报道·历史性变革</a></div>
<div class="right_title-pdf"><a href=../../../page/2017-10/16/14/rmrb2017101614.pdf><img src="../../../tplimg/ico3.gif" border=0 /></a></div>
</div>
<div class="right_title1">
<div class="right_title-name"><a id=pageLink href=nbs.D110000renmrb_15.htm>第15版：砥砺奋进的5年·迎接党的十九大特别报道·历史性变革</a></div>
<div class="right_title-pdf"><a href=../../../page/2017-10/16/15/rmrb2017101615.pdf><img src="../../../tplimg/ico3.gif" border=0 /></a></div>
</div>
<div class="right_title2">
<div class="right_title-name"><a id=pageLink href=nbs.D110000renmrb_16.htm>第16版：砥砺奋进的5年·迎接党的十九大特别报道·历史性变革</a></div>
<div class="right_title-pdf"><a href=../../../page/2017-10/16/16/rmrb2017101616.pdf><img src="../../../tplimg/ico3.gif" border=0 /></a></div>
</div>
<div class="right_title1">
<div class="right_title-name"><a id=pageLink href=nbs.D110000renmrb_17.htm>第17版：综合</a></div>
<div class="right_title-pdf"><a href=../../../page/2017-10/16/17/rmrb2017101617.pdf><img src="../../../tplimg/ico3.gif" border=0 /></a></div>
</div>
<div class="right_title2">
<div class="right_title-name"><a id=pageLink href=nbs.D110000renmrb_18.htm>第18版：国际</a></div>
<div class="right_title-pdf"><a href=../../../page/2017-10/16/18/rmrb2017101618.pdf><img src="../../../tplimg/ico3.gif" border=0 /></a></div>
</div>
<div class="right_title1">
<div class="right_title-name"><a id=pageLink href=nbs.D110000renmrb_19.htm>第19版：广告</a></div>
<div class="right_title-pdf"><a href=../../../page/2017-10/16/19/rmrb2017101619.pdf><img src="../../../tplimg/ico3.gif" border=0 /></a></div>
</div>
<div class="right_title2">
<div class="right_title-name"><a id=pageLink href=nbs.D110000renmrb_20.htm>第20版：广告</a></div>
<div class="right_title-pdf"><a href=../../../page/2017-10/16/20/rmrb2017101620.pdf><img src="../../../tplimg/ico3.gif" border=0 /></a></div>
</div>
<div class="right_title1">
<div class="right_title-name"><a id=pageLink href=nbs.D110000renmrb_21.htm>第21版：广告</a></div>
<div class="right_title-pdf"><a href=../../../page/2017-10/16/21/rmrb2017101621.pdf><img src="../../../tplimg/ico3.gif" border=0 /></a></div>
</div>
<div class="right_title2">
<div class="right_title-name"><a id=pageLink href=nbs.D110000renmrb_22.htm>第22版：各地传真</a></div>
<div class="right_title-pdf"><a href=../../../page/2017-10/16/22/rmrb2017101622.pdf><img src="../../../tplimg/ico3.gif" border=0 /></a></div>
</div>
<div class="right_title1">
<div class="right_title-name"><a id=pageLink href=nbs.D110000renmrb_23.htm>第23版：区域经济</a></div>
<div class="right_title-pdf"><a href=../../../page/2017-10/16/23/rmrb2017101623.pdf><img src="../../../tplimg/ico3.gif" border=0 /></a></div>
</div>
<div class="right_title2">
<div class="right_title-name"><a id=pageLink href=nbs.D110000renmrb_24.htm>第24版：广告</a></div>
<div class="right_title-pdf"><a href=../../../page/2017-10/16/24/rmrb2017101624.pdf><img src="../../../tplimg/ico3.gif" border=0 /></a></div>
</div>
</ul><!-- list endding -->
            </div>
          </div>
          <div  style="width:218px;height:10px;background:#D0EBFE;border-top:1px solid #94D5FF;text-align:center;padding:2px 0 0 0;" id="pageImgDown" align="center"><a href="#"><img src="../../../tplimg/jiao.gif" border="0" alt="" /></a></div>
        </div>
      </div>
    </div>
     <iframe id="postIframe"  
            name="postIframe" src='http://paperpost.people.com.cn/dis/commesPageNew.jsp?artiles=5' frameborder=0 width=555
            scrolling=no height=581 style="margin-left:-5px;float:left;margin-top:10px"><a href="http://58.68.146.103/epaper/rmrb.html" class="ared" style="font-size:16px"><span style="font-weight:bold;">人民日报图文数据库（1946-2014）</span></a><br>开放试用申请，审核通过将获得数据库的全部使用权限</div></iframe>
    <!--我要评报-->
    <div class="title da_t">
      <div><div style="float:left;width:350px;background:none;margin:0px;padding:0px;height:25px">留言须知 <a href="http://www.people.com.cn/GB/50142/104580/index.html" target="_blank">&nbsp;|&nbsp;关于人民日报社</a></div>
	</div>
    </div>
    <div class="note">
      <div name="pageNameForJiaoHu" id="pageNameForJiaoHu" style="display:none" >
        要闻
      </div>
      <FORM name=commentform action=http://paperpost.people.com.cn/comment/saveNodeArtComment.jsp  method=post target="tempForm">
        <!--&nbsp;&nbsp;&nbsp;&nbsp;署名:
        <input type="text" style="width:95px;height:18px;border:1px solid #7F9DB9;" maxLength=64  name="author1"/>
        &nbsp;&nbsp;
        <input name="isGuest" type="hidden"  id="isGuest" value="true" />-->
        <!--匿名发表-->
        <!--p>
          <textarea name="content1" cols="30" rows="6"  id="content1"></textarea>
          <img src="../../../tplimg/fb.gif"  alt="" border="0" style="cursor:hand " onclick="return submitCheck();" /><br/><br/><br/><img src="../../../tplimg/ckpl.gif"  alt="" border="0" style="cursor:hand " onclick="return viewComment();"> </p-->
        <input type=hidden  name="nodename1" />
	<input type=hidden  name="weburl" />
        <input type="hidden"  name="channelname1" />
        <input name="attr" type="hidden" value="2" />
        <input name="isnodecomm" type="hidden" value="1" />
        <input type="hidden" name="author" />
        <input type="hidden" name="content" />
        <INPUT type="hidden"  name="paperdate" />
        <input type="hidden" name="nispagename" />
        <span id="liuyans">
          1.遵守中华人民共和国有关法律、法规，尊重网上道德，承担一切因您的行为而直接或间接引起的法律责任。 
            <br>
            2.人民网拥有管理笔名和留言的一切权力。 <br>
            3.您在人民网留言板发表的言论，人民网有权在网站内转载或引用。 <br>
          </span>
        <input name="nodeid" type=hidden value="1922"><input name="nodename" type=hidden value="01"><input name="nodetype" type=hidden value="0"><input name="nodeurl" type=hidden value="null.htm"><input name="channelid" type=hidden value="1921"><input name="channelname" type=hidden value="人民日报">
        <INPUT name=password type="password" id="password" style="WIDTH: 95px; HEIGHT: 18px;display:none" maxLength=64 />
        <input type="radio" name="rankRadio" style=" display:none;" value="5" />
        <input type="radio" name="rankRadio" style=" display:none;" value="4" />
        <input type="radio" name="rankRadio" style=" display:none;" value="3" />
        <input type="radio" name="rankRadio" style=" display:none;" value="2" />
        <input type="radio" checked name="rankRadio" style=" display:none;" value="1" />
      </form>
      <form name=viewform action=http://paperpost.people.com.cn/comment/nodeComment.jsp method=post>
        <input  name="nodename1" type="hidden" id="nodename1" />
        <input name="channelname1" type="hidden" id="channelname1"  value="" />
        <input name="attr" type="hidden" value="2" />
        <input name="isnodecomm" type="hidden" value="1" />
        <INPUT type="hidden" value="1" name="view" />
        <INPUT type="hidden"  name="paperdate" />
	<input type=hidden  name="weburl" />
        <input name="nispagename" type="hidden" id="nispagename" />
        <input name="nodeid" type=hidden value="1922"><input name="nodename" type=hidden value="01"><input name="nodetype" type=hidden value="0"><input name="nodeurl" type=hidden value="null.htm"><input name="channelid" type=hidden value="1921"><input name="channelname" type=hidden value="人民日报">
      </form>
    </div>
    <!--留言部分-->
    
    <!--结束留言部分-->
  </div>
<!--版权部分-->
<div class="copyright">
  <p class="p1"><span class="red">人 民 网 版 权 所 有 ，未 经 书 面 授 权 禁 止 使 用</span><br />
      <span class="black">Copyright &copy; 1997-2013 by www.people.com.cn.
        all rights reserved</span><a href="http://www.hd315.gov.cn/beian/view.asp?bianhao=0102000101300040" target="_blank"><img src="../../../tplimg/gongshang.gif" width="40" style="float:right;margin:-45px 0px 0 10px;" height="48" alt="" align="middle" border="0" /></a></p>
</div>
<!--结束内容部分-->
<!--日报-->
<DIV  id="rmrbbx" style="display:none;position:absolute;top:50px;left:50%;margin-left:-40px;" onMouseOver="document.getElementById('rmrbbx').style.display = 'block';" onMouseOut="document.getElementById('rmrbbx').style.display = 'none';">
  <table width="100" border="0" cellpadding="0" cellspacing="1" bordercolor="#007CD2" bgcolor="#007CD2">
    <tr>
      <td bgcolor="#D8EFFF" style="padding: 3px;"><table width="100" border="0" cellpadding="0" cellspacing="0">
        <tr>
          <td bgcolor="#FFFFFF" style="padding: 1px;" valign="top"><table width="100" border="0" cellpadding="0" cellspacing="0" height="23">
            <tr>
              <td width="99" bgcolor="#ffffff" align="center" valign="top"><table width="85" border="0" cellpadding="0" cellspacing="0"  style="margin: 5px 0;">
                <tr>
                  <td height="20" align="left" class="fontstyle"><a href="../../../paperindex.htm" target="_blank">人民日报</a></td>
                </tr>
                <tr>
                  <td height="1"></td>
                </tr>
                <tr>
                  <td height="20" align="left" class="fontstyle"><a href="../../../../rmrbhwb/paperindex.htm" target="_blank">人民日报海外版</a></td>
                </tr>
                <tr>
                  <td height="1"></td>
                </tr>
                <tr>
                  <td height="20" align="left" class="fontstyle"><a href="http://www.huanqiu.com/" target="_blank">环球时报</a></td>
                </tr>
                <tr>
                  <td height="1"></td>
                </tr>
                <tr>
                  <td height="20" align="left" class="fontstyle"><a href="http://epaper.stcn.com/" target="_blank">证券时报</a></td>
                </tr>
                <tr>
                  <td height="1"></td>
                </tr>
              </table></td>
            </tr>
          </table></td>
        </tr>
      </table></td>
    </tr>
  </table>
</div>
<!--结束日报-->
<!--周报-->
<DIV  id="rmrbbx1" style="display:none;position:absolute;top:50px;left:50%;margin-left:75px;" onMouseOver="document.getElementById('rmrbbx1').style.display = 'block';" onMouseOut="document.getElementById('rmrbbx1').style.display = 'none';">
  <table width="100" border="0" cellpadding="0" cellspacing="1" bordercolor="#007CD2" bgcolor="#007CD2">
    <tr>
      <td bgcolor="#D8EFFF" style="padding: 3px;"><table width="100" border="0" cellpadding="0" cellspacing="0">
        <tr>
          <td bgcolor="#FFFFFF" style="padding: 1px;" valign="top"><table width="100" border="0" cellpadding="0" cellspacing="0" height="23">
            <tr>
              <td width="99" bgcolor="#ffffff" align="center" valign="top"><table width="85" border="0" cellpadding="0" cellspacing="0"  style="margin: 5px 0;">
                <tr>
                  <td height="20" align="left" class="fontstyle"><a href="../../../../gjjrb/paperindex.htm" target="_blank">国际金融报</a></td>
                </tr>
                <tr>
                  <td height="1"></td>
                </tr>
                <tr>
					<td height="20" align="left" class="fontstyle"><a href="../../../../zgnyb/paperindex.htm" target="_blank">中国能源报</a></td>
				</tr>						  
                <tr>
					<td height="1"></td>
                </tr>
                <tr>
                    <td height="20" align="left" class="fontstyle"><a href="../../../../jksb/paperindex.htm" target="_blank">健康时报</a></td>
                </tr>
                <tr>
                	<td height="1"></td>
                </tr>
                <tr>
                	<td height="20" align="left" class="fontstyle"><a href="../../../../fcyym/paperindex.htm" target="_blank">讽刺与幽默</a></td>
                </tr>
                <tr>
					<td height="1"></td>
                </tr>
                <tr>
                	<td height="20" align="left" class="fontstyle"><a href="../../../../zgcsb/paperindex.htm" target="_blank">中国城市报</a></td>
                </tr>
                <tr>
					<td height="1"></td>
                </tr>
              </table></td>
            </tr>
          </table></td>
        </tr>
      </table></td>
    </tr>
  </table>
</div>
<!--结束周报-->
<DIV  id="rmrbbx2" style="display:none;position:absolute;top:50px;left:50%;margin-left:190px;" onMouseOver="document.getElementById('rmrbbx2').style.display = 'block';" onMouseOut="document.getElementById('rmrbbx2').style.display = 'none';">
  <table width="110" border="0" cellpadding="0" cellspacing="1" bordercolor="#007CD2" bgcolor="#007CD2">
    <tr>
      <td bgcolor="#D8EFFF" style="padding: 3px;"><table width="110" border="0" cellpadding="0" cellspacing="0">
        <tr>
          <td bgcolor="#FFFFFF" style="padding: 1px;" valign="top"><table width="115" border="0" cellpadding="0" cellspacing="0" height="23">
            <tr>
              <td width="115" bgcolor="#ffffff" align="center" valign="top"><table width="115" border="0" cellpadding="0" cellspacing="0"  style="margin: 5px 0 0 3px;">
                <tr>
                  <td height="20" align="left" class="fontstyle"><a href="../../../../xwzx/paperindex.htm" target="_blank">新闻战线</a></td>
                </tr>
                <tr>
                  <td height="1"></td>
                </tr>
                <tr>
                  <td height="20" align="left" class="fontstyle"><a href="../../../../hqrw/paperindex.htm" target="_blank">环球人物</a></td>
                </tr>
                <tr>
                  <td height="1"></td>
                </tr>
                <tr>
                  <td height="20" align="left" class="fontstyle"><a href="../../../../rmlt/paperindex.htm" target="_blank">人民论坛</a></td>
                </tr>
                <tr>
                  <td height="1"></td>
                </tr>
                <tr>
                  <td height="20" align="left" class="fontstyle"><a href="../../../../rmzk/paperindex.htm" target="_blank">人民周刊</a></td>
                </tr>
                <tr>
                  <td height="1"></td>
                </tr>
                <tr>
                  <td height="20" align="left" class="fontstyle"><a href="../../../../zgjjzk/paperindex.htm" target="_blank">中国经济周刊</a></td>
                </tr>
                <tr>
                  <td height="1"></td>
                </tr>
                <tr>
                  <td height="20" align="left" class="fontstyle"><a href="../../../../xaq/paperindex.htm" target="_blank">新安全</a></td>
                </tr>
                <tr>
                  <td height="1"></td>
                </tr>
                <tr>
                   <td height="20" align="left" class="fontstyle"><a href="../../../../mszk/paperindex.htm" target="_blank">民生周刊</a></td>
                </tr>
                <tr>
                   <td height="1"></td>
                </tr>
                <tr>
                   <td height="20" align="left" class="fontstyle"><a href="http://history.people.com.cn/GB/198819/index.html" target="_blank">国家人文历史</a></td>
                </tr>
                <tr>
                   <td height="1"></td>
                </tr>
                 <tr>
                   <td height="20" align="left" class="fontstyle"><a href="../../../../zgby/paperindex.htm" target="_blank">中国报业</a></td>
                		</tr>
                		<tr>
                   			<td height="1"></td>
                </tr>
              </table></td>
            </tr>
          </table></td>
        </tr>
      </table></td>
    </tr>
  </table>
</div>
<!--结束杂志-->
<script language=JavaScript>
<!--
document.write("<div id=detail style=position:absolute;width:300px;></div>");
//-->
</script>
<!-------rqdh版面导航------>
<div id=daydh style="display:none; position:absolute; left:50%;margin-left:-100px; top:110px; filter:alpha(opacity=90);"  onmouseover="document.getElementById('daydh').style.display='block';" >
  <form name=CLD style="padding:0px;margin:0px;">
    <table width="210" border="0" cellpadding="0" cellspacing="1" bordercolor="#007CD2" bgcolor="#007CD2">
      <tr>
        <td bgcolor="#D8EFFF" style="padding: 3px;"><table cellspacing=0 cellpadding=0 width="100%" align=center border=0 bgcolor="#D8EFFF">
          <tr>
            <td><table width="100%" align=center border="0" cellpadding="1" cellspacing="1">
              <tr class="default" align=center>
                <td height=15 colspan=7 bgcolor="#FFFFFF"><table width="100%" border="0" cellpadding="2" cellspacing="0">
                  <tr align="center">
                    <td align="left" nowrap><img src="../../../../../../tiaoshidomain/applications/mp/file_upload/enp/1/121.files/d1.gif" width="7" height="11" style="cursor:hand;" onClick="turnpage(SY,0)" /></td>
                    <td><select class=jumpmenu onChange=changeMPCld() name=SY>
                      <script language=JavaScript>
					for(i=2006;i<2051;i++)
					document.write('<option>'+i+'</option>')
        			</script>
                    </select>
                    </td>
                    <td><img src="../../../../../../tiaoshidomain/applications/mp/file_upload/enp/1/121.files/d.gif" width="7" height="11" style="cursor:hand;" onClick="turnpage(SY,1)" /></td>
                    <td align="center" nowrap><img src="../../../../../../tiaoshidomain/applications/mp/file_upload/enp/1/121.files/d1.gif" width="7" height="11" style="cursor:hand;" onClick="turnpage(SM,0)" /></td>
                    <td><select class=jumpmenu onChange=changeMPCld() name=SM>
                      <script language=JavaScript>
				<!--
					for(i=1;i<13;i++) document.write('<option>'+i+'</option>')
				//-->
        			</script>
                    </select>
                    </td>
                    <td><img src="../../../../../../tiaoshidomain/applications/mp/file_upload/enp/1/121.files/d.gif" width="7" height="11" style="cursor:hand;" onClick="turnpage(SM,1)" /></td>
                    <td align="right" nowrap><strong><font id=GZ fface="Arial, Helvetica, sans-serif"></font></strong></td>
                  </tr>
                </table></td>
              </tr>
              <tr align=middle bgcolor="#FFFFFF" class="default">
                <td bgcolor="#027CD1" align="center" class="fontstyle01"><b><font face="Arial, Helvetica, sans-serif">日</font></b></td>
                <td bgcolor="#027CD1" align="center" class="fontstyle01"><b><font face="Arial, Helvetica, sans-serif">一</font></b></td>
                <td bgcolor="#027CD1" align="center" class="fontstyle01"><b><font face="Arial, Helvetica, sans-serif">二</font></b></td>
                <td bgcolor="#027CD1" align="center" class="fontstyle01"><b><font face="Arial, Helvetica, sans-serif">三</font></b></td>
                <td bgcolor="#027CD1" align="center" class="fontstyle01"><b><font face="Arial, Helvetica, sans-serif">四</font></b></td>
                <td bgcolor="#027CD1" align="center" class="fontstyle01"><b><font face="Arial, Helvetica, sans-serif">五</font></b></td>
                <td bgcolor="#027CD1" align="center" class="fontstyle01"><b><font face="Arial, Helvetica, sans-serif">六</font></b> </td>
              </tr>
              <script language=JavaScript>
		<!--
			var gNum;
			for(i=0;i<6;i++)
			{
				document.write('<tr align=center>');
				for(j=0;j<7;j++)
				{
					gNum = i*7+j;
					document.write('<td  bgcolor="#FFFFFF" class="default" align=center id="GD' + gNum +'" style="cursor: default;" width="14%"><a href="" id="CD' + gNum + '"><span class="date" style="font-family:Verdana, Arial;font-size:11px;"><font _onMouseOver="mOvr(' + gNum +')" onMouseOut="mOut()" id="SD' + gNum +'"');
					document.write('></font></span></a><br><font id="LD' + gNum + '" size=2 class=pt9 style=display:none></font></td>');
				}
				document.write('</tr>');
			}
		//-->
        	</script>
            </table></td>
          </tr>
        </table></td>
      </tr>
      <tr>
        <td align="center" height="22"><a href="#" onClick="autoShowDate();">关闭</a></td>
      </tr>
    </table>
  </form>
</div>
<!-------rqdh版面导航END------>
<!-------文章显示标题开始------>
<div style="display:none">
  <table width="265" border="0" cellspacing="0" cellpadding="0" style="margin-top:3px;">

  <tr>
	<td width="16" align="left"><img src="1.files/icon07.jpg" /></td>
	<td width="271" align="left" class="fontstyle" height="22"> 
<a href=nw.D110000renmrb_20171016_1-01.htm><div style="display:inline" id=mp_nw.D110000renmrb_20171016_1-01>《习近平关于社会主义文化建设论述摘编》出版发行</div></a>
	</td>
  </tr>
  <tr><td background="1.files/dian01.jpg" colspan="2" height="1"></td></tr>
  <tr>
	<td width="16" align="left"  bgcolor="#D8EFFF"><img src="1.files/icon07.jpg" /></td>
	<td width="271" align="left" class="fontstyle" height="22"  bgcolor="#D8EFFF">
<a href=nw.D110000renmrb_20171016_2-01.htm><div style="display:inline"  id=mp_nw.D110000renmrb_20171016_2-01>中共中央召开党外人士座谈会<br>征求对中共十九大报告的意见</div></a>
	</td>
  </tr>
  <tr><td background="1.files/dian01.jpg" colspan="2" height="1"></td></tr>
  <tr>
	<td width="16" align="left"><img src="1.files/icon07.jpg" /></td>
	<td width="271" align="left" class="fontstyle" height="22"> 
<a href=nw.D110000renmrb_20171016_3-01.htm><div style="display:inline" id=mp_nw.D110000renmrb_20171016_3-01>党的十九大代表陆续抵京</div></a>
	</td>
  </tr>
  <tr><td background="1.files/dian01.jpg" colspan="2" height="1"></td></tr>
  <tr>
	<td width="16" align="left"  bgcolor="#D8EFFF"><img src="1.files/icon07.jpg" /></td>
	<td width="271" align="left" class="fontstyle" height="22"  bgcolor="#D8EFFF">
<a href=nw.D110000renmrb_20171016_4-01.htm><div style="display:inline"  id=mp_nw.D110000renmrb_20171016_4-01>砥砺奋进 铸就辉煌</div></a>
	</td>
  </tr>
  <tr><td background="1.files/dian01.jpg" colspan="2" height="1"></td></tr>
  <tr>
	<td width="16" align="left"><img src="1.files/icon07.jpg" /></td>
	<td width="271" align="left" class="fontstyle" height="22"> 
<a href=nw.D110000renmrb_20171016_5-01.htm><div style="display:inline" id=mp_nw.D110000renmrb_20171016_5-01>党的十八大以来大事记</div></a>
	</td>
  </tr>
  <tr><td background="1.files/dian01.jpg" colspan="2" height="1"></td></tr>

</table>
</div>
<!-------文章显示标题结束------>
<img src="../../../tplimg/left_ico.gif" style="display:none;" /> <img src="../../../tplimg/right_ico.gif" style="display:none;" /> <img src="../../../tplimg/ico10.gif" style="display:none;" /> <img src="../../../../../../tiaoshidomain/applications/mp/file_upload/enp/1/../../../tplimg/ico8.gif" style="display:none;" /> <img src="../../../../../../tiaoshidomain/applications/mp/file_upload/enp/1/../../../tplimg/ico9.gif" style="display:none;" /> <img src="../../../tplimg/ti.gif" style="display:none;" /> <img src="../../../tplimg/fb.gif" style="display:none;" />
</div></div>
<script>writeErWeiMa();</script>
<iframe id="tempForm"  
            name="tempForm" src='' frameborder=0 width=0
            scrolling=no height=0></iframe>
</body>
</html>
<script language="javascript">
if(document.getElementById('ozoom')!=null&&document.getElementById('ozoom').offsetHeight<=357)
	document.getElementById('ozoom').style.height = '480px';
</script>
<SCRIPT language=Javascript src="../../../../juas/commons/js/disname2.js"></SCRIPT>
<SCRIPT language=Javascript src="../../../tplimg/webdig_test.js"></SCRIPT>

'''

html2 = """

<!DOCTYPE html PUBLIC "-//W3C//DTD XHTML 1.0 Transitional//EN" "http://www.w3.org/TR/xhtml1/DTD/xhtml1-transitional.dtd">
<html xmlns="http://www.w3.org/1999/xhtml" lang="utf-8">
<head>
<meta http-equiv="content-type" content="text/html;charset=utf-8" />
<meta http-equiv="content-language" content="utf-8" />
<meta name="robots" content="all" />
<meta name="author" content='' />
<meta name="copyright" content="" />
<meta name="description" content="" />
<meta name="keywords" content="" />
<META name='filetype' content='0'>
<META name='publishedtype' content='1'>
<META name='pagetype' content='2'>
<META name='catalogs' content='XTW_0009002'>
<link href="../../../tplimg/mulu_m1.css" type="text/css" rel="stylesheet" rev="stylesheet" media="all" />
<title>人民日报-人民网</title>
<script language="javascript">
function killErrors() {
    return true;
}
window.onerror = killErrors;
</script>
<SCRIPT language=Javascript src="../../../tplimg/prototype.js"></SCRIPT>
<SCRIPT language=Javascript src="../../../tplimg/mp.js"></SCRIPT>
<SCRIPT language=Javascript src="../../../tplimg/calendar2.js"></SCRIPT>
<SCRIPT language=Javascript src="../../../tplimg/range.js"></SCRIPT>
<SCRIPT language=Javascript src="../../../tplimg/lib.js"></SCRIPT>
<SCRIPT language=Javascript src="../../../tplimg/dzb.js"></SCRIPT>
<SCRIPT language=Javascript src="../../../tplimg/new.js"></SCRIPT>
<SCRIPT language=Javascript src="../../../tplimg/jspoints.js"></SCRIPT>
<style>
a.ared:link {
	font-size: 12px;
	color: #FF0000;
	text-decoration: none;
}
a.ared:visited {
	font-size: 12px;
	color: #FF0000;
	text-decoration: none;
}
a.ared:hover {
	font-size: 12px;
	color: #006699;
	text-decoration: none;
}
.un {
	color:#004677;
}
.right_title1 {

}
.right_title2 {

}
.right_title-name {
	padding:3px 5px 0px 5px;
	float:left;
	width:188px;
	line-height:24px;
}
.right_title-pdf {
	padding:5px 5px 0px 0px;
	float:right;
}
</style>
<style>
.head_c2{display:block;float:left;margin:0 15px 0 0;width:91px;color:#004873;height:21px;padding:0 2px 0 2px;background:#fff;border:1px solid #66B1EB;text-align:left;}
.head_c3{float:right; margin:2px 0 0 0;}
</style>
<script type="text/javascript">
function nTabs(tabObj,obj){
	var tabList = document.getElementById(tabObj).getElementsByTagName("li");
	for(i=0; i <tabList.length; i++)
	{
		if (tabList[i].id == obj.id)
		{
			document.getElementById(tabObj+"_Title"+i).className = "active";
    		document.getElementById(tabObj+"_Content"+i).style.display = "block";
		}else{
			document.getElementById(tabObj+"_Title"+i).className = "normal";
			document.getElementById(tabObj+"_Content"+i).style.display = "none";
		}
	}
}

function getStringLength(str)
{
	if (str == null || str == "")
		return 0;
	else
		return str.length;
}

function view(str)
{
 var len = 20;
 var ret = "";
str=str.replace(/<br>/gi," ");
 if(getStringLength(str) > len)
  ret = "<span title='" + str + "'>" + str.substring(0, len) + "...</span>";
 else
  ret = str;
 return ret;
}
function zoomIn() {
 newZoom= parseInt(ozoom.style.zoom)+10+'%'
 ozoom.style.zoom =newZoom;
 }
function zoomOut() {
 newZoom= parseInt(ozoom.style.zoom)-10+'%'
 ozoom.style.zoom =newZoom;
 }

 function submitCheck()
 {
 	 if(document.all("content1").value.length>1000){
	 alert("评论内容超过1000字！");
	 return false;
	 }
	 if(document.all("content1").value.indexOf("<script")!=-1 ||document.all("content1").value.indexOf("<\/")!=-1){
	 alert("评论内容含有特殊字符!");
	 return false;
	 }
	 if(document.all("content1").value == "")
	 {
	 alert("必须填写评论内容！");
	 return false;
	 }
	 document.commentform.paperdate.value = document.getElementById("paperdatediv").innerText.replace(/(^\s*)|(\s*$)/g, "");
	 document.commentform.nispagename.value = escape(document.getElementById("pageNameForJiaoHu").innerText.replace(/(^\s*)|(\s*$)/g, ""));
	var isnodecomment = document.commentform.isnodecomm.value;
	document.commentform.isGuest.value = document.commentform.isGuest.checked;
	document.commentform.rankRadio.value = document.commentform.rankRadio.checked;
	document.commentform.content.value=escape(document.commentform.content1.value);
	document.commentform.author.value=escape(document.commentform.author1.value);
	document.commentform.weburl.value=location.href;

	if (document.commentform.channelname1.value == "")
	{

		document.commentform.channelname1.value = document.commentform.channelname.value;
		document.commentform.nodename1.value = document.commentform.nodename.value;
		document.commentform.channelname.value=escape(document.commentform.channelname.value);
		document.commentform.nodename.value=escape(document.commentform.nodename.value);
	}
	else{

		document.commentform.channelname.value = document.commentform.channelname1.value;
		document.commentform.nodename.value = document.commentform.nodename1.value;
		document.commentform.channelname.value=escape(document.commentform.channelname.value);
		document.commentform.nodename.value=escape(document.commentform.nodename.value);
	}
 	document.commentform.submit();
 	alert("您的留言已经成功提交！");
 	document.commentform.content1.value="";
 }
 function viewComment(){
 		 document.viewform.paperdate.value = document.getElementById("paperdatediv").innerText.replace(/(^\s*)|(\s*$)/g, "");
		 document.viewform.nispagename.value = escape(document.getElementById("pageNameForJiaoHu").innerText.replace(/(^\s*)|(\s*$)/g, ""));
 	 if (document.viewform.channelname1.value =="")
	 {

				document.viewform.channelname1.value = document.viewform.channelname.value;
				document.viewform.nodename1.value = document.viewform.nodename.value;
				document.viewform.nodename.value=escape(document.viewform.nodename.value);
				document.viewform.channelname.value=escape(document.viewform.channelname.value);
		}else
		{

				document.viewform.channelname.value = document.viewform.channelname1.value;
				document.viewform.nodename.value = document.viewform.nodename1.value;
				document.viewform.nodename.value=escape(document.viewform.nodename.value);
				document.viewform.channelname.value=escape(document.viewform.channelname.value);
		}
		document.viewform.action="http://paperpost.people.com.cn/comment/nodeComment.jsp";
		document.viewform.target="";
		document.viewform.weburl.value=location.href;
 		 document.viewform.submit();
 	}

	 function showComment(){
 		document.viewform.paperdate.value = document.getElementById("paperdatediv").innerText.replace(/(^\s*)|(\s*$)/g, "");
 	 if (document.viewform.channelname1.value =="")
	 {

				document.viewform.channelname1.value = document.viewform.channelname.value;
				document.viewform.nodename1.value = document.viewform.nodename.value;
				document.viewform.nodename.value=escape(document.viewform.nodename.value);
				document.viewform.channelname.value=escape(document.viewform.channelname.value);
		}else
		{

				document.viewform.channelname.value = document.viewform.channelname1.value;
				document.viewform.nodename.value = document.viewform.nodename1.value;
				document.viewform.nodename.value=escape(document.viewform.nodename.value);
				document.viewform.channelname.value=escape(document.viewform.channelname.value);
		}
		 document.viewform.action="http://paperpost.people.com.cn/comment/nodeCommentList.jsp";
		 document.viewform.target="NodeCommentFrame";
 		 document.viewform.submit();

 	}

 function dohit(){
  if (document.readyState == 'complete' )
     {
  document.frames("hitClickIframe").document.hitform.url.value = location.href;
  if(document.commentform.isnodecomm.value == '1'){
  document.frames("hitClickIframe").document.hitform.nodeid.value = document.commentform.nodeid.value;
  }else{
  document.frames("hitClickIframe").document.hitform.articleid.value = document.commentform.articleid.value;
  }
  document.frames("hitClickIframe").document.hitform.submit();
  document.hitClickIframe.style.display="none";
  }else
  window.setTimeout("dohit()","300");
}
	function getDate()
	{
		  var url = window.location.pathname.split('/');
		  var length = url.length;
		  document.getElementById("newsIframe").src = "http://paperpost.people.com.cn/"+url[1]+"-"+url[length-3]+"-"+url[length-2]+".html";
	}
</script>
</head>
<SPAN id=leveldiv title=点击查看内容
style="BORDER-TOP-WIDTH: 0px; BORDER-LEFT-WIDTH: 0px; Z-INDEX: 100; LEFT: 233px; BORDER-BOTTOM-WIDTH: 0px; WIDTH: 210px; CURSOR: hand; POSITION: absolute; TOP: 123px; HEIGHT: 34px; BORDER-RIGHT-WIDTH: 0px"></SPAN>
<body onLoad="createStarsPage();getDate();initialize();initMPPage();loadWowi();dohit();showArtPics();">
<div class="div_bg"><div class="div_center">
  <!--左侧版面图部分-->
  <div class="left_c">
    <div class="ban">
      <div>
        <map name=PagePicMap><Area coords="2,53,397,53,397,474,2,474" shape="polygon" href="nw.D110000renmrb_20171018_1-07.htm"><Area coords="128,138,128,94,6,94,6,138,6,218,128,218" shape="polygon" href="nw.D110000renmrb_20171018_2-07.htm"><Area coords="262,198,262,94,136,94,136,216,262,216" shape="polygon" href="nw.D110000renmrb_20171018_3-07.htm"><Area coords="393,138,393,94,271,94,271,138,271,218,393,218" shape="polygon" href="nw.D110000renmrb_20171018_4-07.htm"><Area coords="63,413,62,413,62,278,86,278,86,229,6,229,6,278,6,431,45,431,45,431,63,431" shape="polygon" href="nw.D110000renmrb_20171018_5-07.htm"><Area coords="393,431,393,431,393,431,393,278,393,229,310,229,310,278,335,278,335,431,373,431,375,431,375,431,393,431" shape="polygon" href="nw.D110000renmrb_20171018_6-07.htm"><Area coords="6,444,128,444,128,563,6,563" shape="polygon" href="nw.D110000renmrb_20171018_7-07.htm"><Area coords="262,489,262,444,136,444,136,489,136,563,262,563" shape="polygon" href="nw.D110000renmrb_20171018_8-07.htm"><Area coords="271,444,393,444,393,563,271,563" shape="polygon" href="nw.D110000renmrb_20171018_9-07.htm"></map><img  width=400 height=575 src=../../../page/2017-10/18/07/rmrb2017101807_b.jpg border=0 USEMAP=#PagePicMap></div>
    </div>
    <div class="ban_t">
      <div>
        <ul>
          <li>
            07版:决胜全面小康 开启新的征程·党的十九大特别报道
            &nbsp;
            <a href=../../../page/2017-10/18/07/rmrb2017101807.pdf><IMG src="../../../tplimg/ico4.gif" border=0></a>
            PDF版下载 <span>
              <a class=preart href="nbs.D110000renmrb_06.htm"><img src='../../../tplimg/left_ico.gif' border=0 /> 上一版</a>&nbsp;&nbsp;<a class=preart href="nbs.D110000renmrb_08.htm">下一版 <img src='../../../tplimg/right_ico.gif' border=0 /></a>
            </span></li>
        </ul>
      </div>
    </div>
    <div class="tool"><input type="image" onclick="javascript:window.open('http://ardownload.adobe.com/pub/adobe/reader/win/8.x/8.1/chs/AdbeRdr810_zh_CN.exe')" src="../../../tplimg/button.gif" name="" style="float:left;padding-left:40px"/><img src="../../../tplimg/button1.gif" style="display:none"/><img src="../../../tplimg/button2.gif"  style="display:none"/><a href="node_1921.htm"><img src="../../../tplimg/button3.gif" border="0" style="float:right;padding-right:40px" /></a></div>
  <!-- -->
  <!--版面打分-->
	<div class="title da_t" style="width:416px;margin-top:10px;margin-left:10px;float:none;margin-right:0px;">
      <div style="width:404px;">我给版面打分</div>
    </div>
    <div class="pai" style="width:396px;height:50px;border:1px solid #7DBCEF;padding-left:20px">
      <FORM id=pointsform name=pointsform action="" method=post
                  target=pointsIframe  style=" display:none;">
                  <INPUT type=hidden name=paperdate />
        <INPUT
                              type=hidden name=nodename1 />
        <INPUT type=hidden
                              name=channelname1 />
        <INPUT type=hidden name=title1 />
        <INPUT type=hidden value=2 name=attr />
        <!--attr 2 数字报刊 1 翔宇-->
        <INPUT type=hidden value=1
                              name=isnodecomm />
        <!--isnodecomm 2 文章评论 1 版面或栏目评论-->
        <INPUT
                              type=hidden value=2 name=pointtype />
        <!--pointtype 2 计算平均分（现阶段必须设为2） 1 统计类型-->
        <!--此列为插件生成的组件-->
        <input name="nodeid" type=hidden value="1928"><input name="nodename" type=hidden value="07"><input name="nodetype" type=hidden value="0"><input name="nodeurl" type=hidden value="null.htm"><input name="channelid" type=hidden value="1921"><input name="channelname" type=hidden value="人民日报">
        <div id="paperdatediv">
          2017-October-18
        </div>
      </FORM>
      <form name="pForm" id="pForm">
        <input type="radio" name="pointVal" value="1" onClick="pv(1)"/>
        1分&nbsp;&nbsp;
        <input type="radio" name="pointVal" value="2" onClick="pv(2)" />
        2分&nbsp;&nbsp;
        <input type="radio" name="pointVal" value="3" onClick="pv(3)" checked="checked" />
        3分&nbsp;&nbsp;
        <input type="radio" name="pointVal" value="4" onClick="pv(4)" />
        4分&nbsp;&nbsp;
        <input type="radio" name="pointVal" value="5" onClick="pv(5)" />
        5分 &nbsp; <img src="../../../tplimg/ti.gif"  alt="" border="0" style="cursor:hand " onclick="submitPoints(document.pForm.Input2.value);" />
        <!--<p>本版得分:<span>4.1分</span>(共有<span>19</span>位网友打分)</p>-->
        <input name="Input2" type="hidden" value="3" />
      </form>
      <iframe id="pointsIframe"
            name="pointsIframe" src="about:blank" frameborder=0 width=375
            scrolling=no height=30></iframe>
    </div>
    <div class="title"style="margin-top:10px">
      <div>新闻排行榜</div>
    </div>
    <div class="pai">
      <div>
        <!--
	    <span>1</span><a href="">我看到了你，也看到了我的种点</a><br />
		<span>2</span><a href="">我看到了你，也看到了我的种点</a><br />
		<span>3</span><a href="">我看到了你，也看到了我的种点</a><br />
		<span>4</span><a href="">我看到了你，也看到了我的种点</a><br />
		<span>5</span><a href="">我看到了你，也看到了我的种点</a><br />
		<span>6</span><a href="">我看到了你，也看到了我的种点</a><br />
		<span>7</span><a href="">我看到了你，也看到了我的种点</a><br />
		<span>8</span><a href="">我看到了你，也看到了我的种点</a><br />
		<span>9</span><a href="">我看到了你，也看到了我的种点</a><br />
		<span>10</span><a href="">我看到了你，也看到了我的种点</a><br />-->
        <iframe name="newsIframe" id="newsIframe" style="font-size:12px;" border="0" width="95%" height="240" frameborder="0" src=""></iframe>
        <br />
        <iframe name="hitClickIframe" style="font-size:12px;" id="hitClickIframe" height="0" width="0" border="0" frameborder="0" src="../../../tplimg/hitPost.htm"></iframe>
      </div>
    </div>
    <div class="title">
      <div id="bqsm">版权声明</div>
    </div>
    <div class="pai f_link" id="bqsm_nr" style="line-height:25px">　　《人民日报》（电子版）的一切内容(包括但不限于文字、图片、PDF、图表、标志、标识、商标、版面设计、专栏目录与名称、内容分类标准以及为读者提供的任何信息)仅供人民网读者阅读、学习研究使用，未经人民网股份有限公司及/或相关权利人书面授权，任何单位及个人不得将《人民日报》（电子版）所登载、发布的内容用于商业性目的，包括但不限于转载、复制、发行、制作光盘、数据库、触摸展示等行为方式，或将之在非本站所属的服务器上作镜像。否则，人民网股份有限公司将采取包括但不限于网上公示、向有关部门举报、诉讼等一切合法手段，追究侵权者的法律责任。</div><!-- -->  
  </div>
  <!--右侧目录部分-->
  <div class="right_c">
    <div style="margin:0 auto;width:530px;height:70px;text-align:right;padding:8px 0 0 20px;">
      <div style="height:70px;">
        <div style="float:left; width:390px;">
          <div style="height:23px; padding:10px 0px;">
            <div onMouseOver="document.getElementById('rmrbbx').style.display = 'block';" onMouseOut="document.getElementById('rmrbbx').style.display = 'none';" class="head_c2">
              <div style="float:left">日&nbsp;报</div>
              <div  class="head_c3"><img src="../../../tplimg/ico10.gif" border="0" alt="" /></div>
            </div>
            <div onMouseOver="document.getElementById('rmrbbx1').style.display = 'block';" onMouseOut="document.getElementById('rmrbbx1').style.display = 'none';" class="head_c2">
              <div style="float:left">周&nbsp;报</div>
              <div  class="head_c3"><img src="../../../tplimg/ico10.gif" border="0" alt="" /></div>
            </div>
            <div onMouseOver="document.getElementById('rmrbbx2').style.display = 'block';" onMouseOut="document.getElementById('rmrbbx2').style.display = 'none';" class="head_c2">
              <div style="float:left">杂&nbsp;志</div>
              <div  class="head_c3"><img src="../../../tplimg/ico10.gif" border="0" alt="" /></div>
            </div>
          </div>
          <div style="text-align:left;">
            <div style="float:left; width:370px;"><div id="riqi_"  style="float:left;">
            人民日报
            2017年10月18日 星期三
            </div><div id="peopledata" style="float:right; display:none" class="peopledata"></div>
		   <div style="float:left; color:#004773; display:none; padding-left:5px;" id="infowelcome">&nbsp;欢迎您：<span id="disname" class="un">用户ID名称</span></div></div>
         </div>
        </div>
        <div style="float:left;"><a href="http://www.people.com.cn"><img src="../../../tplimg/logo.jpg" border="0" alt="人民网" /></a></div>
      </div>
    </div>
    <div style="margin:0 auto; color:#004773; height:20px; width:525px; padding:8px 10px 10px 20px; text-align: left;float:left;">
      <div style="float:left; width:50px;">往期回顾</div>
      <div style="float:left; width:60px; padding-top:2px;"><a onClick="autoShowDate();" style="cursor:hand;" title="鼠标点击，显示日历牌"><img src="../../../tplimg/ico1.gif" border="0" alt="" /></a></div>
      <div style="float:left; width:80px;display:none" id="paperSearch"><a href="http://search.people.com.cn/rmw/GB/bkzzsearch/index.jsp" target="_blank">人民网检索</a></div>
      <div style="float:left; display:none; font-weight:bold;" id="usercenter"><a href="../../../notice/notice.htm" class="ared" target="_blank">《人民日报》数字报取消收费的通知</a></div>
      <div style="float:right; text-align:right;">&nbsp;<a href="#" onClick="goPrePeriod()">&lt;上一期</a>&nbsp;&nbsp;&nbsp;<a href="#" onClick="goNextPeriod()">下一期&gt;</a></div>
    </div>
    <div class="mobilepaper" id="mobilepaper"></div>
    <!--目录与标题-->
    <DIV id="ozoom" style="zoom:100%;">
      <div class="list_t">
        <!--新闻标题-->
        <div class="list_l">
          <div class="l_t">
            07版:决胜全面小康 开启新的征程·党的十九大特别报道
          </div>
          <div class="l_b" id="titleImgUp"><a href="#"><img src="../../../tplimg/jiao1.gif" border="0" alt="" /></a></div>
          <div class="l_c">
            <div id="titleList"  style="height:440px;overflow:hidden;">
              <!-- list starting -->
              <ul>


<li>
<a href=nw.D110000renmrb_20171018_1-07.htm><script>document.write(view("回应人民新期待  "))</script></a></li>
<li class="one">
 <a href=nw.D110000renmrb_20171018_2-07.htm><script>document.write(view("栋梁之材涌出来  "))</script></a></li>
<li>
       <!-- 视频-->
        <a style="MARGIN-LEFT: -18px;position:relative;top:4px" href=nw.D110000renmrb_20171018_3-07.htm><img src="../../../tplimg/video.png" height="16px" border="0"/></a>
       <!-- 文章-->
       <!-- 专题-->
<a href=nw.D110000renmrb_20171018_3-07.htm><script>document.write(view("就业好了一切好  "))</script></a></li>
<li class="one">
 <a href=nw.D110000renmrb_20171018_4-07.htm><script>document.write(view("跨省打工钱包鼓  "))</script></a></li>
<li>
       <!-- 视频-->
        <a style="MARGIN-LEFT: -18px;position:relative;top:4px" href=nw.D110000renmrb_20171018_5-07.htm><img src="../../../tplimg/video.png" height="16px" border="0"/></a>
       <!-- 文章-->
       <!-- 专题-->
<a href=nw.D110000renmrb_20171018_5-07.htm><script>document.write(view("低保成了定心丸  "))</script></a></li>
<li class="one">
       <!-- 视频-->
        <a style="MARGIN-LEFT: -18px;position:relative;top:4px" href=nw.D110000renmrb_20171018_6-07.htm><img src="../../../tplimg/video.png" height="16px" border="0"/></a>
       <!-- 文章-->
       <!-- 专题-->
 <a href=nw.D110000renmrb_20171018_6-07.htm><script>document.write(view("小镇能做大手术  "))</script></a></li>
<li>
       <!-- 视频-->
        <a style="MARGIN-LEFT: -18px;position:relative;top:4px" href=nw.D110000renmrb_20171018_7-07.htm><img src="../../../tplimg/video.png" height="16px" border="0"/></a>
       <!-- 文章-->
       <!-- 专题-->
<a href=nw.D110000renmrb_20171018_7-07.htm><script>document.write(view("搬出棚户笑开颜  "))</script></a></li>
<li class="one">
 <a href=nw.D110000renmrb_20171018_8-07.htm><script>document.write(view("青山绿水寿星多  "))</script></a></li>
<li>
       <!-- 视频-->
        <a style="MARGIN-LEFT: -18px;position:relative;top:4px" href=nw.D110000renmrb_20171018_9-07.htm><img src="../../../tplimg/video.png" height="16px" border="0"/></a>
       <!-- 文章-->
       <!-- 专题-->
<a href=nw.D110000renmrb_20171018_9-07.htm><script>document.write(view("生活好了爱唱歌  "))</script></a></li>

</ul><!-- list endding -->
            </div>
          </div>
          <div style="width:316px;height:10px;background:#D0EBFE;border-top:1px solid #94D5FF;text-align:center;padding:2px 0 0 0;" id="titleImgDown" align="center"><a href="#"><img src="../../../tplimg/jiao.gif" border="0" alt="" /></a></div>
        </div>
        <!--版面目录-->
        <div class="list_r">
          <div class="l_t l_t1">版面目录</div>
          <div class="l_b l_b1" id="pageImgUp"><a href="#"><img src="../../../tplimg/jiao1.gif" border="0" alt="" /></a></div>
          <div class="l_c l_c1">
            <div id="pageList" style="overflow:hidden;height:440px;">
              <!-- list starting -->
              <ul>
<div class="right_title1">
<div class="right_title-name"><a id=pageLink href=nbs.D110000renmrb_01.htm>第01版：要闻</a></div>
<div class="right_title-pdf"><a href=../../../page/2017-10/18/01/rmrb2017101801.pdf><img src="../../../tplimg/ico3.gif" border=0 /></a></div>
</div>
<div class="right_title2">
<div class="right_title-name"><a id=pageLink href=nbs.D110000renmrb_02.htm>第02版：要闻</a></div>
<div class="right_title-pdf"><a href=../../../page/2017-10/18/02/rmrb2017101802.pdf><img src="../../../tplimg/ico3.gif" border=0 /></a></div>
</div>
<div class="right_title1">
<div class="right_title-name"><a id=pageLink href=nbs.D110000renmrb_03.htm>第03版：要闻</a></div>
<div class="right_title-pdf"><a href=../../../page/2017-10/18/03/rmrb2017101803.pdf><img src="../../../tplimg/ico3.gif" border=0 /></a></div>
</div>
<div class="right_title2">
<div class="right_title-name"><a id=pageLink href=nbs.D110000renmrb_04.htm>第04版：要闻</a></div>
<div class="right_title-pdf"><a href=../../../page/2017-10/18/04/rmrb2017101804.pdf><img src="../../../tplimg/ico3.gif" border=0 /></a></div>
</div>
<div class="right_title1">
<div class="right_title-name"><a id=pageLink href=nbs.D110000renmrb_05.htm>第05版：决胜全面小康 开启新的征程·党的十九大特别报道</a></div>
<div class="right_title-pdf"><a href=../../../page/2017-10/18/05/rmrb2017101805.pdf><img src="../../../tplimg/ico3.gif" border=0 /></a></div>
</div>
<div class="right_title2">
<div class="right_title-name"><a id=pageLink href=nbs.D110000renmrb_06.htm>第06版：决胜全面小康 开启新的征程·党的十九大特别报道</a></div>
<div class="right_title-pdf"><a href=../../../page/2017-10/18/06/rmrb2017101806.pdf><img src="../../../tplimg/ico3.gif" border=0 /></a></div>
</div>
<div class="right_title1">
<div class="right_title-name"><a id=pageLink href=./nbs.D110000renmrb_07.htm>第07版：决胜全面小康 开启新的征程·党的十九大特别报道</a></div>
<div class="right_title-pdf"><a href=../../../page/2017-10/18/07/rmrb2017101807.pdf><img src="../../../tplimg/ico3.gif" border=0 /></a></div>
</div>
<div class="right_title2">
<div class="right_title-name"><a id=pageLink href=nbs.D110000renmrb_08.htm>第08版：决胜全面小康 开启新的征程·党的十九大特别报道</a></div>
<div class="right_title-pdf"><a href=../../../page/2017-10/18/08/rmrb2017101808.pdf><img src="../../../tplimg/ico3.gif" border=0 /></a></div>
</div>
<div class="right_title1">
<div class="right_title-name"><a id=pageLink href=nbs.D110000renmrb_09.htm>第09版：决胜全面小康 开启新的征程·党的十九大特别报道 </a></div>
<div class="right_title-pdf"><a href=../../../page/2017-10/18/09/rmrb2017101809.pdf><img src="../../../tplimg/ico3.gif" border=0 /></a></div>
</div>
<div class="right_title2">
<div class="right_title-name"><a id=pageLink href=nbs.D110000renmrb_10.htm>第10版：决胜全面小康 开启新的征程·党的十九大特别报道 </a></div>
<div class="right_title-pdf"><a href=../../../page/2017-10/18/10/rmrb2017101810.pdf><img src="../../../tplimg/ico3.gif" border=0 /></a></div>
</div>
<div class="right_title1">
<div class="right_title-name"><a id=pageLink href=nbs.D110000renmrb_11.htm>第11版：决胜全面小康 开启新的征程·党的十九大特别报道 </a></div>
<div class="right_title-pdf"><a href=../../../page/2017-10/18/11/rmrb2017101811.pdf><img src="../../../tplimg/ico3.gif" border=0 /></a></div>
</div>
<div class="right_title2">
<div class="right_title-name"><a id=pageLink href=nbs.D110000renmrb_12.htm>第12版：决胜全面小康 开启新的征程·党的十九大特别报道 </a></div>
<div class="right_title-pdf"><a href=../../../page/2017-10/18/12/rmrb2017101812.pdf><img src="../../../tplimg/ico3.gif" border=0 /></a></div>
</div>
<div class="right_title1">
<div class="right_title-name"><a id=pageLink href=nbs.D110000renmrb_13.htm>第13版：要闻</a></div>
<div class="right_title-pdf"><a href=../../../page/2017-10/18/13/rmrb2017101813.pdf><img src="../../../tplimg/ico3.gif" border=0 /></a></div>
</div>
<div class="right_title2">
<div class="right_title-name"><a id=pageLink href=nbs.D110000renmrb_14.htm>第14版：理论</a></div>
<div class="right_title-pdf"><a href=../../../page/2017-10/18/14/rmrb2017101814.pdf><img src="../../../tplimg/ico3.gif" border=0 /></a></div>
</div>
<div class="right_title1">
<div class="right_title-name"><a id=pageLink href=nbs.D110000renmrb_15.htm>第15版：要闻</a></div>
<div class="right_title-pdf"><a href=../../../page/2017-10/18/15/rmrb2017101815.pdf><img src="../../../tplimg/ico3.gif" border=0 /></a></div>
</div>
<div class="right_title2">
<div class="right_title-name"><a id=pageLink href=nbs.D110000renmrb_16.htm>第16版：广告</a></div>
<div class="right_title-pdf"><a href=../../../page/2017-10/18/16/rmrb2017101816.pdf><img src="../../../tplimg/ico3.gif" border=0 /></a></div>
</div>
<div class="right_title1">
<div class="right_title-name"><a id=pageLink href=nbs.D110000renmrb_17.htm>第17版：国际</a></div>
<div class="right_title-pdf"><a href=../../../page/2017-10/18/17/rmrb2017101817.pdf><img src="../../../tplimg/ico3.gif" border=0 /></a></div>
</div>
<div class="right_title2">
<div class="right_title-name"><a id=pageLink href=nbs.D110000renmrb_18.htm>第18版：国际</a></div>
<div class="right_title-pdf"><a href=../../../page/2017-10/18/18/rmrb2017101818.pdf><img src="../../../tplimg/ico3.gif" border=0 /></a></div>
</div>
<div class="right_title1">
<div class="right_title-name"><a id=pageLink href=nbs.D110000renmrb_19.htm>第19版：广告</a></div>
<div class="right_title-pdf"><a href=../../../page/2017-10/18/19/rmrb2017101819.pdf><img src="../../../tplimg/ico3.gif" border=0 /></a></div>
</div>
<div class="right_title2">
<div class="right_title-name"><a id=pageLink href=nbs.D110000renmrb_20.htm>第20版：广告</a></div>
<div class="right_title-pdf"><a href=../../../page/2017-10/18/20/rmrb2017101820.pdf><img src="../../../tplimg/ico3.gif" border=0 /></a></div>
</div>
<div class="right_title1">
<div class="right_title-name"><a id=pageLink href=nbs.D110000renmrb_21.htm>第21版：广告</a></div>
<div class="right_title-pdf"><a href=../../../page/2017-10/18/21/rmrb2017101821.pdf><img src="../../../tplimg/ico3.gif" border=0 /></a></div>
</div>
<div class="right_title2">
<div class="right_title-name"><a id=pageLink href=nbs.D110000renmrb_22.htm>第22版：区域经济</a></div>
<div class="right_title-pdf"><a href=../../../page/2017-10/18/22/rmrb2017101822.pdf><img src="../../../tplimg/ico3.gif" border=0 /></a></div>
</div>
<div class="right_title1">
<div class="right_title-name"><a id=pageLink href=nbs.D110000renmrb_23.htm>第23版：各地传真</a></div>
<div class="right_title-pdf"><a href=../../../page/2017-10/18/23/rmrb2017101823.pdf><img src="../../../tplimg/ico3.gif" border=0 /></a></div>
</div>
<div class="right_title2">
<div class="right_title-name"><a id=pageLink href=nbs.D110000renmrb_24.htm>第24版：广告</a></div>
<div class="right_title-pdf"><a href=../../../page/2017-10/18/24/rmrb2017101824.pdf><img src="../../../tplimg/ico3.gif" border=0 /></a></div>
</div>
</ul><!-- list endding -->
            </div>
          </div>
          <div  style="width:218px;height:10px;background:#D0EBFE;border-top:1px solid #94D5FF;text-align:center;padding:2px 0 0 0;" id="pageImgDown" align="center"><a href="#"><img src="../../../tplimg/jiao.gif" border="0" alt="" /></a></div>
        </div>
      </div>
    </div>
     <iframe id="postIframe"  
            name="postIframe" src='http://paperpost.people.com.cn/dis/commesPageNew.jsp?artiles=9' frameborder=0 width=555
            scrolling=no height=581 style="margin-left:-5px;float:left;margin-top:10px"><a href="http://58.68.146.103/epaper/rmrb.html" class="ared" style="font-size:16px"><span style="font-weight:bold;">人民日报图文数据库（1946-2014）</span></a><br>开放试用申请，审核通过将获得数据库的全部使用权限</div></iframe>
    <!--我要评报-->
    <div class="title da_t">
      <div><div style="float:left;width:350px;background:none;margin:0px;padding:0px;height:25px">留言须知 <a href="http://www.people.com.cn/GB/50142/104580/index.html" target="_blank">&nbsp;|&nbsp;关于人民日报社</a></div>
	</div>
    </div>
    <div class="note">
      <div name="pageNameForJiaoHu" id="pageNameForJiaoHu" style="display:none" >
        决胜全面小康 开启新的征程·党的十九大特别报道
      </div>
      <FORM name=commentform action=http://paperpost.people.com.cn/comment/saveNodeArtComment.jsp  method=post target="tempForm">
        <!--&nbsp;&nbsp;&nbsp;&nbsp;署名:
        <input type="text" style="width:95px;height:18px;border:1px solid #7F9DB9;" maxLength=64  name="author1"/>
        &nbsp;&nbsp;
        <input name="isGuest" type="hidden"  id="isGuest" value="true" />-->
        <!--匿名发表-->
        <!--p>
          <textarea name="content1" cols="30" rows="6"  id="content1"></textarea>
          <img src="../../../tplimg/fb.gif"  alt="" border="0" style="cursor:hand " onclick="return submitCheck();" /><br/><br/><br/><img src="../../../tplimg/ckpl.gif"  alt="" border="0" style="cursor:hand " onclick="return viewComment();"> </p-->
        <input type=hidden  name="nodename1" />
	<input type=hidden  name="weburl" />
        <input type="hidden"  name="channelname1" />
        <input name="attr" type="hidden" value="2" />
        <input name="isnodecomm" type="hidden" value="1" />
        <input type="hidden" name="author" />
        <input type="hidden" name="content" />
        <INPUT type="hidden"  name="paperdate" />
        <input type="hidden" name="nispagename" />
        <span id="liuyans">
          1.遵守中华人民共和国有关法律、法规，尊重网上道德，承担一切因您的行为而直接或间接引起的法律责任。 
            <br>
            2.人民网拥有管理笔名和留言的一切权力。 <br>
            3.您在人民网留言板发表的言论，人民网有权在网站内转载或引用。 <br>
          </span>
        <input name="nodeid" type=hidden value="1928"><input name="nodename" type=hidden value="07"><input name="nodetype" type=hidden value="0"><input name="nodeurl" type=hidden value="null.htm"><input name="channelid" type=hidden value="1921"><input name="channelname" type=hidden value="人民日报">
        <INPUT name=password type="password" id="password" style="WIDTH: 95px; HEIGHT: 18px;display:none" maxLength=64 />
        <input type="radio" name="rankRadio" style=" display:none;" value="5" />
        <input type="radio" name="rankRadio" style=" display:none;" value="4" />
        <input type="radio" name="rankRadio" style=" display:none;" value="3" />
        <input type="radio" name="rankRadio" style=" display:none;" value="2" />
        <input type="radio" checked name="rankRadio" style=" display:none;" value="1" />
      </form>
      <form name=viewform action=http://paperpost.people.com.cn/comment/nodeComment.jsp method=post>
        <input  name="nodename1" type="hidden" id="nodename1" />
        <input name="channelname1" type="hidden" id="channelname1"  value="" />
        <input name="attr" type="hidden" value="2" />
        <input name="isnodecomm" type="hidden" value="1" />
        <INPUT type="hidden" value="1" name="view" />
        <INPUT type="hidden"  name="paperdate" />
	<input type=hidden  name="weburl" />
        <input name="nispagename" type="hidden" id="nispagename" />
        <input name="nodeid" type=hidden value="1928"><input name="nodename" type=hidden value="07"><input name="nodetype" type=hidden value="0"><input name="nodeurl" type=hidden value="null.htm"><input name="channelid" type=hidden value="1921"><input name="channelname" type=hidden value="人民日报">
      </form>
    </div>
    <!--留言部分-->
    
    <!--结束留言部分-->
  </div>
<!--版权部分-->
<div class="copyright">
  <p class="p1"><span class="red">人 民 网 版 权 所 有 ，未 经 书 面 授 权 禁 止 使 用</span><br />
      <span class="black">Copyright &copy; 1997-2013 by www.people.com.cn.
        all rights reserved</span><a href="http://www.hd315.gov.cn/beian/view.asp?bianhao=0102000101300040" target="_blank"><img src="../../../tplimg/gongshang.gif" width="40" style="float:right;margin:-45px 0px 0 10px;" height="48" alt="" align="middle" border="0" /></a></p>
</div>
<!--结束内容部分-->
<!--日报-->
<DIV  id="rmrbbx" style="display:none;position:absolute;top:50px;left:50%;margin-left:-40px;" onMouseOver="document.getElementById('rmrbbx').style.display = 'block';" onMouseOut="document.getElementById('rmrbbx').style.display = 'none';">
  <table width="100" border="0" cellpadding="0" cellspacing="1" bordercolor="#007CD2" bgcolor="#007CD2">
    <tr>
      <td bgcolor="#D8EFFF" style="padding: 3px;"><table width="100" border="0" cellpadding="0" cellspacing="0">
        <tr>
          <td bgcolor="#FFFFFF" style="padding: 1px;" valign="top"><table width="100" border="0" cellpadding="0" cellspacing="0" height="23">
            <tr>
              <td width="99" bgcolor="#ffffff" align="center" valign="top"><table width="85" border="0" cellpadding="0" cellspacing="0"  style="margin: 5px 0;">
                <tr>
                  <td height="20" align="left" class="fontstyle"><a href="../../../paperindex.htm" target="_blank">人民日报</a></td>
                </tr>
                <tr>
                  <td height="1"></td>
                </tr>
                <tr>
                  <td height="20" align="left" class="fontstyle"><a href="../../../../rmrbhwb/paperindex.htm" target="_blank">人民日报海外版</a></td>
                </tr>
                <tr>
                  <td height="1"></td>
                </tr>
                <tr>
                  <td height="20" align="left" class="fontstyle"><a href="http://www.huanqiu.com/" target="_blank">环球时报</a></td>
                </tr>
                <tr>
                  <td height="1"></td>
                </tr>
                <tr>
                  <td height="20" align="left" class="fontstyle"><a href="http://epaper.stcn.com/" target="_blank">证券时报</a></td>
                </tr>
                <tr>
                  <td height="1"></td>
                </tr>
              </table></td>
            </tr>
          </table></td>
        </tr>
      </table></td>
    </tr>
  </table>
</div>
<!--结束日报-->
<!--周报-->
<DIV  id="rmrbbx1" style="display:none;position:absolute;top:50px;left:50%;margin-left:75px;" onMouseOver="document.getElementById('rmrbbx1').style.display = 'block';" onMouseOut="document.getElementById('rmrbbx1').style.display = 'none';">
  <table width="100" border="0" cellpadding="0" cellspacing="1" bordercolor="#007CD2" bgcolor="#007CD2">
    <tr>
      <td bgcolor="#D8EFFF" style="padding: 3px;"><table width="100" border="0" cellpadding="0" cellspacing="0">
        <tr>
          <td bgcolor="#FFFFFF" style="padding: 1px;" valign="top"><table width="100" border="0" cellpadding="0" cellspacing="0" height="23">
            <tr>
              <td width="99" bgcolor="#ffffff" align="center" valign="top"><table width="85" border="0" cellpadding="0" cellspacing="0"  style="margin: 5px 0;">
                <tr>
                  <td height="20" align="left" class="fontstyle"><a href="../../../../gjjrb/paperindex.htm" target="_blank">国际金融报</a></td>
                </tr>
                <tr>
                  <td height="1"></td>
                </tr>
                <tr>
					<td height="20" align="left" class="fontstyle"><a href="../../../../zgnyb/paperindex.htm" target="_blank">中国能源报</a></td>
				</tr>						  
                <tr>
					<td height="1"></td>
                </tr>
                <tr>
                    <td height="20" align="left" class="fontstyle"><a href="../../../../jksb/paperindex.htm" target="_blank">健康时报</a></td>
                </tr>
                <tr>
                	<td height="1"></td>
                </tr>
                <tr>
                	<td height="20" align="left" class="fontstyle"><a href="../../../../fcyym/paperindex.htm" target="_blank">讽刺与幽默</a></td>
                </tr>
                <tr>
					<td height="1"></td>
                </tr>
                <tr>
                	<td height="20" align="left" class="fontstyle"><a href="../../../../zgcsb/paperindex.htm" target="_blank">中国城市报</a></td>
                </tr>
                <tr>
					<td height="1"></td>
                </tr>
              </table></td>
            </tr>
          </table></td>
        </tr>
      </table></td>
    </tr>
  </table>
</div>
<!--结束周报-->
<DIV  id="rmrbbx2" style="display:none;position:absolute;top:50px;left:50%;margin-left:190px;" onMouseOver="document.getElementById('rmrbbx2').style.display = 'block';" onMouseOut="document.getElementById('rmrbbx2').style.display = 'none';">
  <table width="110" border="0" cellpadding="0" cellspacing="1" bordercolor="#007CD2" bgcolor="#007CD2">
    <tr>
      <td bgcolor="#D8EFFF" style="padding: 3px;"><table width="110" border="0" cellpadding="0" cellspacing="0">
        <tr>
          <td bgcolor="#FFFFFF" style="padding: 1px;" valign="top"><table width="115" border="0" cellpadding="0" cellspacing="0" height="23">
            <tr>
              <td width="115" bgcolor="#ffffff" align="center" valign="top"><table width="115" border="0" cellpadding="0" cellspacing="0"  style="margin: 5px 0 0 3px;">
                <tr>
                  <td height="20" align="left" class="fontstyle"><a href="../../../../xwzx/paperindex.htm" target="_blank">新闻战线</a></td>
                </tr>
                <tr>
                  <td height="1"></td>
                </tr>
                <tr>
                  <td height="20" align="left" class="fontstyle"><a href="../../../../hqrw/paperindex.htm" target="_blank">环球人物</a></td>
                </tr>
                <tr>
                  <td height="1"></td>
                </tr>
                <tr>
                  <td height="20" align="left" class="fontstyle"><a href="../../../../rmlt/paperindex.htm" target="_blank">人民论坛</a></td>
                </tr>
                <tr>
                  <td height="1"></td>
                </tr>
                <tr>
                  <td height="20" align="left" class="fontstyle"><a href="../../../../rmzk/paperindex.htm" target="_blank">人民周刊</a></td>
                </tr>
                <tr>
                  <td height="1"></td>
                </tr>
                <tr>
                  <td height="20" align="left" class="fontstyle"><a href="../../../../zgjjzk/paperindex.htm" target="_blank">中国经济周刊</a></td>
                </tr>
                <tr>
                  <td height="1"></td>
                </tr>
                <tr>
                  <td height="20" align="left" class="fontstyle"><a href="../../../../xaq/paperindex.htm" target="_blank">新安全</a></td>
                </tr>
                <tr>
                  <td height="1"></td>
                </tr>
                <tr>
                   <td height="20" align="left" class="fontstyle"><a href="../../../../mszk/paperindex.htm" target="_blank">民生周刊</a></td>
                </tr>
                <tr>
                   <td height="1"></td>
                </tr>
                <tr>
                   <td height="20" align="left" class="fontstyle"><a href="http://history.people.com.cn/GB/198819/index.html" target="_blank">国家人文历史</a></td>
                </tr>
                <tr>
                   <td height="1"></td>
                </tr>
                 <tr>
                   <td height="20" align="left" class="fontstyle"><a href="../../../../zgby/paperindex.htm" target="_blank">中国报业</a></td>
                		</tr>
                		<tr>
                   			<td height="1"></td>
                </tr>
              </table></td>
            </tr>
          </table></td>
        </tr>
      </table></td>
    </tr>
  </table>
</div>
<!--结束杂志-->
<script language=JavaScript>
<!--
document.write("<div id=detail style=position:absolute;width:300px;></div>");
//-->
</script>
<!-------rqdh版面导航------>
<div id=daydh style="display:none; position:absolute; left:50%;margin-left:-100px; top:110px; filter:alpha(opacity=90);"  onmouseover="document.getElementById('daydh').style.display='block';" >
  <form name=CLD style="padding:0px;margin:0px;">
    <table width="210" border="0" cellpadding="0" cellspacing="1" bordercolor="#007CD2" bgcolor="#007CD2">
      <tr>
        <td bgcolor="#D8EFFF" style="padding: 3px;"><table cellspacing=0 cellpadding=0 width="100%" align=center border=0 bgcolor="#D8EFFF">
          <tr>
            <td><table width="100%" align=center border="0" cellpadding="1" cellspacing="1">
              <tr class="default" align=center>
                <td height=15 colspan=7 bgcolor="#FFFFFF"><table width="100%" border="0" cellpadding="2" cellspacing="0">
                  <tr align="center">
                    <td align="left" nowrap><img src="../../../../../../tiaoshidomain/applications/mp/file_upload/enp/1/121.files/d1.gif" width="7" height="11" style="cursor:hand;" onClick="turnpage(SY,0)" /></td>
                    <td><select class=jumpmenu onChange=changeMPCld() name=SY>
                      <script language=JavaScript>
					for(i=2006;i<2051;i++)
					document.write('<option>'+i+'</option>')
        			</script>
                    </select>
                    </td>
                    <td><img src="../../../../../../tiaoshidomain/applications/mp/file_upload/enp/1/121.files/d.gif" width="7" height="11" style="cursor:hand;" onClick="turnpage(SY,1)" /></td>
                    <td align="center" nowrap><img src="../../../../../../tiaoshidomain/applications/mp/file_upload/enp/1/121.files/d1.gif" width="7" height="11" style="cursor:hand;" onClick="turnpage(SM,0)" /></td>
                    <td><select class=jumpmenu onChange=changeMPCld() name=SM>
                      <script language=JavaScript>
				<!--
					for(i=1;i<13;i++) document.write('<option>'+i+'</option>')
				//-->
        			</script>
                    </select>
                    </td>
                    <td><img src="../../../../../../tiaoshidomain/applications/mp/file_upload/enp/1/121.files/d.gif" width="7" height="11" style="cursor:hand;" onClick="turnpage(SM,1)" /></td>
                    <td align="right" nowrap><strong><font id=GZ fface="Arial, Helvetica, sans-serif"></font></strong></td>
                  </tr>
                </table></td>
              </tr>
              <tr align=middle bgcolor="#FFFFFF" class="default">
                <td bgcolor="#027CD1" align="center" class="fontstyle01"><b><font face="Arial, Helvetica, sans-serif">日</font></b></td>
                <td bgcolor="#027CD1" align="center" class="fontstyle01"><b><font face="Arial, Helvetica, sans-serif">一</font></b></td>
                <td bgcolor="#027CD1" align="center" class="fontstyle01"><b><font face="Arial, Helvetica, sans-serif">二</font></b></td>
                <td bgcolor="#027CD1" align="center" class="fontstyle01"><b><font face="Arial, Helvetica, sans-serif">三</font></b></td>
                <td bgcolor="#027CD1" align="center" class="fontstyle01"><b><font face="Arial, Helvetica, sans-serif">四</font></b></td>
                <td bgcolor="#027CD1" align="center" class="fontstyle01"><b><font face="Arial, Helvetica, sans-serif">五</font></b></td>
                <td bgcolor="#027CD1" align="center" class="fontstyle01"><b><font face="Arial, Helvetica, sans-serif">六</font></b> </td>
              </tr>
              <script language=JavaScript>
		<!--
			var gNum;
			for(i=0;i<6;i++)
			{
				document.write('<tr align=center>');
				for(j=0;j<7;j++)
				{
					gNum = i*7+j;
					document.write('<td  bgcolor="#FFFFFF" class="default" align=center id="GD' + gNum +'" style="cursor: default;" width="14%"><a href="" id="CD' + gNum + '"><span class="date" style="font-family:Verdana, Arial;font-size:11px;"><font _onMouseOver="mOvr(' + gNum +')" onMouseOut="mOut()" id="SD' + gNum +'"');
					document.write('></font></span></a><br><font id="LD' + gNum + '" size=2 class=pt9 style=display:none></font></td>');
				}
				document.write('</tr>');
			}
		//-->
        	</script>
            </table></td>
          </tr>
        </table></td>
      </tr>
      <tr>
        <td align="center" height="22"><a href="#" onClick="autoShowDate();">关闭</a></td>
      </tr>
    </table>
  </form>
</div>
<!-------rqdh版面导航END------>
<!-------文章显示标题开始------>
<div style="display:none">
  <table width="265" border="0" cellspacing="0" cellpadding="0" style="margin-top:3px;">

  <tr>
	<td width="16" align="left"><img src="1.files/icon07.jpg" /></td>
	<td width="271" align="left" class="fontstyle" height="22"> 
<a href=nw.D110000renmrb_20171018_1-07.htm><div style="display:inline" id=mp_nw.D110000renmrb_20171018_1-07>回应人民新期待</div></a>
	</td>
  </tr>
  <tr><td background="1.files/dian01.jpg" colspan="2" height="1"></td></tr>
  <tr>
	<td width="16" align="left"  bgcolor="#D8EFFF"><img src="1.files/icon07.jpg" /></td>
	<td width="271" align="left" class="fontstyle" height="22"  bgcolor="#D8EFFF">
<a href=nw.D110000renmrb_20171018_2-07.htm><div style="display:inline"  id=mp_nw.D110000renmrb_20171018_2-07>栋梁之材涌出来</div></a>
	</td>
  </tr>
  <tr><td background="1.files/dian01.jpg" colspan="2" height="1"></td></tr>
  <tr>
	<td width="16" align="left"><img src="1.files/icon07.jpg" /></td>
	<td width="271" align="left" class="fontstyle" height="22"> 
<a href=nw.D110000renmrb_20171018_3-07.htm><div style="display:inline" id=mp_nw.D110000renmrb_20171018_3-07>就业好了一切好</div></a>
	</td>
  </tr>
  <tr><td background="1.files/dian01.jpg" colspan="2" height="1"></td></tr>
  <tr>
	<td width="16" align="left"  bgcolor="#D8EFFF"><img src="1.files/icon07.jpg" /></td>
	<td width="271" align="left" class="fontstyle" height="22"  bgcolor="#D8EFFF">
<a href=nw.D110000renmrb_20171018_4-07.htm><div style="display:inline"  id=mp_nw.D110000renmrb_20171018_4-07>跨省打工钱包鼓</div></a>
	</td>
  </tr>
  <tr><td background="1.files/dian01.jpg" colspan="2" height="1"></td></tr>
  <tr>
	<td width="16" align="left"><img src="1.files/icon07.jpg" /></td>
	<td width="271" align="left" class="fontstyle" height="22"> 
<a href=nw.D110000renmrb_20171018_5-07.htm><div style="display:inline" id=mp_nw.D110000renmrb_20171018_5-07>低保成了定心丸</div></a>
	</td>
  </tr>
  <tr><td background="1.files/dian01.jpg" colspan="2" height="1"></td></tr>
  <tr>
	<td width="16" align="left"  bgcolor="#D8EFFF"><img src="1.files/icon07.jpg" /></td>
	<td width="271" align="left" class="fontstyle" height="22"  bgcolor="#D8EFFF">
<a href=nw.D110000renmrb_20171018_6-07.htm><div style="display:inline"  id=mp_nw.D110000renmrb_20171018_6-07>小镇能做大手术</div></a>
	</td>
  </tr>
  <tr><td background="1.files/dian01.jpg" colspan="2" height="1"></td></tr>
  <tr>
	<td width="16" align="left"><img src="1.files/icon07.jpg" /></td>
	<td width="271" align="left" class="fontstyle" height="22"> 
<a href=nw.D110000renmrb_20171018_7-07.htm><div style="display:inline" id=mp_nw.D110000renmrb_20171018_7-07>搬出棚户笑开颜</div></a>
	</td>
  </tr>
  <tr><td background="1.files/dian01.jpg" colspan="2" height="1"></td></tr>
  <tr>
	<td width="16" align="left"  bgcolor="#D8EFFF"><img src="1.files/icon07.jpg" /></td>
	<td width="271" align="left" class="fontstyle" height="22"  bgcolor="#D8EFFF">
<a href=nw.D110000renmrb_20171018_8-07.htm><div style="display:inline"  id=mp_nw.D110000renmrb_20171018_8-07>青山绿水寿星多</div></a>
	</td>
  </tr>
  <tr><td background="1.files/dian01.jpg" colspan="2" height="1"></td></tr>
  <tr>
	<td width="16" align="left"><img src="1.files/icon07.jpg" /></td>
	<td width="271" align="left" class="fontstyle" height="22"> 
<a href=nw.D110000renmrb_20171018_9-07.htm><div style="display:inline" id=mp_nw.D110000renmrb_20171018_9-07>生活好了爱唱歌</div></a>
	</td>
  </tr>
  <tr><td background="1.files/dian01.jpg" colspan="2" height="1"></td></tr>

</table>
</div>
<!-------文章显示标题结束------>
<img src="../../../tplimg/left_ico.gif" style="display:none;" /> <img src="../../../tplimg/right_ico.gif" style="display:none;" /> <img src="../../../tplimg/ico10.gif" style="display:none;" /> <img src="../../../../../../tiaoshidomain/applications/mp/file_upload/enp/1/../../../tplimg/ico8.gif" style="display:none;" /> <img src="../../../../../../tiaoshidomain/applications/mp/file_upload/enp/1/../../../tplimg/ico9.gif" style="display:none;" /> <img src="../../../tplimg/ti.gif" style="display:none;" /> <img src="../../../tplimg/fb.gif" style="display:none;" />
</div></div>
<script>writeErWeiMa();</script>
<iframe id="tempForm"  
            name="tempForm" src='' frameborder=0 width=0
            scrolling=no height=0></iframe>
</body>
</html>
<script language="javascript">
if(document.getElementById('ozoom')!=null&&document.getElementById('ozoom').offsetHeight<=357)
	document.getElementById('ozoom').style.height = '480px';
</script>
<SCRIPT language=Javascript src="../../../../juas/commons/js/disname2.js"></SCRIPT>
<SCRIPT language=Javascript src="../../../tplimg/webdig_test.js"></SCRIPT>
"""


datetime = str(datetime.date.today()).split('-')  # 对日期进行拆分，返回一个['2017', '10', '09']形式的列表

url_prefix = 'http://paper.people.com.cn/rmrb/html/'  # url前缀
url_prefix_add = 'http://paper.people.com.cn/rmrb/html/' + datetime[0] + '-' + datetime[1] + '/' + datetime[
    2] + '/'  # url前缀带日期
url_prefix_add2 = 'http://paper.people.com.cn/rmrb/html/' + datetime[0] + '-' + datetime[1] + '/' + datetime[
    2] + '/' + 'nbs.D110000renmrb_01.htm'  # 头版完整url

#print(url_prefix)
#print(url_prefix_add)
print(url_prefix_add2)

soup = BeautifulSoup(''.join(html2))

banmiankuai = soup.find('div',{'id':'pageList'})
#print(banmiankuai)
list1 = []
for link in banmiankuai.findAll('a'):
    if 'pdf' in link['href']:
        continue
    #print(link.contents[0].strip())
    #print(url_prefix_add + link['href'].lstrip(r'./'))
    vol_title = link.contents[0].strip()

    zhengwenlian = soup.find('div',{'id':'titleList'})
    wenzhang = []
    juanbiao = []

    for link2 in zhengwenlian.findAll('a'):
        #print(link2)
        videolink = re.compile(r'src="')
        vlinkfind = videolink.findall(str(link2))
    #print(vlinkfind)
        if not vlinkfind:
        #continue
    #print(url_prefix_add + link2['href'])
    #print(link2)
    #print(link2.contents[0])
    #print(link2.contents[0].contents[0].lstrip(r'document.write(view("').rstrip(r'"))').strip().replace('<br>', ' '))
            til = link2.contents[0].contents[0].lstrip(r'document.write(view("').rstrip(r'"))').strip().replace('<br>', ' ')
            url = link['href']
            ans = {'title':til , 'url': url}
            ans0 = (vol_title,ans)
            wenzhang.append(ans0)

#print(wenzhang)
            #list1.append(link2)
        print(link2)
        try:
            find_title = re.compile(r'<.*><script>document\.write\(view\("(.*)"\)\)</script></a>')
            search_title = find_title.search(str(link2))
            print(search_title.group(1).replace('<br>', ' ').strip())
        except:
            pass
    #lchange = re.compile(r'<a.*\("')
    #rchange = re.compile(r'"\).*</a>')
    #lcha = lchange.search(str(link2))
    #rcha = rchange.search(str(link2))
    #lre = lchange.sub('',str(link2))
    #rre = rchange.sub('',lre)
    #print(rre)
    #print(lcha.group())
    #print(rcha.group())
#print(list1)