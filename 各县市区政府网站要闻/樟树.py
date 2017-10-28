# coding=utf-8

from BeautifulSoup import BeautifulSoup
import datetime, re

doc = """

<!DOCTYPE html PUBLIC "-//W3C//DTD XHTML 1.0 Transitional//EN" "http://www.w3.org/TR/xhtml1/DTD/xhtml1-transitional.dtd">
<html xmlns="http://www.w3.org/1999/xhtml">
<head>
<meta http-equiv="Content-Type" content="text/html; charset=utf-8" />
<title>综合信息</title>
<link href="../../images/zgzs.css" rel="stylesheet" type="text/css" />
</head>

<body style="margin:0; padding:0; background:url(../../images/zgzsbg_01.jpg) top center no-repeat" background="../../images/zgzsbg_01.jpg">
<div><!DOCTYPE html PUBLIC "-//W3C//DTD XHTML 1.0 Transitional//EN" "http://www.w3.org/TR/xhtml1/DTD/xhtml1-transitional.dtd">
<html xmlns="http://www.w3.org/1999/xhtml">
<head>
<meta http-equiv="Content-Type" content="text/html; charset=utf-8" />
<title>页头嵌套</title>
<link href="../../images/zgzs.css" rel="stylesheet" type="text/css" />
<script type="text/javascript" src="../../images/zgzs_js.js"></script>
<style type="text/css">
body {
	background-image: url(../site40/zgzstop_28.jpg);
}
</style>
</head>
<body background="../../images/zgzstop_28.jpg" style="margin:0; padding:0; background:url(../site40/zgzsbg_01.jpg) top no-repeat; font-size: 9px;">
<table width="1002" border="0" align="center" cellpadding="0" cellspacing="0">
  <tr>
  </tr>

        <td width="57%" height="21" align="left" class="STYLE20"></td>
        <td>&nbsp;</td>
        <td width="43%" align="right" class="STYLE20"><a href="../../zt/dwgk/" target="_blank"><font color="#FF0000">阳光党务</font></a> | <script language="javascript" charset="gb2312" src="../../images/jfzh.js"></script> | <a href="../../rssdy/" target="_blank">RSS</a> </td>
      </tr>
    </table></td>
<table width="1002" border="0" align="center" cellpadding="0" cellspacing="0">
  <tr>
    <td height="27" background="../../images/zgzstop_02.jpg"><object classid="clsid:D27CDB6E-AE6D-11cf-96B8-444553540000" codebase="http://download.macromedia.com/pub/shockwave/cabs/flash/swflash.cab#version=9,0,28,0" width="1002" height="266">
      <param name="movie" value="../../images/top.swf" />
      <param name="quality" value="high" />
      <embed src="../../images/top.swf" quality="high" pluginspage="http://www.adobe.com/shockwave/download/download.cgi?P1_Prod_Version=ShockwaveFlash" type="application/x-shockwave-flash" width="1002" height="266"></embed>
  </object></td>
  </tr>
</table>
<table width="1002" border="0" align="center" cellpadding="0" cellspacing="0">
  <tr>
    <td align="center"><img src="../../images/zgzstop_07.jpg" width="1002" height="8" /></td>
  </tr>
  <tr>
    <td height="37"><table width="100%" border="0" cellspacing="0" cellpadding="0">
      <tr>
        <td width="1%" height="37" align="left" background="../../images/zgzstop_10.jpg"><img src="../../images/zgzstop_08.jpg" width="5" height="37" /></td>
        <td width="98%" background="../../images/zgzstop_10.jpg"><table width="100%" border="0" cellspacing="0" cellpadding="0">
          <tr>
            <td width="75%" height="37"><table width="100%" border="0" cellspacing="0" cellpadding="0">
              <tr>
                <td width="100" align="center"><table width="76" border="0" cellspacing="0" cellpadding="0">
                    <tr>
                      <td height="37" align="center" class="STYLE60" id="qh0" onmousemove="qh(0)"><span><a href="../../" target="_blank">网站首页</a></span> </td>
                    </tr>
                </table></td>
                <td width="2" align="center"><img src="../../images/zgzstop_12.jpg" width="2" height="37" /></td>
                <td width="100" height="37" align="center"><table width="76" border="0" cellspacing="0" cellpadding="0">
                    <tr>
                      <td height="37" align="center" class="STYLE2" id="qh1" onmousemove="qh(1)"><span ><a href="../../zjzs/" target="_blank">走进樟树</a></span></td>
                    </tr>
                </table></td>
                <td width="2" align="center"><img src="../../images/zgzstop_12.jpg" width="2" height="37" /></td>
                <td width="100" align="center"><table width="76" border="0" cellspacing="0" cellpadding="0">
                    <tr>
                      <td height="37" align="center" class="STYLE2" id="qh2" onmousemove="qh(2)"><span><a href="../" target="_blank"> 政务公开</a></span></td>
                    </tr>
                </table></td>
                <td width="2" align="center" class="STYLE2"><img src="../../images/zgzstop_12.jpg" width="2" height="37" /></td>
                <td width="100" align="center"><table width="76" border="0" cellspacing="0" cellpadding="0">
                    <tr>
                      <td height="37" align="center" class="STYLE2" id="qh3" onmousemove="qh(3)"><span > <a href="../../zmhd/" target="_blank">政民互动</a></span></td>
                    </tr>
                </table></td>
                <td width="2" align="center"><img src="../../images/zgzstop_12.jpg" width="2" height="37" /></td>
                <td width="100" align="center"><table width="76" border="0" cellspacing="0" cellpadding="0">
                    <tr>
                      <td height="37" align="center" class="STYLE2" id="qh4" onmousemove="qh(4)"><span ><a href="../../wsfw/" target="_blank">网上服务</a></span></td>
                    </tr>
                </table></td>
                <td width="2" align="center"><img src="../../images/zgzstop_12.jpg" width="2" height="37" /></td>
                <td width="100" align="center"><table width="76" border="0" cellspacing="0" cellpadding="0">
                    <tr>
                      <td height="37" align="center" class="STYLE2" id="qh5" onmousemove="qh(5)"><span ><a href="../../tzzs/" target="_blank">投资樟树</a></span></td>
                    </tr>
                </table></td>
                <td width="2" align="center"><img src="../../images/zgzstop_12.jpg" width="2" height="37" /></td>
                <td width="100" align="center"><table width="76" border="0" cellspacing="0" cellpadding="0">
                    <tr>
                      <td height="37" align="center" class="STYLE2" id="qh6" onmousemove="qh(6)"><span ><a href="../../lyzs/" target="_blank">旅游樟树</a></span></td>
                    </tr>
                </table></td>
                <td width="2" align="center"><img src="../../images/zgzstop_12.jpg" width="2" height="37" /></td>
                <td width="100" align="center"><table width="76" border="0" cellspacing="0" cellpadding="0">
                    <tr>
                      <td height="37" align="center" class="STYLE2" id="qh7" onmousemove="qh(7)"><span ><a href="../../wsfw/fwsn/" target="_blank">服务三农</a></span></td>
                    </tr>
                </table></td>
              </tr>
            </table></td>
            <td width="25%">
            <form name="SearchForm" method="post" accept-charset="utf-8" action="http://xxjs.yichun.gov.cn:8082/was5/web/search" target="_blank" style="margin:0; padding:0" onsubmit="SearchForm_onsubmit();return false;">
            <table width="100%" border="0" cellspacing="0" cellpadding="0">
              <tr>
                <td width="60%" height="37" align="center"><input type="hidden" id="searchword" name="searchword" />
                <input type="hidden" name="channelid" value="251664" />
                <INPUT id="keyword" name="keyword" width="145" height="25" /></td>
                <td width="18%" align="center"><input type="image" src="../../images/zgzstop_19.jpg" width="39" height="21" style="cursor:pointer" name="button" id="button" /></td>
                <td width="22%" align="center"><a href="http://xxjs.yichun.gov.cn:8082/was5/web/wcmadvanced.jsp?channelid=251664" target="_blank"><img src="../../images/zgzstop_21.jpg" width="59" height="21" /></a></td>
              </tr>
            </table>
            </form>
            <script type="text/javascript"> 
							function SearchForm_onsubmit() {
								 var tempkeyword=document.SearchForm.keyword.value;
								 
								 var tempchannelid=document.SearchForm.keyword.value;

								 if(!tempkeyword){
									alert("请输入关键字");
									return false;
								 }
								 if(zhuru(tempkeyword)==1){
								    alert("含有非法字符");
									return false;
								 }
								document.SearchForm.searchword.value="%"+tempkeyword+"%";
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
        <td width="1%" align="right" background="../../images/zgzstop_10.jpg"><img src="../../images/zgzstop_14.jpg" width="6" height="37" /></td>
      </tr>
    </table></td>
  </tr>
  <tr>
    <td height="50"><table width="100%" border="0" cellspacing="0" cellpadding="0">
      <tr>
        <td width="6%" height="50" background="../../images/zgzstop_28.jpg"><img src="../../images/zgzstop_26.jpg" width="6" height="50" /><img src="../../images/zgzstop_40.jpg" width="50" height="50" /></td>
        <td width="93%" height="50" background="../../images/zgzstop_28.jpg"><table width="100%" border="0" cellspacing="0" cellpadding="0">
          <tr>
            <td width="38%" height="50" align="left" valign="top" background="../../images/zgzsmain01_44.jpg"><div style="width:100%; height: 50px; overflow: hidden" id="mq" onmouseover="iScrollAmount=0" onmouseout="iScrollAmount=2">
              <table width="100%" border="0" cellspacing="0" cellpadding="0">
                
                  <tr>
                    <td><table width="100%" border="0" cellspacing="0" cellpadding="0">
                      <tr>
                        <td width="82%" height="25" align="left"><span class="STYLE12"><a href="../../wsfw/fwsm/smgg/tdgg/201705/t20170517_376590.html" title="停电通知!5月18-19日樟树这些地方要停电,请相互告知!" target="_blank">
                          停电通知!5月18-19日樟树这些地方...
                          </a></span></td>
                        <td width="12%" class="STYLE10" style=" font-size:12px">05-17</td>
                        </tr>
                      </table></td>
                    </tr>
                  
                  <tr>
                    <td><table width="100%" border="0" cellspacing="0" cellpadding="0">
                      <tr>
                        <td width="82%" height="25" align="left"><span class="STYLE12"><a href="../../wsfw/fwsm/smgg/tsgg/201608/t20160808_345856.html" title="停 水 公 告" target="_blank">
                          停 水 公 告
                          </a></span></td>
                        <td width="12%" class="STYLE10" style=" font-size:12px">08-08</td>
                        </tr>
                      </table></td>
                    </tr>
                  
                  <tr>
                    <td><table width="100%" border="0" cellspacing="0" cellpadding="0">
                      <tr>
                        <td width="82%" height="25" align="left"><span class="STYLE12"><a href="../../wsfw/fwsm/smgg/tdgg/201701/t20170111_362269.html" title="停电公告" target="_blank">
                          停电公告
                          </a></span></td>
                        <td width="12%" class="STYLE10" style=" font-size:12px">01-06</td>
                        </tr>
                      </table></td>
                    </tr>
                  
                  <tr>
                    <td><table width="100%" border="0" cellspacing="0" cellpadding="0">
                      <tr>
                        <td width="82%" height="25" align="left"><span class="STYLE12"><a href="../../wsfw/fwsm/smgg/tdgg/201508/t20150807_307214.html" title="市供电公司2015年33周检修计划表（8月10号-8月16号）" target="_blank">
                          市供电公司2015年33周检修计划表...
                          </a></span></td>
                        <td width="12%" class="STYLE10" style=" font-size:12px">08-07</td>
                        </tr>
                      </table></td>
                    </tr>
                  
                  <tr>
                    <td><table width="100%" border="0" cellspacing="0" cellpadding="0">
                      <tr>
                        <td width="82%" height="25" align="left"><span class="STYLE12"><a href="../../wsfw/fwsm/smgg/tsgg/201508/t20150831_309689.html" title="停 水 公 告" target="_blank">
                          停 水 公 告
                          </a></span></td>
                        <td width="12%" class="STYLE10" style=" font-size:12px">08-31</td>
                        </tr>
                      </table></td>
                    </tr>
                  
                  <tr>
                    <td><table width="100%" border="0" cellspacing="0" cellpadding="0">
                      <tr>
                        <td width="82%" height="25" align="left"><span class="STYLE12"><a href="../../wsfw/fwsm/smgg/tdgg/201507/t20150731_305789.html" title="市供电公司2015年32周检修计划表（8月03号-8月09号）" target="_blank">
                          市供电公司2015年32周检修计划表...
                          </a></span></td>
                        <td width="12%" class="STYLE10" style=" font-size:12px">07-31</td>
                        </tr>
                      </table></td>
                    </tr>
                  
                  <tr>
                    <td><table width="100%" border="0" cellspacing="0" cellpadding="0">
                      <tr>
                        <td width="82%" height="25" align="left"><span class="STYLE12"><a href="../../wsfw/fwsm/smgg/tsgg/201508/t20150831_309687.html" title="停 水 公 告" target="_blank">
                          停 水 公 告
                          </a></span></td>
                        <td width="12%" class="STYLE10" style=" font-size:12px">08-31</td>
                        </tr>
                      </table></td>
                    </tr>
                  
                  <tr>
                    <td><table width="100%" border="0" cellspacing="0" cellpadding="0">
                      <tr>
                        <td width="82%" height="25" align="left"><span class="STYLE12"><a href="../../wsfw/fwsm/smgg/ldgz/201703/t20170310_367656.html" title="关于驾车时禁止接打手机和按规定使用安全带交通安全管理通告" target="_blank">
                          关于驾车时禁止接打手机和按规定...
                          </a></span></td>
                        <td width="12%" class="STYLE10" style=" font-size:12px">03-10</td>
                        </tr>
                      </table></td>
                    </tr>
                  
                  <tr>
                    <td><table width="100%" border="0" cellspacing="0" cellpadding="0">
                      <tr>
                        <td width="82%" height="25" align="left"><span class="STYLE12"><a href="../../wsfw/fwsm/smgg/tsgg/201507/t20150723_305012.html" title="污水处理厂、大丰饲料厂、西堡王家村等路段停水公告" target="_blank">
                          污水处理厂、大丰饲料厂、西堡王...
                          </a></span></td>
                        <td width="12%" class="STYLE10" style=" font-size:12px">07-22</td>
                        </tr>
                      </table></td>
                    </tr>
                  
                  <tr>
                    <td><table width="100%" border="0" cellspacing="0" cellpadding="0">
                      <tr>
                        <td width="82%" height="25" align="left"><span class="STYLE12"><a href="../../wsfw/fwsm/smgg/ldgz/201702/t20170210_363482.html" title="樟树交警2017年元宵节“两公布一提示”" target="_blank">
                          樟树交警2017年元宵节“两公布一...
                          </a></span></td>
                        <td width="12%" class="STYLE10" style=" font-size:12px">02-10</td>
                        </tr>
                      </table></td>
                    </tr>
                  
                  <tr>
                    <td><table width="100%" border="0" cellspacing="0" cellpadding="0">
                      <tr>
                        <td width="82%" height="25" align="left"><span class="STYLE12"><a href="../../wsfw/fwsm/smgg/fwcq/201701/t20170123_363028.html" title="【交警公告】2017春运来了！拥堵&限行……樟树这些地方将实施交通管制" target="_blank">
                          【交警公告】2017春运来了！拥堵&...
                          </a></span></td>
                        <td width="12%" class="STYLE10" style=" font-size:12px">01-11</td>
                        </tr>
                      </table></td>
                    </tr>
                  
                  <tr>
                    <td><table width="100%" border="0" cellspacing="0" cellpadding="0">
                      <tr>
                        <td width="82%" height="25" align="left"><span class="STYLE12"><a href="../../wsfw/fwsm/smgg/ldgz/201702/t20170206_363277.html" title="2017年春节节后返程“两公布一提示”" target="_blank">
                          2017年春节节后返程“两公布一提示”
                          </a></span></td>
                        <td width="12%" class="STYLE10" style=" font-size:12px">02-06</td>
                        </tr>
                      </table></td>
                    </tr>
                  
                </table>
              </div>
              <script language="javascript">
                       var oMarquee = document.getElementById("mq"); //滚动对象
                       var iLineHeight = 25; //单行高度，像素
                       var iLineCount = 100; //实际行数
                       var iScrollAmount = 2; //每次滚动高度，像素
                       function run() {
                        oMarquee.scrollTop += iScrollAmount;
                        if ( oMarquee.scrollTop == iLineCount * iLineHeight )
                         oMarquee.scrollTop = 0;
                        if ( oMarquee.scrollTop % iLineHeight == 0 ) {
                         window.setTimeout( "run()", 2000 );
                        } else {
                         window.setTimeout( "run()", 50 );
                         }
                       }
                       oMarquee.innerHTML += oMarquee.innerHTML;
                       window.setTimeout( "run()", 2000 );
                       </script></td>
            <td width="22%" height="50"><table width="100%" border="0" cellspacing="0" cellpadding="0">
              <tr>
                <td width="13%" height="31" align="center"><img src="../../images/zgzstop_35.jpg" width="13" height="16" /></td>
                <td width="87%" align="center" class="STYLE3"><script type="text/javascript">
var oMyDate=new Date();
var iYear=oMyDate.getFullYear();
var iMonth=oMyDate.getMonth()+1;
var iDate=oMyDate.getDate();
var iDay=oMyDate.getDay();
switch(iDay){
	case 0:
		iDay="星期日";
		break;
	case 1:
		iDay="星期一";
		break;
	case 2:
		iDay="星期二";
		break;
	case 3:
		iDay="星期三";
		break;
	case 4:
		iDay="星期四";
		break;
	case 5:
		iDay="星期五";
		break;
	case 6:
		iDay="星期六";
		break;
	default:
		iDay="error";
	
}
document.write(""+iYear+"年"+iMonth+"月"+iDate+"日 "+iDay);

</script></td>
                </tr>
            </table></td>
            <td width="27%"><table width="100%" height="28" border="0" cellpadding="0" cellspacing="0">
              <tr>
                <td width="258" height="22" align="center"><iframe src="http://m.weather.com.cn/m/pn3/weather.htm?id=101240509T " width="250" height="20" marginwidth="0" marginheight="0" hspace="0" vspace="0" frameborder="0" scrolling="no" allowtransparency="true"></iframe></td>
                </tr>
              </table></td>
            <td width="13%"><table width="100%" border="0" cellspacing="0" cellpadding="0">
              <tr>
                <td width="82%" height="24" align="center" valign="middle"><span class="STYLE12"> <a href="http://www.zhangshu.gov.cn/zt/wfxxjb/201612/t20161213_357735.htm"></a></a></span><a href="http://www.zhangshu.gov.cn/zt/wfxxjb/201612/t20161213_357735.htm"><span class="STYLE5">在线举报平台</span></a></td>
              </tr>
              <tr>
                <td height="25" align="center" valign="middle"><a href="http://www.12377.cn/"><span class="STYLE5">打击新闻敲诈</span></a></td>
              </tr>
            </table></td>
            </tr>
        </table></td>
        </tr>
    </table></td>
  </tr>
</table>
</body>
</html></div>
<table width="1002" border="0" align="center" cellpadding="0" cellspacing="0">
  <tr>
    <td height="25"><table width="100%" height="25" border="0" cellpadding="0" cellspacing="0">
      <tr>
        <td width="3%" align="center"><img src="../../images/zgzs01_03.jpg" width="14" height="14" /></td>
        <td width="97%" align="left" class="STYLE16 STYLE25"><strong>您的当前位置：</strong><a href="../../" title="首页" class="CurrChnlCls">首页</a>&nbsp;&gt;&gt;&nbsp;<a href="../" title="政务公开" class="CurrChnlCls">政务公开</a>&nbsp;&gt;&gt;&nbsp;<a href="./" title="综合信息" class="CurrChnlCls">综合信息</a></td>
      </tr>
    </table></td>
  </tr>
  <tr>
    <td height="13" style="background:url(../site40/zgzs01_06.jpg) repeat-x top"></td>
  </tr>
</table>
<table width="1002" height="672" border="0" align="center" cellpadding="0" cellspacing="0">
  <tr>
  <td width="232" valign="top"><table width="231" border="0" cellspacing="0" cellpadding="0">
      <tr>
        <td height="372" valign="top"><table width="100%" border="0" cellspacing="0" cellpadding="0">
          <tr>
            <td height="241" valign="top"><table width="100%" border="0" cellspacing="0" cellpadding="0">
                <tr>
                  <td height="34" background="../../images/zgzsmain01_05.jpg"><table width="100%" border="0" cellspacing="0" cellpadding="0">
                      <tr>
                        <td width="10%" height="34" align="left"><img src="../../images/zgzsmain01_03.jpg" width="23" height="34" /></td>
                        <td width="82%" align="left" class="STYLE8">领导介绍</td>
                        <td width="8%" align="right"><img src="../../images/zgzsmain01_07.jpg" width="6" height="34" /></td>
                      </tr>
                  </table></td>
                </tr>
                <tr>
                  <td height="205"><table width="100%" style="border-bottom:#e1e1e1 1px solid; border-left:#e1e1e1 1px solid; border-right:#e1e1e1 1px solid;" height="201" border="0" cellpadding="0" cellspacing="0">
                      <tr>
                        <td align="center"><a href="../ldjs/sw/" target="_blank"><img src="../../images/zgzsmain01_20.jpg" width="213" height="44" /></a></td>
                      </tr>
                      <tr>
                        <td align="center"><a href="../ldjs/rd/" target="_blank"><img src="../../images/zgzsmain01_23.jpg" width="213" height="44" /></a></td>
                      </tr>
                      <tr>
                        <td align="center"><a href="../ldjs/zf/" target="_blank"><img src="../../images/zgzsmain01_30.jpg" width="213" height="44" /></a></td>
                      </tr>
                      <tr>
                        <td align="center"><a href="../ldjs/zx/" target="_blank"><img src="../../images/zgzsmain01_32.jpg" width="213" height="44" /></a></td>
                      </tr>
                  </table></td>
                </tr>
            </table></td>
          </tr>
          <tr>
            <td height="136" valign="top"><table width="231" border="0" cellspacing="0" cellpadding="0">
              <tr>
                <td height="33"><img src="../../images/zgzsmain01_34.jpg" width="231" height="33" /></td>
              </tr>
              <tr>
                <td height="96" valign="top"><table width="100%" style="border-bottom:#b3c8e3 1px solid; border-left:#b3c8e3 1px solid; border-right:#b3c8e3 1px solid;" border="0" cellspacing="0" cellpadding="0">
                    <tr>
                      <td height="95"><FORM id="MailFormLogin2" method="post" name="MailFormLogin" 
            action="http://mail.zhangshu.gov.cn/coremail/fcg/login" target="_self"><table width="100%" border="0" cellspacing="0" cellpadding="0">
                          <tr>
                            <td height="22"><table width="100%" height="30" border="0" cellpadding="0" cellspacing="0">
                                <tr>
                                  <td width="30%" align="center" class="STYLE12">用户名：</td>
                                  <td width="70%" align="left"><INPUT size=12 name=user width="145" height="20" /></td>
                                </tr>
                            </table></td>
                          </tr>
                          <tr>
                            <td><table width="100%" height="30" border="0" cellpadding="0" cellspacing="0">
                                <tr>
                                  <td width="30%" align="center" class="STYLE12">密  码：</td>
                                  <td width="70%" align="left"><INPUT size=12 type=password name=pass width="145" height="20" /></td>
                                </tr>
                            </table></td>
                          </tr>
                          <tr>
                            <td align="center"><table width="64%" height="25" border="0" cellpadding="0" cellspacing="0">
                                <tr>
                                  <td align="center"><input type="image" width="57" height="23" src="../../images/zgzsmain01_51.jpg" /></td>
                                  <td align="center"><img src="../../images/zgzsmain01_53.jpg" width="57" height="23" onclick="document.forms.MailFormLogin.reset();" /></td>
                                </tr>
                            </table></td>
                          </tr>
                      </table>
                      </FORM></td>
                    </tr>
                </table></td>
              </tr>
            </table></td>
          </tr>
        </table></td>
      </tr>
      
      <tr>
        <td valign="top"><table width="100%" border="0" cellspacing="0" cellpadding="0">
          <tr>
            <td height="31" background="../../images/zgzsmain01_05.jpg"><table width="100%" border="0" cellspacing="0" cellpadding="0">
                <tr>
                  <td width="10%" height="34" align="left"><img src="../../images/zgzsmain01_03.jpg" width="23" height="34" /></td>
                  <td width="82%" align="left" class="STYLE8">便民服务</td>
                  <td width="8%" align="right"><img src="../../images/zgzsmain01_07.jpg" width="6" height="34" /></td>
                </tr>
            </table></td>
          </tr>
          <tr>
            <td height="107" valign="top" bgcolor="#FFFFFF"><table width="100%" style="border-bottom:#e1e1e1 1px solid; border-left:#e1e1e1 1px solid; border-right:#e1e1e1 1px solid;" height="104" border="0" cellpadding="0" cellspacing="0">
                <tr>
                  <td><table width="100%" height="96" border="0" cellpadding="0" cellspacing="0">
                    
                      <tr valign="top">
                      
                        <td align="center"><table width="72" border="0" cellspacing="0" cellpadding="0">
                            <tr>
                              <td width="17" height="20" align="center"><img src="../../images/zgzsz3_93.jpg" width="6" height="5" /></td>
                              <td width="55" align="left" class="bmfw"><a href="../../wsfw/bmfw/bgxz/" target="_blank">
                                  表格下载
                                  </a></td>
                            </tr>
                        </table></td>
                        
                        <td align="center"><table width="72" border="0" cellspacing="0" cellpadding="0">
                            <tr>
                              <td width="17" height="20" align="center"><img src="../../images/zgzsz3_93.jpg" width="6" height="5" /></td>
                              <td width="55" align="left" class="bmfw"><a href="../../wsfw/bmfw/gjqc/" target="_blank">
                                  公交汽车
                                  </a></td>
                            </tr>
                        </table></td>
                        
                        <td align="center"><table width="72" border="0" cellspacing="0" cellpadding="0">
                            <tr>
                              <td width="17" height="20" align="center"><img src="../../images/zgzsz3_93.jpg" width="6" height="5" /></td>
                              <td width="55" align="left" class="bmfw"><a href="../../wsfw/bmfw/ztqc/" target="_blank">
                                  长途汽车
                                  </a></td>
                            </tr>
                        </table></td>
                        
                       </tr>
                      
                      <tr valign="top">
                      
                        <td align="center"><table width="72" border="0" cellspacing="0" cellpadding="0">
                            <tr>
                              <td width="17" height="20" align="center"><img src="../../images/zgzsz3_93.jpg" width="6" height="5" /></td>
                              <td width="55" align="left" class="bmfw"><a href="../../wsfw/bmfw/hcsk/" target="_blank">
                                  火车时刻
                                  </a></td>
                            </tr>
                        </table></td>
                        
                        <td align="center"><table width="72" border="0" cellspacing="0" cellpadding="0">
                            <tr>
                              <td width="17" height="20" align="center"><img src="../../images/zgzsz3_93.jpg" width="6" height="5" /></td>
                              <td width="55" align="left" class="bmfw"><a href="../../wsfw/bmfw/fjhb/" target="_blank">
                                  飞机航班
                                  </a></td>
                            </tr>
                        </table></td>
                        
                        <td align="center"><table width="72" border="0" cellspacing="0" cellpadding="0">
                            <tr>
                              <td width="17" height="20" align="center"><img src="../../images/zgzsz3_93.jpg" width="6" height="5" /></td>
                              <td width="55" align="left" class="bmfw"><a href="../../wsfw/bmfw/cydh/" target="_blank">
                                  常用电话
                                  </a></td>
                            </tr>
                        </table></td>
                        
                       </tr>
                      
                      <tr valign="top">
                      
                        <td align="center"><table width="72" border="0" cellspacing="0" cellpadding="0">
                            <tr>
                              <td width="17" height="20" align="center"><img src="../../images/zgzsz3_93.jpg" width="6" height="5" /></td>
                              <td width="55" align="left" class="bmfw"><a href="../../wsfw/bmfw/yzbm/" target="_blank">
                                  邮政编码
                                  </a></td>
                            </tr>
                        </table></td>
                        
                        <td align="center"><table width="72" border="0" cellspacing="0" cellpadding="0">
                            <tr>
                              <td width="17" height="20" align="center"><img src="../../images/zgzsz3_93.jpg" width="6" height="5" /></td>
                              <td width="55" align="left" class="bmfw"><a href="../../wsfw/bmfw/xxyl/" target="_blank">
                                  学校一览
                                  </a></td>
                            </tr>
                        </table></td>
                        
                        <td align="center"><table width="72" border="0" cellspacing="0" cellpadding="0">
                            <tr>
                              <td width="17" height="20" align="center"><img src="../../images/zgzsz3_93.jpg" width="6" height="5" /></td>
                              <td width="55" align="left" class="bmfw"><a href="../../wsfw/bmfw/yyyl/" target="_blank">
                                  医院一览
                                  </a></td>
                            </tr>
                        </table></td>
                        
                       </tr>
                      
                  </table></td>
                </tr>
            </table></td>
          </tr>
        </table></td>
      </tr>
      <tr>
        <td height="138" valign="top"><table width="100%" style="border:#e1e1e1 1px solid" height="145" border="0" cellpadding="0" cellspacing="0" bgcolor="#FFFFFF">
          <tr>
            <td height="74" align="center" valign="middle"><a href="../../zmhd/szxx/" target="_blank"><img src="../../images/zgzsz2_24.jpg" width="207" height="67" /></a></td>
          </tr>
          <tr>
            <td height="69" align="center" valign="middle"><a href="../../zmhd/12388jbsl/" target="_blank"><img src="../../images/zgzsz2_28.jpg" width="207" height="58" /></a></td>
          </tr>
        </table></td>
      </tr>
    </table></td>
    <td width="770" height="672" valign="top"><table width="99%" border="0" cellspacing="0" cellpadding="0">
      <tr>
        <td height="34" background="../../images/zgzsmain01_05.jpg"><table width="100%" border="0" cellspacing="0" cellpadding="0">
            <tr>
              <td width="3%" height="34" align="left"><img src="../../images/zgzsmain01_03.jpg" width="23" height="34" /></td>
              <td width="89%" align="left" class="STYLE8">综合信息</td>
              <td width="8%" align="right"><img src="../../images/zgzsmain01_07.jpg" width="6" height="34" /></td>
            </tr>
        </table></td>
      </tr>
      <tr>
        <td height="624" valign="top"><table width="100%" style="border-bottom:#e1e1e1 1px solid; border-left:#e1e1e1 1px solid; border-right:#e1e1e1 1px solid;" height="629" border="0" cellpadding="0" cellspacing="0">
          <tr>
            <td height="600" align="center" valign="top"><table width="99%" border="0" cellspacing="0" cellpadding="0">
                        
              <tr valign="center" style="padding:0 3px; marign:0 3px;">
              <td width="3%" height="25" align="center"><img src="../../images/zgzszy01_07.jpg" width="6" height="7" /></td>
                <td width="87%" height="25" align="left" class="STYLE25 STYLE26"><a href="./201710/t20171019_398276.html" target="_blank"><span class="STYLE25">江西（樟树）医药产业招商引资推介会举行</span></a></td>
                <td width="10%"><span class="STYLE12">10-19</span></td>
              </tr>
              
              <tr valign="center" style="padding:0 3px; marign:0 3px;">
              <td width="3%" height="25" align="center"><img src="../../images/zgzszy01_07.jpg" width="6" height="7" /></td>
                <td width="87%" height="25" align="left" class="STYLE25 STYLE26"><a href="./201710/t20171019_398275.html" target="_blank"><span class="STYLE25">江西省药品第三方现代物流启动仪式举行</span></a></td>
                <td width="10%"><span class="STYLE12">10-19</span></td>
              </tr>
              
              <tr valign="center" style="padding:0 3px; marign:0 3px;">
              <td width="3%" height="25" align="center"><img src="../../images/zgzszy01_07.jpg" width="6" height="7" /></td>
                <td width="87%" height="25" align="left" class="STYLE25 STYLE26"><a href="./201710/t20171019_398274.html" target="_blank"><span class="STYLE25">副省长李贻煌等领导视察樟树第48届全国药交会交易会场</span></a></td>
                <td width="10%"><span class="STYLE12">10-19</span></td>
              </tr>
              
              <tr valign="center" style="padding:0 3px; marign:0 3px;">
              <td width="3%" height="25" align="center"><img src="../../images/zgzszy01_07.jpg" width="6" height="7" /></td>
                <td width="87%" height="25" align="left" class="STYLE25 STYLE26"><a href="./201710/t20171018_398194.html" target="_blank"><span class="STYLE25">樟树首次举办全国药店团购会</span></a></td>
                <td width="10%"><span class="STYLE12">10-18</span></td>
              </tr>
              
              <tr valign="center" style="padding:0 3px; marign:0 3px;">
              <td width="3%" height="25" align="center"><img src="../../images/zgzszy01_07.jpg" width="6" height="7" /></td>
                <td width="87%" height="25" align="left" class="STYLE25 STYLE26"><a href="./201710/t20171016_398067.html" target="_blank"><span class="STYLE25">振兴中国药都 弘扬中华医药一一樟树第48届全国药材药品交易会...</span></a></td>
                <td width="10%"><span class="STYLE12">10-16</span></td>
              </tr>
              
              <tr valign="center" style="padding:0 3px; marign:0 3px;">
              <td width="3%" height="25" align="center"><img src="../../images/zgzszy01_07.jpg" width="6" height="7" /></td>
                <td width="87%" height="25" align="left" class="STYLE25 STYLE26"><a href="./201710/t20171016_398027.html" target="_blank"><span class="STYLE25">中国（樟树）中医药峰会在樟树举行</span></a></td>
                <td width="10%"><span class="STYLE12">10-16</span></td>
              </tr>
              
              <tr valign="center" style="padding:0 3px; marign:0 3px;">
              <td width="3%" height="25" align="center"><img src="../../images/zgzszy01_07.jpg" width="6" height="7" /></td>
                <td width="87%" height="25" align="left" class="STYLE25 STYLE26"><a href="./201710/t20171016_398026.html" target="_blank"><span class="STYLE25">宜春市政协主席陈荣到我市调研</span></a></td>
                <td width="10%"><span class="STYLE12">10-16</span></td>
              </tr>
              
              <tr valign="center" style="padding:0 3px; marign:0 3px;">
              <td width="3%" height="25" align="center"><img src="../../images/zgzszy01_07.jpg" width="6" height="7" /></td>
                <td width="87%" height="25" align="left" class="STYLE25 STYLE26"><a href="./201710/t20171011_397574.html" target="_blank"><span class="STYLE25">樟树启动实施“智慧城市”建设</span></a></td>
                <td width="10%"><span class="STYLE12">10-11</span></td>
              </tr>
              
              <tr valign="center" style="padding:0 3px; marign:0 3px;">
              <td width="3%" height="25" align="center"><img src="../../images/zgzszy01_07.jpg" width="6" height="7" /></td>
                <td width="87%" height="25" align="left" class="STYLE25 STYLE26"><a href="./201710/t20171011_397571.html" target="_blank"><span class="STYLE25">樟树市成功入选2017年多个百强县市榜</span></a></td>
                <td width="10%"><span class="STYLE12">10-11</span></td>
              </tr>
              
              <tr valign="center" style="padding:0 3px; marign:0 3px;">
              <td width="3%" height="25" align="center"><img src="../../images/zgzszy01_07.jpg" width="6" height="7" /></td>
                <td width="87%" height="25" align="left" class="STYLE25 STYLE26"><a href="./201710/t20171010_397432.html" target="_blank"><span class="STYLE25">2017“樟树·中国药都杯”中日韩围棋大师赛暨中国围棋甲级联...</span></a></td>
                <td width="10%"><span class="STYLE12">10-10</span></td>
              </tr>
              
              <tr valign="center" style="padding:0 3px; marign:0 3px;">
              <td width="3%" height="25" align="center"><img src="../../images/zgzszy01_07.jpg" width="6" height="7" /></td>
                <td width="87%" height="25" align="left" class="STYLE25 STYLE26"><a href="./201710/t20171009_397388.html" target="_blank"><span class="STYLE25">红色革命遗迹——毛泽东旧居免费对外开放</span></a></td>
                <td width="10%"><span class="STYLE12">10-09</span></td>
              </tr>
              
              <tr valign="center" style="padding:0 3px; marign:0 3px;">
              <td width="3%" height="25" align="center"><img src="../../images/zgzszy01_07.jpg" width="6" height="7" /></td>
                <td width="87%" height="25" align="left" class="STYLE25 STYLE26"><a href="./201709/t20170930_397102.html" target="_blank"><span class="STYLE25">刘安安书记参观《江山多娇》柯克中国山水画展</span></a></td>
                <td width="10%"><span class="STYLE12">09-30</span></td>
              </tr>
              
              <tr valign="center" style="padding:0 3px; marign:0 3px;">
              <td width="3%" height="25" align="center"><img src="../../images/zgzszy01_07.jpg" width="6" height="7" /></td>
                <td width="87%" height="25" align="left" class="STYLE25 STYLE26"><a href="./201709/t20170928_396616.html" target="_blank"><span class="STYLE25">宜春市重大项目巡查组成员到我市巡查</span></a></td>
                <td width="10%"><span class="STYLE12">09-28</span></td>
              </tr>
              
              <tr valign="center" style="padding:0 3px; marign:0 3px;">
              <td width="3%" height="25" align="center"><img src="../../images/zgzszy01_07.jpg" width="6" height="7" /></td>
                <td width="87%" height="25" align="left" class="STYLE25 STYLE26"><a href="./201709/t20170929_396862.html" target="_blank"><span class="STYLE25">刘安安调研秀美乡村、重大项目建设和棚户区改造工作</span></a></td>
                <td width="10%"><span class="STYLE12">09-29</span></td>
              </tr>
              
              <tr valign="center" style="padding:0 3px; marign:0 3px;">
              <td width="3%" height="25" align="center"><img src="../../images/zgzszy01_07.jpg" width="6" height="7" /></td>
                <td width="87%" height="25" align="left" class="STYLE25 STYLE26"><a href="./201709/t20170929_396861.html" target="_blank"><span class="STYLE25">省林业厅巡视员魏运华到我市调研</span></a></td>
                <td width="10%"><span class="STYLE12">09-29</span></td>
              </tr>
              
              <tr valign="center" style="padding:0 3px; marign:0 3px;">
              <td width="3%" height="25" align="center"><img src="../../images/zgzszy01_07.jpg" width="6" height="7" /></td>
                <td width="87%" height="25" align="left" class="STYLE25 STYLE26"><a href="./201709/t20170926_396174.html" target="_blank"><span class="STYLE25">中国城镇化促进会来我市考察</span></a></td>
                <td width="10%"><span class="STYLE12">09-26</span></td>
              </tr>
              
              <tr valign="center" style="padding:0 3px; marign:0 3px;">
              <td width="3%" height="25" align="center"><img src="../../images/zgzszy01_07.jpg" width="6" height="7" /></td>
                <td width="87%" height="25" align="left" class="STYLE25 STYLE26"><a href="./201709/t20170926_396173.html" target="_blank"><span class="STYLE25">省水利厅厅长罗小云到我市督导河道采砂管理工作</span></a></td>
                <td width="10%"><span class="STYLE12">09-26</span></td>
              </tr>
              
              <tr valign="center" style="padding:0 3px; marign:0 3px;">
              <td width="3%" height="25" align="center"><img src="../../images/zgzszy01_07.jpg" width="6" height="7" /></td>
                <td width="87%" height="25" align="left" class="STYLE25 STYLE26"><a href="./201709/t20170925_396074.html" target="_blank"><span class="STYLE25">樟树市举行“砺剑2017”反恐处突演习</span></a></td>
                <td width="10%"><span class="STYLE12">09-25</span></td>
              </tr>
              
              <tr valign="center" style="padding:0 3px; marign:0 3px;">
              <td width="3%" height="25" align="center"><img src="../../images/zgzszy01_07.jpg" width="6" height="7" /></td>
                <td width="87%" height="25" align="left" class="STYLE25 STYLE26"><a href="./201709/t20170925_395989.html" target="_blank"><span class="STYLE25">省政府批复同意樟树工业园区扩区和调整区位</span></a></td>
                <td width="10%"><span class="STYLE12">09-25</span></td>
              </tr>
              
              <tr valign="center" style="padding:0 3px; marign:0 3px;">
              <td width="3%" height="25" align="center"><img src="../../images/zgzszy01_07.jpg" width="6" height="7" /></td>
                <td width="87%" height="25" align="left" class="STYLE25 STYLE26"><a href="./201709/t20170925_395981.html" target="_blank"><span class="STYLE25">省综合应急救援工作督导组到樟树督导</span></a></td>
                <td width="10%"><span class="STYLE12">09-25</span></td>
              </tr>
              
              <tr valign="center" style="padding:0 3px; marign:0 3px;">
              <td width="3%" height="25" align="center"><img src="../../images/zgzszy01_07.jpg" width="6" height="7" /></td>
                <td width="87%" height="25" align="left" class="STYLE25 STYLE26"><a href="./201709/t20170922_395692.html" target="_blank"><span class="STYLE25">2017国际（樟树）中医药博览会暨中国药都（樟树）第48届全国...</span></a></td>
                <td width="10%"><span class="STYLE12">09-22</span></td>
              </tr>
              
              <tr valign="center" style="padding:0 3px; marign:0 3px;">
              <td width="3%" height="25" align="center"><img src="../../images/zgzszy01_07.jpg" width="6" height="7" /></td>
                <td width="87%" height="25" align="left" class="STYLE25 STYLE26"><a href="./201709/t20170925_396059.html" target="_blank"><span class="STYLE25">樟树市对省环保督察组交办信访件16-10处理情况</span></a></td>
                <td width="10%"><span class="STYLE12">09-25</span></td>
              </tr>
              
              <tr valign="center" style="padding:0 3px; marign:0 3px;">
              <td width="3%" height="25" align="center"><img src="../../images/zgzszy01_07.jpg" width="6" height="7" /></td>
                <td width="87%" height="25" align="left" class="STYLE25 STYLE26"><a href="./201709/t20170925_396057.html" target="_blank"><span class="STYLE25">樟树市对省环保督察组交办信访件15-7处理情况</span></a></td>
                <td width="10%"><span class="STYLE12">09-25</span></td>
              </tr>
              
              <tr valign="center" style="padding:0 3px; marign:0 3px;">
              <td width="3%" height="25" align="center"><img src="../../images/zgzszy01_07.jpg" width="6" height="7" /></td>
                <td width="87%" height="25" align="left" class="STYLE25 STYLE26"><a href="./201709/t20170925_396056.html" target="_blank"><span class="STYLE25">樟树市对省环保督察组交办信访件14-12处理情况</span></a></td>
                <td width="10%"><span class="STYLE12">09-25</span></td>
              </tr>
              
              <tr><td>
                </td>
              </tr>
            </table></td>
          </tr>
          <tr><td><table width="100%" cellpadding="0" cellspacing="0">
              <tr>
                <td width="100%" height="25" align="center" style="font-size:12px"><script language="javascript">
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
<script>createPageHTML(21, 0, "index", "html");</script></td>
                </tr>
                </table></td></tr>
        </table></td>
      </tr>
    </table></td>
    
  </tr>
</table>
<div><style type="text/css">
body {
	background-image: url();
}
.STYLE2.STYLE26 a {
	color: #0080FF;
}
</style>
<table width="1002" border="0" align="center" cellpadding="0" cellspacing="0">
  <tr>
    <td height="118" valign="top" background="../site40/zgzsmain03_48.jpg"><table width="100%" border="0" cellspacing="0" cellpadding="0">
        <tr>
          <td height="33" colspan="3" align="center" class="STYLE2 STYLE26"><a href="http://www.zhangshu.gov.cn/lxwm/201211/t20121127_171256.html" target="_blank">联系我们</a> | <a href="javascript:this.style.behavior='url(#default#homepage)';this.setHomePage(document.location.href);">设为首页</a> | <a href="javascript:window.external.addFavorite(document.location.href,document.title)">加入收藏</a> | <a href="http://202.109.164.35:9000/wcm/" target="_blank">后台管理</a></td>
        </tr>
        <tr>
          <td width="23%" height="83" align="center" class="STYLE3 a1"><script id="_jiucuo_" sitecode='3609820008' src='../../images/jiucuo.js'></script></td>
          <td width="50%" align="center" class="STYLE3 a1"><p>主办：樟树市人民政府 承办：樟树市信息中心<br />
            Copyright © 2006 People's Government of Zhangshu . All Rights Reserved <br />樟树市人民政府版权所有<br />
          制作单位：樟树市政务信息化工作办公室 赣ICP备10003342号-1</p></td>
          <td width="27%" align="center" class="STYLE3 a1"><script type="text/javascript">document.write(unescape("%3Cspan id='_ideConac' %3E%3C/span%3E%3Cscript src='http://dcs.conac.cn/js/15/232/0886/41170852/CA152320886411708520002.js' type='text/javascript'%3E%3C/script%3E"));</script>&nbsp;</td>
        </tr>
      </table></td>
  </tr>
</table></div>

</body>
</html>

"""

soup = BeautifulSoup(''.join(doc))

table = soup.find('table', {'width': '99%'})

print(table)

datetime_t = str(datetime.date.today()).split('-')
# print(datetime_t)


articles_link = []
for tr in table.findAll('tr'):
    # print(tr)

    find_today = re.compile(r'(\d\d)-(\d\d)</span>')  # 构建找到末尾发布日期的正则表达式
    month = find_today.search(str(tr))  # 把上面构建的表达式作用于findAll找出来的内容

    try:
        d1 = datetime.date.today()  # 获取今天的日期
        d2 = datetime.date(int(datetime_t[0]), int(month.group(1)), int(month.group(2)))  # 获取新闻的日期
        days_betwen = (d1 - d2).days  # 获取日期差
        if days_betwen <= 30:
            articles_link.append(str(tr))

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