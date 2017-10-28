#coding=utf-8

from BeautifulSoup import BeautifulSoup
import datetime

html = '''
<html><head><meta http-equiv="Content-Type" content="text/html; charset=utf-8" />
<title>打造新型传媒集团·江西日报社数字报</title>
<link href="../../../tplimg/global.css" type="text/css"/>
<link href="../../../tplimg/calendar.css" rel="stylesheet" type="text/css"/>
<SCRIPT language=Javascript src="../../../tplimg/prototype.js"></SCRIPT>
<SCRIPT language=Javascript src="../../../tplimg/mp.js"></SCRIPT>
<SCRIPT language=Javascript src="../../../tplimg/calendar2.js"></SCRIPT>
<SCRIPT language=Javascript src="../../../tplimg/range.js"></SCRIPT>
<SCRIPT language=Javascript src="../../../tplimg/aheading.js"></SCRIPT>
<SCRIPT id=oMapScript event=onmouseover() for=pagepicmap>
rangeDeltaX = 15;
rangeDeltaY = -13;
 drawLine(event.srcElement);
 </SCRIPT>
<SCRIPT LANGUAGE="JavaScript">
var tid = null;
var speed=1000;
var jk=-1;

var colors=new Array();
 colors[0]="#FF0000";
 colors[1]="#00FF00";
 colors[2]="#0000FF";

function blink(){
 var obj = eval("document.all." + "test1" );
 var obj2 = eval("document.all." + "test2" );
 
 jk++;
 if(jk==3){
 	jk=-1;
 }
 //obj.style.color = colors[jk];
 //obj2.style.color = colors[jk];
 // tid = setTimeout("blink('"+ objId +"')",500);
}
setInterval("blink()", speed);
</SCRIPT>

<SCRIPT language=Javascript>
function turnpage(src,mode){

 currPos = src.selectedIndex;

 if(mode==0){//前翻
 	if(currPos==0) return;
	else {
	 src.selectedIndex = currPos -1;
	 src.onchange();
	} 
 }else{
 if(currPos == src.length-1)
	 return;
	 else {
	 src.selectedIndex = currPos +1;
	 src.onchange();
	 }
 }
}
function changeMPCld()
{
 var y,m;
 y=CLD.SY.selectedIndex+2006;
 m=CLD.SM.selectedIndex;
 //alert(m);
 OBJ_MP_LOADACTION.loadPeriods("",y+"-"+appendZero(m+1));

}
</SCRIPT>
<SCRIPT id=oMapScript1 event=onmouseout() for=pagepicmap>
 MouseOutMap();
</SCRIPT>

<style type="text/css">
<!--
body {
	background-image: url();
	background-color: #F7FAFF;

}
.Ltd1 {
	BORDER-RIGHT: #555 1px solid; PADDING-RIGHT: 10px; BORDER-TOP: #555 1px solid; PADDING-LEFT: 18px; PADDING-BOTTOM: 10px; BORDER-LEFT: #555 1px solid; PADDING-TOP: 10px; BORDER-BOTTOM: #555 1px solid
}
.style7 {font-size: 9px}
.style16 {
	font-family: "隶书";
	font-size: 36px;
	font-style: italic;
	color: #FFFFFF;
}
#pgn {
	position: absolute;
	width: 150px;
	padding: 0px;
	border: 1px solid #292929;
	background: #e8e8e8;
	font-size: 12px;
	line-height: 130%;
	z-index: 2;
	left:835px;
	top:155px;
	display:none;
}
.style17 {
	font-size: 16px;
	font-weight: bold;
}
.style19 {font-size: 16px}
.px12_1 {
	font-size: 12px;
	line-height: 15px;
	color: #000000;
}
.style30 {color: #FFFFFF}
.STYLE3 {font-size: 12px}
.STYLE25 {	font-size: 14px;
	line-height: 18px;
}
td{font-size:12px}
.style31 {color: white}
.style32 {
	font-size: 14px;
	font-weight: bold;
	color: #ED2429;
}
.bg1 {
	margin-top: 10px;
	margin-bottom: 10px;
}
-->
</style>
</head>
<body>
<SPAN id=leveldiv title=点击查看内容 
style="BORDER-TOP-WIDTH: 0px; BORDER-LEFT-WIDTH: 0px; Z-INDEX: 100; LEFT: 233px; BORDER-BOTTOM-WIDTH: 0px; WIDTH: 210px; CURSOR: hand; POSITION: absolute; TOP: 123px; HEIGHT: 34px; BORDER-RIGHT-WIDTH: 0px"></SPAN>

<body onLoad="initialize();initMPPage();" text=#000000 vlink=#000000 alink=#ff0000 link=#000000 leftmargin=0 topmargin=0 marginheight="0" marginwidth="0">

<!-- 版面导航div -->
<DIV id=pgn onMouseOver="getElementById('pgn').style.display='block';" onMouseOut="getElementById('pgn').style.display='none';">
 <UL> <Li>&nbsp;<a id=pageLink href=node_187.htm>A01： 头版</a></Li> <Li>&nbsp;<a id=pageLink href=node_188.htm>A02： 要闻</a></Li> <Li>&nbsp;<a id=pageLink href=node_189.htm>A03： 天下</a></Li> <Li>&nbsp;<a id=pageLink href=node_190.htm>A04： 专刊</a></Li> <Li>&nbsp;<a id=pageLink href=node_191.htm>B01： 专刊</a></Li> <Li>&nbsp;<a id=pageLink href=node_192.htm>B02： 综合</a></Li> <Li>&nbsp;<a id=pageLink href=node_193.htm>B03： 学与思</a></Li> <Li>&nbsp;<a id=pageLink href=node_194.htm>B04： 专刊</a></Li> <Li>&nbsp;<a id=pageLink href=node_195.htm>C01： 策划</a></Li> <Li>&nbsp;<a id=pageLink href=node_196.htm>C02： 关注</a></Li> <Li>&nbsp;<a id=pageLink href=node_197.htm>C03： 旅游</a></Li> <Li>&nbsp;<a id=pageLink href=node_198.htm>C04： 体育·娱乐</a></Li> </UL>
</DIV>
<!-- 版面导航div -->
<table width="1014" border="0" align="center" cellpadding="0" cellspacing="0">
 <tr>
 <td align="center"><iframe marginwidth=0 marginheight=0 src="http://common.jxnews.com.cn/sys/nav1014.htm" frameborder=0 width=1014 scrolling=no height=70 align=center></iframe></td>
 </tr>
</table>
<table cellspacing=0 cellpadding=0 width=1002 align=center border=0 background="../../../tplimg/bg.jpg">
 <tr>
 <td valign=top width=400><table cellspacing=0 cellpadding=0 align=right border=0>
 <tr>
 <td 
 align=left><table height="146" border=0 cellpadding=0 cellspacing=0>
 <tr>
 <td width="280" rowspan="3" valign="top"
 
 ><img src="../../../tplimg/jwb_red_r1_c1.jpg" width="23" height="100"></td>
 <td valign="top" bgcolor=#ffffff><img src="../../../tplimg/jwb_red_r1_c2.jpg" width="381" height="24"></td>
 <td rowspan="2" valign="top" background=../../../tplimg/jwb_red_r6_c3.jpg><img src="../../../tplimg/jwb_red_r1_c3.jpg" width="9" height="134"></td>
 </tr>
 <tr>
 <td width="280" class="Ltd1" bgcolor=#ffffff><MAP NAME="pagepicmap"><Area coords="5,72,228,72,228,207,5,207" shape="polygon" href="content_401862.htm"><Area coords="232,73,344,73,344,288,232,288" shape="polygon" href="content_401863.htm"><Area coords="94,242,29,242,29,242,29,242,27,212,5,212,5,389,5,392,5,442,94,442" shape="polygon" href="content_401864.htm"><Area coords="265,500,344,500,344,400,344,397,344,325,344,323,344,295,232,295,232,323,288,325,288,397,288,397,287,374,232,374,232,529,265,529" shape="polygon" href="content_401865.htm"><Area coords="227,366,227,364,227,335,99,335,99,364,163,366,163,392,99,392,99,442,227,442" shape="polygon" href="content_401866.htm"></MAP><img src=../../../page/186/2017-10-09/A01/58271507497937890.jpg border=0 USEMAP=#PagePicMap> </td>
 </tr>
 <tr>
 <td height="23" align=left valign="top"><img src="../../../tplimg/jwb_red_r8_c2.jpg" width="381" height="9"></td>
 <td valign="top"><img src="../../../tplimg/jwb_red_r8_c3.jpg" width="9" height="9"></td>
 </tr>
 </table>
 <table style="MARGIN-BOTTOM: 3px" cellspacing=0 cellpadding=5 
 width=411 border=0>
 <tr>
 <td width="202" align=left class=px12>第A01版：<STRONG>头版</STRONG>
 </td>
 <td width="30" 
 align=right nowrap class=px12 
 style="PADDING-RIGHT: 0px; PADDING-LEFT: 0px; PADDING-BOTTOM: 0px; PADDING-TOP: 0px"><table width=100% border=0><tr><td nowrap width=50% class=px12></td><td nowrap width=50% class=px12><a class=preart href="node_188.htm"><span style='font-size:12px;font-family:webdings'>4</span>下一版</a>&nbsp;&nbsp;</td></tr></table></td>
 <td width=149 
 align=right valign=center nowrap class=px12 style="PADDING-RIGHT: 5px"><a href=../../../page/186/2017-10-09/A01/51281507497937890.pdf><IMG height=16 src="../../../tplimg/pdf.gif" width=16 border=0></a></td>
 </tr>
 </table>
 <table style="BORDER-TOP: #555 1px solid" cellspacing=0 
 cellpadding=4 width=411 border=0>
 <tr>
 <td width=403 
 align=left valign="top" 
 style="BORDER-TOP: #d2d2d2 5px solid; BORDER-LEFT: #999 1px solid"><TABLE cellSpacing=0 cellPadding=1 border=0> <TBODY> <tr> <TD class=default valign="top"> <img src="../../../tplimg/checkbox.gif" width="10" height="10"> </TD> <td class=default valign="top"> <a href=content_401862.htm><div style="display:inline" id=mp401862>站在新的更高起点探索生态文明建设</div></a> </td> </TR><tr> <TD class=default valign="top"> <img src="../../../tplimg/checkbox.gif" width="10" height="10"> </TD> <td class=default valign="top"> <a href=content_401863.htm><div style="display:inline" id=mp401863>为美丽中国贡献“江西智慧”</div></a> </td> </TR><tr> <TD class=default valign="top"> <img src="../../../tplimg/checkbox.gif" width="10" height="10"> </TD> <td class=default valign="top"> <a href=content_401864.htm><div style="display:inline" id=mp401864>吉安绣好全域脱贫攻坚新画卷</div></a> </td> </TR><tr> <TD class=default valign="top"> <img src="../../../tplimg/checkbox.gif" width="10" height="10"> </TD> <td class=default valign="top"> <a href=content_401865.htm><div style="display:inline" id=mp401865>国家有前途 个人才有前途</div></a> </td> </TR><tr> <TD class=default valign="top"> <img src="../../../tplimg/checkbox.gif" width="10" height="10"> </TD> <td class=default valign="top"> <a href=content_401866.htm><div style="display:inline" id=mp401866>一片茶叶带富一方百姓</div></a> </td> </TR> </TBODY> </TABLE> </td>
 </tr>
 </table>
 <table width="95%" border="0" align="center" cellpadding="0" cellspacing="0">
 <tr>
 <td height="25" align="center" background="../../../tplimg/red_a1.jpg"><span class="style30 STYLE3"><strong><span class="px12"><span class="style30"><strong>*** </strong></span></span>江西日报即时新闻排行榜<span class="px12"><span class="style30"><strong> ***</strong></span></span></strong></span></td>
 </tr>
 <tr>
 <td bgcolor="#e8e8e8"><iframe marginwidth=0 marginheight=0 src="http://www.jxnews.com.cn/djpd/iframe/rank.htm" frameborder=0 width=390 scrolling=no height=180 align=center></iframe></td>
 </tr>
 </table>
 <table width="95%" border="0" align="center" cellpadding="0" cellspacing="0">
 <tr>
 <td height="25" align="center" background="../../../tplimg/red_a1.jpg"><span class="px12"><span class="style30"><strong>*** </strong></span><strong><a href="http://bbs.jxnews.com.cn/" target="_blank" class="style31">大江网论坛热帖</a></strong><span class="style30"><strong> ***</strong></span></span></td>
 </tr>
 <tr>
 <td align="left" valign="middle"><iframe marginwidth=0 marginheight=0 src="http://www.jxnews.com.cn/djpd/iframe/lt.htm" frameborder=0 width=390 scrolling=no height=150 align=center></iframe></td>
 </tr>
 <tr>
 <td align="right" valign="top"><a href="http://bbs.jxnews.com.cn/" target="_blank"><strong>更多...</strong></a>&nbsp;&nbsp;</td>
 </tr>
 </table></td>
 </tr>
 </table></td>
 <td valign=top width=602><table height=30 cellspacing=0 cellpadding=0 width="100%" border=0>
 <tr>
 <td ><div align="center" class="style16"></div>
 <table height=29 cellspacing=0 cellpadding=0 width="100%" 
 border=0>
 <tr align=right>
 <td height="29" align="right" class=whitenav><a href="http://epaper.jxnews.com.cn:8080/fly/" target="_blank"><strong>文章搜索</strong></a><strong><a href="http://epaper.jxnews.com.cn:8080/fly/" target="_blank"><strong>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;</strong></a><a href="http://epaper.jxnews.com.cn:8080/fly/" target="_blank"><strong>&nbsp;&nbsp;&nbsp;&nbsp;</strong></a><strong><a href="http://epaper.jxnews.com.cn:8080/fly/" target="_blank"><strong>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;</strong></a>&nbsp;&nbsp;&nbsp;<a href="http://epaper.jxnews.com.cn:8080/fly/" target="_blank"><strong>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;</strong></a><a href="http://epaper.jxnews.com.cn:8080/fly/" target="_blank"><strong>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;</strong></a><a href="http://epaper.jxnews.com.cn:8080/fly/" target="_blank"><strong>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;</strong></a><a href="http://epaper.jxnews.com.cn:8080/fly/" target="_blank"><strong>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;</strong></a><a href="http://epaper.jxnews.com.cn:8080/fly/" target="_blank"><strong>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;</strong></a><a href="http://epaper.jxnews.com.cn:8080/fly/" target="_blank"><strong>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;</strong></a><a href="http://epaper.jxnews.com.cn:8080/fly/" target="_blank"><strong>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;</strong></a><a href="http://epaper.jxnews.com.cn:8080/fly/" target="_blank"><strong>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;</strong></a><a href="http://epaper.jxnews.com.cn:8080/fly/" target="_blank"><strong>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;</strong></a><a href="http://epaper.jxnews.com.cn:8080/fly/" target="_blank"><strong>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;</strong></a><a href="http://epaper.jxnews.com.cn:8080/fly/" target="_blank"><strong>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;</strong></a><a href="http://epaper.jxnews.com.cn:8080/fly/" target="_blank"><strong>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;</strong></a><a href="http://epaper.jxnews.com.cn:8080/fly/" target="_blank"><strong>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;</strong></a><a href="http://epaper.jxnews.com.cn:8080/fly/" target="_blank"><strong>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;</strong></a><a href="http://epaper.jxnews.com.cn:8080/fly/" target="_blank"><strong>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;</strong></a><a href="http://epaper.jxnews.com.cn:8080/fly/" target="_blank"><strong>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;</strong></a><a href="http://epaper.jxnews.com.cn:8080/fly/" target="_blank"><strong>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;</strong></a><a href="http://epaper.jxnews.com.cn:8080/fly/" target="_blank"><strong>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;</strong></a><a href="http://epaper.jxnews.com.cn:8080/fly/" target="_blank"><strong>&nbsp;&nbsp;&nbsp;&nbsp;</strong></a>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;<span onMouseOver="getElementById('pgn').style.display='block';"><span onMouseOver="getElementById('pgn').style.display='block';">&nbsp;</span>
 <a href="node_187.htm">版面导航</a>
&nbsp;&nbsp;&nbsp;&nbsp;</span></strong></strong></td>
 </tr>
 </table></td>
 </tr>
 </table>
 <table width="589" height="507" border=0 cellpadding=0 cellspacing=0>
 <tr valign=top>
 <td rowspan="4"><table width="100%" border=0 bgcolor="#FCFCFC">
 <tr>
 <td width="144" align=center class=default><img src="../../../tplimg/jxrb.gif" width="91" height="28">&nbsp;<a href="http://www.jxnews.com.cn/jxrb/" target="_blank" class="style32">电子版</a></td>
 <td width="229" align=right bgcolor="#FCFCFC" class=default><strong><font face="Arial, Helvetica, sans-serif"> <strong><font 
 face="Arial, Helvetica, sans-serif">
 2017
 </font></strong> 年
 10
 月
 9
 日　星期
 <font class=weekday>一</font>
&nbsp;&nbsp; </font></strong></td>
 </tr>
 </table>
 <table style="BORDER-TOP: #999 1px solid; MARGIN-BOTTOM: 5px" 
 cellspacing=0 cellpadding=0 width="100%" border=0>
 <tr>
 <td width=249 bgcolor=#e8e8e8 class=default style="PADDING-RIGHT: 3px; PADDING-LEFT: 3px; PADDING-BOTTOM: 3px; PADDING-TOP: 3px">&nbsp;<strong>版面导航</strong></td>
 </tr>
 </table>
 <img name="" src="" width="15" height="8" alt="">
 <table cellspacing=0 cellpadding=2 width=100% border=0><tbody> <tr> <td class=default align=left>&nbsp;<a id=pageLink href=node_187.htm>第A01版：头版</a></td> <td nowrap align=middle width=55><a href=../../../page/186/2017-10-09/A01/51281507497937890.pdf><img height=16 src="../../../tplimg/pdf.gif" width=16 border=0></a></td></tr> <tr bgcolor=#e8e8e8> <td align=left class=default>&nbsp;<a id=pageLink href=node_188.htm>第A02版：要闻</a></td> <td nowrap align=middle width=55><a href=../../../page/186/2017-10-09/A02/54571507497938890.pdf><img height=16 src="../../../tplimg/pdf.gif" width=16 border=0></a></td></tr> <tr> <td class=default align=left>&nbsp;<a id=pageLink href=node_189.htm>第A03版：天下</a></td> <td nowrap align=middle width=55><a href=../../../page/186/2017-10-09/A03/46961507497912968.pdf><img height=16 src="../../../tplimg/pdf.gif" width=16 border=0></a></td></tr> <tr bgcolor=#e8e8e8> <td align=left class=default>&nbsp;<a id=pageLink href=node_190.htm>第A04版：专刊</a></td> <td nowrap align=middle width=55><a href=../../../page/186/2017-10-09/A04/3421507497913828.pdf><img height=16 src="../../../tplimg/pdf.gif" width=16 border=0></a></td></tr> <tr> <td class=default align=left>&nbsp;<a id=pageLink href=node_191.htm>第B01版：专刊</a></td> <td nowrap align=middle width=55><a href=../../../page/186/2017-10-09/B01/5051507497914812.pdf><img height=16 src="../../../tplimg/pdf.gif" width=16 border=0></a></td></tr> <tr bgcolor=#e8e8e8> <td align=left class=default>&nbsp;<a id=pageLink href=node_192.htm>第B02版：综合</a></td> <td nowrap align=middle width=55><a href=../../../page/186/2017-10-09/B02/51571507497915828.pdf><img height=16 src="../../../tplimg/pdf.gif" width=16 border=0></a></td></tr> <tr> <td class=default align=left>&nbsp;<a id=pageLink href=node_193.htm>第B03版：学与思</a></td> <td nowrap align=middle width=55><a href=../../../page/186/2017-10-09/B03/54481507497916828.pdf><img height=16 src="../../../tplimg/pdf.gif" width=16 border=0></a></td></tr> <tr bgcolor=#e8e8e8> <td align=left class=default>&nbsp;<a id=pageLink href=node_194.htm>第B04版：专刊</a></td> <td nowrap align=middle width=55><a href=../../../page/186/2017-10-09/B04/92441507497917828.pdf><img height=16 src="../../../tplimg/pdf.gif" width=16 border=0></a></td></tr> <tr> <td class=default align=left>&nbsp;<a id=pageLink href=node_195.htm>第C01版：策划</a></td> <td nowrap align=middle width=55><a href=../../../page/186/2017-10-09/C01/94711507497918828.pdf><img height=16 src="../../../tplimg/pdf.gif" width=16 border=0></a></td></tr> <tr bgcolor=#e8e8e8> <td align=left class=default>&nbsp;<a id=pageLink href=node_196.htm>第C02版：关注</a></td> <td nowrap align=middle width=55><a href=../../../page/186/2017-10-09/C02/91101507497919828.pdf><img height=16 src="../../../tplimg/pdf.gif" width=16 border=0></a></td></tr> <tr> <td class=default align=left>&nbsp;<a id=pageLink href=node_197.htm>第C03版：旅游</a></td> <td nowrap align=middle width=55><a href=../../../page/186/2017-10-09/C03/57851507497920812.pdf><img height=16 src="../../../tplimg/pdf.gif" width=16 border=0></a></td></tr> <tr bgcolor=#e8e8e8> <td align=left class=default>&nbsp;<a id=pageLink href=node_198.htm>第C04版：体育·娱乐</a></td> <td nowrap align=middle width=55><a href=../../../page/186/2017-10-09/C04/57311507497921843.pdf><img height=16 src="../../../tplimg/pdf.gif" width=16 border=0></a></td></tr> </tbody></table> 
 <table width="100%" border="0" cellspacing="0" cellpadding="0">
 <tr>
 <td><img name="" src="" width="15" height="8" alt=""> </td>
 </tr>
 </table>
 <table width="100%" border="0" cellspacing="0" cellpadding="0">
 <tr>
 <td background="../../../tplimg/red_a1.jpg" class=default style="PADDING-RIGHT: 3px; solid; PADDING-LEFT: 3px; BORDER-TOP: #555 1px solid; PADDING-BOTTOM: 3px; PADDING-TOP: 3px; BORDER-BOTTOM: #d2d2d2 1px solid"><div align="center" class="whitenav">
 <div align="center"><span class="style30 STYLE3"><strong><span class="px12"><span class="style30"><strong>*** </strong></span></span><a href="http://www.jxnews.com.cn/djpd/rank/" target="_blank">大江网即时新闻排行榜</a><span class="px12"><span class="style30"><strong> ***</strong></span></span></strong></span></div>
 </div></td>
 </tr>
 <tr>
 <td bgcolor="#e8e8e8"><iframe marginwidth=0 marginheight=0 src="http://www.jxnews.com.cn/djpd/iframe/rank1.htm" frameborder=0 width=382 scrolling=no height=330 align=center></iframe></td>
 </tr>
 <tr>
 <td height="25" align="right" valign="top"><a href="http://www.jxnews.com.cn/djpd/rank/" target="_blank"><strong>更多...</strong></a>&nbsp;&nbsp;</td>
 </tr>
 </table>
 <table width="100%" border="0" cellspacing="0" cellpadding="0">
 <tr>
 <td height="25" align="center" background="../../../tplimg/red_a1.jpg"><span class="px12"><span class="style30"><strong>*** 大江网推荐内容 ***</strong></span></span></td>
 </tr>
 <tr>
 <td><table width="100%" border="0" align="center" cellpadding="1" cellspacing="1">
 <tr>
 <td height="110" align="center" bgcolor="#CCCCCC"><iframe marginwidth=0 marginheight=0 src="http://www.jxnews.com.cn/djpd/iframe/tj1.htm" frameborder=0 width=382 scrolling=no height=130 align=center></iframe></td>
 </tr>
 <tr>
 <td align="center" bgcolor="#e8e8e8"><iframe marginwidth=0 marginheight=0 src="http://www.jxnews.com.cn/djpd/iframe/tj2.htm" frameborder=0 width=382 scrolling=no height=220 align=center></iframe></td>
 </tr>
 </table></td>
 </tr>
 </table></td>
 <td rowspan="4" align="center">&nbsp;</td>
 <td width="195" height="115" align="center"><table width=100% border=0 align="center" cellpadding=0 cellspacing=0 style="MARGIN-TOP: 5px">
 <tr>
 <td><script language=JavaScript>
<!--
document.write("<div id=detail style=position:absolute;width:300px;></div>");
//-->
 </script>
 <table cellspacing=0 cellpadding=0 width="100%" border=0>
 <tr>
 <td width="214" height="34" colspan="2" align="center" bgcolor="#FFFFFF"><div class="style7"> <span class="style12"><span class="px12 style10 style17"><span class="px12 style10 style19"><a href="#" onClick="openRMP()"><font id="test1" color=red>伴乐翻页阅读(下载)</font></a></span></span></span> <br>
 </div></td>
 </tr>
 <tr>
 <td background="../../../tplimg/red_a1.jpg" class=default style="PADDING-RIGHT: 3px; BORDER-TOP: #555 1px solid; PADDING-LEFT: 3px; PADDING-BOTTOM: 3px; PADDING-TOP: 3px; BORDER-BOTTOM: #d2d2d2 1px solid"><div align="center" onClick="calendar()"><strong class="whitenav"><font style="CURSOR: hand">按日期查阅</font></strong></div></td>
 </tr>
 <tr align="center">
 <td><table width="201" height="100" border="0" cellpadding="0" cellspacing="0">
 <tr>
 <td height="33" colspan="2" align="left" bgcolor="#FFFFFF"><form name=CLD style="padding:0px;margin:0px;">
 <table cellspacing=0 cellpadding=0 width="100%" align=center border=0>
 <tr>
 <td><table width="100%" align=center border="0" cellpadding="1" cellspacing="1">
 <tr class="default" align=center>
 <td height=15 colspan=7 bgcolor="#d2d2d2"><table width="100%" border="0" cellpadding="2" cellspacing="0">
 <tr align="center">
 <td align="left" nowrap><img src="../../../tplimg/d1.gif" width="7" height="11" style="cursor:hand;" onClick="turnpage(SY,0)"></td>
 <td><select class=jumpmenu onChange=changeCld() name=SY>
 <script language=JavaScript>
					for(i=2006;i<2051;i++)
					document.write('<option>'+i+'</option>')
 			</script>
 </select>
 </td>
 <td><img src="../../../tplimg/d.gif" width="7" height="11" style="cursor:hand;" onClick="turnpage(SY,1)"></td>
 <td align="center" nowrap><img src="../../../tplimg/d1.gif" width="7" height="11" style="cursor:hand;" onClick="turnpage(SM,0)"></td>
 <td><select class=jumpmenu onChange=changeMPCld() name=SM>
 <script language=JavaScript>
				<!-- 
					for(i=1;i<13;i++) document.write('<option>'+i+'</option>')
				//-->
 			</script>
 </select>
 </td>
 <td><img src="../../../tplimg/d.gif" width="7" height="11" style="cursor:hand;" onClick="turnpage(SM,1)"></td>
 <td align="right" nowrap><strong><font id=GZ fface="Arial, Helvetica, sans-serif"></font></strong></td>
 </tr>
 </table></td>
 </tr>
 <tr align=middle bgcolor="#e8e8e8" class="default">
 <td align="center" class="default"><b><font face="Arial, Helvetica, sans-serif">日</font></b></td>
 <td align="center" bgcolor="#e8e8e8" class="default"><b><font face="Arial, Helvetica, sans-serif">一</font></b></td>
 <td align="center" class="default"><b><font face="Arial, Helvetica, sans-serif">二</font></b></td>
 <td align="center" class="default"><b><font face="Arial, Helvetica, sans-serif">三</font></b></td>
 <td align="center" class="default"><b><font face="Arial, Helvetica, sans-serif">四</font></b></td>
 <td align="center" class="default"><b><font face="Arial, Helvetica, sans-serif">五</font></b></td>
 <td align="center" class="default"><b><font face="Arial, Helvetica, sans-serif">六</font></b> </td>
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
					document.write('<td bgcolor="#d2d2d2" class="default" align=center id="GD' + gNum +'" style="cursor: default;" width="14%"><a href="" id="CD' + gNum + '"><span class="date" style="font-family:Verdana, Arial;font-size:11px;"><font _onMouseOver="mOvr(' + gNum +')" onMouseOut="mOut()" id="SD' + gNum +'"');
					document.write('></font></span></a><br><font id="LD' + gNum + '" size=2 class=pt9 style=display:none></font></td>');
				}
				document.write('</tr>');
			}
		//-->
 	</script>
 </table></td>
 </tr>
 </table>
 </form></td>
 </tr>
 </table></td>
 </tr>
 <tr align="center">
 <td></td>
 </tr>
 <tr><td> 
 <input name="keyword" id="keyword" style="width: 165px; height: 20px;" type="text"/>
 <input name="Btsearch" id="Btsearch" style="height: 20px;" onClick="searchWord()" type="button" value="搜索"/>
 </td></tr>
 <tr> 
 <tr>
 <td background="../../../tplimg/red_a1.jpg" class=default style="PADDING-RIGHT: 3px; solid; PADDING-LEFT: 3px; BORDER-TOP: #555 1px solid; PADDING-BOTTOM: 3px; PADDING-TOP: 3px; BORDER-BOTTOM: #d2d2d2 1px solid"></td>
 </tr>
 <tr>
 <td background="../../../tplimg/red_a1.jpg" class=default style="PADDING-RIGHT: 3px; solid; PADDING-LEFT: 3px; BORDER-TOP: #555 1px solid; PADDING-BOTTOM: 3px; PADDING-TOP: 3px; BORDER-BOTTOM: #d2d2d2 1px solid"><table width="100%" border="0" cellspacing="0" cellpadding="0">
 <tr>
 <th scope="col"><a href="http://ad.jxnews.com.cn/2012/zss/AdbeRdr708_zh_CN.zip"><span class="style19"><font color=white>PDF阅读器下载</font></span><img src="../../../tplimg/pdf.gif" width="16" height="16" border="0"></a></th>
 </tr>
 </table></td>
 </tr>
 <tr >
 <td valign="top" align="center"><table width="100%" border="0" cellspacing="0" cellpadding="0">
 <tr>
 <td><table width="100%" border="0" cellspacing="0" cellpadding="0">
 <tr>
 <td>&nbsp;</td>
 </tr>
 <tr>
 <td height="28" align="center" bgcolor="#e8e8e8"><span class="default"><strong>电子版</strong></span></td>
 </tr>
 <tr>
 <td><table width="100%" border="0" cellspacing="0" cellpadding="0">
 <tr align="center">
 <td width="50%" height="25" bgcolor="#FFFFFF"><a href="http://www.jxnews.com.cn/jxrb/" target="_blank"><img src="../../../tplimg/06jx27.gif" width="89" height="30" border="0"></a> </td>
 <td width="50%"><a href="http://www.jxnews.com.cn/xxrb/" target="_top"><img src="../../../tplimg/06jx28.gif" width="89" height="30" border="0"></a></td>
 </tr>
 <tr align="center" bgcolor="#e8e8e8">
 <td width="50%" height="25"> <a href="http://www.jxnews.com.cn/jndsb/" target="_blank"><img src="../../../tplimg/06jx29.gif" width="114" height="28" border="0"></a></td>
 <td width="50%"> <a href="http://www.jxnews.com.cn/jxfzb/" target="_blank"><img src="../../../tplimg/06jx30.gif" width="97" height="28" border="0"></a></td>
 </tr>
 </table>
 <table width="100%" border="0" cellspacing="0" cellpadding="0">
 
 <tr>
 <td height="40" align="center"><table width="210" height="40" border="0" cellpadding="0" cellspacing="0" class="bg1">
 <tr>
 <td><object classid="clsid:D27CDB6E-AE6D-11cf-96B8-444553540000" codebase="http://download.macromedia.com/pub/shockwave/cabs/flash/swflash.cab#version=7,0,19,0" width="210" height="40">
 <param name="movie" value="http://ad.jxnews.com.cn/2011/zss/images/jb21040.swf">
 <param name="quality" value="high">
 <embed src="http://ad.jxnews.com.cn/2011/zss/images/jb21040.swf" quality="high" pluginspage="http://www.macromedia.com/go/getflashplayer" type="application/x-shockwave-flash" width="210" height="40"></embed>
 </object></td>
 </tr>
 </table> </td>
 </tr>
 </table>
 <table width="100%" border="0" cellspacing="0" cellpadding="0">
 </table></td>
 </tr>
 </table></td>
 </tr>
 </table></td>
 </tr>
 <tr >
 <td valign="top" align="center"><table width="100%" border="0" align="center" cellpadding="0" cellspacing="0">
 <tr>
 <td background="../../../tplimg/red_a1.jpg" class=default style="PADDING-RIGHT: 3px; solid; PADDING-LEFT: 3px; BORDER-TOP: #555 1px solid; PADDING-BOTTOM: 3px; PADDING-TOP: 3px; BORDER-BOTTOM: #d2d2d2 1px solid"><div align="center" class="whitenav">
 <div align="center"><span class="style19 style30"><strong>通联</strong></span></div>
 </div></td>
 </tr>
 <tr>
 <td height="310" bgcolor="#e8e8e8"><table width="100%" border="0" align="center" cellpadding="1" cellspacing="1" bgcolor="#666666" style="line-height:140%">
 <tr class="px12_1">
 <td width="70" bgcolor="#CCCCCC">
 <div align="right">电话总机:</div></td>
 <td bgcolor="#FFFFFF"><div align="center">86849114</div></td>
 </tr>
 <tr class="px12_1">
 <td bgcolor="#CCCCCC">
 <div align="right">夜班:</div></td>
 <td bgcolor="#FFFFFF"><div align="center">86849790 86849865(FAX)</div></td>
 </tr>
 <tr class="px12_1">
 <td bgcolor="#CCCCCC">
 <div align="right">广告部:</div></td>
 <td bgcolor="#FFFFFF"><div align="center">86849868</div></td>
 </tr>
 <tr class="px12_1">
 <td bgcolor="#CCCCCC">
 <div align="right">总编办:</div></td>
 <td bgcolor="#FFFFFF"><div align="center">86849545</div></td>
 </tr>
 <tr class="px12_1">
 <td bgcolor="#CCCCCC"><div align="right">出版部:</div></td>
 <td bgcolor="#FFFFFF"><div align="center">86849226</div></td>
 </tr>
 <tr class="px12_1">
 <td bgcolor="#CCCCCC">
 <div align="right">经济部:</div></td>
 <td bgcolor="#FFFFFF"><div align="center">86849086</div></td>
 </tr>
 <tr class="px12_1">
 <td bgcolor="#CCCCCC">
 <div align="right">政教部:</div></td>
 <td bgcolor="#FFFFFF"><div align="center">86849002</div></td>
 </tr>
 <tr class="px12_1">
 <td bgcolor="#CCCCCC">
 <div align="right">理论评论部:</div></td>
 <td bgcolor="#FFFFFF"><div align="center">86849029</div></td>
 </tr>
 
									<tr class="px12_1">
 <td bgcolor="#CCCCCC"><div align="right">都市新刊:</div></td>
 <td bgcolor="#FFFFFF"><div align="center">86849999</div></td>
 </tr>
 <tr class="px12_1">
 <td bgcolor="#CCCCCC"><div align="right">副刊部:</div></td>
 <td bgcolor="#FFFFFF"><div align="center">86849116</div></td>
 </tr>
 <tr class="px12_1">
 <td bgcolor="#CCCCCC">
 <div align="right">文体部:</div></td>
 <td bgcolor="#FFFFFF"><div align="center">86849195</div></td>
 </tr>
 <tr class="px12_1">
 <td bgcolor="#CCCCCC">
 <div align="right">记者部:</div></td>
 <td bgcolor="#FFFFFF"><div align="center">86849289</div></td>
 </tr>
 <tr class="px12_1">
 <td bgcolor="#CCCCCC">
 <div align="right">大江网:</div></td>
 <td bgcolor="#FFFFFF"><div align="center">86849073</div></td>
 </tr>
 <tr class="px12_1">
 <td bgcolor="#CCCCCC">
 <div align="right">摄影部:</div></td>
 <td bgcolor="#FFFFFF"><div align="center">86849056</div></td>
 </tr>
 <tr class="px12_1">
 <td bgcolor="#CCCCCC">
 <div align="right">发行中心:</div></td>
 <td bgcolor="#FFFFFF"><div align="center">86849176</div></td>
 </tr>
 <tr class="px12_1">
 <td bgcolor="#CCCCCC">
 <div align="right">群工部:</div></td>
 <td bgcolor="#FFFFFF"><div align="center">86849045 86849395(FAX)</div></td>
 </tr>
 </table></td>
 </tr>
 </table></td>
 </tr>
 <tr >
 <td height="70" align="center" valign="top" bgcolor="#E8E8E8"><a href="http://bbs.jxnews.com.cn/forumdisplay.php?s=37cf8e0f9b2fc8080684f4d64361d048&f=131" target="_blank"><img src="../../../tplimg/bl.jpg" width="200" height="60" border="0"></a></td>
 </tr>
 </table>
 <table width="100%" border="0" cellspacing="0" cellpadding="0">
 <tr>
 <td height="25" align="center" background="../../../tplimg/red_a1.jpg" class="style31"><strong>*** </strong><span class="white"><strong><a href="http://www.jxnews.com.cn/zt/" target="_blank" class="whitenav">大江网精彩专题</a></strong></span><strong> ***</strong></td>
 </tr>
 <tr>
 <td align="left"><iframe marginwidth=0 marginheight=0 src="http://www.jxnews.com.cn/djpd/iframe/zt.htm" frameborder=0 width=200 scrolling=no height=90 align=center></iframe></td>
 </tr>
 <tr>
 <td align="right"><a href="http://www.jxnews.com.cn/zt/" target="_blank"><strong>更多...</strong></a>&nbsp;&nbsp;</td>
 </tr>
 </table></td>
 </tr>
 </table></td>
 </tr>
 </table>
 
 <table>
 <tr>
 <td><object classid="clsid:D27CDB6E-AE6D-11cf-96B8-444553540000" codebase="http://download.macromedia.com/pub/shockwave/cabs/flash/swflash.cab#version=7,0,19,0" 
 width="382" height="200">
 <param name="movie" value="http://www.aheading.com/sit/qfgg/qfgg-1.0.swf">
 <param name="quality" value="high">
 <embed src="http://www.aheading.com/sit/qfgg/qfgg-1.0.swf" quality="high" 
 pluginspage="http://www.macromedia.com/go/getflashplayer" type="application/x-shockwave-flash" width="382" height="200"></embed>
 </object></td>
 </tr> 
 </table>
 
 </td>
 </tr>
 <tr bgcolor="#A90110">
 <td colspan="2" style="line-height: 120%">&nbsp;</td>
 </tr>
</table>
<table width="1014" border="0" align="center" cellpadding="0" cellspacing="0">
 <tr>
 <td align="center"><iframe marginwidth="0" marginheight="0" src="http://common.jxnews.com.cn/sys/bottom.htm" frameborder="0" width="1014" scrolling="No" height="100" align="center"></iframe></td>
 </tr>
</table>
<!--流量统计代码开始-->
<script language="JavaScript" src="http://www.jxnews.com.cn/js/epaper.js"></script>
<!--流量统计代码结束-->
</body>
</html>
<!--enpproperty <founder-date>2017-10-09 23:59:57</founder-date><founder-pagenum>A01</founder-pagenum><founder-papername>江西日报</founder-papername><founder-type>2</founder-type><founder-pagepicurl>jxrb/page/186/2017-10-09/A01/1141507497937906.jpg</founder-pagepicurl><founder-content>江西日报</founder-content> /enpproperty-->
'''

datetime = str(datetime.date.today()).split('-')  #对日期进行拆分，返回一个['2017', '10', '09']形式的列表

url_prefix = 'http://epaper.jxnews.com.cn/jxrb/html/'
url_prefix_add = 'http://epaper.jxnews.com.cn/jxrb/html/' + datetime[0] + '-' + datetime[1] + '/' + datetime[2] + '/'
url_prefix_add2 = 'http://epaper.jxnews.com.cn/jxrb/html/' + datetime[0] + '-' + datetime[1] + '/' + datetime[2] + '/' + 'node_187.htm'

print(url_prefix_add)

soup = BeautifulSoup(''.join(html))

#print(soup)

banmiankuai = soup.find('table',{'cellpadding':'2'})

#print(banmiankuai)
urlist = []

for link in banmiankuai.findAll('a'):
    if 'pdf' in link['href']:
        continue
    urlist.append(url_prefix_add + link['href'])
print(urlist)


td = soup.find('td',{'width':'403'})

print(td)

for link in td.findAll('a'):
    print(link['href'])
    print(link.contents[0])
dic = dict(name='tr', attrs={'bgcolor':'#FFFFFF'})
print(dic)