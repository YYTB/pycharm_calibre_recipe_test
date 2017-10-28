# coding=utf-8

from BeautifulSoup import BeautifulSoup
import datetime, re

doc = """

<!DOCTYPE html PUBLIC "-//W3C//DTD XHTML 1.0 Transitional//EN" "http://www.w3.org/TR/xhtml1/DTD/xhtml1-transitional.dtd">
<html xmlns="http://www.w3.org/1999/xhtml">
<head>
<meta http-equiv="Content-Type" content="text/html; charset=utf-8" />
<meta name="Keywords" content="中国袁州,袁州区,yuanzhou,yuanzhouqu,yichunshiyuanzhou,袁州区,袁州区政府,宜春市袁州区">
<meta name="Description" content="中国袁州区政府官方网站，yuanzhouquZhengfu.">
<title>袁州区政府网</title>
<link href="../../../images/yzWeb.css" type="text/css" rel="stylesheet" />
<script src="../../../images/yzq.js"></script>
<script src="../../../images/Client.js"></script>
<style type="text/css">
<!--
body {
	background-image: url(../../../images/yz_bg.gif);
	background-position:center top;
	background-repeat:no-repeat;
	margin:0px;padding:0px;
}
-->
</style>
</head>
<body>
<table width="1004" border="0" align="center" cellpadding="0" cellspacing="0">
  <tr>
    <td height="30" background="../../../images/yz_sbg.gif"><table width="285" border="0" align="right" cellpadding="0" cellspacing="0">
      <tr>
        <td height="30" align="center" width="37"><img src="../../../images/she.jpg" width="13" height="13" /></td>
        <td width="57" align="left"><a title="把本站设为首页" onclick="this.style.behavior='url(#default#homepage)';this.setHomePage('http://www.yzq.gov.cn/');" href="#" class="she">设为首页</a></td>
        <td width="37" align="center"><img src="../../../images/she.jpg" width="13" height="13" /></td>
        <td width="57" align="left"><a title="把本站加入收藏夹" onclick="javascript:window.external.addFavorite('http://www.yzq.gov.cn','袁州区政府网')" href="#" class="she">收藏本站</a></td>
        <td width="30" align="center"><img src="../../../images/she.jpg" width="13" height="13" /></td>
        <td width="57" align="left"><script src="../../../images/2013jfzh.js"></script></td>
        <td width="10">&nbsp;</td>
      </tr>
    </table></td>
  </tr>
  <tr>
    <td><img src="../../../images/yz_top.gif" width="1004" height="232" /></td>
  </tr>
  <tr>
    <td height="40" background="../../../images/yz_dhbg.gif"><table width="820" border="0" align="left" cellpadding="0" cellspacing="0">
     <tr><td height="8"></td></tr>
      <tr align="center">
        <td width="70"></td>
        <td height="31" width="100"><a href="../../../"><img src="../../../images/shouye.gif" width="85" height="31" /></a></td>
        <td width="130"><a href="../../../mlyz/" target=_blank><img src="../../../images/mlyz.gif" width="105" height="31" /></a></td>
        <td width="130"><a href="../../" target=_blank><img src="../../../images/zwgk.gif" width="105" height="31" /></a></td>
        <td width="130"><a href="../../../wsbs/" target=_blank><img src="../../../images/wsbs.gif" width="105" height="31" /></a></td>
        <td width="130"><a href="../../../zmhd/" target=_blank><img src="../../../images/zmhd.gif" width="105" height="31" /></a></td>
        <td width="130"><a href="../../../wzdh/" target=_blank><img src="../../../images/wzdh.gif" width="105" height="31" /></a></td>
      </tr>
    </table></td>
  </tr>
  <tr>
    <td height="40" background="../../../images/yz_tqbg.gif"><table width="100%" border="0" cellspacing="0" cellpadding="0">
      <tr>
         <td width="20" align="right"></td>
        <td height="30" width="180" align="left" valign="middle">今天是：<span class="Content_ExtField">
              <script>
 <!---                            
 today=new Date();               
 var hours = today.getHours();       
 var minutes = today.getMinutes();       
 var seconds = today.getSeconds();    
 var timeValue = "<FONT class=cn3>" + ((hours >12) ? hours -12 :hours); timeValue += ((minutes < 10) ? "<BLINK><FONT class=cn3>:</FONT></BLINK>0" : "<BLINK><FONT class=cn3>:</FONT></BLINK>") + minutes+"</FONT></FONT>";       
 timeValue += (hours >= 12) ? "<FONT class=cn3><I><B>pm</B></I></FONT>" : "<FONT class=cn3><B><I>am</I></B></FONT>";       
 function initArray(){           
 this.length=initArray.arguments.length       
 for(var i=0;i<this.length;i++)       
 this[i+1]=initArray.arguments[i] }       
 var d=new initArray("<font class=cn3>星期日","<font class=cn3>星期一","<font class=cn3>星期二","<font class=cn3>星期三","<font class=cn3>星期四","<font class=cn3>星期五","<font class=cn3>星期六"); document.write("<font class=cn3>",today.getYear(),"<font class=cn3>年","<font class=cn3>",today.getMonth()+1,"<font class=cn3>月","<font class=cn3>",today.getDate(),"<font class=cn3>日 </FONT>",d[today.getDay()+1]," ");        
//-->                            
                </script>
            </span></td>
          <td width="20"></td>
         <td width="65" align="center"></td>
         <td width="260" valign="middle" align="left"></td>
        <td>
         <form  name="SearchForm" method="post"  accept-charset="utf-8"  action="http://xxjs.yichun.gov.cn:8082/was5/web/search" target="_blank" style="margin:0; padding:0" onsubmit="SearchForm_onsubmit();return false;">
        <table width="100%" border="0" cellspacing="0" cellpadding="0">
          <tr>
            <td height="30" width="39" align="center"><img src="../../../images/ss.gif" width="19" height="20" /></td>
            <td width="70"><strong style="color:#e46120;">信息检索：</strong></td>
            <td width="130" valign="middle"><input type="hidden" name="searchword" />
              <input type="hidden" name="channelid" value="259155" />
              <INPUT id="keyword" name="keyword" class=text maxLength=20 size=14 /></td>
              <td width="90"><SELECT name=type>
                <OPTION selected 
                    value="DOCTITLE">信息标题</OPTION>
                <OPTION 
                    value="doccontent">信息正文</OPTION>
              </SELECT></td>
            <td width="130"><input type="submit" style="cursor:pointer" class="btn_blue55" name="button" id="button" value="搜 索" /><input type="button" class="btn_blue56" style="cursor:pointer" name="button" id="button" value="高级检索" onclick="window.open('http://xxjs.yichun.gov.cn:8082/was5/web/wcmadvanced.jsp?channelid=259155')" /></td>
          </tr>
        </table>
        </form>
         <script type="text/javascript"> 
							function SearchForm_onsubmit() {
								 var tempkeyword=document.SearchForm.keyword.value;
								 var tempchannelid=document.SearchForm.keyword.value;
								 var searchtype=document.SearchForm.type.value;
								 if(!tempkeyword){
									alert("请输入关键字");
									return false;
								 }
								 if(zhuru(tempkeyword)==1){
								    alert("含有非法字符");
									return false;
								 }
								document.SearchForm.searchword.value=searchtype+"=%"+tempkeyword+"%";
								 if(!window.ActiveXObject){document.charset='utf-8';}
								document.charset='utf-8';
								document.SearchForm.submit();
							} 
							function zhuru(zhi){
								var re= new Array("and","exec","insert","select","update","chr","mid","master","or","truncate","declare","join","delete","char");
								var pan=0;
								for(var i=0;i<re.length;i++){
									if(zhi.indexOf(re[i])>-1)//有sql注入
									{
										pan=1;
										break;
									}
								}
								return pan;
							}
						</script>
        </td>
      </tr>
    </table></td>
  </tr>
  <tr>
    <td height="8"></td>
  </tr>
</table>
<table width="1004" border="0" align="center" cellpadding="0" cellspacing="0" bgcolor="#FFFFFF">
<tr></tr>
<tr>
  <td width="6"></td>
  <td width="262" valign="top"><table width="100%" border="0" cellspacing="0" cellpadding="0">
    <tr>
      <td height="27" background="../../../images/2014lblm.jpg"><table width="100%" border="0" cellspacing="0" cellpadding="0">
        <tr>
          <td height="27" width="20"></td>
          <td align="left" class="cjfw">政务动态</td>
        </tr>
      </table></td>
    </tr>
    <tr>
      <td id="bk" bgcolor="#ffefdb">
      <table width="92%" border="0" align="center" cellpadding="0" cellspacing="0" style="margin-top:10px;">
       
       
        <tr>
          <td height="25" width="18%" align="center"><img src="../../../images/jian.gif" width="11" height="11" /></td>
          <td width="74%" align="left"><a href="./" target="_parent" class="lmmc">政务要闻</a></td>
        </tr>
          
           
       
        <tr>
          <td height="25" width="18%" align="center"><img src="../../../images/jian.gif" width="11" height="11" /></td>
          <td width="74%" align="left"><a href="../zhxx/" target="_parent" class="lmmc">综合信息</a></td>
        </tr>
          
           
       
        <tr>
          <td height="25" width="18%" align="center"><img src="../../../images/jian.gif" width="11" height="11" /></td>
          <td width="74%" align="left"><a href="../yzsp/" target="_parent" class="lmmc">袁州视频</a></td>
        </tr>
          
           
       
        <tr>
          <td height="25" width="18%" align="center"><img src="../../../images/jian.gif" width="11" height="11" /></td>
          <td width="74%" align="left"><a href="../dbtxw/" target="_parent" class="lmmc">大标题新闻</a></td>
        </tr>
          
           
       
        <tr>
          <td height="25" width="18%" align="center"><img src="../../../images/jian.gif" width="11" height="11" /></td>
          <td width="74%" align="left"><a href="../gggs/" target="_parent" class="lmmc">公告公示</a></td>
        </tr>
          
           
       
        <tr>
          <td height="25" width="18%" align="center"><img src="../../../images/jian.gif" width="11" height="11" /></td>
          <td width="74%" align="left"><a href="../rdzt/" target="_parent" class="lmmc">热点专题</a></td>
        </tr>
          
           
      </table>
      </td>
    </tr>
  </table></td>
  <td width="15"></td>
  <td valign="top" width="715"><table width="100%" border="0" cellspacing="0" cellpadding="0">
    <tr>
      <td background="../../../images/qysmbg.jpg"><table width="100%" border="0" cellspacing="0" cellpadding="0" id="bk">
                      <tr>
                        <td height="30" width="95" align="center" style="color:#7c7c7c">您的当前位置</td>
                        <td background="../../../images/2014zfzx.jpg" style="color:#7c7c7c" align="left"><a href="../../../" title="首页" class="CurrChnlCls">首页</a>&nbsp;&gt;&gt;&nbsp;<a href="../../" title="政务公开" class="CurrChnlCls">政务公开</a>&nbsp;&gt;&gt;&nbsp;<a href="../" title="政务动态" class="CurrChnlCls">政务动态</a>&nbsp;&gt;&gt;&nbsp;<a href="./" title="政务要闻" class="CurrChnlCls">政务要闻</a></td>
                      </tr>
                    </table></td>
    </tr>
    <tr>
      <td height="12"></td>
    </tr>
    <tr>
      <td><table width="100%" border="0" cellspacing="0" cellpadding="0">
        <tr>
          <td background="../../../images/2014mcbg.jpg" height="27"><table width="100%" border="0" cellspacing="0" cellpadding="0">
  <tr>
    <td height="27" width="20">&nbsp;</td>
    <td class="cjfw">政务要闻</td>
  </tr>
</table></td>
        </tr>
        <tr>
          <td id="bk"><TABLE width="97%" border=0 align="center" cellPadding=1 cellSpacing=1 style="margin-top:10px;">
                          <TBODY>
                            
							
                            <TR>
                              <TD height=25 align="left"><IMG src="../../../images/lb-xtb.gif" width=4 height=6 />&nbsp;<A 
                        href="./201710/t20171020_398361.html">袁州区财政局掀起学习贯彻省、市、区有关文件精神热潮</A></TD>
                              <TD width="60" align="right">2017-10-20</TD>
                            </TR>
                            
                            <TR>
                              <TD height=25 align="left"><IMG src="../../../images/lb-xtb.gif" width=4 height=6 />&nbsp;<A 
                        href="./201710/t20171020_398360.html">袁州区农业局进行脱贫攻坚“百日行动”部署工作</A></TD>
                              <TD width="60" align="right">2017-10-20</TD>
                            </TR>
                            
                            <TR>
                              <TD height=25 align="left"><IMG src="../../../images/lb-xtb.gif" width=4 height=6 />&nbsp;<A 
                        href="./201710/t20171019_398230.html">袁州医药工业园组织收看十九大开幕会</A></TD>
                              <TD width="60" align="right">2017-10-19</TD>
                            </TR>
                            
                            <TR>
                              <TD height=25 align="left"><IMG src="../../../images/lb-xtb.gif" width=4 height=6 />&nbsp;<A 
                        href="./201710/t20171019_398228.html">慈化镇组织观看十九大开幕会</A></TD>
                              <TD width="60" align="right">2017-10-19</TD>
                            </TR>
                            
                            <TR>
                              <TD height=25 align="left"><IMG src="../../../images/lb-xtb.gif" width=4 height=6 />&nbsp;<A 
                        href="./201710/t20171019_398220.html">袁州区广大党员干部和群众收听收看党的十九大开幕盛况</A></TD>
                              <TD width="60" align="right">2017-10-18</TD>
                            </TR>
                            
                            <TR height=1>
                              <TD colspan=2 class="GroupBlankLine"></TD>
                            </TR>
                             
							
                            <TR>
                              <TD height=25 align="left"><IMG src="../../../images/lb-xtb.gif" width=4 height=6 />&nbsp;<A 
                        href="./201710/t20171018_398142.html">袁州区查处侵害群众利益问题326个</A></TD>
                              <TD width="60" align="right">2017-10-18</TD>
                            </TR>
                            
                            <TR>
                              <TD height=25 align="left"><IMG src="../../../images/lb-xtb.gif" width=4 height=6 />&nbsp;<A 
                        href="./201710/t20171018_398141.html">袁州区市场监管局三阳分局集中治理食品安全</A></TD>
                              <TD width="60" align="right">2017-10-18</TD>
                            </TR>
                            
                            <TR>
                              <TD height=25 align="left"><IMG src="../../../images/lb-xtb.gif" width=4 height=6 />&nbsp;<A 
                        href="./201710/t20171018_398140.html">袁州区举办“喜迎十九大老年书画作品展”</A></TD>
                              <TD width="60" align="right">2017-10-18</TD>
                            </TR>
                            
                            <TR>
                              <TD height=25 align="left"><IMG src="../../../images/lb-xtb.gif" width=4 height=6 />&nbsp;<A 
                        href="./201710/t20171017_398088.html">袁州区做好畜牧兽医医疗卫生津贴发放工作</A></TD>
                              <TD width="60" align="right">2017-10-17</TD>
                            </TR>
                            
                            <TR>
                              <TD height=25 align="left"><IMG src="../../../images/lb-xtb.gif" width=4 height=6 />&nbsp;<A 
                        href="./201710/t20171016_398039.html">袁州文化墙秀出文明景</A></TD>
                              <TD width="60" align="right">2017-10-16</TD>
                            </TR>
                            
                            <TR height=1>
                              <TD colspan=2 class="GroupBlankLine"></TD>
                            </TR>
                             
							
                            <TR>
                              <TD height=25 align="left"><IMG src="../../../images/lb-xtb.gif" width=4 height=6 />&nbsp;<A 
                        href="./201710/t20171016_398038.html">三阳狠抓环境整治扮靓家园</A></TD>
                              <TD width="60" align="right">2017-10-16</TD>
                            </TR>
                            
                            <TR>
                              <TD height=25 align="left"><IMG src="../../../images/lb-xtb.gif" width=4 height=6 />&nbsp;<A 
                        href="./201710/t20171016_398030.html">袁州区四措并举开展降成本优环境专项行动</A></TD>
                              <TD width="60" align="right">2017-10-16</TD>
                            </TR>
                            
                            <TR>
                              <TD height=25 align="left"><IMG src="../../../images/lb-xtb.gif" width=4 height=6 />&nbsp;<A 
                        href="./201710/t20171013_397991.html">中心城区棚户区改造第二批签约工作启动啦</A></TD>
                              <TD width="60" align="right">2017-10-13</TD>
                            </TR>
                            
                            <TR>
                              <TD height=25 align="left"><IMG src="../../../images/lb-xtb.gif" width=4 height=6 />&nbsp;<A 
                        href="./201710/t20171013_397885.html">袁州区完成中央环保督察反馈的22家问题猪场整改工作</A></TD>
                              <TD width="60" align="right">2017-10-13</TD>
                            </TR>
                            
                            <TR>
                              <TD height=25 align="left"><IMG src="../../../images/lb-xtb.gif" width=4 height=6 />&nbsp;<A 
                        href="./201710/t20171013_397884.html">袁州区签约引进总投资40亿元的年产750万只品牌钟表及2500万套可穿戴设备生产项目</A></TD>
                              <TD width="60" align="right">2017-10-13</TD>
                            </TR>
                            
                            <TR height=1>
                              <TD colspan=2 class="GroupBlankLine"></TD>
                            </TR>
                             
							
                            <TR>
                              <TD height=25 align="left"><IMG src="../../../images/lb-xtb.gif" width=4 height=6 />&nbsp;<A 
                        href="./201710/t20171013_397883.html">化成街道特色文化街巷接地气润民心</A></TD>
                              <TD width="60" align="right">2017-10-13</TD>
                            </TR>
                            
                            <TR>
                              <TD height=25 align="left"><IMG src="../../../images/lb-xtb.gif" width=4 height=6 />&nbsp;<A 
                        href="./201710/t20171013_397882.html">袁州医药工业园11家涉水企业全部完成在线监控设施建设</A></TD>
                              <TD width="60" align="right">2017-10-13</TD>
                            </TR>
                            
                            <TR>
                              <TD height=25 align="left"><IMG src="../../../images/lb-xtb.gif" width=4 height=6 />&nbsp;<A 
                        href="./201710/t20171012_397795.html">袁州区兽医处方专项整顿行动成效显著</A></TD>
                              <TD width="60" align="right">2017-10-12</TD>
                            </TR>
                            
                            <TR>
                              <TD height=25 align="left"><IMG src="../../../images/lb-xtb.gif" width=4 height=6 />&nbsp;<A 
                        href="./201710/t20171012_397794.html">袁州区：严厉整治和查处侵害群众利益突出问题</A></TD>
                              <TD width="60" align="right">2017-10-12</TD>
                            </TR>
                            
                            <TR>
                              <TD height=25 align="left"><IMG src="../../../images/lb-xtb.gif" width=4 height=6 />&nbsp;<A 
                        href="./201710/t20171012_397789.html">袁州发展鲜花产业助农脱贫</A></TD>
                              <TD width="60" align="right">2017-10-12</TD>
                            </TR>
                            
                            <TR height=1>
                              <TD colspan=2 class="GroupBlankLine"></TD>
                            </TR>
                             
							
                            <TR>
                              <TD height=25 align="left"><IMG src="../../../images/lb-xtb.gif" width=4 height=6 />&nbsp;<A 
                        href="./201710/t20171011_397581.html">鲁旭东主持召开环城西路环境综合整治工作会议</A></TD>
                              <TD width="60" align="right">2017-10-11</TD>
                            </TR>
                            
                            <TR>
                              <TD height=25 align="left"><IMG src="../../../images/lb-xtb.gif" width=4 height=6 />&nbsp;<A 
                        href="./201710/t20171011_397578.html">袁州区下浦街道财政所转作风强建设塑形象</A></TD>
                              <TD width="60" align="right">2017-10-11</TD>
                            </TR>
                            
                            <TR>
                              <TD height=25 align="left"><IMG src="../../../images/lb-xtb.gif" width=4 height=6 />&nbsp;<A 
                        href="./201710/t20171011_397577.html">慈化镇开展“十诊”工作保平安</A></TD>
                              <TD width="60" align="right">2017-10-11</TD>
                            </TR>
                            
                            <TR>
                              <TD height=25 align="left"><IMG src="../../../images/lb-xtb.gif" width=4 height=6 />&nbsp;<A 
                        href="./201710/t20171011_397575.html">袁州区：举办老年书画作品展</A></TD>
                              <TD width="60" align="right">2017-10-11</TD>
                            </TR>
                            
                            <TR>
                              <TD height=25 align="left"><IMG src="../../../images/lb-xtb.gif" width=4 height=6 />&nbsp;<A 
                        href="./201710/t20171010_397448.html">袁州区财政局举办“庆国庆 迎十九大”演讲赛</A></TD>
                              <TD width="60" align="right">2017-10-10</TD>
                            </TR>
                            
                            <TR height=1>
                              <TD colspan=2 class="GroupBlankLine"></TD>
                            </TR>
                             
                          </TBODY>
                      </TABLE></td>
        </tr>
        <tr><td><div align="center">
                                <table width="94%" border="0" align="center" cellpadding="0" cellspacing="0">
                                  <tr>
                                    <td align="center" height="40"><script>

<!--

function createPageHTML(_nPageCount, _nCurrIndex, _sPageName, _sPageExt)
{ 
//tita 翻页函数

//定义翻页的字体样式
var styleDIY = "fystyle";

if(_nPageCount == null || _nPageCount<=0){
return; 
} 

//tita
document.write("　　");

if(_nPageCount==1)
	document.write("<font class=\"" + styleDIY +"\">首页</font> <font class=\"" + styleDIY +"\">上一页</font> <font class=\"" + styleDIY +"\">下一页</font> <font class=\"" + styleDIY +"\">尾页</font>")
else
{
	if(_nPageCount==2)
	{
		if (_nCurrIndex==0)
			document.write("<font class=\"" + styleDIY +"\">首页</font> <font class=\"" + styleDIY +"\">上一页</font> <a href=\""+_sPageName+"_" + (_nCurrIndex+1) + "."+_sPageExt+"\" class=\"" + styleDIY +"\">下一页</a> <a href=\""+_sPageName+"_" + (_nPageCount-1) + "."+_sPageExt+"\" class=\"" + styleDIY +"\">尾页</a>")
		else
		{
			if (_nCurrIndex==1)
				document.write("<a href=\""+_sPageName+"."+_sPageExt+"\" class=\"" + styleDIY +"\">首页</a> <a href=\""+_sPageName+"."+_sPageExt+"\" class=\"" + styleDIY +"\">上一页</a> <font class=\"" + styleDIY +"\">下一页</font> <font class=\"" + styleDIY +"\">尾页</font>")
		}
	}
	else
	{
		if (_nCurrIndex==0)
			document.write("<font class=\"" + styleDIY +"\">首页</font> <font class=\"" + styleDIY +"\">上一页</font> <a href=\""+_sPageName+"_" + (_nCurrIndex+1) + "."+_sPageExt+"\" class=\"" + styleDIY +"\">下一页</a> <a href=\""+_sPageName+"_" + (_nPageCount-1) + "."+_sPageExt+"\" class=\"" + styleDIY +"\">尾页</a>")
		else
		{
			if (_nCurrIndex==1)
				document.write("<a href=\""+_sPageName+"."+_sPageExt+"\" class=\"" + styleDIY +"\">首页</a> <a href=\""+_sPageName+"."+_sPageExt+"\" class=\"" + styleDIY +"\">上一页</a> <a href=\""+_sPageName+"_" + (_nCurrIndex+1) + "."+_sPageExt+"\" class=\"" + styleDIY +"\">下一页</a> <a href=\""+_sPageName+"_" + (_nPageCount-1) + "."+_sPageExt+"\" class=\"" + styleDIY +"\">尾页</a>")
			else
			{
				if (_nCurrIndex<_nPageCount-1)
					document.write("<a href=\""+_sPageName+"."+_sPageExt+"\" class=\"" + styleDIY +"\">首页</a> <a href=\""+_sPageName+"_" + (_nCurrIndex-1) + "."+_sPageExt+"\" class=\"" + styleDIY +"\">上一页</a> <a href=\""+_sPageName+"_" + (_nCurrIndex+1) + "."+_sPageExt+"\" class=\"" + styleDIY +"\">下一页</a> <a href=\""+_sPageName+"_" + (_nPageCount-1) + "."+_sPageExt+"\" class=\"" + styleDIY +"\">尾页</a>")
				else
				{
					if (_nCurrIndex==_nPageCount-1)
						document.write("<a href=\""+_sPageName+"."+_sPageExt+"\" class=\"" + styleDIY +"\">首页</a> <a href=\""+_sPageName+"_" + (_nCurrIndex-1) + "."+_sPageExt+"\" class=\"" + styleDIY +"\">上一页</a> <font class=\"" + styleDIY +"\">下一页</font> <font class=\"" + styleDIY +"\">尾页</font>")
				}
			}
		}
	}
}
document.write("　<font class=\"" + styleDIY +"\">总共" + _nPageCount + "页</font>　");
document.write("<font class=\"" + styleDIY +"\">当前第" + (_nCurrIndex+1) + "页</font>　");
document.write("<select name=\"select\" style=\"margin-bottom:-3px;\" onchange=\"location.replace(this.value)\">");
document.write("<option selected >转到</option>");
for(var i=0; i<_nPageCount; i++)
{
	if(i==0)
		document.write("<option value=\""+_sPageName+"."+_sPageExt+"\">第1页</option>");
	else
		document.write("<option value=\""+_sPageName+"_" + i + "."+_sPageExt+"\">第"+(i+1)+"页</option>");
}
document.write("</select>");
//tita 
} //WCM置标



-->

</script>
<script>createPageHTML(120, 0, "index", "html");</script></td>
                                  </tr>
                                </table>
                      </div></td></tr>
      </table></td>
    </tr>
  </table></td>
  <td width="6">&nbsp;</td>
</tr>
</table>
<table width="1004" border="0" align="center" cellpadding="0" cellspacing="0">
  <tr>
    <td height="10"></td>
  </tr>
</table>
<table width="1004" border="0" align="center" cellpadding="0" cellspacing="0">
  <tr>
    <td><table border="0" cellspacing="0" cellpadding="0" width="100%" align="center" id="bk" background="../../../images/qysmbg.jpg">
            <tbody>
                <tr>
                    <td width="100" height="30" align="center" class="cjfw">友情链接</td>
                    <td width="242">
                    <div align="center"><select style="background-color: #ffffff; color: #000000" class="zf1" onchange="javascript:window.open(this.options[this.selectedIndex].value)" name="select">
                    <option selected="selected">区政府部门网站</option>         
                    <option value="http://www.yzqggzy.com/">袁州区公共资源交易网</option>
                    <option value="http://www.yzqtravel.gov.cn/">袁州旅游网</option>
                     <option value="http://ycyzq.jxgtt.gov.cn/Index.shtml">宜春市国土资源局袁州分局</option>
                    </select></div>
                    </td>
                    <td width="220" align="center">
                    <div align="center"><select style="background-color: #ffffff; color: #000000" class="zf1" onchange="javascript:window.open(this.options[this.selectedIndex].value)" name="select3">
                    <option selected="selected">县市区政府网站</option>
                    <option value="http://www.yichun.gov.cn/">中国宜春政府网</option>
                    <option value="http://www.zhangshu.gov.cn/">樟树政府网</option>
                    <option value="http://www.gaoan.gov.cn/">高安政府网</option>
                    <option value="http://www.wanzai.gov.cn/">万载政府网</option>
                    <option value="http://www.shanggao.gov.cn/">上高政府网</option>
                    <option value="http://www.jxyf.gov.cn/">宜丰政府网</option>
                    <option value="http://www.fengxin.gov.cn/">奉新政府网</option>
                    <option value="http://www.jxjaxzf.gov.cn/">靖安政府网</option>
                    <option value="http://www.tonggu.gov.cn/">铜鼓政府网</option>
                    <option value="http://www.jxfc.gov.cn/">丰城政府网</option>
                    </select></div>
                    </td>
                    <td width="220" align="center"><div align="center"> <div align="center"> <select style="background-color: #ffffff; color: #000000" class="q2" onchange="javascript:window.open(this.options[this.selectedIndex].value)" name="select2">
                    <option selected="selected">国内各政府网站</option>
                    <option value="http://www.gov.cn/">中央人民政府网站</option>
                    <option value="http://www.beijing.gov.cn/">首都之窗</option>
                    <option value="http://www.sh.gov.cn/">中国上海</option>
                    <option value="http://www.wh.gov.cn/">武汉市人民政府</option>
                    <option value="http://www.xm.gov.cn/">厦门市人民政府</option>
                    <option value="http://www.guangzhou.gov.cn/">中国广州网</option>
                    <option value="http://www.hangzhou.gov.cn/">杭州市人民政府</option>
                    <option value="http://www.sz.gov.cn/">深圳政府在线</option>
                    <option value="http://www.chengdu.gov.cn/">中国成都</option>
                    <option value="http://www.shenyang.gov.cn/">沈阳市人民政府</option>
                    <option value="http://www.dalian.gov.cn/">中国大连</option>
                    <option value="http://www.harbin.gov.cn/">中国哈尔滨</option>
                    <option value="http://www.jinan.gov.cn/">济南市人民政府</option>
                    <option value="http://www.cc.jl.gov.cn/">长春市人民政府</option>
                    <option value="http://www.ningbo.gov.cn/">宁波市人民政府</option>
                    <option value="http://www.gov.qd.sd.cn/n172/index.html">青岛政务网</option>
                    </select></div></div></td>
                    <td width="220">
                    <div align="center"><select style="background-color: #ffffff; color: #000000" class="q2" onchange="javascript:window.open(this.options[this.selectedIndex].value)" name="select4">
                    <option selected="selected">江西省政府网站</option>
                    <option value="http://www.nc.gov.cn/">南昌市</option>
                    <option value="http://www.jiujiang.gov.cn/">九江市</option>
                    <option value="http://www.jdz.gov.cn/">景德镇市</option>
                    <option value="http://www.pingxiang.gov.cn/">萍乡市</option>
                    <option value="http://www.xinyu.gov.cn/">新余市</option>
                    <option value="http://www.zgsr.gov.cn/">上饶市</option>
                    <option value="http://www.yingtan.gov.cn/">鹰潭市</option>
                    <option value="http://www.jian.gov.cn/">吉安市</option>
                    <option value="http://www.ganzhou.gov.cn/">赣州市</option>
                    <option value="http://www.jxfz.gov.cn/">抚州市</option>
                    </select></div>
                    </td>
                </tr>
            </tbody>
    </table></td>
  </tr>
  <tr>
    <td height="142" background="../../../images/bottombg.gif" valign="top"><table width="70%" border="0" cellspacing="0" cellpadding="0" align="center">
      <tr>
        <td height="30"></td>
      </tr>
      <tr>
        <td height="30" align="center">主办：袁州区人民政府　 承办：袁州区人民政府办公室  　技术支持：袁州区信息服务中心</td>
      </tr>
      <tr>
        <td height="30" align="center">电子邮件：yzq@yzq.gov.cn 　邮编：336000</td>
      </tr>
      <tr>
        <td height="30" align="center">版权所有 赣ICP备05010765号</td>
      </tr>
    </table></td>
  </tr>
</table> 
</body>
</html>

"""

soup = BeautifulSoup(''.join(doc))

table = soup.find('table', {'width': '97%'})

datetime_t = str(datetime.date.today()).split('-')
# print(datetime_t)


articles_link = []
for tr in table.findAll('tr'):
    # print(tr)

    find_today = re.compile(r'(\d\d)-(\d\d)</td>')  # 构建找到末尾发布日期的正则表达式
    month = find_today.search(str(tr))  # 把上面构建的表达式作用于findAll找出来的内容

    try:
        d1 = datetime.date.today()  # 获取今天的日期
        d2 = datetime.date(int(datetime_t[0]), int(month.group(1)), int(month.group(2)))  # 获取新闻的日期
        days_betwen = (d1 - d2).days  # 获取日期差
        if days_betwen <= 30:
            articles_link.append(str(tr))

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