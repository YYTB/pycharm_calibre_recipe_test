#coding=utf-8
from BeautifulSoup import BeautifulSoup
import datetime  # 导入日期时间模块，各版面的url根据发行日期改变。
html = '''

<html><head>
<meta http-equiv=Content-Type content="text/html; charset=utf-8">
<title>中国旅游报社-电子报平台</title>
<META http-equiv=Page-Enter content=blendTrans(duration=0.2)>
<META http-equiv=Page-Exit content=blendTrans(duration=0.2)>
<link href="../../../tplimg/calendar.css" rel="stylesheet" type="text/css"/>
<SCRIPT language=Javascript src="../../../tplimg/swfobject.js"></SCRIPT>
<SCRIPT language=Javascript src="../../../tplimg/prototype.js"></SCRIPT>
<SCRIPT language=Javascript src="../../../tplimg/mp.js"></SCRIPT>
<SCRIPT language=Javascript src="../../../tplimg/calendar2.js"></SCRIPT>
<SCRIPT language=Javascript src="../../../tplimg/range.js"></SCRIPT>
<style type="text/css">
<!--
body {
	background-image: url();
	background-color: #F7FAFF;

}
body,td,th,prelink {font-size: 12px;}
.STYLE30 {color: #FF9200; font-weight: bold; }
.commonlight2{background-color:#a2dbff;}
.commoncolor3{background-color:#FFFFFF;}
#pageChangeEffect{margin-top: -606px; margin-left:-20px!important;margin-left:-440px; POSITION: absolute;}
-->
#zindexDiv{
    position:absolute;
    width:expression(this.nextSibling.offsetWidth);
    height:expression(this.nextSibling.offsetHeight);
    top:expression(this.nextSibling.offsetTop);
    left:expression(this.nextSibling.offsetLeft);
    }
</style>
<script language="javascript">

function MM_swapImgRestore() { //v3.0
  var i,x,a=document.MM_sr; for(i=0;a&&i<a.length&&(x=a[i])&&x.oSrc;i++) x.src=x.oSrc;
}

function MM_preloadImages() { //v3.0
  var d=document; if(d.images){ if(!d.MM_p) d.MM_p=new Array();
    var i,j=d.MM_p.length,a=MM_preloadImages.arguments; for(i=0; i<a.length; i++)
    if (a[i].indexOf("#")!=0){ d.MM_p[j]=new Image; d.MM_p[j++].src=a[i];}}
}

function MM_findObj(n, d) { //v4.01
  var p,i,x;  if(!d) d=document; if((p=n.indexOf("?"))>0&&parent.frames.length) {
    d=parent.frames[n.substring(p+1)].document; n=n.substring(0,p);}
  if(!(x=d[n])&&d.all) x=d.all[n]; for (i=0;!x&&i<d.forms.length;i++) x=d.forms[i][n];
  for(i=0;!x&&d.layers&&i<d.layers.length;i++) x=MM_findObj(n,d.layers[i].document);
  if(!x && d.getElementById) x=d.getElementById(n); return x;
}

function MM_swapImage() { //v3.0

 var i,j=0,x,a=MM_swapImage.arguments; document.MM_sr=new Array; for(i=0;i<(a.length-2);i+=3)
 if ((x=MM_findObj(a[i]))!=null){document.MM_sr[j++]=x; if(!x.oSrc) x.oSrc=x.src; x.src=a[i+2];}
}

</script>
</head>

<SPAN id=leveldiv title=点击查看内容 
style="BORDER-TOP-WIDTH: 0px; BORDER-LEFT-WIDTH: 0px; Z-INDEX: 100; LEFT: 233px; BORDER-BOTTOM-WIDTH: 0px; WIDTH: 210px; CURSOR: hand; POSITION: absolute; TOP: 123px; HEIGHT: 34px; BORDER-RIGHT-WIDTH: 0px"></SPAN>

<body onLoad="initialize();initMPPage();" text=#000000 vlink=#000000 alink=#ff0000 link=#000000 leftmargin=0 topmargin=0 marginheight="0" marginwidth="0">
<table width="1002" height="30" border="0" align="center" cellpadding="0" cellspacing="0">
  <tr>
    <td bgcolor="#0066CC">&nbsp;</td>
  </tr>
</table>
<table cellspacing=0 cellpadding=0 width=1002 align=center border=0 background="../../../tplimg/bg.jpg" id="logoTable">
  <tr>
    <td width=354 valign=top><table width="380" border=0 align=right cellpadding=0 cellspacing=0>
        <tr>
          <td width="380" align=right>
	        <table width="381" height="146" border=0 cellpadding=0 cellspacing=0>
              <tr>
                <td width="23" rowspan="3" valign="top"
                
                >&nbsp;</td>
                <td width="322" valign="top" height="2"></td>
                <td width="10" rowspan="2" valign="top" background="../../../tplimg/jwb_red_r6_c3.jpg" style="background-repeat:repeat-y"><img src="../../../tplimg/jwb_red_r1_c3.jpg" width="7" height="121"></td>
              </tr>
              <tr>
                <td width="310" height="500" bgcolor=#ffffff style="BORDER: #0065AD 2px solid"><map name=PagePicMap><Area coords="203,28,343,28,343,194,203,194" shape="polygon" href="content_306582.htm?div=-1"><Area coords="6,97,193,97,193,359,6,359" shape="polygon" href="content_306587.htm?div=-1"><Area coords="6,385,227,385,227,527,6,527" shape="polygon" href="content_306588.htm?div=-1"><Area coords="237,368,343,368,343,494,237,494" shape="polygon" href="content_306593.htm?div=-1"><Area coords="203,204,343,204,343,323,203,323" shape="polygon" href="content_306597.htm?div=0"><Area coords="203,204,343,204,343,323,203,323" shape="polygon" href="content_306597.htm?div=-1"></map><img src=../../../images/2017-10/13/01/ZGLYB2017101301_b.jpg border=0 USEMAP=#PagePicMap>
   
   <div class="pageflash"><div id="pageChangeEffect" onMouseOver="this.style.display = 'none';"> </div></div>
   <script type="text/javascript">
	 var so = new SWFObject("../../../tplimg/page_effect.swf", "mymovie", "737", "625", "7" , "#336699");
	 so.addParam("wmode", "transparent");
	 so.write("pageChangeEffect");
	</script>				</td>
              </tr>
              <tr>
                <td height="23" align=left valign="top"><img src="../../../tplimg/jwb_red_r8_c2.jpg" width="358" height="9"></td>
                <td valign="top"><img src="../../../tplimg/jwb_red_r8_c3.jpg" width="9" height="9"></td>
              </tr>
            </table>
              <table width=373 border=0 cellpadding=5 cellspacing=0 style="MARGIN-BOTTOM: 3px">
                <tr>
                  <td width="13" align=left>&nbsp;</td>
                  <td width="145" align=left>第01版：<STRONG>旅游报01版</STRONG></td>
                  <td width="125" align=right nowrap style="PADDING-RIGHT: 0px; PADDING-LEFT: 0px; PADDING-BOTTOM: 0px; PADDING-TOP: 0px"><a class=preart href="node_2.htm"><span style='font-size:12px;font-family:webdings'>4</span>下一版</a></td>
                  <td width="50" align=right valign=center nowrap style="PADDING-RIGHT: 5px"><a href=../../../images/2017-10/13/01/ZGLYB2017101301.pdf><IMG height=16  
src="../../../tplimg/pdf.gif" width=16 border=0></a></td>
                </tr>
            </table>          
              <table width="368" height="70" border="0" cellpadding="0" cellspacing="0">
                <tr>
                  <td>&nbsp;</td>
                </tr>
              </table></td>
        </tr>
        <tr>
    </table></td>
    <td valign=top><table cellspacing=0 cellpadding=0 width="621" border=0>
        <tr>
          <td height="61" colspan="8" align="left" valign="bottom" bgcolor="#0066CC" background="../../../tplimg/title-1.jpg" style="background-repeat:no-repeat">
           <div style="text-align:right; border:0; padding:0 30px 0 0;">
          <a href="http://itunes.apple.com/cn/app/zhong-guo-lu-you-bao/id521946380?mt=8" target="_blank">
           <img src="../../../tplimg/iphone.jpg">
          </a>
          <a href="http://itunes.apple.com/cn/app/zhong-guo-lu-you-baohd/id522603318?mt=8" target="_blank">
           <img src="../../../tplimg/ipad.jpg">
          </a>
          
          <a href="http://www.toptour.cn/detail/info92881.htm" target="_blank">
           <img src="../../../tplimg/Android.jpg">
          </a>
          </div>
          </td>
        </tr>
		<tr>
          <td height="5" colspan="8" bgcolor="#FFFBFF"></td>
        </tr>
        <tr>
          <td width="47" height="33" align="left" valign="top">　<img src="../../../tplimg/menu_r1_c1.jpg"> <img src="../../../tplimg/menu_r1_c2.jpg"></td>
          <td width="194" align="left"><span class="paperdate"><strong>2017年10月13日 星期五</strong></span></td>
          <td width="30" align="left" valign="top" class="whitenav"><img src="../../../tplimg/menu_r1_c1.jpg"> <img src="../../../tplimg/menu_r1_c3.jpg"></td>
          <td width="69" align="left" class="whitenav"><span onMouseOver="document.getElementById('bmdh').style.display = 'block';" onMouseOut="document.getElementById('bmdh').style.display = 'none';">版面导航</span></td>
          <td width="14" align="left" valign="top" class="whitenav"><img src="../../../tplimg/menu_r1_c1.jpg"></td>
          <td width="71" align="left" class="whitenav"><span onMouseOver="document.getElementById('btdh').style.display = 'block';" onMouseOut="document.getElementById('btdh').style.display = 'none';">标题导航</span></td>
          <td width="184" height="33" align="left"><span id="upqi" style="display:none"><img src="../../../tplimg/pre.gif"><a href="#" onClick="goPrePeriod()">上一期</a>&nbsp;&nbsp;<a href="#" onClick="goNextPeriod()">下一期</a><img src="../../../tplimg/next.gif" width="5" height="9"></span></td>
        </tr>
      </table>
        <table width="610" height="507" border=0 cellpadding=0 cellspacing=0>
          <tr valign=top>
            <td width="365" rowspan="4"><table width="100%" height="17" border=0 cellpadding=5 cellspacing=0>
                <tr>
                  <td></td>
                </tr>
              </table>
                <table width="390" height="352" border="0" cellpadding="0" cellspacing="0" style="BORDER: #BDDBF7 1px solid">
                  <tr>
                    <td bgcolor="#FFFFFF" height="4"></td>
                  </tr>
                  <tr>
                    <td bgcolor="#FFFFFF" height="20" style="PADDING-LEFT: 10px;"><span class="STYLE30"><a href="#" class="STYLE30">标题导航</a></span></td>
                  </tr>
                  <tr>
                    <td align="left" bgcolor="#FFFFFF"> <img src="../../../tplimg/image06.jpg" width="370" height="8"></td>
                  </tr>
                  <tr>
                    <td valign="top" bgcolor="#FFFFFF" style="PADDING-LEFT: 10px;"><DIV style="height:300px; overflow-y:scroll; width:97%;">
                        <ul class="ul02_l">


<li>&middot;<a href=content_306582.htm?div=-1><div style="display:inline" id=mp306582>宁夏固原：红色旅游底色更足</div></a>



<li>&middot;<a href=content_306587.htm?div=-1><div style="display:inline" id=mp306587>多措并举推动澳门融入世界旅游大格局</div></a>



<li>&middot;<a href=content_306588.htm?div=-1><div style="display:inline" id=mp306588>甘肃：全域旅游从“环境革命”抓起</div></a>



<li>&middot;<a href=content_306593.htm?div=-1><div style="display:inline" id=mp306593>杭州入选全球旅游最佳实践样本城市</div></a>



<li>&middot;<a href=content_306597.htm?div=0><div style="display:inline" id=mp306597>喜迎十九大展现新成就</div></a>



</ul>


                    </DIV></td>
                  </tr>
              </table>
          
                <table width="100%" height="10" border="0" cellpadding="0" cellspacing="0">
                  <tr>
                    <td height="10"></td>
                  </tr>
                </table>
                <table width="390" height="111" border="0" cellpadding="0" cellspacing="0" style="BORDER: #BDDBF7 1px solid">
                  <tr>
                    <td height="25" background="../../../tplimg/bg-2.jpg"> 　<span class="whitenav">版权声明</span></td>
                  </tr>
                  
                  <tr>
                    <td height="118" align="center" valign="middle" class="px12"><table width="93%" height="100" border="0" cellpadding="0" cellspacing="0">
                      <tr>
                        <td align="left" valign="top">　　<span class="px12">《中国旅游报》（数字报）的一切内容仅供中国旅游报读者阅读、学习研究使用，未经中国旅游报相关权利人书面授权，任何单位及个人不得将《中国旅游报》（数字报）所登载、发布的内容用于任何商业性目的，或将之在非本站所属的服务器上作镜像。否则，中国旅游报社将采取一切合法手段，追究侵权者的法律责任。</span></td>
                      </tr>
                    </table></td>
                  </tr>
                </table></td>
            <td width="10" rowspan="4" align="center"></td>
            <td width="200" height="115" align="center"><table width="100%" height="17" border="0" cellpadding="0" cellspacing="0">
              <tr>
                <td></td>
              </tr>
            </table>
              <table width="100%" border=0 cellpadding=0 
            cellspacing=0 style="BORDER-TOP: #999 0px solid; MARGIN-BOTTOM: 5px">
                <tr>
                  <td align="right" valign="top"><table width="100%" border="0" cellpadding="0" cellspacing="0" style="BORDER: #BDDBF7 1px solid">
                    <tr>
                      <td background="../../../tplimg/bg-2.jpg" class=default style="PADDING-RIGHT: 3px; BORDER-TOP: #BDDBF7 0px solid; PADDING-LEFT: 3px; PADDING-BOTTOM: 1px; PADDING-TOP: 3px; BORDER-BOTTOM: #BDDBF7 0px solid"><div style="PADDING-LEFT: 20px;"><strong class="whitenav">版面目录</strong></div></td>
                    </tr>
                    <tr>
                      <td bgcolor="#FFFFFF" style="BORDER-TOP: #C0C0C0 1px solid"><div style="height:250px; overflow-y:scroll; width:100%;">
                           <table cellspacing=0 cellpadding=2 width=100% border=0><tbody>
<tr>
                <td class=default align=left>&nbsp;<a id=pageLink href=./node_1.htm>第01版：旅游报01版</a></td>
                <td nowrap align=middle width=55><a href=../../../images/2017-10/13/01/ZGLYB2017101301.pdf><img height=16 
                  src="../../../tplimg/pdf.gif" width=16 border=0></a></td></tr>

<tr bgcolor=#e8e8e8>
                <td align=left class=default>&nbsp;<a id=pageLink href=node_2.htm>第02版：旅游报02版</a></td>
                <td nowrap align=middle width=55><a href=../../../images/2017-10/13/02/ZGLYB2017101302.pdf><img height=16 
                  src="../../../tplimg/pdf.gif" width=16 border=0></a></td></tr>
<tr>
                <td class=default align=left>&nbsp;<a id=pageLink href=node_3.htm>第03版：旅游报03版</a></td>
                <td nowrap align=middle width=55><a href=../../../images/2017-10/13/03/ZGLYB2017101303.pdf><img height=16 
                  src="../../../tplimg/pdf.gif" width=16 border=0></a></td></tr>

<tr bgcolor=#e8e8e8>
                <td align=left class=default>&nbsp;<a id=pageLink href=node_4.htm>第04版：旅游报04版</a></td>
                <td nowrap align=middle width=55><a href=../../../images/2017-10/13/04/ZGLYB2017101304.pdf><img height=16 
                  src="../../../tplimg/pdf.gif" width=16 border=0></a></td></tr>
<tr>
                <td class=default align=left>&nbsp;<a id=pageLink href=node_5.htm>第05版：旅游报05版</a></td>
                <td nowrap align=middle width=55><a href=../../../images/2017-10/13/05/ZGLYB2017101305.pdf><img height=16 
                  src="../../../tplimg/pdf.gif" width=16 border=0></a></td></tr>

<tr bgcolor=#e8e8e8>
                <td align=left class=default>&nbsp;<a id=pageLink href=node_6.htm>第06版：旅游报06版</a></td>
                <td nowrap align=middle width=55><a href=../../../images/2017-10/13/06/ZGLYB2017101306.pdf><img height=16 
                  src="../../../tplimg/pdf.gif" width=16 border=0></a></td></tr>
<tr>
                <td class=default align=left>&nbsp;<a id=pageLink href=node_8.htm>第08版：旅游报08版</a></td>
                <td nowrap align=middle width=55><a href=../../../images/2017-10/13/08/ZGLYB2017101308.pdf><img height=16 
                  src="../../../tplimg/pdf.gif" width=16 border=0></a></td></tr>

</tbody></table>

                      </div></td>
                    </tr>
                  </table></td>
                </tr>
              </table>
              <table width=100% border=0 align="center" cellpadding=0 cellspacing=0>

                <tr>
                  <td align="right" valign="top"><script language=JavaScript>
<!--
document.write("<div id=detail style=position:absolute;width:300px;></div>");
//-->
    </script>
                      <table cellspacing=0 cellpadding=0 width="200" border=0>
                        
                        <tr>
                          <td background="../../../tplimg/bg-2.jpg" class=default style="PADDING-RIGHT: 3px; BORDER-TOP: #BDDBF7 1px solid; PADDING-LEFT: 3px; PADDING-BOTTOM: 0px; PADDING-TOP: 3px; BORDER-BOTTOM: #BDDBF7 0px solid; BORDER-LEFT: #BDDBF7 1px solid; BORDER-RIGHT: #BDDBF7 1px solid;"><div align="center" onClick="calendar()"><strong class="whitenav"><font style="CURSOR: hand; ">按日期查阅</font></strong></div></td>
                        </tr>
                        <tr align="center">
                          <td><table width="200" height="100" border="0" cellpadding="0" cellspacing="0" style="BORDER: #BDDBF7 1px solid">
                              <tr>
                                <td height="33"  colspan="2" align="left" bgcolor="#FFFFFF"><form name=CLD style="padding:0px;margin:0px;">
                                    <table cellspacing=0 cellpadding=0 width="100%" align=center border=0>
                                      <tr>
                                        <td><table width="100%" align=center border="0" cellpadding="1" cellspacing="1">
                                            <tr class="default" align=center>
                                              <td height=15 colspan=7 bgcolor="#BDDFF7"><table width="100%" border="0" cellpadding="2" cellspacing="0">
                                                  <tr align="center">
                                                    <td align="left" nowrap><img src="../../../tplimg/d1.gif" width="7" height="11" style="cursor:hand;" onClick="turnpage(SY,0)"></td>
                                                    <td><select class=jumpmenu onChange=changeMPCld() name=SY>
                                                        <script language=JavaScript>
					for(i=2006;i<2051;i++)
					document.write('<option>'+i+'</option>')
        			</script>
                                                      </select>                                                    </td>
                                                    <td><img src="../../../tplimg/d.gif" width="7" height="11" style="cursor:hand;" onClick="turnpage(SY,1)"></td>
                                                    <td align="center" nowrap><img src="../../../tplimg/d1.gif" width="7" height="11" style="cursor:hand;" onClick="turnpage(SM,0)"></td>
                                                    <td><select class=jumpmenu onChange=changeMPCld() name=SM>
                                                        <script language=JavaScript>
				<!-- 
					for(i=1;i<13;i++) document.write('<option>'+i+'</option>')
				//-->
        			</script>
                                                      </select>                                                    </td>
                                                    <td><img src="../../../tplimg/d.gif" width="7" height="11" style="cursor:hand;" onClick="turnpage(SM,1)"></td>
                                                    <td align="right" nowrap><strong><font id=GZ fface="Arial, Helvetica, sans-serif"></font></strong></td>
                                                  </tr>
                                              </table></td>
                                            </tr>
                                            <tr align=middle bgcolor="#E7F3FF" class="default">
                                              <td align="center" class="default"><b><font face="Arial, Helvetica, sans-serif">日</font></b></td>
                                              <td align="center" class="default"><b><font face="Arial, Helvetica, sans-serif">一</font></b></td>
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
					document.write('<td  bgcolor="#D6EBFF" class="default" align=center id="GD' + gNum +'" style="cursor: default;" width="14%"><a href="" id="CD' + gNum + '"><span class="date" style="font-family:Verdana, Arial;font-size:11px;"><font _onMouseOver="mOvr(' + gNum +')" onMouseOut="mOut()" id="SD' + gNum +'"');
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
                        
						
						<tr>
							<td>&nbsp;</td>
					  </tr>
                  </table></td>
                </tr>
            </table></td>
		  </tr>
    </table>
	<div style="display:none"></div></td>
  </tr>
 <tr>
    <td height="45" colspan="2" background="../../../tplimg/bg-3.jpg" style="PADDING-BOTTOM: 12px;"><div align="center" style="color:#000000;">
	<a href="http://www.toptour.cn/corp/about_ctn/" 
target="_blank"> 关于我们 </a> 
	|<a href="http://www.toptour.cn/corp/chinatourismnews/" 
target="_blank"> 报纸订阅 </a>
	|<a href="http://www.toptour.cn/corp/chinatourismnews/" 
target="_blank"> 广告招商 </a>
	|<a href="http://www.toptour.cn/corp/cooperation/" 
target="_blank"> 活动招商 </a>
	|<a href="http://www.toptour.cn/corp/chinatourismnews/" 
target="_blank"> 发行服务 </a>
	|<a href="http://www.toptour.cn/corp/chinatourismnews/" 
target="_blank"> 采编名单 </a> 
	|<a href="http://www.toptour.cn/corp/card/" 
target="_blank"> 导游证挂失 </a>
	|<a href="http://www.ctnews.com.cn/jqsp/jqsp1.htm" target="_blank"> 景区视频 </a></div></td>
  </tr>
  <tr>
    <td colspan="2" align="center" style="line-height: 120%"><table width="100%" border="0" cellspacing="0" cellpadding="0">
      <tr>
        <td height="70" align="center" style="line-height: 200%;"><p><span class="px12">国内统一刊号：CN11-0013　　          邮发代号：1-40 　　     新闻热线：010-85166219<br>
              <A href="http://net.china.com.cn/" target="_blank">中国互联网不良信息举报中心</A> 中华人民共和国互联网新闻信息许可证 （国新网 许可证编号：1012006032） <BR>
CopyRight by www.ctnews.com.cn　 京ICP备030067号<BR>
版权所有 中国旅游报 中国 北京 </span></p>
          </td>
      </tr>
    </table></td>
  </tr>
</table>
<!-------bmdh版面导航------>
<div id=bmdh onMouseOver="document.getElementById('bmdh').style.display = 'block';" onMouseOut="document.getElementById('bmdh').style.display = 'none';">
<TABLE width="200px"  border=0 cellPadding=2 cellSpacing=0 bgcolor="#FFFFFF">
 <TBODY>
<TR  id=row_black1  onMouseOver="Javascript:focus_row_black(1)"  onMouseOut="Javascript:blur_row_black(1)">
       <TD align=left>&nbsp;</TD>
       <TD align=left height=24 class="black" >&nbsp;<a href=./node_1.htm class="black" id=pageLink>第01版：旅游报01版</a></TD>
   <TD width=28 align=middle noWrap>
       <a href=../../../images/2017-10/13/01/ZGLYB2017101301.pdf><IMG height=16 src="../../../tplimg/pdf.gif" width=16 border=0></a>
   </TD>
</TR>
<TR  id=row_black2  onMouseOver="Javascript:focus_row_black(2)"  onMouseOut="Javascript:blur_row_black(2)">
       <TD align=left>&nbsp;</TD>
       <TD align=left height=24 class="black" >&nbsp;<a href=node_2.htm class="black" id=pageLink>第02版：旅游报02版</a></TD>
   <TD width=28 align=middle noWrap>
       <a href=../../../images/2017-10/13/02/ZGLYB2017101302.pdf><IMG height=16 src="../../../tplimg/pdf.gif" width=16 border=0></a>
   </TD>
</TR>
<TR  id=row_black3  onMouseOver="Javascript:focus_row_black(3)"  onMouseOut="Javascript:blur_row_black(3)">
       <TD align=left>&nbsp;</TD>
       <TD align=left height=24 class="black" >&nbsp;<a href=node_3.htm class="black" id=pageLink>第03版：旅游报03版</a></TD>
   <TD width=28 align=middle noWrap>
       <a href=../../../images/2017-10/13/03/ZGLYB2017101303.pdf><IMG height=16 src="../../../tplimg/pdf.gif" width=16 border=0></a>
   </TD>
</TR>
<TR  id=row_black4  onMouseOver="Javascript:focus_row_black(4)"  onMouseOut="Javascript:blur_row_black(4)">
       <TD align=left>&nbsp;</TD>
       <TD align=left height=24 class="black" >&nbsp;<a href=node_4.htm class="black" id=pageLink>第04版：旅游报04版</a></TD>
   <TD width=28 align=middle noWrap>
       <a href=../../../images/2017-10/13/04/ZGLYB2017101304.pdf><IMG height=16 src="../../../tplimg/pdf.gif" width=16 border=0></a>
   </TD>
</TR>
<TR  id=row_black5  onMouseOver="Javascript:focus_row_black(5)"  onMouseOut="Javascript:blur_row_black(5)">
       <TD align=left>&nbsp;</TD>
       <TD align=left height=24 class="black" >&nbsp;<a href=node_5.htm class="black" id=pageLink>第05版：旅游报05版</a></TD>
   <TD width=28 align=middle noWrap>
       <a href=../../../images/2017-10/13/05/ZGLYB2017101305.pdf><IMG height=16 src="../../../tplimg/pdf.gif" width=16 border=0></a>
   </TD>
</TR>
<TR  id=row_black6  onMouseOver="Javascript:focus_row_black(6)"  onMouseOut="Javascript:blur_row_black(6)">
       <TD align=left>&nbsp;</TD>
       <TD align=left height=24 class="black" >&nbsp;<a href=node_6.htm class="black" id=pageLink>第06版：旅游报06版</a></TD>
   <TD width=28 align=middle noWrap>
       <a href=../../../images/2017-10/13/06/ZGLYB2017101306.pdf><IMG height=16 src="../../../tplimg/pdf.gif" width=16 border=0></a>
   </TD>
</TR>
<TR  id=row_black8  onMouseOver="Javascript:focus_row_black(8)"  onMouseOut="Javascript:blur_row_black(8)">
       <TD align=left>&nbsp;</TD>
       <TD align=left height=24 class="black" >&nbsp;<a href=node_8.htm class="black" id=pageLink>第08版：旅游报08版</a></TD>
   <TD width=28 align=middle noWrap>
       <a href=../../../images/2017-10/13/08/ZGLYB2017101308.pdf><IMG height=16 src="../../../tplimg/pdf.gif" width=16 border=0></a>
   </TD>
</TR>
</TBODY>
</TABLE>
</div>
<!-------bmdh版面导航END------>
<!-- -------------------------标题导航-------------->
<iframe id="zindexDiv" frameborder="0"></iframe>
<DIV id=btdh onMouseOver="document.getElementById('btdh').style.display = 'block';" onMouseOut="document.getElementById('btdh').style.display = 'none';">
 <TABLE border=0 cellPadding=2 cellSpacing=0 bgcolor="#FFFFFF" width=277>
<tbody>

<tr height=27px  id=row_black306582  onMouseOver="Javascript:focus_row_black(306582)"  onMouseOut="Javascript:blur_row_black(306582)">
<td width=10px></td>
<td class="black">
<a href=content_306582.htm?div=-1>宁夏固原：红色旅游底色更足</a>
</td></TR>
<tr height=27px  id=row_black306587  onMouseOver="Javascript:focus_row_black(306587)"  onMouseOut="Javascript:blur_row_black(306587)">
<td width=10px></td>
<td class="black">
<a href=content_306587.htm?div=-1>多措并举推动澳门融入世界旅游大格局</a>
</td></TR>
<tr height=27px  id=row_black306588  onMouseOver="Javascript:focus_row_black(306588)"  onMouseOut="Javascript:blur_row_black(306588)">
<td width=10px></td>
<td class="black">
<a href=content_306588.htm?div=-1>甘肃：全域旅游从“环境革命”抓起</a>
</td></TR>
<tr height=27px  id=row_black306593  onMouseOver="Javascript:focus_row_black(306593)"  onMouseOut="Javascript:blur_row_black(306593)">
<td width=10px></td>
<td class="black">
<a href=content_306593.htm?div=-1>杭州入选全球旅游最佳实践样本城市</a>
</td></TR>
<tr height=27px  id=row_black306597  onMouseOver="Javascript:focus_row_black(306597)"  onMouseOut="Javascript:blur_row_black(306597)">
<td width=10px></td>
<td class="black">
<a href=content_306597.htm?div=0>喜迎十九大展现新成就</a>
</td></TR>


</tbody></TABLE>

<!-- -------------------------标题导航 END -------------->
</DIV>

<script src="http://s21.cnzz.com/stat.php?id=4991647&web_id=4991647&show=pic" language="JavaScript"></script>


</body>
</html>
'''


