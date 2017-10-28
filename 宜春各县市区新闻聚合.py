# coding=utf-8

from BeautifulSoup import BeautifulSoup
import datetime,re

yuanzhou = 'http://www.yzq.gov.cn/zwgk/zwdt/zwyw/' #袁州要闻
shanggao = ''
wanzai = 'http://www.wanzai.gov.cn/news-list-wanzaiyaowen.html' #万载要闻
fengcheng = 'http://www.jxfc.gov.cn/n3/n13/index.html' #丰城新闻
zhangshu = 'http://www.zhangshu.gov.cn/zwgk/zhxx/' #樟树综合信息
gaoan = ''
yifeng = ''
fengxin = ''
tonggu = ''
jingan = ''


yuanzhou_html = '''

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

                            <TR height=1>
                              <TD colspan=2 class="GroupBlankLine"></TD>
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

                            <TR height=1>
                              <TD colspan=2 class="GroupBlankLine"></TD>
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

                            <TR>
                              <TD height=25 align="left"><IMG src="../../../images/lb-xtb.gif" width=4 height=6 />&nbsp;<A 
                        href="./201710/t20171010_397447.html">袁州区就业局：失业保险扩面征缴助推就业创业</A></TD>
                              <TD width="60" align="right">2017-10-10</TD>
                            </TR>

                            <TR>
                              <TD height=25 align="left"><IMG src="../../../images/lb-xtb.gif" width=4 height=6 />&nbsp;<A 
                        href="./201710/t20171009_397372.html">袁州区畜牧水产局开展 “讲道德，有品行”学习讨论</A></TD>
                              <TD width="60" align="right">2017-10-09</TD>
                            </TR>

                            <TR height=1>
                              <TD colspan=2 class="GroupBlankLine"></TD>
                            </TR>


                            <TR>
                              <TD height=25 align="left"><IMG src="../../../images/lb-xtb.gif" width=4 height=6 />&nbsp;<A 
                        href="./201710/t20171009_397366.html">袁州区畜牧水产局扎实开展招商引资工作</A></TD>
                              <TD width="60" align="right">2017-10-09</TD>
                            </TR>

                            <TR>
                              <TD height=25 align="left"><IMG src="../../../images/lb-xtb.gif" width=4 height=6 />&nbsp;<A 
                        href="./201710/t20171009_397365.html">袁州区在全市率先启动农民建房网上联并审批</A></TD>
                              <TD width="60" align="right">2017-10-09</TD>
                            </TR>

                            <TR>
                              <TD height=25 align="left"><IMG src="../../../images/lb-xtb.gif" width=4 height=6 />&nbsp;<A 
                        href="./201710/t20171009_397363.html">袁州区为建档立卡贫困户代缴城乡居民基本养老保险费</A></TD>
                              <TD width="60" align="right">2017-10-09</TD>
                            </TR>

                            <TR>
                              <TD height=25 align="left"><IMG src="../../../images/lb-xtb.gif" width=4 height=6 />&nbsp;<A 
                        href="./201709/t20170930_397197.html">楠木乡抓好安全工作</A></TD>
                              <TD width="60" align="right">2017-09-30</TD>
                            </TR>

                            <TR>
                              <TD height=25 align="left"><IMG src="../../../images/lb-xtb.gif" width=4 height=6 />&nbsp;<A 
                        href="./201709/t20170930_397196.html">江西星火生物科技有限公司油脂加工厂项目顺利推进</A></TD>
                              <TD width="60" align="right">2017-09-30</TD>
                            </TR>

                            <TR height=1>
                              <TD colspan=2 class="GroupBlankLine"></TD>
                            </TR>


                            <TR>
                              <TD height=25 align="left"><IMG src="../../../images/lb-xtb.gif" width=4 height=6 />&nbsp;<A 
                        href="./201709/t20170930_397130.html">袁州区加强“两节”市场监管保障食品安全</A></TD>
                              <TD width="60" align="right">2017-09-30</TD>
                            </TR>

                            <TR>
                              <TD height=25 align="left"><IMG src="../../../images/lb-xtb.gif" width=4 height=6 />&nbsp;<A 
                        href="./201709/t20170929_396887.html">袁州区财政局举办“喜迎党的十九大 心中话儿向党说”演讲比赛</A></TD>
                              <TD width="60" align="right">2017-09-29</TD>
                            </TR>

                            <TR>
                              <TD height=25 align="left"><IMG src="../../../images/lb-xtb.gif" width=4 height=6 />&nbsp;<A 
                        href="./201709/t20170929_396879.html">袁州区畜牧水产局参观“党在我心中”革命历史教育展</A></TD>
                              <TD width="60" align="right">2017-09-29</TD>
                            </TR>

                            <TR>
                              <TD height=25 align="left"><IMG src="../../../images/lb-xtb.gif" width=4 height=6 />&nbsp;<A 
                        href="./201709/t20170929_396877.html">袁州区财政局积极组织在职党员进社区</A></TD>
                              <TD width="60" align="right">2017-09-29</TD>
                            </TR>

                            <TR>
                              <TD height=25 align="left"><IMG src="../../../images/lb-xtb.gif" width=4 height=6 />&nbsp;<A 
                        href="./201709/t20170928_396658.html">袁州区开展健康扶贫医保政策下乡宣传活动</A></TD>
                              <TD width="60" align="right">2017-09-28</TD>
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
'''

