# coding=utf-8

from BeautifulSoup import BeautifulSoup
import datetime,re

doc = """

<!DOCTYPE html PUBLIC "-//W3C//DTD XHTML 1.0 Transitional//EN" "http://www.w3.org/TR/xhtml1/DTD/xhtml1-transitional.dtd">
<html xmlns="http://www.w3.org/1999/xhtml">
<head>
<meta http-equiv="Content-Type" content="text/html; charset=utf-8" />
<title>中国宜春_公开</title>
<link href="../../../images/2016yc_Web.css" type="text/css" rel="stylesheet" />
<script language="javascript" src="../../../images/jquery.pack.js"></script>
<script src="../../../images/2016Client.js"></script>
<script src="../../../images/2016yczfw.js"></script>
<script src="../../../images/2016hd_index.js"></script>

<style type="text/css">
<!--
body {
	background-image: url(../../../images/2016bg.jpg);
	background-color:#ffffff;
	background-repeat:no-repeat;
	background-position:center top;
	 margin:0px;padding:0px;
}
-->
</style>
</head>
<body>
<table width="999" border="0" align="center" cellpadding="0" cellspacing="0">
  <tr>
    <td height="35" bgcolor="#f0f0f0"><table width="100%" border="0" cellspacing="0" cellpadding="0">
      <tr align="center">
        <td height="35" width="58"><a href="../../../"><img src="../../../images/2016sw.jpg" width="47" height="24" /></a></td>
        <td width="56"><a href="http://www.ycrd.gov.cn/" target="_blank"><img src="../../../images/2016rd.jpg" width="47" height="24" /></a></td>
        <td width="57"><a href="http://www.zxyc.gov.cn/" target="_blank"><img src="../../../images/2016zx.jpg" width="50" height="24" /></a></td>
        <td width="442" valign="middle">
        <table width="90%" border="0" cellspacing="0" cellpadding="0">
          <tr>
           <form action="http://mail.yichun.gov.cn/coremail/login.jsp" method="post" name="MailFormLogin" target="_self" id="MailFormLogin2" style="height:25px;">
            <td width="18%" align="center" style="color:#b70d0d;">政务邮箱：</td>
            <td width="13%">用户名</td>
            <td width="20%" align="center" valign="middle"><input type="text" name="uid" size="8" style="height:22px; border:1px #a7a7a7 solid;" /></td>
            <td width="7%">密码</td>
            <td width="20%" align="center" valign="middle"><input type="password" name="password" size="8" style="height:22px; border:1px #a7a7a7 solid;" /></td>
            <td width="11%" valign="middle"><input name="enter" type="submit" id="enter" value="登录" /></td>
            <td width="11%"><input name="login" type="reset" value="重置" /><input type="hidden" name="domain" id="domain" value="yichun.gov.cn" />
<input type="hidden" name="face" value="XT5" /> </td>
            </form>
          </tr>
        </table>
        </td>
        <td width="62"><a target="_blank" href="http://www.yichun.gov.cn/wzdh/bwzdh/201701/t20170125_491624.html"><img title="微信" src="../../../images/2014gb_1212_weixin.png" width="25" height="25" /></a></td>
         <td width="31" align="left"><a target="_blank" href="http://e.weibo.com/u/3860420669/"><img title="政务微博" src="../../../images/2016zw_wb.jpg" width="25" height="25" /></a></td>
        <td width="65"><script src="../../../images/2016jfzh.js"></script></td>
        <td width="57"><a target="_blank" href="/English/index.html">English</a></td>
        <td width="49"><A href="../../../rss/" 
            target=_blank> RSS订阅</A></td>
	    <td width="59"><A href="../../../index_2166.html" 
            target=_blank> 掌上宜春</A></td>
		<td width="63" align="left"></td>
      </tr>
    </table></td>
  </tr>
  <tr>
    <td height="152" background="../../../images/2016topbg.jpg" style="background-repeat:no-repeat;"><table width="100%" border="0" cellspacing="0" cellpadding="0">
  <tr>
    <td height="109" onmouseover="dh_change(1)"></td>
  </tr>
  <tr>
    <td><table width="100%" border="0" cellspacing="0" cellpadding="0">
      <tr align="left" valign="bottom">
        <td height="40" width="85" id="topdh1"><a href="../../../"><img id="headernavimg1" src="../../../images/2016headernavimg1_off.jpg" width="85" height="35" /></a></td>
        <td width="85" id="topdh2" height="40"><a href="../../../zjyc/" alt="市情"><img id="headernavimg2" src="../../../images/2016headernavimg2_off.jpg" width="85" height="35" /></a></td>
        <td width="85" id="topdh3"><a href="../../" alt="公开"><img id="headernavimg3" src="../../../images/2016headernavimg3_off.jpg" width="85" height="35" /></a></td>
        <td width="85" id="topdh4"><a href="../../../wsbs/" alt="服务"><img id="headernavimg4" src="../../../images/2016headernavimg4_off.jpg" width="85" height="35" /></a></td>
        <td width="85" id="topdh5"><a href="../../../zmhd/" alt="互动"><img id="headernavimg5" src="../../../images/2016headernavimg5_off.jpg" width="85" height="35" /></a></td>
        <td width="85" id="topdh6"><a href="../../../sj/" alt="数据"><img id="headernavimg6" src="../../../images/2016headernavimg6_off.jpg" width="85" height="35" /></a></td>
       <!-- <td width="85" id="topdh7"><a href="../../../cy/" alt="产业"><img id="headernavimg7" src="../../../images/2016headernavimg7_off.jpg" width="85" height="35" /></a></td>-->
        <td width="320" id="topdh8"></td>
        <td><form  name="SearchForm" method="post"  accept-charset="utf-8"  action="http://xxjs.yichun.gov.cn:8082/was5/web/search" target="_blank" style="margin:0; padding:0" onsubmit="SearchForm_onsubmit();return false;"><table width="100%" border="0" cellspacing="0" cellpadding="0">
          <tr>
            <td width="226" height="40"><input type="hidden" name="searchword" />
              <input type="hidden" name="channelid" value="290182" />
              <INPUT id="keyword" name="keyword" maxLength=20 size=30 /></td>
            <td width="38"><input type="submit" class="btn_blue55" style="cursor:pointer" name="button" id="button" value="" /></td>
          </tr>
        </table></form>
         <script type="text/javascript"> 
							function SearchForm_onsubmit() {
								 var tempkeyword=document.SearchForm.keyword.value;
								// alert(tempkeyword);
								 //var tempchannelid=document.SearchForm.channelid.value;

								 if(!tempkeyword){
									alert("请输入关键字");
									return false;
								 }
								 if(zhuru(tempkeyword)==1){
								    alert("含有非法字符");
									return false;
								 }
								document.SearchForm.submit();
//11
</script>
        </td>
      </tr>
    </table></td>
  </tr>
  <tr>
    <td height="3"><img src="../../../images/2016topreb.jpg" width="999" height="3" /></td></tr>
</table>
</td>
  </tr>
</table>
<table width="999" border="0" align="center" cellpadding="0" cellspacing="0">
  <tr>
    <td height="20"></td>
  </tr>
  <tr>
    <td><table width="100%" border="0" cellspacing="0" cellpadding="0">
      <tr>
        <td width="680" valign="top"><table width="100%" border="0" cellspacing="0" cellpadding="0">
  <tr>
    <td height="30" class="grsm" valign="top">您现在的位置：<a href="../../../" title="首页" class="CurrChnlCls">首页</a>&nbsp;&gt;&gt;&nbsp;<a href="../../" title="公开" class="CurrChnlCls">公开</a>&nbsp;&gt;&gt;&nbsp;<a href="../" title="政务动态" class="CurrChnlCls">政务动态</a>&nbsp;&gt;&gt;&nbsp;<a href="./" title="政务要闻" class="CurrChnlCls">政务要闻</a> </td>
  </tr>
  <tr>
    <td><table width="100%" border="0" cellspacing="0" cellpadding="0">
      <tr>
        <td><table width="100%" border="0" cellspacing="0" cellpadding="0">
  <tr align="left">
    <td width="20" height="35"><img src="../../../images/2016gkb.jpg" width="8" height="21" /></td>
    <td class="gk" width="400">政务要闻</td>
    <td align="right" width="260"></td>
  </tr>
</table></td>
      </tr>
      <tr>
        <td></td>
      </tr>
    </table></td>
  </tr>
  <tr>
    <td><table width="100%" border="0" cellspacing="0" cellpadding="0" style="margin-top:15px;">
      <tr>
        <td height="500" valign="top"><TABLE width="100%" border=0 align="center" cellPadding=1 cellSpacing=1 style="margin-top:5px;">
                          <TBODY>
                            
							
                            <TR>
                              <TD height=30 align="left">&nbsp;<img src="../../../images/2016hei.jpg" width="3" height="3" />&nbsp;<A style="font-size:14px;" 
                        href="./201710/t20171015_521060.html">我市在广州举行生态招商推介会</A></TD>
                              <TD width="80" align="left" style="font-size:14px; color:#999">2017-10-14</TD>
                            </TR>
                            
                            <TR>
                              <TD height=30 align="left">&nbsp;<img src="../../../images/2016hei.jpg" width="3" height="3" />&nbsp;<A style="font-size:14px;" 
                        href="./201710/t20171015_521061.html">省政协调研组在宜调研</A></TD>
                              <TD width="80" align="left" style="font-size:14px; color:#999">2017-10-14</TD>
                            </TR>
                            
                            <TR>
                              <TD height=30 align="left">&nbsp;<img src="../../../images/2016hei.jpg" width="3" height="3" />&nbsp;<A style="font-size:14px;" 
                        href="./201710/t20171015_521062.html">张小平在宜丰县调研</A></TD>
                              <TD width="80" align="left" style="font-size:14px; color:#999">2017-10-14</TD>
                            </TR>
                            
                            <TR>
                              <TD height=30 align="left">&nbsp;<img src="../../../images/2016hei.jpg" width="3" height="3" />&nbsp;<A style="font-size:14px;" 
                        href="./201710/t20171013_520878.html">市本级国有资产清收统管整合工作领导小组会议召开</A></TD>
                              <TD width="80" align="left" style="font-size:14px; color:#999">2017-10-13</TD>
                            </TR>
                            
                            <TR>
                              <TD height=30 align="left">&nbsp;<img src="../../../images/2016hei.jpg" width="3" height="3" />&nbsp;<A style="font-size:14px;" 
                        href="./201710/t20171013_520879.html">提高政治站位坚守责任担当 持续推进风清气正政治生态建设</A></TD>
                              <TD width="80" align="left" style="font-size:14px; color:#999">2017-10-13</TD>
                            </TR>
                            
                            <TR height=1>
                              <TD colspan=2 class="GroupBlankLine"></TD>
                            </TR>
                            
							
                            <TR>
                              <TD height=30 align="left">&nbsp;<img src="../../../images/2016hei.jpg" width="3" height="3" />&nbsp;<A style="font-size:14px;" 
                        href="./201710/t20171012_520779.html">学习借鉴萍乡先进经验 加快宜春海绵城市建设</A></TD>
                              <TD width="80" align="left" style="font-size:14px; color:#999">2017-10-12</TD>
                            </TR>
                            
                            <TR>
                              <TD height=30 align="left">&nbsp;<img src="../../../images/2016hei.jpg" width="3" height="3" />&nbsp;<A style="font-size:14px;" 
                        href="./201710/t20171012_520776.html">张小平率队在深圳考察华为公司</A></TD>
                              <TD width="80" align="left" style="font-size:14px; color:#999">2017-10-12</TD>
                            </TR>
                            
                            <TR>
                              <TD height=30 align="left">&nbsp;<img src="../../../images/2016hei.jpg" width="3" height="3" />&nbsp;<A style="font-size:14px;" 
                        href="./201710/t20171012_520780.html">市政协组织开展“促进民办教育事业发展”专题视察活动</A></TD>
                              <TD width="80" align="left" style="font-size:14px; color:#999">2017-10-12</TD>
                            </TR>
                            
                            <TR>
                              <TD height=30 align="left">&nbsp;<img src="../../../images/2016hei.jpg" width="3" height="3" />&nbsp;<A style="font-size:14px;" 
                        href="./201710/t20171012_520782.html">我市与中国建筑“牵手”</A></TD>
                              <TD width="80" align="left" style="font-size:14px; color:#999">2017-10-12</TD>
                            </TR>
                            
                            <TR>
                              <TD height=30 align="left">&nbsp;<img src="../../../images/2016hei.jpg" width="3" height="3" />&nbsp;<A style="font-size:14px;" 
                        href="./201710/t20171012_520785.html">精准扶贫助推全面小康——“喜迎十九大　展示新成就”之扶贫攻坚篇</A></TD>
                              <TD width="80" align="left" style="font-size:14px; color:#999">2017-10-12</TD>
                            </TR>
                            
                            <TR height=1>
                              <TD colspan=2 class="GroupBlankLine"></TD>
                            </TR>
                            
							
                            <TR>
                              <TD height=30 align="left">&nbsp;<img src="../../../images/2016hei.jpg" width="3" height="3" />&nbsp;<A style="font-size:14px;" 
                        href="./201710/t20171012_520784.html">宜春一小微企业创业园获批国家示范基地</A></TD>
                              <TD width="80" align="left" style="font-size:14px; color:#999">2017-10-12</TD>
                            </TR>
                            
                            <TR>
                              <TD height=30 align="left">&nbsp;<img src="../../../images/2016hei.jpg" width="3" height="3" />&nbsp;<A style="font-size:14px;" 
                        href="./201710/t20171011_520684.html">颜赣辉率市学习考察团在新余市学习考察</A></TD>
                              <TD width="80" align="left" style="font-size:14px; color:#999">2017-10-11</TD>
                            </TR>
                            
                            <TR>
                              <TD height=30 align="left">&nbsp;<img src="../../../images/2016hei.jpg" width="3" height="3" />&nbsp;<A style="font-size:14px;" 
                        href="./201710/t20171011_520686.html">张小平：坚决防范和遏制各类安全生产事故发生 为党的十九大胜利召开营造安全稳定环境</A></TD>
                              <TD width="80" align="left" style="font-size:14px; color:#999">2017-10-11</TD>
                            </TR>
                            
                            <TR>
                              <TD height=30 align="left">&nbsp;<img src="../../../images/2016hei.jpg" width="3" height="3" />&nbsp;<A style="font-size:14px;" 
                        href="./201710/t20171011_520689.html">张小平：扎实推动智慧经济产业特色小镇建设 为建设美丽宜春决胜全面小康奠定坚实基础</A></TD>
                              <TD width="80" align="left" style="font-size:14px; color:#999">2017-10-11</TD>
                            </TR>
                            
                            <TR>
                              <TD height=30 align="left">&nbsp;<img src="../../../images/2016hei.jpg" width="3" height="3" />&nbsp;<A style="font-size:14px;" 
                        href="./201710/t20171011_520690.html">市四届人大常委会举行第六次会议</A></TD>
                              <TD width="80" align="left" style="font-size:14px; color:#999">2017-10-11</TD>
                            </TR>
                            
                            <TR height=1>
                              <TD colspan=2 class="GroupBlankLine"></TD>
                            </TR>
                            
							
                            <TR>
                              <TD height=30 align="left">&nbsp;<img src="../../../images/2016hei.jpg" width="3" height="3" />&nbsp;<A style="font-size:14px;" 
                        href="./201710/t20171011_520695.html">市政府召开中心城区大气污染防治工作调度会</A></TD>
                              <TD width="80" align="left" style="font-size:14px; color:#999">2017-10-11</TD>
                            </TR>
                            
                            <TR>
                              <TD height=30 align="left">&nbsp;<img src="../../../images/2016hei.jpg" width="3" height="3" />&nbsp;<A style="font-size:14px;" 
                        href="./201710/t20171011_520685.html">宜春国庆中秋长假旅游市场揽金逾30亿元</A></TD>
                              <TD width="80" align="left" style="font-size:14px; color:#999">2017-10-11</TD>
                            </TR>
                            
                            <TR>
                              <TD height=30 align="left">&nbsp;<img src="../../../images/2016hei.jpg" width="3" height="3" />&nbsp;<A style="font-size:14px;" 
                        href="./201710/t20171010_520595.html">我市发出“决战工业八千亿做大宜春中心城区做强市本级”动员令</A></TD>
                              <TD width="80" align="left" style="font-size:14px; color:#999">2017-10-10</TD>
                            </TR>
                            
                            <TR>
                              <TD height=30 align="left">&nbsp;<img src="../../../images/2016hei.jpg" width="3" height="3" />&nbsp;<A style="font-size:14px;" 
                        href="./201710/t20171010_520588.html">我市将启动旅游公路教育片区建设宜阳新区核心区亮化</A></TD>
                              <TD width="80" align="left" style="font-size:14px; color:#999">2017-10-10</TD>
                            </TR>
                            
                            <TR>
                              <TD height=30 align="left">&nbsp;<img src="../../../images/2016hei.jpg" width="3" height="3" />&nbsp;<A style="font-size:14px;" 
                        href="./201710/t20171010_520596.html">我市颁发首张“二十四证合一”营业执照</A></TD>
                              <TD width="80" align="left" style="font-size:14px; color:#999">2017-10-10</TD>
                            </TR>
                            
                            <TR height=1>
                              <TD colspan=2 class="GroupBlankLine"></TD>
                            </TR>
                            
                          </TBODY>
                      </TABLE>
                      </td>
      </tr>
      <tr><td><table width="94%" border="0" align="center" cellpadding="0" cellspacing="0">
                                  <tr>
                                    <td align="center" height="45"><script>

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
<script>createPageHTML(50, 0, "index", "html");</script></td>
                                  </tr>
                        </table></td></tr>
    </table></td>
  </tr>
</table>
</td>
        <td width="20"></td>
        <td valign="top" width="299"><table width="100%" border="0" cellspacing="0" cellpadding="0">
          <tr>
            <td style="padding-bottom:10px;"><table width="100%" border="0" cellspacing="0" cellpadding="0" bgcolor="#eeeeee">
              <tr>
                <td width="50" height="38" align="center"><img src="../../../images/2016xxgk.jpg" width="13" height="12" /></td>
                <td align="left"><a href="http://www.yichun.gov.cn/xxgk/gkzn/201508/t20150829_449101.html" target="_blank" class="gkzn">政府信息公开指南</a></td>
              </tr>
            </table></td>
          </tr>
          <tr>
            <td style="padding-bottom:10px;"><table width="100%" border="0" cellspacing="0" cellpadding="0" bgcolor="#eeeeee">
              <tr>
                <td width="50" height="38" align="center"><img src="../../../images/2016gk2.jpg" width="13" height="14" /></td>
                <td align="left"><a href="http://xxgk.yichun.gov.cn/" target="_blank" class="gkzn">政府信息公开目录</a></td>
              </tr>
            </table></td>
          </tr>
          <tr>
            <td style="padding-bottom:10px;"><table width="100%" border="0" cellspacing="0" cellpadding="0" bgcolor="#eeeeee">
              <tr>
                <td width="50" height="38" align="center"><img src="../../../images/2016gk3.jpg" width="13" height="15" /></td>
                <td align="left"><a href="http://www.yichun.gov.cn/xxgk/gkndbg/" target="_blank" class="gkzn">政府信息公开年度报告</a></td>
              </tr>
            </table></td>
          </tr>
          <tr>
            <td style="padding-bottom:10px;"><table width="100%" border="0" cellspacing="0" cellpadding="0" bgcolor="#eeeeee">
              <tr>
                <td width="50" height="38" align="center"><img src="../../../images/2016gk4.jpg" width="13" height="15" /></td>
                <td align="left"><a href="http://xxgk.yichun.gov.cn/" target="_blank" class="gkzn">政府部门信息公开目录</a></td>
              </tr>
            </table></td>
          </tr>
          <tr>
            <td style="padding-bottom:15px;"><table width="100%" border="0" cellspacing="0" cellpadding="0" bgcolor="#eeeeee">
              <tr>
                <td width="50" height="38" align="center"><img src="../../../images/2016gk4.jpg" width="13" height="15" /></td>
                <td align="left"><a href="http://xxgk.yichun.gov.cn/ysqgk/" target="_blank" class="gkzn">依申请公开</a></td>
              </tr>
            </table></td>
          </tr>
        </table>
          <table width="100%" border="0" cellspacing="0" cellpadding="0">
          <tr align="center">
    <td height="90"><a href="../../ldjs/"><img id="xxgkpt1" src="../../../images/2016xxgkpt1_off.jpg" width="90" height="77" onMouseOver="wzdh_change(1)" /></a></td>
    <td height="90"><a href="../../jgsz/"><img id="xxgkpt2" src="../../../images/2016xxgkpt2_off.jpg" width="90" height="77" onMouseOver="wzdh_change(2)" /></a></td>
    <td><a href="../../ghygb/"><img id="xxgkpt3" src="../../../images/2016xxgkpt3_off.jpg" width="90" height="77" onMouseOver="wzdh_change(3)" /></a></td>
  </tr>
  <tr align="center">
    <td height="90"><a href="../../cjxx/"><img id="xxgkpt4" src="../../../images/2016xxgkpt4_off.jpg" width="90" height="77" onMouseOver="wzdh_change(4)" /></a></td>
    <td><a href="../../zdjcgk/zdgc/"><img id="xxgkpt5" src="../../../images/2016xxgkpt5_off.jpg" width="90" height="77" onMouseOver="wzdh_change(5)" /></a></td>
    <td><a href="../../ycsxwfbg/"><img id="xxgkpt6" src="../../../images/2016xxgkpt6_off.jpg" width="90" height="77" onMouseOver="wzdh_change(6)" /></a></td>
  </tr>
  <tr align="center">
    <td height="90"><a href="../../jdjc/"><img id="xxgkpt7" src="../../../images/2016xxgkpt7_off.jpg" width="90" height="77" onMouseOver="wzdh_change(7)" /></a></td>
    <td><a href="../../wbkyc/"><img id="xxgkpt8" src="../../../images/2016xxgkpt8_off.jpg" width="90" height="77" onMouseOver="wzdh_change(8)" /></a></td>
    <td><a href="../../zcwj/zczy/"><img id="xxgkpt9" src="../../../images/2016xxgkpt9_off.jpg" width="90" height="77" onMouseOver="wzdh_change(9)" /></a></td>
  </tr>
   <tr align="center">
    <td height="90"><a href="../../zfhy/"><img id="xxgkpt10" src="../../../images/2016xxgkpt10_off.jpg" width="90" height="77" onMouseOver="wzdh_change(10)" /></a></td>
    <td><a href="../../tjxx/"><img id="xxgkpt11" src="../../../images/2016xxgkpt11_off.jpg" width="90" height="77" onMouseOver="wzdh_change(11)" /></a></td>
    <td><a href="../../../ztbd/"><img id="xxgkpt12" src="../../../images/2016xxgkpt12_off.jpg" width="90" height="77" onMouseOver="wzdh_change(12)" /></a></td>
  </tr>
</table>
<table width="100%" border="0" cellspacing="0" cellpadding="0">
<tr><td height="15"></td></tr>
            <tr>
            <td align="center"><a href="http://gcly.yichun.gov.cn" target="_blank"><img src="../../../images/2016gcly1.jpg" width="299" height="77" /></a></td>
          </tr>
</table>
<table width="100%" border="0" cellspacing="0" cellpadding="0" style="margin-top:15px;">
  <tr>
    <td><table width="100%" border="0" cellspacing="0" cellpadding="0">
  <tr align="right">
    <td width="20" height="30"><img src="../../../images/2016gkb.jpg" width="8" height="21" /></td>
    <td width="100"><a href="../../zfgg/" target="_self"  class="gk">政府公告</a></td>
    <td width="179"></td>
  </tr>
</table></td>
  </tr>
  <tr>
    <td><table width="99%" border="0" align="center" cellpadding="0" cellspacing="0" style="margin-top:5px;">
                                      
                                        <tr>
                                        <td width="12" align="center"><img src="../../../images/2016hei.jpg" width="3" height="3" /></td>
                                          <td height="30" align="left"><a href="../../zfgg/zwgg/201710/t20171009_520570.html" target="_blank">宜春市政府办公室2017年公开选调工作人员...</a></td>              
                                        </tr>
                                        <tr>
                                        <td width="12" align="center"><img src="../../../images/2016hei.jpg" width="3" height="3" /></td>
                                          <td height="30" align="left"><a href="../../zfgg/zwgg/201710/t20171010_520610.html" target="_blank">宜春市特种设备行政许可发证前公示（2017...</a></td>              
                                        </tr>
                                        <tr>
                                        <td width="12" align="center"><img src="../../../images/2016hei.jpg" width="3" height="3" /></td>
                                          <td height="30" align="left"><a href="../../zfgg/zwgg/201710/t20171009_520564.html" target="_blank">宜春市生活垃圾焚烧发电项目环境影响评价...</a></td>              
                                        </tr>
                                        <tr>
                                        <td width="12" align="center"><img src="../../../images/2016hei.jpg" width="3" height="3" /></td>
                                          <td height="30" align="left"><a href="../../zfgg/zwgg/201709/t20170929_520229.html" target="_blank">第三届“宜春市突出贡献人才”拟表彰人选公示</a></td>              
                                        </tr>
                                        <tr>
                                        <td width="12" align="center"><img src="../../../images/2016hei.jpg" width="3" height="3" /></td>
                                          <td height="30" align="left"><a href="../../zfgg/zwgg/201709/t20170929_520185.html" target="_blank">宜春市映月大道工程社会稳定风险评估公众...</a></td>              
                                        </tr>
                                        <tr>
                                        <td width="12" align="center"><img src="../../../images/2016hei.jpg" width="3" height="3" /></td>
                                          <td height="30" align="left"><a href="../../zfgg/zwgg/201709/t20170925_519466.html" target="_blank">宜春技术经济开发区规划环境影响评价第一...</a></td>              
                                        </tr>
                                      </table></td>
  </tr>
</table>

        </td>
      </tr>
    </table></td>
  </tr>
</table>
<table width="999" height="126" border="0" align="center" cellpadding="0" cellspacing="0" bgcolor="#f0f0f0">
  <tr>
    <td height="20" align="center" bgcolor="#FFFFFF">
</td>
  </tr>
  <tr>
    <td height="25" align="center"><a href="../../../fzxx/wzsm/" target="_blank">网站声明</a> | <a href="../../../wzdh/bwzdh/" target="_blank">网站地图</a> | <a href="../../../fzxx/wzbz/" target="_blank">网站帮助</a> | <A href="mailto:webmaster@yichun.gov.cn" target="_blank">联系我们</A> | <a target="_blank" href="http://wpa.qq.com/msgrd?v=3&uin=2513807704&site=www.yichun.gov.cn&menu=yes"><img src="../../../images/2017qqjiszx.jpg" width="13" height="15" alt="QQ及时咨询" title="QQ及时咨询" /> QQ及时咨询(2513807704)</a></td>
  </tr>
  <tr>
    <td align="center" valign="top"><table width="800" border="0" cellspacing="0" cellpadding="0" style="font-size:12px; margin-bottom:7px;">
        <tr>
          <td height="30" colspan="3" align="center" style="padding-left:130px;">主办：宜春市人民政府 承办：宜春市人民政府办公室　　　　</td>
          <td width="100" rowspan="2" align="center"><script type="text/javascript">document.write(unescape("%3Cspan id='_ideConac' %3E%3C/span%3E%3Cscript src='http://dcs.conac.cn/js/15/232/0000/60470056/CA152320000604700560002.js' type='text/javascript'%3E%3C/script%3E"));</script></td>
        </tr>
        <tr>
          <td width="410" height="30" align="center">技术支持：宜春市政务信息化工作办公室　版权所有：中国宜春政府网</td>
          <td width="120" align="left">赣ICP备06000141号</td>
          <td width="170"> 
		 		<a target="_blank" href="http://www.beian.gov.cn/portal/registerSystemInfo?recordcode=36090202000004" style="display:inline-block;text-decoration:none;height:12px;line-height:12px;">赣公网安备 36090202000004号</p></a>
	 	  </td>
        </tr>
    </table></td>
  </tr>
</table>
</body>
</html>

"""

soup = BeautifulSoup(''.join(doc))

table = soup.find('table', { 'style' : 'margin-top:5px;' })

datetime_t = str(datetime.date.today()).split('-')
#print(datetime_t)


articles_link = []
for tr in table.findAll('tr'):
    #print(tr)

    find_today = re.compile(r'(\d\d)-(\d\d)</td>')  # 构建找到末尾发布日期的正则表达式
    month = find_today.search(str(tr))  # 把上面构建的表达式作用于findAll找出来的内容

    try:
        d1 = datetime.date.today()  # 获取今天的日期
        d2 = datetime.date(int(datetime_t[0]), int(month.group(1)), int(month.group(2)))  # 获取新闻的日期
        days_betwen = (d1 - d2).days #获取日期差
        if days_betwen <= 30 :
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