datetime = str(datetime.date.today()).split('-')  # 对日期进行拆分，返回一个['2017', '10', '09']形式的列表

url_prefix = 'http://news.ctnews.com.cn/zglyb/html/'  # url前缀
url_prefix_add = 'http://news.ctnews.com.cn/zglyb/html/' + datetime[0] + '-' + datetime[1] + '/' + datetime[
        2] + '/'  # url前缀带日期
url_prefix_add2 = 'http://news.ctnews.com.cn/zglyb/html/' + datetime[0] + '-' + datetime[1] + '/' + datetime[
        2] + '/' + 'node_1.htm'  # 完整url

print(url_prefix)
print(url_prefix_add)
print(url_prefix_add2)

soup = BeautifulSoup(''.join(html))

banmiankuai = soup.find('table',{'cellpadding':'2','width':'100%'})
print(banmiankuai)
for link in banmiankuai.findAll('a'):
    if 'pdf' in link['href']:
        continue
    print(url_prefix_add + link['href'].lstrip(r'./'))
    print(link.contents[0].strip())

zhengwenlian = soup.find('ul',{'class':'ul02_l'})

print(zhengwenlian)

for li in zhengwenlian.findAll('a'):
    print(url_prefix_add + li['href'])
    print(li.contents[0].contents[0].strip())