wanzai_html = '''

<!doctype html>
<html lang="en">
<head>
	<meta charset="UTF-8">
	<title>万载要闻</title>
	<link rel="stylesheet" href="/statics/wanzai_gov/css/wz.css" type="text/css">
	<script src="/statics/wanzai_gov/js/jquery-1.10.2.min.js"></script>
</head>
<body style="height:1218px;" class="changeb">
<script>
var _hmt = _hmt || [];
(function() {
  var hm = document.createElement("script");
  hm.src = "https://hm.baidu.com/hm.js?8a00f6855eb2c9968f65945df04a3b99";
  var s = document.getElementsByTagName("script")[0]; 
  s.parentNode.insertBefore(hm, s);
})();
</script>


<div id="top">
		<div class="top_out">
			<div class="top_inner1">
				<img src="/statics/wanzai_gov/images/d1.png" alt="" style="position:relative;top:5px;"><a href="http://www.wanzai.gov.cn/news-list-huquanshun.html">县委</a><div></div>
				<img src="/statics/wanzai_gov/images/d2.png" alt=""><a href="http://www.wanzai.gov.cn/news-list-zhangqinghua.html">县人大</a><div></div>
				<img src="/statics/wanzai_gov/images/d2.png" alt=""><a href="http://www.wanzai.gov.cn/news-list-dyc1.html">县政府</a><div></div>
				<img src="/statics/wanzai_gov/images/d3.png" alt=""><a href="http://www.wanzai.gov.cn/news-list-longshegeng.html" style="position:relative;left:5px;">县政协</a>
			</div>
			<div class="top_inner2">
				<span id="weather"></span>
			</div>
			<div class="top_inner3">
				<div style="width:80px;"><img src="/statics/wanzai_gov/images/xu.png" alt=""><a href="javascript:void(0)" onclick="kqNav();">无障碍浏览</a></div>
				<div><img src="/statics/wanzai_gov/images/xu.png" alt=""><a href="">政务微博</a></div>
				<div><img src="/statics/wanzai_gov/images/xu.png" alt=""><a class="fanti" href="javascript:s2tt()">繁体中文</a><a class="jianti" href="javascript:t2ss()">简体中文</a></div>
				<div><img src="/statics/wanzai_gov/images/xu.png" alt=""><a href="javascript:void(0)" onclick="SetHome(this,window.location)">设为首页</a></div>
				<div><img src="/statics/wanzai_gov/images/xu.png" alt=""><a href="javascript:alert('请按 Ctrl+D 手动收藏!');">加入收藏</a></div>
			</div>
		</div>
	</div>
	<script type="text/javascript" language="javascript" src="/statics/wanzai_gov/js/transform.js"></script>
	<script src="/statics/wanzai_gov/js/toolbar.js" type="text/javascript"></script>
　　<script type="text/javascript" language="javascript">
	　　function s2tt(){
			document.body.innerHTML = s2t(document.body.innerHTML);
			$(".fanti").hide();
			$(".jianti").show();
		}

	　　function t2ss(){
			document.body.innerHTML = t2s(document.body.innerHTML);
			$(".jianti").hide();
			$(".fanti").show();
		}
		function SetHome(obj,vrl){   
			try{   
				obj.style.behavior='url(#default#homepage)';obj.setHomePage(vrl);   
			}   
			catch(e){   
				if(window.netscape) {   
					try {   
						netscape.security.PrivilegeManager.enablePrivilege("UniversalXPConnect");   
					}   
					catch (e) {   
						alert("此操作被浏览器拒绝！\n请在浏览器地址栏输入“about:config”并回车\n然后将 [signed.applets.codebase_principal_support]的值设置为'true',双击即可。");   
					}   
					var prefs = Components.classes['@mozilla.org/preferences-service;1'].getService(Components.interfaces.nsIPrefBranch);   
					prefs.setCharPref('browser.startup.homepage',vrl);   
				}else{   
					alert("您的浏览器不支持，请按照下面步骤操作：1.打开浏览器设置。2.点击设置网页。3.输入："+vrl+"点击确定。");   
				}   
			}   
		} 
	</script>
	<div id="title">
		<div id="logo">
			<img src="/statics/wanzai_gov/images/logo1.png" alt="">
		</div>
		<div id="search">
          	<form class="search-form" method="get" target="_blank" action="http://www.wanzai.gov.cn/index.php">
				<input name="c" type="hidden" value="so">
				<input name="module" type="hidden" value="news">
				<input type="text" id="text" placeholder="请输入关键字" style="color:#a9a9a9;font-size:12px;" name="keyword">
				<button id="btn" type="submit">search</button>
			</form>
		</div>
	</div>
	<div id="nav">
		<a href="/" style="margin-left:0;"><img class="img1" src="/statics/wanzai_gov/images/house1.png" alt="" id="nav1"><img class="img2" src="/statics/wanzai_gov/images/house2.png" alt="">网站首页</a>
		<a href="http://www.wanzai.gov.cn/news-list-meiliwanzai.html"><img class="img1" src="/statics/wanzai_gov/images/ta1.png" alt=""><img class="img2" src="/statics/wanzai_gov/images/ta2.png" alt="">魅力万载</a>
		<a href="http://www.wanzai.gov.cn/news-list-zhengwugongkai.html"><img class="img1" src="/statics/wanzai_gov/images/ge1.png" alt=""><img class="img2" src="/statics/wanzai_gov/images/ge2.png" alt="">政务公开</a>
		<a href="http://www.wanzai.gov.cn/news-list-zhengminhudong.html"><img class="img1" src="/statics/wanzai_gov/images/chat1.png" alt=""><img class="img2" src="/statics/wanzai_gov/images/chat2.png" alt="">政民互动</a>
        <a href="http://www.wanzai.gov.cn/news-list-banshifuwu.html"><img class="img1" src="/statics/wanzai_gov/images/ye1.png" alt=""><img class="img2" src="/statics/wanzai_gov/images/ye2.png" alt="">办事服务</a>
		<a href="http://www.wanzai.gov.cn/news-list-zhaoshangyinzi.html"><img class="img1" src="/statics/wanzai_gov/images/money1.png" alt=""><img class="img2" src="/statics/wanzai_gov/images/money2.png" alt="">招商引资</a>		
		<a href="http://www.wanzai.gov.cn/news-list-weizhengwanzai.html"><img class="img1" src="/statics/wanzai_gov/images/heart1.png" alt=""><img class="img2" src="/statics/wanzai_gov/images/heart2.png" alt="">微政万载</a>
	</div>	<div id="middle_list_zwgk">
		<div id="middle_list_left">
			<div class="middle_list_left_top"><img src="/statics/wanzai_gov/images/list_title.png" alt=""><span>政务公开</span></div>
			<div id="left_lan">
								<a href="http://www.wanzai.gov.cn/news-list-wanzaiyaowen.html"><p><span>万载要闻</span><img src="/statics/wanzai_gov/images/gy.png" class="gy" alt=""><img src="/statics/wanzai_gov/images/wy.png" class="wy" alt=""></p></a>
								<a href="http://www.wanzai.gov.cn/news-list-xiangzhenbumendongtai.html"><p><span>乡镇部门动态</span><img src="/statics/wanzai_gov/images/gy.png" class="gy" alt=""><img src="/statics/wanzai_gov/images/wy.png" class="wy" alt=""></p></a>
								<a href="http://www.wanzai.gov.cn/news-list-shipinxinwen.html"><p><span>视频新闻</span><img src="/statics/wanzai_gov/images/gy.png" class="gy" alt=""><img src="/statics/wanzai_gov/images/wy.png" class="wy" alt=""></p></a>
								<a href="http://www.wanzai.gov.cn/news-list-tongzhigonggao.html"><p><span>通知公告</span><img src="/statics/wanzai_gov/images/gy.png" class="gy" alt=""><img src="/statics/wanzai_gov/images/wy.png" class="wy" alt=""></p></a>
								<a href="http://www.wanzai.gov.cn/news-list-zhengcewenjian.html"><p><span>政策文件</span><img src="/statics/wanzai_gov/images/gy.png" class="gy" alt=""><img src="/statics/wanzai_gov/images/wy.png" class="wy" alt=""></p></a>
								<a href="http://www.wanzai.gov.cn/news-list-renshixinxi.html"><p><span>人事信息</span><img src="/statics/wanzai_gov/images/gy.png" class="gy" alt=""><img src="/statics/wanzai_gov/images/wy.png" class="wy" alt=""></p></a>
								<a href="http://www.wanzai.gov.cn/news-list-zhengfushuju.html"><p><span>政府数据</span><img src="/statics/wanzai_gov/images/gy.png" class="gy" alt=""><img src="/statics/wanzai_gov/images/wy.png" class="wy" alt=""></p></a>
								<a href="http://www.wanzai.gov.cn/news-list-zhongguozhengfuwangzhongyaozhe.html"><p><span>中国政府网政策</span><img src="/statics/wanzai_gov/images/gy.png" class="gy" alt=""><img src="/statics/wanzai_gov/images/wy.png" class="wy" alt=""></p></a>
								<a href="http://www.wanzai.gov.cn/news-list-zhengfuxinxigongkai.html"><p><span>政府信息公开</span><img src="/statics/wanzai_gov/images/gy.png" class="gy" alt=""><img src="/statics/wanzai_gov/images/wy.png" class="wy" alt=""></p></a>
								<a href="http://www.wanzai.gov.cn/news-list-qitalanmu.html"><p><span>其他栏目</span><img src="/statics/wanzai_gov/images/gy.png" class="gy" alt=""><img src="/statics/wanzai_gov/images/wy.png" class="wy" alt=""></p></a>
								<a href="http://www.wanzai.gov.cn/news-list-ztzl.html"><p><span>专题专栏</span><img src="/statics/wanzai_gov/images/gy.png" class="gy" alt=""><img src="/statics/wanzai_gov/images/wy.png" class="wy" alt=""></p></a>
							</div>
		</div>
		<div id="middle_list_right">
			<div id="middle_list_tit">
				<div class="div11"><img src="/statics/wanzai_gov/images/lmr_icon.png" alt="">&nbsp;&nbsp;万载要闻</div>
				<div class="div2">
					<img src="/statics/wanzai_gov/images/littleh.png" alt="">
					<a href="\">网站首页</a><span>></span><a href="http://www.wanzai.gov.cn/news-list-zhengwugongkai.html">政务公开</a><span>></span><a href="http://www.wanzai.gov.cn/news-list-wanzaiyaowen.html">万载要闻</a>				</div>
			</div>
			<div id="right_con">
								<div><a href="http://www.wanzai.gov.cn/news-show-8960.html" target="_blank" alt="万载县发布禁火令">万载县发布禁火令</a><p>2017-10-13</p></div>
								<div><a href="http://www.wanzai.gov.cn/news-show-8959.html" target="_blank" alt="市委常委、组织部长蔡清平深入潭埠镇视察">市委常委、组织部长蔡清平深入潭埠镇视察</a><p>2017-10-13</p></div>
								<div><a href="http://www.wanzai.gov.cn/news-show-8955.html" target="_blank" alt="国家安监总局一行督导我县花炮产业发展及安全生产工作">国家安监总局一行督导我县花炮产业发展及安全生产工作</a><p>2017-10-13</p></div>
								<div><a href="http://www.wanzai.gov.cn/news-show-8953.html" target="_blank" alt="万载县湘鄂赣革命根据地旧址入选全国红色旅游经典景区三期总体建设方案">万载县湘鄂赣革命根据地旧址入选全国红色旅游经典景区三期总体建设方案</a><p>2017-10-12</p></div>
								<div><a href="http://www.wanzai.gov.cn/news-show-8947.html" target="_blank" alt="喜迎十九大，万载在行动">喜迎十九大，万载在行动</a><p>2017-10-12</p></div>
								<div><a href="http://www.wanzai.gov.cn/news-show-8948.html" target="_blank" alt="刘学松副县长视察三兴汇鑫源烟花公司">刘学松副县长视察三兴汇鑫源烟花公司</a><p>2017-10-12</p></div>
								<div><a href="http://www.wanzai.gov.cn/news-show-8942.html" target="_blank" alt="熊敏剑副县长主持召开全县交通沿线环境综合整治部署推进暨现场督查会议  ">熊敏剑副县长主持召开全县交通沿线环境综合整治部署推进暨现场督查会议  </a><p>2017-10-11</p></div>
								<div><a href="http://www.wanzai.gov.cn/news-show-8933.html" target="_blank" alt="刘学松副县长到县花炮局调研，为全县花炮产业长远发展谋突破">刘学松副县长到县花炮局调研，为全县花炮产业长远发展谋突破</a><p>2017-10-11</p></div>
								<div><a href="http://www.wanzai.gov.cn/news-show-8929.html" target="_blank" alt="万载县两家省级农业龙头企业被认定为&quot;江西老字号&quot;企业">万载县两家省级农业龙头企业被认定为&quot;江西老字号&quot;企业</a><p>2017-10-11</p></div>
								<div><a href="http://www.wanzai.gov.cn/news-show-8924.html" target="_blank" alt="万载县借势棚改“四个更”提高人民群众幸福指数">万载县借势棚改“四个更”提高人民群众幸福指数</a><p>2017-10-10</p></div>
								<div><a href="http://www.wanzai.gov.cn/news-show-8920.html" target="_blank" alt="万载县“三举措”强化扶贫资金监管">万载县“三举措”强化扶贫资金监管</a><p>2017-10-10</p></div>
								<div><a href="http://www.wanzai.gov.cn/news-show-8895.html" target="_blank" alt="万载县参赛项目荣获首届湘赣边青年创新创业大赛二等奖">万载县参赛项目荣获首届湘赣边青年创新创业大赛二等奖</a><p>2017-09-30</p></div>
								<div><a href="http://www.wanzai.gov.cn/news-show-8892.html" target="_blank" alt="邓湧川县长在全县重点工作布置会上就我县十六项工作作出部署">邓湧川县长在全县重点工作布置会上就我县十六项工作作出部署</a><p>2017-09-30</p></div>
								<div><a href="http://www.wanzai.gov.cn/news-show-8880.html" target="_blank" alt="抓落实 促成效 万载县实施县长交办事项通知单制度 ">抓落实 促成效 万载县实施县长交办事项通知单制度 </a><p>2017-09-29</p></div>
								<div><a href="http://www.wanzai.gov.cn/news-show-8875.html" target="_blank" alt="万载县公路沿线环境综合治理见成效 ">万载县公路沿线环境综合治理见成效 </a><p>2017-09-29</p></div>
								<div><a href="http://www.wanzai.gov.cn/news-show-8874.html" target="_blank" alt="夏布品牌“隐逸轩”获 “江西老字号”认定，万载 实现“江西老字号”零突破">夏布品牌“隐逸轩”获 “江西老字号”认定，万载 实现“江西老字号”零突破</a><p>2017-09-29</p></div>
								<div><a href="http://www.wanzai.gov.cn/news-show-8862.html" target="_blank" alt="万载县促推锂电新能源项目为宜春打造“亚洲锂都”添砖加瓦">万载县促推锂电新能源项目为宜春打造“亚洲锂都”添砖加瓦</a><p>2017-09-28</p></div>
								<div><a href="http://www.wanzai.gov.cn/news-show-8861.html" target="_blank" alt="万载县“五个优先”强攻工业上项目">万载县“五个优先”强攻工业上项目</a><p>2017-09-28</p></div>
								<div><a href="http://www.wanzai.gov.cn/news-show-8860.html" target="_blank" alt="万载县新签约总投资2.87亿元的商业综合体项目 ">万载县新签约总投资2.87亿元的商业综合体项目 </a><p>2017-09-28</p></div>
								<div><a href="http://www.wanzai.gov.cn/news-show-8849.html" target="_blank" alt="万载县14个乡镇年中人民代表大会顺利召开">万载县14个乡镇年中人民代表大会顺利召开</a><p>2017-09-27</p></div>
							</div>
			<div id="right_tz">
				<div style="width:162px;">共595条记录 1/30页</div>
				<div style="width:62px;"><a href="http://www.wanzai.gov.cn/news-list-wanzaiyaowen-1.html">首页</a></div>
				<div><a href="javascript:volid(0);">上一页</a></div>
				<div><a href="http://www.wanzai.gov.cn/news-list-wanzaiyaowen-2.html">下一页</a></div>
				<div style="width:62px;"><a href="http://www.wanzai.gov.cn/news-list-wanzaiyaowen-30.html">末页</a></div>
				<div style="width:412px;"><p>跳转到<select class="page_zdy"><option value="http://www.wanzai.gov.cn/news-list-wanzaiyaowen-1.html">1</option><option value="http://www.wanzai.gov.cn/news-list-wanzaiyaowen-2.html">2</option><option value="http://www.wanzai.gov.cn/news-list-wanzaiyaowen-3.html">3</option><option value="http://www.wanzai.gov.cn/news-list-wanzaiyaowen-4.html">4</option><option value="http://www.wanzai.gov.cn/news-list-wanzaiyaowen-5.html">5</option><option value="http://www.wanzai.gov.cn/news-list-wanzaiyaowen-6.html">6</option><option value="http://www.wanzai.gov.cn/news-list-wanzaiyaowen-7.html">7</option><option value="http://www.wanzai.gov.cn/news-list-wanzaiyaowen-8.html">8</option><option value="http://www.wanzai.gov.cn/news-list-wanzaiyaowen-9.html">9</option><option value="http://www.wanzai.gov.cn/news-list-wanzaiyaowen-10.html">10</option><option value="http://www.wanzai.gov.cn/news-list-wanzaiyaowen-11.html">11</option><option value="http://www.wanzai.gov.cn/news-list-wanzaiyaowen-12.html">12</option><option value="http://www.wanzai.gov.cn/news-list-wanzaiyaowen-13.html">13</option><option value="http://www.wanzai.gov.cn/news-list-wanzaiyaowen-14.html">14</option><option value="http://www.wanzai.gov.cn/news-list-wanzaiyaowen-15.html">15</option><option value="http://www.wanzai.gov.cn/news-list-wanzaiyaowen-16.html">16</option><option value="http://www.wanzai.gov.cn/news-list-wanzaiyaowen-17.html">17</option><option value="http://www.wanzai.gov.cn/news-list-wanzaiyaowen-18.html">18</option><option value="http://www.wanzai.gov.cn/news-list-wanzaiyaowen-19.html">19</option><option value="http://www.wanzai.gov.cn/news-list-wanzaiyaowen-20.html">20</option><option value="http://www.wanzai.gov.cn/news-list-wanzaiyaowen-21.html">21</option><option value="http://www.wanzai.gov.cn/news-list-wanzaiyaowen-22.html">22</option><option value="http://www.wanzai.gov.cn/news-list-wanzaiyaowen-23.html">23</option><option value="http://www.wanzai.gov.cn/news-list-wanzaiyaowen-24.html">24</option><option value="http://www.wanzai.gov.cn/news-list-wanzaiyaowen-25.html">25</option><option value="http://www.wanzai.gov.cn/news-list-wanzaiyaowen-26.html">26</option><option value="http://www.wanzai.gov.cn/news-list-wanzaiyaowen-27.html">27</option><option value="http://www.wanzai.gov.cn/news-list-wanzaiyaowen-28.html">28</option><option value="http://www.wanzai.gov.cn/news-list-wanzaiyaowen-29.html">29</option><option value="http://www.wanzai.gov.cn/news-list-wanzaiyaowen-30.html">30</option></select>页</p></div>
			</div>
		</div>
	</div>
	<div id="bottom">
		<div id="bnav">
			<a href="">
				设为首页
			</a> | 
			<a href="">
				加入收藏
			</a> | 
			<a href="http://www.wanzai.gov.cn/news-list-wzdh.html">
				网站导航
			</a> | 
			<a href="">
				使用帮助
			</a> | 
			<a href="">
				隐私声明
			</a> | 
			<a href="">
				联系我们
			</a>
		</div>
		<div id="foot">
			<p>主办：万载县人民政府 承办：万载县人民政府办公室 技术支持：<a href="https://www.vwell.cn/">维网科技</a></p>
			<p>中文域名：万载政府网.政务 赣ICP备11002306号</p>
			<p>版本所有：万载县人民政府门户网站 您是第
			<span style="font-weight:bold;"> 2 5 4 8 6 9 6 </span>
			位访问者</p>
		</div>
        <div class="lpic">
        	<span class="_ideConac">
           		<a href="//bszs.conac.cn/sitename?method=show&amp;id=15ECDB592A9329B9E053022819AC61B0" target="_blank"><img id="imgConac" vspace="0" hspace="0" border="0" src="//dcs.conac.cn/image/red_error.png" data-bd-imgshare-binded="1"></a>
            </span>
            
        </div>
        <div  class="rpic">
        	<script id="_jiucuo_" sitecode='3609220011' src='http://pucha.kaipuyun.cn/exposure/jiucuo.js'></script>
        </div>
	</div></body>
<script src="/statics/wanzai_gov/js/jquery.leoweather.min.js"></script>
<script src="/statics/wanzai_gov/js/javascript.js"></script>
<script>
  $("#left_lan a:contains('政府信息公开')").attr('href','http://xxgk.wanzai.gov.cn/zgwz/zfxxgk_29957/'); 
	for( var i=0; i< $("#left_lan a").length; i++ ) {     
	    $("#left_lan a").eq(i).hover(function(){
			$(this).find('.gy').hide();
			$(this).find('.wy').show();
		},function(){
		    $(this).find('.wy').hide();
			$(this).find('.gy').show();
		});      
	};
	for (var i = 0; i < $("#left_lan a:contains('万载要闻')").length; i++) {
		if ($("#left_lan a:contains('万载要闻')").eq(i).text()=="万载要闻") {
			$("#left_lan a:contains('万载要闻')").eq(i).css({ "background":"#0daae5","border-color":"#0daae5" });
			$("#left_lan a:contains('万载要闻')").eq(i).find('span').css("color","#fff")
		};
	};
	$("#right_con div:even").css("background","#f6f6f6");
	$(document).ready(function(){
		$('.page_zdy').change(function(){
			var p1=$(this).children('option:selected').val();
			window.location.href=p1;
		})
	})
</script>
</html>
'''
fengcheng_html = '''

<!doctype html public "-//w3c//dtd xhtml 1.0 transitional//en" "http://www.w3.org/tr/xhtml1/dtd/xhtml1-transitional.dtd">
<html xmlns="http://www.w3.org/1999/xhtml">
<head>
<meta http-equiv="content-type" content="text/html; charset=utf-8" />

<!--start component 当前路径(ym_title)-->
<title>
 丰城新闻 – 
丰城市政府网
</title>
<meta name="keywords" content="丰城市政府网 
丰城市政府网
 新闻中心
 丰城新闻
 ">
<meta name="Description" content="丰城市政府网" />
<meta name="title" 
content="丰城市政府网 
新闻中心 
丰城新闻 
">

<link rel="shortcut icon" type="image/x-icon" href="../../dbsource/136170/229264.ico" />
<!--end component 当前路径(ym_title)-->

<!--start component HTML组件(js_and_css)-->
<link rel="stylesheet" type="text/css" href="../../template/1/5.css">
<link rel="stylesheet" type="text/css" href="../../template/1/1.css">
<link rel="stylesheet" type="text/css" href="../../template/1/7.css">
<script type="text/javascript" src="../../template/1/2.js"></script>
<script type="text/javascript" src="../../template/1/3.js"></script>
<script type="text/javascript">
  $(function() {
   $('.nav_doc li').find('.sub_nav').hide();
   $('.nav_doc li').hover(function() {
    $(this).removeClass("bg").addClass("nav_cur").children('.sub_nav').fadeIn(100);
   }, function() {
    $(this).removeClass("nav_cur").addClass("bg").children('.sub_nav').fadeOut(50);
   });
  });
</script>
<!--end component HTML组件(js_and_css)-->

</head>
<body>

<!--start component HTML组件(顶部导航)-->
<div class="top_doc">
  <div class="td_con">
    <div class="tn_l">
<!--
      <ul>
        <li class="qw_bg">市委</li>
        <li class="qrd_bg">人大</li>
        <li class="qzx_bg">政协</li>
      </ul>
-->
    </div>
    <!--tn_l end-->
    <div class="tn_time">
<script type="text/javascript" src="../../template/1/6.js"></script>
    </div>
    <div class="tn_tq">
 <iframe src="http://i.tianqi.com/index.php?c=code&py=fengcheng1&id=5" marginwidth="0" marginheight="0" hspace="0" vspace="0" frameborder="0" scrolling="no" height="29" allowtransparency="allowtransparency" width="233" style="margin-top:-2px"></iframe>
    </div>
    <!--天气，时间 end-->
    <div class="tn_nav">
      <div class="tn_btn">
        <!--    <select name="" style="background:none">
    <option>电子统一政务平台</option>
    </select>-->
        <a href=http://10.88.9.219/ess/officeportal/fcbgmy/  target="_blank" >电子统一政务平台</a> </div>
      <div class="fr"><!-- <a href="../../n128/n261/index.html" target="_blank" class="green">【政府微博】</a> <a href="../../n128/n261/index.html" target="_blank" class="green">【政府微信】</a>  --><a id="StranLink" href="javascript:void(0)" title="以繁体中文浏览">繁体版</a> | <a href="../../n128/n176/index.html" target="_blank">RSS订阅</a></div>
<div class="fr" style="padding-top: 3px;padding-right: 10px;">
<a href="/c642583/content.html" target="_blank" title="微博" style="background: url(../../dbsource/114783/642465.jpg) no-repeat left bottom;display: inline-block;height: 17px;width: 21px;"></a>
<a href="/c642583/content.html" target="_blank" title="微信" style="background: url(../../dbsource/114783/642464.jpg) no-repeat left bottom;display: inline-block;height: 18px;width: 24px;"></a>
</div>
    </div>
    <!--tn_nav end-->
  </div>
</div>
<!--top_doc end-->
<!--end component HTML组件(顶部导航)-->


<!--start component HTML组件(banner)-->
<div class="banner_main">
  <div class="banner">
    <div class="b_logo">
  <object classid="clsid:D27CDB6E-AE6D-11cf-96B8-444553540000" codebase="http://download.macromedia.com/pub/shockwave/cabs/flash/swflash.cab#version=9,0,28,0" width="998" height="197">
    <param name="movie" value="../../dbsource/113370/113371.swf" />
    <param name="quality" value="high" />
    <param name="wmode" value="transparent" />
    <embed src="../../dbsource/113370/113371.swf" wmode="transparent" quality="high" pluginspage="http://www.adobe.com/shockwave/download/download.cgi?P1_Prod_Version=ShockwaveFlash" type="application/x-shockwave-flash" width="998" height="197"></embed>
  </object>
</div>
  </div>
<!--banner end-->
</div>
<!--banner_main end-->
<!--end component HTML组件(banner)-->


<!--start component 导航条(nav)-->
<div class="nav">
  <div class="nav_doc">
    <div class="fl">
      <ul>
        <li class="bg" style="background:none"><a class="nav_a" href="../../index.html">网站首页</a></li>
        <li class="bg"><a class="nav_a" href="../../n4/index.html">魅力丰城</a>
          <!--<div class="sub_nav"> <a href="../../n4/n16/index.html" class="sub_a">丰城概况</a> <a href="../../n4/n17/index.html" class="sub_a">走进丰城</a> <a href="../../n4/n106/index.html" class="sub_a">历史文化</a> <a href="../../n4/n107/index.html" class="sub_a">旅游指南</a><a href="../../n4/n108/index.html" class="sub_a">餐饮住宿</a><a href="../../n4/n109/index.html" class="sub_a">风景名胜</a></div>-->
        </li>
        <li class="bg"><a class="nav_a" href="../../n5/index.html">政务公开</a></li>
        <li class="bg"><a class="nav_a" href="../../n6/index.html" target="_blank">政务服务</a></li>
        <li class="bg"><a class="nav_a" href="../../n111/index.html">公共服务</a></li>
        <li class="bg"><a class="nav_a" href="../../n7/index.html">政民互动</a></li>
<!--        <li class="bg"><a class="nav_a" href="../../n8/index.html" target="_blank">在线访谈</a></li>-->
        <li class="bg"><a class="nav_a" href="../../n10/index.html">特色专题</a></li>
      </ul>
    </div>
    <div class="search">
 <!--<form method="post" action=http://cms.jxfc.gov.cn/wlkj_fc/fcs/indexDys target="_blank">
<input name="fullText" type="text" value="请输入搜索关键字" class="search_text" onFocus="if(this.value=='请输入搜索关键字') this.value='';" onBlur="if(this.value=='') this.value='请输入搜索关键字';">
&nbsp;
<input type="submit" class="search_btn" value="" style="text-indent:-9999px\9;">
</form>--> 
<form method="post" action="http://data.jxfc.gov.cn/FengChSearch/article/openSearch?dn=www" target="_blank">
<input name="fulltext" type="text" value="请输入搜索关键字" class="search_text" onFocus="if(this.value=='请输入搜索关键字') this.value='';" onBlur="if(this.value=='') this.value='请输入搜索关键字';">

<input type="submit" class="search_btn" value="" style="text-indent:-9999px\9;">
</form>
    </div>
  </div>
  <!--nav_doc end-->
  </div>
<!--nav end-->
<!--end component 导航条(nav)-->

<div class="hr-10"></div>
<div class="area">

<!--start component 导航条(左侧导航)-->
<div class="list_l" style="width:224px">
   <div class="list_l_tit02">
                 <h2>新闻中心</h2>
   </div>
   <div class="l_nav_box">
    <div class="l_nav">
     <div class="hr-17"></div> 
 <div class="sonname sm_bg02"><a href="../../n3/n13/index.html" target="_self">丰城新闻</a></div>
<ul class="sonnames">
 </ul>
<div class="sonname sm_bg02"><a href="../../n3/n14/index.html" target="_self">媒体聚焦</a></div>
<ul class="sonnames">
 </ul>
<div class="sonname sm_bg02"><a href="../../n3/n15/index.html" target="_self">视频新闻</a></div>
<ul class="sonnames">
 </ul>
                   </div>
   </div>
   <div class="l_bot">
    <img src="../../template/1/38.jpg" style="vertical-align: bottom; margin-left:1px;" />
   </div>
               <script type="text/javascript">
$(document).ready(function() {
 //给当前栏目名加当前样式
 var _nowlmm = $(".r_list_top h2").html();
 //先看最终栏目
 $('.sonnames li').each(function(i) {
  if ($('.sonnames li a').eq(i).text() == _nowlmm) {
   $('.sonnames li').eq(i).parent("ul").prev(".sonname").addClass('jushita');
  }
 })
 //再看父栏目
 $('.sonname').each(function(i) {
  if ($('.sonname a').eq(i).text() == _nowlmm) {
   $('.sonname').eq(i).addClass('jushita');
  }
 })
 //展开有子栏目的栏目
 if($(".jushita").next("ul").find("li").length>0){
  $(".jushita").addClass("showdown").next("ul").slideToggle(500);
 }
 //点击动作
 $(".sonname").click(function() {
  if($(this).hasClass('jushita')){return;}
  if($(".jushita").next("ul").find("li").length>0){
   $(".jushita").next("ul").slideToggle(500);
  }
  $(".jushita").removeClass("jushita").removeClass("showdown");
  $(this).addClass("jushita");

  if($(".jushita").next("ul").find("li").length>0){
   $(".jushita").addClass("showdown").next("ul").slideToggle(500);
  }
 });
});
   </script>
  </div>
        <!--list_l end-->
<!--end component 导航条(左侧导航)-->


<!--start component HTML组件(div_start)-->
<div class="list_r" style=" width:759px">
<!--end component HTML组件(div_start)-->

<!--start component 当前路径(列表-导航路径)-->
   <div class="zwgg_tit">

            <dt><h2>丰城新闻</h2><h3></h3></dt>
            <dd><strong>当前位置：</strong><a href="../../index.html" >首页</a> 
&gt;&gt;
<a href="../../n3/index.html" >新闻中心</a> 
&gt;&gt;
<a href="../../n3/n13/index.html" >丰城新闻</a> 
</dd>
   </div>
<!--end component 当前路径(列表-导航路径)-->

<!--start component HTML组件(div02_star)-->
   <div class="list">
    <div class="hr-5"></div>

<!--end component HTML组件(div02_star)-->

<!--start component 内容全集(公用_list内全集)-->
<div id="comp_958"> 
     <ul>
     <li><span>[2017-10-13]</span><a href="../../n3/n13/c672769/content.html" class="lst_bg02" target='_blank'>胡江萍调研我市重点交通工程项目推进情况</a></li>
     <li><span>[2017-10-13]</span><a href="../../n3/n13/c672760/content.html" class="lst_bg02" target='_blank'>丰城市老城区棚户区改造工作调度会召开</a></li>
     <li><span>[2017-10-13]</span><a href="../../n3/n13/c672751/content.html" class="lst_bg02" target='_blank'>丰城市侨联第三届六次全委扩大会议顺利召开</a></li>
     <li><span>[2017-10-13]</span><a href="../../n3/n13/c672742/content.html" class="lst_bg02" target='_blank'>共青团丰城市第六次代表大会胜利闭幕</a></li>
     <li><span>[2017-10-13]</span><a href="../../n3/n13/c672733/content.html" class="lst_bg02" target='_blank'>龙津洲新区组织全体党员干部观看《榜样》</a></li>
     <li><span>[2017-10-13]</span><a href="../../n3/n13/c672724/content.html" class="lst_bg02" target='_blank'>上塘重拳出击依法拆除非法砖瓦窑厂</a></li>
     <li><span>[2017-10-12]</span><a href="../../n3/n13/c672668/content.html" class="lst_bg02" target='_blank'>丰城市“五个确保”扎实推进土地开发复垦工作  </a></li>
     <li><span>[2017-10-12]</span><a href="../../n3/n13/c672659/content.html" class="lst_bg02" target='_blank'>荣塘镇筑牢信访维稳防火墙</a></li>
     <li><span>[2017-10-12]</span><a href="../../n3/n13/c672650/content.html" class="lst_bg02" target='_blank'>同田乡扎实做好十九大前信访维稳工作</a></li>
     <li><span>[2017-10-12]</span><a href="../../n3/n13/c672641/content.html" class="lst_bg02" target='_blank'>上塘镇开展血吸虫病防治知识进校园活动</a></li>
     <li><span>[2017-10-12]</span><a href="../../n3/n13/c672632/content.html" class="lst_bg02" target='_blank'>秀市镇坪荫社区清洗饮水池 为居民送上放心水</a></li>
     <li><span>[2017-10-11]</span><a href="../../n3/n13/c672544/content.html" class="lst_bg02" target='_blank'>丰城市化解产能过剩成效初显  </a></li>
     <li><span>[2017-10-11]</span><a href="../../n3/n13/c672535/content.html" class="lst_bg02" target='_blank'>市农业局举办农业技术人员培训班</a></li>
     <li><span>[2017-10-11]</span><a href="../../n3/n13/c672526/content.html" class="lst_bg02" target='_blank'>尚庄举行广场舞汇演庆祝双节</a></li>
     <li><span>[2017-10-11]</span><a href="../../n3/n13/c672517/content.html" class="lst_bg02" target='_blank'>荣塘镇扎实做好“两节”期间回访工作</a></li>
     <li><span>[2017-10-10]</span><a href="../../n3/n13/c672462/content.html" class="lst_bg02" target='_blank'>总投资约2.1亿元的贵澳智慧富硒产业园项目落户丰城</a></li>
     <li><span>[2017-10-10]</span><a href="../../n3/n13/c672453/content.html" class="lst_bg02" target='_blank'>胡江萍视察中国爱情花卉小镇</a></li>
     <li><span>[2017-10-10]</span><a href="../../n3/n13/c672444/content.html" class="lst_bg02" target='_blank'>孙渡公办中心幼儿园与新疆阿克陶县巴仁乡且克双语幼儿园开展“千校手拉手”活动</a></li>
     <li><span>[2017-10-10]</span><a href="../../n3/n13/c672435/content.html" class="lst_bg02" target='_blank'>小港“垃圾兑换银行”变废为宝</a></li>
     <li><span>[2017-10-10]</span><a href="../../n3/n13/c672426/content.html" class="lst_bg02" target='_blank'>铁路袁渡圆满完成非法砖瓦厂整改任务</a></li>
     <li><span>[2017-10-09]</span><a href="../../n3/n13/c672331/content.html" class="lst_bg02" target='_blank'>宜春市新上项目巡查组在丰城巡查</a></li>
    </ul>
    </div>
    <div class="page" id="pag_958">
<script>
  var purl="../../n3/n13/index_958" 
 var org= jQuery("#comp_958").html(); 
 function goPub(uu){ 
if(pageName==maxPageNum) {
 pageName=0;}
 if(pageName==0){ 
  jQuery("#comp_958").html(org);
 writePaging();} 
 else{ 
    jQuery("#comp_958").load(uu,writePaging);
         }
 }
 function createUrl(pName){ 
   var u=window.location.href; 
  var index=u.indexOf("/manageweb") 
  if(index!=-1){ 
   var uu=purl+"&pageName="+pName 
      return "javascript:pageName="+pName+";goPub('"+uu+"')" 
    }
   index=u.indexOf("/serviceweb");
     if(index!=-1){ 
      var uu=purl+"_"+pName+".html";
      return   "javascript:pageName="+pName+";goPub('"+uu+"')" 
 }else{
  var uu= purl+"_"+pName+".html";
     return "javascript:pageName="+pName+";goPub('"+uu+"')"; 
 } 
} 
   function writePaging(){ 
    var sss=""; 
   var displayNum=10; 
     if (pageName==0) pageName=maxPageNum; 
   if (pageName<maxPageNum){ 
    var url=createUrl(0); sss +="<a href="+url+"  target='_self'>首页</a>&nbsp;"; 
url=createUrl(pageName+1); 
  sss +="<a href="+ url+ "  target='_self'>上页</a>&nbsp;"; 
} 
 var ccc = pageName+displayNum-1;
if (ccc>maxPageNum) ccc=maxPageNum; 
  while (ccc>pageName){ 
   url=createUrl(ccc); 
 if(ccc<=displayNum) {
 sss += "<a href="+ url+ " target='_self'>"+(maxPageNum-ccc+1)+"</a>&nbsp;"; 
 }else if(pageName>=ccc) {
  sss += "<a href="+ url+ " target='_self'>"+(maxPageNum-ccc+1)+"</a>&nbsp;"; }
 ccc--; 
 } 
 sss += "<a href='javascript:void(0);' class='cur'>"+(maxPageNum-ccc+1)+"</a>&nbsp;"; 
 ccc--; 
  while (ccc>=1 && ccc>=(pageName-displayNum+1)){ 
    url=createUrl(ccc); 
  sss += "<a href=" +url+ "  target='_self'>"+(maxPageNum-ccc+1)+"</a>&nbsp;"; 
 ccc--;
 } 
 if (pageName>1){ 
 url=createUrl(pageName-1); 
  sss += "<a href="+ url+"  target='_self'>下页</a>&nbsp;"; 
 url=createUrl(1); 
  sss += "<a href="+ url+" target='_self'>尾页</a>"; 
 } 
  sss += "&nbsp;总页数:"+maxPageNum; 
var pagPlace=document.getElementById("pag_958"); 
 pagPlace.innerHTML=sss;
}
  var maxPageNum=0;
      document.cookie="maxPageNum958=199";
    maxPageNum = 199;
    if (maxPageNum>1){
    var sss="";
          pageName = 0;
        writePaging();
  }
</script>
  </div>
 <div style='display:none'><a href='../../n3/n13/index_958_1.html'></a><a href='../../n3/n13/index_958_2.html'></a><a href='../../n3/n13/index_958_3.html'></a><a href='../../n3/n13/index_958_4.html'></a><a href='../../n3/n13/index_958_5.html'></a><a href='../../n3/n13/index_958_6.html'></a><a href='../../n3/n13/index_958_7.html'></a><a href='../../n3/n13/index_958_8.html'></a><a href='../../n3/n13/index_958_9.html'></a><a href='../../n3/n13/index_958_10.html'></a><a href='../../n3/n13/index_958_11.html'></a><a href='../../n3/n13/index_958_12.html'></a><a href='../../n3/n13/index_958_13.html'></a><a href='../../n3/n13/index_958_14.html'></a><a href='../../n3/n13/index_958_15.html'></a><a href='../../n3/n13/index_958_16.html'></a><a href='../../n3/n13/index_958_17.html'></a><a href='../../n3/n13/index_958_18.html'></a><a href='../../n3/n13/index_958_19.html'></a><a href='../../n3/n13/index_958_20.html'></a><a href='../../n3/n13/index_958_21.html'></a><a href='../../n3/n13/index_958_22.html'></a><a href='../../n3/n13/index_958_23.html'></a><a href='../../n3/n13/index_958_24.html'></a><a href='../../n3/n13/index_958_25.html'></a><a href='../../n3/n13/index_958_26.html'></a><a href='../../n3/n13/index_958_27.html'></a><a href='../../n3/n13/index_958_28.html'></a><a href='../../n3/n13/index_958_29.html'></a><a href='../../n3/n13/index_958_30.html'></a><a href='../../n3/n13/index_958_31.html'></a><a href='../../n3/n13/index_958_32.html'></a><a href='../../n3/n13/index_958_33.html'></a><a href='../../n3/n13/index_958_34.html'></a><a href='../../n3/n13/index_958_35.html'></a><a href='../../n3/n13/index_958_36.html'></a><a href='../../n3/n13/index_958_37.html'></a><a href='../../n3/n13/index_958_38.html'></a><a href='../../n3/n13/index_958_39.html'></a><a href='../../n3/n13/index_958_40.html'></a><a href='../../n3/n13/index_958_41.html'></a><a href='../../n3/n13/index_958_42.html'></a><a href='../../n3/n13/index_958_43.html'></a><a href='../../n3/n13/index_958_44.html'></a><a href='../../n3/n13/index_958_45.html'></a><a href='../../n3/n13/index_958_46.html'></a><a href='../../n3/n13/index_958_47.html'></a><a href='../../n3/n13/index_958_48.html'></a><a href='../../n3/n13/index_958_49.html'></a><a href='../../n3/n13/index_958_50.html'></a><a href='../../n3/n13/index_958_51.html'></a><a href='../../n3/n13/index_958_52.html'></a><a href='../../n3/n13/index_958_53.html'></a><a href='../../n3/n13/index_958_54.html'></a><a href='../../n3/n13/index_958_55.html'></a><a href='../../n3/n13/index_958_56.html'></a><a href='../../n3/n13/index_958_57.html'></a><a href='../../n3/n13/index_958_58.html'></a><a href='../../n3/n13/index_958_59.html'></a><a href='../../n3/n13/index_958_60.html'></a><a href='../../n3/n13/index_958_61.html'></a><a href='../../n3/n13/index_958_62.html'></a><a href='../../n3/n13/index_958_63.html'></a><a href='../../n3/n13/index_958_64.html'></a><a href='../../n3/n13/index_958_65.html'></a><a href='../../n3/n13/index_958_66.html'></a><a href='../../n3/n13/index_958_67.html'></a><a href='../../n3/n13/index_958_68.html'></a><a href='../../n3/n13/index_958_69.html'></a><a href='../../n3/n13/index_958_70.html'></a><a href='../../n3/n13/index_958_71.html'></a><a href='../../n3/n13/index_958_72.html'></a><a href='../../n3/n13/index_958_73.html'></a><a href='../../n3/n13/index_958_74.html'></a><a href='../../n3/n13/index_958_75.html'></a><a href='../../n3/n13/index_958_76.html'></a><a href='../../n3/n13/index_958_77.html'></a><a href='../../n3/n13/index_958_78.html'></a><a href='../../n3/n13/index_958_79.html'></a><a href='../../n3/n13/index_958_80.html'></a><a href='../../n3/n13/index_958_81.html'></a><a href='../../n3/n13/index_958_82.html'></a><a href='../../n3/n13/index_958_83.html'></a><a href='../../n3/n13/index_958_84.html'></a><a href='../../n3/n13/index_958_85.html'></a><a href='../../n3/n13/index_958_86.html'></a><a href='../../n3/n13/index_958_87.html'></a><a href='../../n3/n13/index_958_88.html'></a><a href='../../n3/n13/index_958_89.html'></a><a href='../../n3/n13/index_958_90.html'></a><a href='../../n3/n13/index_958_91.html'></a><a href='../../n3/n13/index_958_92.html'></a><a href='../../n3/n13/index_958_93.html'></a><a href='../../n3/n13/index_958_94.html'></a><a href='../../n3/n13/index_958_95.html'></a><a href='../../n3/n13/index_958_96.html'></a><a href='../../n3/n13/index_958_97.html'></a><a href='../../n3/n13/index_958_98.html'></a><a href='../../n3/n13/index_958_99.html'></a><a href='../../n3/n13/index_958_100.html'></a><a href='../../n3/n13/index_958_101.html'></a><a href='../../n3/n13/index_958_102.html'></a><a href='../../n3/n13/index_958_103.html'></a><a href='../../n3/n13/index_958_104.html'></a><a href='../../n3/n13/index_958_105.html'></a><a href='../../n3/n13/index_958_106.html'></a><a href='../../n3/n13/index_958_107.html'></a><a href='../../n3/n13/index_958_108.html'></a><a href='../../n3/n13/index_958_109.html'></a><a href='../../n3/n13/index_958_110.html'></a><a href='../../n3/n13/index_958_111.html'></a><a href='../../n3/n13/index_958_112.html'></a><a href='../../n3/n13/index_958_113.html'></a><a href='../../n3/n13/index_958_114.html'></a><a href='../../n3/n13/index_958_115.html'></a><a href='../../n3/n13/index_958_116.html'></a><a href='../../n3/n13/index_958_117.html'></a><a href='../../n3/n13/index_958_118.html'></a><a href='../../n3/n13/index_958_119.html'></a><a href='../../n3/n13/index_958_120.html'></a><a href='../../n3/n13/index_958_121.html'></a><a href='../../n3/n13/index_958_122.html'></a><a href='../../n3/n13/index_958_123.html'></a><a href='../../n3/n13/index_958_124.html'></a><a href='../../n3/n13/index_958_125.html'></a><a href='../../n3/n13/index_958_126.html'></a><a href='../../n3/n13/index_958_127.html'></a><a href='../../n3/n13/index_958_128.html'></a><a href='../../n3/n13/index_958_129.html'></a><a href='../../n3/n13/index_958_130.html'></a><a href='../../n3/n13/index_958_131.html'></a><a href='../../n3/n13/index_958_132.html'></a><a href='../../n3/n13/index_958_133.html'></a><a href='../../n3/n13/index_958_134.html'></a><a href='../../n3/n13/index_958_135.html'></a><a href='../../n3/n13/index_958_136.html'></a><a href='../../n3/n13/index_958_137.html'></a><a href='../../n3/n13/index_958_138.html'></a><a href='../../n3/n13/index_958_139.html'></a><a href='../../n3/n13/index_958_140.html'></a><a href='../../n3/n13/index_958_141.html'></a><a href='../../n3/n13/index_958_142.html'></a><a href='../../n3/n13/index_958_143.html'></a><a href='../../n3/n13/index_958_144.html'></a><a href='../../n3/n13/index_958_145.html'></a><a href='../../n3/n13/index_958_146.html'></a><a href='../../n3/n13/index_958_147.html'></a><a href='../../n3/n13/index_958_148.html'></a><a href='../../n3/n13/index_958_149.html'></a><a href='../../n3/n13/index_958_150.html'></a><a href='../../n3/n13/index_958_151.html'></a><a href='../../n3/n13/index_958_152.html'></a><a href='../../n3/n13/index_958_153.html'></a><a href='../../n3/n13/index_958_154.html'></a><a href='../../n3/n13/index_958_155.html'></a><a href='../../n3/n13/index_958_156.html'></a><a href='../../n3/n13/index_958_157.html'></a><a href='../../n3/n13/index_958_158.html'></a><a href='../../n3/n13/index_958_159.html'></a><a href='../../n3/n13/index_958_160.html'></a><a href='../../n3/n13/index_958_161.html'></a><a href='../../n3/n13/index_958_162.html'></a><a href='../../n3/n13/index_958_163.html'></a><a href='../../n3/n13/index_958_164.html'></a><a href='../../n3/n13/index_958_165.html'></a><a href='../../n3/n13/index_958_166.html'></a><a href='../../n3/n13/index_958_167.html'></a><a href='../../n3/n13/index_958_168.html'></a><a href='../../n3/n13/index_958_169.html'></a><a href='../../n3/n13/index_958_170.html'></a><a href='../../n3/n13/index_958_171.html'></a><a href='../../n3/n13/index_958_172.html'></a><a href='../../n3/n13/index_958_173.html'></a><a href='../../n3/n13/index_958_174.html'></a><a href='../../n3/n13/index_958_175.html'></a><a href='../../n3/n13/index_958_176.html'></a><a href='../../n3/n13/index_958_177.html'></a><a href='../../n3/n13/index_958_178.html'></a><a href='../../n3/n13/index_958_179.html'></a><a href='../../n3/n13/index_958_180.html'></a><a href='../../n3/n13/index_958_181.html'></a><a href='../../n3/n13/index_958_182.html'></a><a href='../../n3/n13/index_958_183.html'></a><a href='../../n3/n13/index_958_184.html'></a><a href='../../n3/n13/index_958_185.html'></a><a href='../../n3/n13/index_958_186.html'></a><a href='../../n3/n13/index_958_187.html'></a><a href='../../n3/n13/index_958_188.html'></a><a href='../../n3/n13/index_958_189.html'></a><a href='../../n3/n13/index_958_190.html'></a><a href='../../n3/n13/index_958_191.html'></a><a href='../../n3/n13/index_958_192.html'></a><a href='../../n3/n13/index_958_193.html'></a><a href='../../n3/n13/index_958_194.html'></a><a href='../../n3/n13/index_958_195.html'></a><a href='../../n3/n13/index_958_196.html'></a><a href='../../n3/n13/index_958_197.html'></a><a href='../../n3/n13/index_958_198.html'></a><a href='../../n3/n13/index_958_199.html'></a></div>
<!--end component 内容全集(公用_list内全集)-->

<!--start component HTML组件(div02_end)-->
</div>
<!--end component HTML组件(div02_end)-->

<!--start component HTML组件(div_end)-->
   <div class="r_list_bot"></div>
  </div>
<!--end component HTML组件(div_end)-->

        <div class="clear"></div>
</div>
<!--列表框 end-->


<!--start component HTML组件(footer)-->
<div class="footer" style="position:relative;">
<div style="

position: absolute; top: 115px; right: 343px; width: 110px; height: 55px; 

">
<script id="_jiucuo_" sitecode='3609810078' src='http://pucha.kaipuyun.cn/exposure/jiucuo.js'></script>
</div>

  <div class="ft_nav"><a href="javascript:;" onclick="SetHome(this,'http://218.95.73.34/web2/subject/n1/n2/index.html')" target="_self">设为首页</a> | <a href="javascript:;" onclick="AddFavorite('http://218.95.73.34/web2/subject/n1/n2/index.html','丰城市政府网')" target="_self">加入收藏</a> | <a href="../../n128/n129/index.html" target="_blank">网站地图</a> | <a href="../../n128/n130/index.html" target="_blank">使用帮助</a> 
<!-- | <a href="../../n128/n131/index.html" target="_blank">常见问题</a>--> | <a href="../../n128/n132/index.html" target="_blank">免责申明</a> <!--| <a href="../../n128/n133/index.html" target="_blank">联系我们</a>--></div>
  <div class="ft_txt"> 主办：丰城市人民政府 承办：丰城市信息中心<br />
    Copyright © 2013 All Rights Reserved 丰城市人民政府版权所有<br />
    <a href="http://www.miitbeian.gov.cn/" target="_blank" style="color: #4b4b4b;">赣ICP备14007126号-1</a>
<div style="text-align:center">
<script type="text/javascript">document.write(unescape("%3Cspan id='_ideConac' %3E%3C/span%3E%3Cscript  src='http://dcs.conac.cn/js/15/232/0885/40695803/CA152320885406958030002.js' type='text/javascript'%3E%3C/script%3E"));</script>
</div>
</div>
</div>
<script type="text/javascript" src="../../template/1/378.js"></script>
<script type="text/javascript" src="../../dbsource/114783/114784.js"></script>
<!--footer end-->
<!--end component HTML组件(footer)-->

</body>
</html>

'''

