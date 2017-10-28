#coding=utf-8

from BeautifulSoup import BeautifulSoup
import datetime,re

doc = """
																																																																																																																								<!DOCTYPE html PUBLIC "-//W3C//DTD XHTML 1.0 Transitional//EN" "http://www.w3.org/TR/xhtml1/DTD/xhtml1-transitional.dtd">
<html xmlns="http://www.w3.org/1999/xhtml">
<head>
<meta http-equiv="Content-Type" content="text/html; charset=utf-8" />
 <meta http-equiv="X-UA-Compatible" content="IE=Edge,chrome=1 ">
<title>江西旅游网_地市动态</title>
<style type="text/css">
<!--
.neiye  {
	font-size: 12px;
	color: #000000;
	text-decoration: none;
	
}
.dangqian  {
	font-size: 12px;
	color: #005ba1;
	text-decoration: none;
}

.lanmudao {
	font-size: 16px;
	font-weight: bold;
	color: #ffffff;
	text-decoration: none;
}

-->
</style>
<link href="/css/zh_cn/DefaultSkin.css" type=text/css rel=stylesheet>


<SCRIPT language=javascript src="/resource/uploadfile/zh_cn/gb20170801/js/jquery.js"></SCRIPT>
<SCRIPT language=javascript src="/resource/uploadfile/zh_cn/gb20170801/js/kxbdMarquee.js"></SCRIPT>
<SCRIPT language=javascript src="/resource/uploadfile/zh_cn/gb20170801/js/wza.js"></SCRIPT>
<script type="text/javascript" src="/resource/uploadfile/zh_cn/gb20170801/js/swfobject_modified.js"></script>
</head>

<body>
<STYLE type=text/css>
  #nav{ background: url('/resource/uploadfile/zh_cn/navbar.png') no-repeat top center;position:absolute;top:289px;left:0;right:0 }
    .Qcenter{ width: 1030px; height: 70px; margin: 0 auto;  }
      .Qul{ margin-left: 22px; margin-top: 39px;  height: 59px; }
        .Qul .Qlib{ float: left; height: 59px; margin-right: 1px; position: relative; overflow:visible; }
        .Qul .Qlib a{ display: block; height: 30px; font-size: 16px; color: #fff; font-family: "微软雅黑";}
          #Qli1{ width: 168px; background: url('/resource/uploadfile/zh_cn/Qindex.png') no-repeat center; }
          #Qli2{ width: 182px; background: url('/resource/uploadfile/zh_cn/Qlydt.png') no-repeat center; }
          #Qli3{ width: 219px; background: url('/resource/uploadfile/zh_cn/Qlvwjj.png') no-repeat center; }
          #Qli4{ width: 204px; background: url('/resource/uploadfile/zh_cn/Qzwgk.png') no-repeat center; }
          #Qli5{ width: 208px; background: url('/resource/uploadfile/zh_cn/Qbsfw.png') no-repeat center; }
          .Qul .Qlib:hover #Qli1{ width: 168px; background: url('/resource/uploadfile/zh_cn/Qindex2.png') no-repeat center;  }
          .Qul .Qlib:hover #Qli2{ width: 182px; background: url('/resource/uploadfile/zh_cn/Qlydt2.png') no-repeat center;}
          .Qul .Qlib:hover #Qli3{ width: 219px; background: url('/resource/uploadfile/zh_cn/Qlvwjj2.png') no-repeat center;}
          .Qul .Qlib:hover #Qli4{ width: 204px; background: url('/resource/uploadfile/zh_cn/Qzwgk2.png') no-repeat center; }
          .Qul .Qlib:hover #Qli5{ width: 208px; background: url('/resource/uploadfile/zh_cn/Qbsfw2.png') no-repeat center;}
        .Qdiv{ width: 182px; min-height:255px; position: absolute; z-index:10000; font-size: 0; margin-left: -40px; display: none; }
        .Qdiv1{ top: 44px; left: 39px; }
        .Qdiv2{ top: 44px; left: 56px; }
        .Qdiv3{ top: 44px; left: 53px; }
          .Qdiv li,.Qdiv2 li,.Qdiv3 li{ height: 39px; line-height: 38px; text-align: center; margin: 0; padding: 0; background: url('/resource/uploadfile/zh_cn/Qcen.png') repeat-y center; }
          .Qimg{ margin-top: -1px; }
        .Qul .Qlib:hover .Qdiv{ display: block; }
</STYLE>
<div class=headWrap>
<div class=top>
<div class=center>
<div class=fle>
<P>欢迎来到江西省旅游委员会政务网<SPAN id=weltime>
<SCRIPT language=javascript>
    $(function(){
    var Mdate = new Date();
    var Mnow = "";
    Mnow = Mdate.getFullYear()+"年"; 
    Mnow = Mnow + (Mdate.getMonth()+1)+"月"; 
    Mnow = Mnow + Mdate.getDate()+"日";
    var Week = ['日','一','二','三','四','五','六'];
    Mnow = Mnow + " 星期" + Week[Mdate.getDay()];
    $("#weltime").text(Mnow); 
    });
             </SCRIPT>
 </SPAN></P></div>
<div class=fri><A href="Column.shtml?p5=3474">快速通道</A> 丨 <A onclick=OpentoolBar(); href="javascript:void(0);">无障碍服务</A> 丨 <A href="Column.shtml?p5=14">一站式服务</A> | <A href="http://mail.jxta.gov.cn" target=_blank>邮箱登录</A><!-- &nbsp;&nbsp; <A href="http://tour.jxnews.com.cn/">江西旅游网</A>&nbsp;&nbsp;<A href="http://www.jxhsly.cn/">江西红色旅游网</A> --> </div></div></div>
<div id=header>
<div class=banner>
<object id="FlashID" classid="clsid:D27CDB6E-AE6D-11cf-96B8-444553540000" width="1002" height="326">
  <param name="movie" value="/resource/uploadfile/zh_cn/gb20170801/flash.swf" />
  <param name="quality" value="high" />
  <param name="wmode" value="Transparent" />
  <param name="swfversion" value="8.0.35.0" />
  <!-- 此 param 标签提示使用 Flash Player 6.0 r65 和更高版本的用户下载最新版本的 Flash Player。如果您不想让用户看到该提示，请将其删除。 -->
  <param name="expressinstall" value="Scripts/expressInstall.swf" />
  <!-- 下一个对象标签用于非 IE 浏览器。所以使用 IECC 将其从 IE 隐藏。 -->
  <!--[if !IE]>-->
  <object type="application/x-shockwave-flash" data="/resource/uploadfile/zh_cn/gb20170801/flash.swf" width="1002" height="326">
    <!--<![endif]-->
    <param name="quality" value="high" />
    <param name="wmode" value="transparent" />
    <param name="swfversion" value="8.0.35.0" />
    <param name="expressinstall" value="Scripts/expressInstall.swf" />
    <!-- 浏览器将以下替代内容显示给使用 Flash Player 6.0 和更低版本的用户。 -->
    <div>
      <h4>此页面上的内容需要较新版本的 Adobe Flash Player。</h4>
      <p><a href="http://www.adobe.com/go/getflashplayer"><img src="http://www.adobe.com/images/shared/download_buttons/get_flash_player.gif" alt="获取 Adobe Flash Player" width="112" height="33" /></a></p>
    </div>
    <!--[if !IE]>-->
  </object>
  <!--<![endif]-->
</object>
<script type="text/javascript">
swfobject.registerObject("FlashID");
</script></div></div>
<div id="nav" class="nav">
<div class="Qcenter">
<UL class="Qul">
<LI class="Qcurrent Qlib"><A id="Qli1" href="/"></A></LI>
<LI class="Qlib"><A id="Qli2" href="/Column.shtml?p5=13"></A>
<UL class="Qdiv1 Qdiv"><IMG alt="" src="/resource/uploadfile/zh_cn/Qtop.png"> 
<LI><A href="/Column.shtml?p5=101">图片新闻</A> </LI>
<LI><A href="/Column.shtml?p5=26">旅游快报</A> </LI>
<LI><A href="/Column.shtml?p5=28">地市动态</A> </LI>
<LI><A href="/Column.shtml?p5=27">行业动态</A> </LI>
<LI><A href="/Column.shtml?p5=721">通知公告</A> </LI>
<LI><A href="/Column.shtml?p5=3550">新闻发布会</A></LI>
<LI><A href="/Column.shtml?p5=3527">一句话工作动态</A></LI>
<LI><A href="/Column.shtml?p5=3509">国务院重要政策信息</A>  </LI>
<IMG class="Qimg"  alt="" src="/resource/uploadfile/zh_cn/Qbootom.png"></UL></LI>
<LI class="Qlib"><A id="Qli3" href="/Column.shtml?p5=12"></A>
<UL class="Qdiv2 Qdiv"><IMG alt="" src="/resource/uploadfile/zh_cn/Qtop.png"> 
<LI><A href="/Column.shtml?p5=75">办公位置</A> </LI>
<LI><A href="/Column.shtml?p5=76">职能介绍</A> </LI>
<LI><A href="/Column.shtml?p5=77">领导介绍</A> </LI>
<LI><A href="/Column.shtml?p5=3553">兼职委员介绍</A> </LI>
<LI><A href="/Column.shtml?p5=78">机构设置</A> </LI>
<LI><A href="/Column.shtml?p5=704">地市旅游委</A> </LI><IMG class="Qimg"  alt="" src="/resource/uploadfile/zh_cn/Qbootom.png"> </UL></LI>
<LI class="Qlib"><A id="Qli4" href="/Column.shtml?p5=11"></A>
<UL class="Qdiv3 Qdiv"><IMG alt="" src="/resource/uploadfile/zh_cn/Qtop.png"> 
<LI><A href="/Column.shtml?p5=3514">文件通知</A> </LI>
<LI><A href="/Column.shtml?p5=3430">财政公开</A> </LI>
<LI><A href="/Column.shtml?p5=3439">财政预决算</A> </LI>
<LI><A href="/Column.shtml?p5=3437">招标采购</A> </LI>
<LI><A href="/Column.shtml?p5=3440">人事信息</A> </LI>
<LI><A href="/Column.shtml?p5=707">旅游规划</A> </LI>
<LI><A href="/Column.shtml?p5=3488">政策与解读</A> </LI>
<LI><A href="/Column.shtml?p5=16">政策法规</A> </LI>
<LI><A href="/Column.shtml?p5=722">旅游统计</A> </LI>
<LI><A href="/Column.shtml?p5=3599 ">减税降费</A> </LI>
<LI><A href="/Column.shtml?p5=3489">权利责任清单</A>  </LI><IMG class="Qimg"  alt="" src="/resource/uploadfile/zh_cn/Qbootom.png"></UL></LI>
<LI class="Qlib"><A id="Qli5" href="/Column.shtml?p5=708"></A>
<UL class="Qdiv2 Qdiv"><IMG alt="" src="/resource/uploadfile/zh_cn/Qtop.png"> 
<LI><A href="/Column.shtml?p5=709">行政审批</A> </LI>
<LI><A href="/ReferForm.shtml?p5=101">在线咨询</A> </LI>
<LI><A href="http://www.jxzwfww.gov.cn/xzpp/bmfl/slfw_1897/">在线申报</A> </LI>
<LI><A href="/Column.shtml?p5=711">办事指南</A> </LI>
<LI><A href="/Column.shtml?p5=712">在线下载</A> </LI>
<LI><A href="/Column.shtml?p5=3551">整理汇编</A> </LI><IMG class="Qimg" alt="" src="/resource/uploadfile/zh_cn/Qbootom.png"> </UL></LI></UL></div>
</div></div>
<div id="c">
  <div id="container">
<table width="990" border="0" align="center" cellpadding="0" cellspacing="0">
  <tr>
    <td width="752" valign="top"><table width="100%" border="0" align="center" cellpadding="0" cellspacing="0">
      <tr>
        <td height="28" background="resource/images/djxlyw/m1_03.jpg" class="dangqian" style="padding-left:28px; padding-top:4px"><a href='Index.shtml'>首页</a>&nbsp;&nbsp;&nbsp;>>&nbsp;&nbsp;&nbsp;<a href='Column.shtml?p5=13'>旅游动态</a>&nbsp;&nbsp;&nbsp;>>&nbsp;&nbsp;&nbsp;<a href='Column.shtml?p5=28'>地市动态</a></td>
      </tr>
      <tr>
        <td><table width="100%" border="0" align="center" cellpadding="0" cellspacing="0" background="resource/images/djxlyw/m31.jpg">
          <tr>
            <td height="522" valign="top" background="resource/images/djxlyw/m1_07.jpg" class="neiye" style="background-repeat:repeat-x; padding-left:24px; padding-top:6px; padding-right:5px; line-height:26px"><table style="border:1px solid #c2d9a3; " width="95%" height="30" border="0" cellpadding="0" cellspacing="0" bgcolor="#eefbdf">
  <tr>
    <td align="center" style="padding:5px;"><a href="Column.shtml?p5=763" target=_blank>南昌</a> | <a href="Column.shtml?p5=764" target=_blank>九江</a> | <a href="Column.shtml?p5=770" target=_blank>鹰潭</a> | <a href="Column.shtml?p5=767" target=_blank>宜春</a> | <a href="Column.shtml?p5=771" target=_blank>萍乡</a> | <a href="Column.shtml?p5=765" target=_blank>赣州</a> | <a href="Column.shtml?p5=768" target=_blank>吉安</a> | <a href="Column.shtml?p5=766" target=_blank>上饶</a> | <a href="Column.shtml?p5=772" target=_blank>新余</a> | <a href="Column.shtml?p5=769" target=_blank>抚州</a> | <a href="Column.shtml?p5=773" target=_blank>景德镇</a></td>
  </tr>
</table><!--栏目稿件分页列表开始-->
<table width=100% id=Table cellpadding=1 cellspacing=1 align=left>
<tr>
<td width=87%><img src='resource/images/djxlyw/dicon02.gif' border=0>&nbsp;<a href='News.shtml?p5=530558' title='铜鼓“四升级”舞活生态经济龙头'  target='_blank' ><font color='0'>铜鼓“四升级”舞活生态经济龙头</font></a></td><td width=13%><font color='0'>2017-10-05</font></td></tr>
<tr>
<td width=87%><img src='resource/images/djxlyw/dicon02.gif' border=0>&nbsp;<a href='News.shtml?p5=530438' title='万载：中秋舞火龙 傩舞祈安康'  target='_blank' ><font color='0'>万载：中秋舞火龙 傩舞祈安康</font></a></td><td width=13%><font color='0'>2017-10-05</font></td></tr>
<tr>
<td width=87%><img src='resource/images/djxlyw/dicon02.gif' border=0>&nbsp;<a href='News.shtml?p5=530356' title='国庆期间，吉安这些景区游客爆棚！'  target='_blank' ><font color='0'>国庆期间，吉安这些景区游客爆棚！</font></a></td><td width=13%><font color='0'>2017-10-04</font></td></tr>
<tr>
<td width=87%><img src='resource/images/djxlyw/dicon02.gif' border=0>&nbsp;<a href='News.shtml?p5=530296' title='贫困户端上旅游“金饭碗”'  target='_blank' ><font color='0'>贫困户端上旅游“金饭碗”</font></a></td><td width=13%><font color='0'>2017-10-04</font></td></tr>
<tr>
<td width=87%><img src='resource/images/djxlyw/dicon02.gif' border=0>&nbsp;<a href='News.shtml?p5=530216' title='“乡味”浓，樟树首届乡村运动会热闹开赛'  target='_blank' ><font color='0'>“乡味”浓，樟树首届乡村运动会热闹开赛</font></a></td><td width=13%><font color='0'>2017-10-04</font></td></tr>
<tr>
<td width=87%><img src='resource/images/djxlyw/dicon02.gif' border=0>&nbsp;<a href='News.shtml?p5=529976' title='喜迎国庆，万载民俗文化旅游精彩纷呈'  target='_blank' ><font color='0'>喜迎国庆，万载民俗文化旅游精彩纷呈</font></a></td><td width=13%><font color='0'>2017-10-03</font></td></tr>
<tr>
<td width=87%><img src='resource/images/djxlyw/dicon02.gif' border=0>&nbsp;<a href='News.shtml?p5=529618' title='庆国庆，樟树旗袍秀展演引千人围观'  target='_blank' ><font color='0'>庆国庆，樟树旗袍秀展演引千人围观</font></a></td><td width=13%><font color='0'>2017-10-01</font></td></tr>
<tr>
<td width=87%><img src='resource/images/djxlyw/dicon02.gif' border=0>&nbsp;<a href='News.shtml?p5=529598' title='九江启动旅游整治“秋风”行动 全面净化旅游市场秩序 '  target='_blank' ><font color='0'>九江启动旅游整治“秋风”行动 全面净化旅游市场秩序</font></a></td><td width=13%><font color='0'>2017-10-01</font></td></tr>
<tr>
<td width=87%><img src='resource/images/djxlyw/dicon02.gif' border=0>&nbsp;<a href='News.shtml?p5=529510' title='婺源篁岭摆《可爱的中国》 喜迎国庆'  target='_blank' ><font color='0'>婺源篁岭摆《可爱的中国》 喜迎国庆</font></a></td><td width=13%><font color='0'>2017-10-01</font></td></tr>
<tr>
<td width=87%><img src='resource/images/djxlyw/dicon02.gif' border=0>&nbsp;<a href='News.shtml?p5=529500' title='厉害了我的国 全球华人诵读“可爱的中国” 向世界推介大美上饶'  target='_blank' ><font color='0'>厉害了我的国 全球华人诵读“可爱的中国” 向世界推介大美上饶</font></a></td><td width=13%><font color='0'>2017-10-01</font></td></tr>
<tr>
<td width=87%><img src='resource/images/djxlyw/dicon02.gif' border=0>&nbsp;<a href='News.shtml?p5=529238' title='红色革命遗迹——毛泽东同志旧居将于今日正式对外开放'  target='_blank' ><font color='0'>红色革命遗迹——毛泽东同志旧居将于今日正式对外开放</font></a></td><td width=13%><font color='0'>2017-09-30</font></td></tr>
<tr>
<td width=87%><img src='resource/images/djxlyw/dicon02.gif' border=0>&nbsp;<a href='News.shtml?p5=529127' title='浔阳区开展“中秋、国庆”节前旅游安全大检查活动'  target='_blank' ><font color='0'>浔阳区开展“中秋、国庆”节前旅游安全大检查活动</font></a></td><td width=13%><font color='0'>2017-09-30</font></td></tr>
<tr>
<td width=87%><img src='resource/images/djxlyw/dicon02.gif' border=0>&nbsp;<a href='News.shtml?p5=529117' title='全民诵读传递对“可爱的中国”砥砺奋进之声'  target='_blank' ><font color='0'>全民诵读传递对“可爱的中国”砥砺奋进之声</font></a></td><td width=13%><font color='0'>2017-09-30</font></td></tr>
<tr>
<td width=87%><img src='resource/images/djxlyw/dicon02.gif' border=0>&nbsp;<a href='News.shtml?p5=529107' title='我市开展国庆节假日旅游安全专项督查'  target='_blank' ><font color='0'>我市开展国庆节假日旅游安全专项督查</font></a></td><td width=13%><font color='0'>2017-09-30</font></td></tr>
<tr>
<td width=87%><img src='resource/images/djxlyw/dicon02.gif' border=0>&nbsp;<a href='News.shtml?p5=529097' title='吉安市智慧旅游平台正式上线'  target='_blank' ><font color='0'>吉安市智慧旅游平台正式上线</font></a></td><td width=13%><font color='0'>2017-09-30</font></td></tr>
<tr><td class='' colspan=2>
<table width="100%"><tr><td class="pagenextclass">&nbsp;</td></tr><tr><td><form name='strongPageNext' id='strongPageNext' action='toto.asp'>
共&nbsp;1367页&nbsp;&nbsp;&nbsp;20493&nbsp;条记录&nbsp;&nbsp;&nbsp;当前页:&nbsp;1&nbsp;&nbsp;&nbsp;首页&nbsp;&nbsp;&nbsp;上一页&nbsp;&nbsp;&nbsp;
第<select class="conditionSelectBox" name='pageNo' onChange='javascript:gotoCurrentPage(this.value)'><option value='1' selected='selected' >1/1367</option><option value='2'>2/1367</option><option value='3'>3/1367</option><option value='4'>4/1367</option><option value='5'>5/1367</option><option value='6'>6/1367</option><option value='7'>7/1367</option><option value='8'>8/1367</option><option value='9'>9/1367</option><option value='10'>10/1367</option><option value='11'>11/1367</option><option value='12'>12/1367</option><option value='13'>13/1367</option><option value='14'>14/1367</option><option value='15'>15/1367</option><option value='16'>16/1367</option><option value='17'>17/1367</option><option value='18'>18/1367</option><option value='19'>19/1367</option><option value='20'>20/1367</option><option value='21'>21/1367</option><option value='22'>22/1367</option><option value='23'>23/1367</option><option value='24'>24/1367</option><option value='25'>25/1367</option><option value='26'>26/1367</option><option value='27'>27/1367</option><option value='28'>28/1367</option><option value='29'>29/1367</option><option value='30'>30/1367</option><option value='31'>31/1367</option><option value='32'>32/1367</option><option value='33'>33/1367</option><option value='34'>34/1367</option><option value='35'>35/1367</option><option value='36'>36/1367</option><option value='37'>37/1367</option><option value='38'>38/1367</option><option value='39'>39/1367</option><option value='40'>40/1367</option><option value='41'>41/1367</option><option value='42'>42/1367</option><option value='43'>43/1367</option><option value='44'>44/1367</option><option value='45'>45/1367</option><option value='46'>46/1367</option><option value='47'>47/1367</option><option value='48'>48/1367</option><option value='49'>49/1367</option><option value='50'>50/1367</option><option value='51'>51/1367</option><option value='52'>52/1367</option><option value='53'>53/1367</option><option value='54'>54/1367</option><option value='55'>55/1367</option><option value='56'>56/1367</option><option value='57'>57/1367</option><option value='58'>58/1367</option><option value='59'>59/1367</option><option value='60'>60/1367</option><option value='61'>61/1367</option><option value='62'>62/1367</option><option value='63'>63/1367</option><option value='64'>64/1367</option><option value='65'>65/1367</option><option value='66'>66/1367</option><option value='67'>67/1367</option><option value='68'>68/1367</option><option value='69'>69/1367</option><option value='70'>70/1367</option><option value='71'>71/1367</option><option value='72'>72/1367</option><option value='73'>73/1367</option><option value='74'>74/1367</option><option value='75'>75/1367</option><option value='76'>76/1367</option><option value='77'>77/1367</option><option value='78'>78/1367</option><option value='79'>79/1367</option><option value='80'>80/1367</option><option value='81'>81/1367</option><option value='82'>82/1367</option><option value='83'>83/1367</option><option value='84'>84/1367</option><option value='85'>85/1367</option><option value='86'>86/1367</option><option value='87'>87/1367</option><option value='88'>88/1367</option><option value='89'>89/1367</option><option value='90'>90/1367</option><option value='91'>91/1367</option><option value='92'>92/1367</option><option value='93'>93/1367</option><option value='94'>94/1367</option><option value='95'>95/1367</option><option value='96'>96/1367</option><option value='97'>97/1367</option><option value='98'>98/1367</option><option value='99'>99/1367</option><option value='100'>100/1367</option><option value='101'>101/1367</option><option value='102'>102/1367</option><option value='103'>103/1367</option><option value='104'>104/1367</option><option value='105'>105/1367</option><option value='106'>106/1367</option><option value='107'>107/1367</option><option value='108'>108/1367</option><option value='109'>109/1367</option><option value='110'>110/1367</option><option value='111'>111/1367</option><option value='112'>112/1367</option><option value='113'>113/1367</option><option value='114'>114/1367</option><option value='115'>115/1367</option><option value='116'>116/1367</option><option value='117'>117/1367</option><option value='118'>118/1367</option><option value='119'>119/1367</option><option value='120'>120/1367</option><option value='121'>121/1367</option><option value='122'>122/1367</option><option value='123'>123/1367</option><option value='124'>124/1367</option><option value='125'>125/1367</option><option value='126'>126/1367</option><option value='127'>127/1367</option><option value='128'>128/1367</option><option value='129'>129/1367</option><option value='130'>130/1367</option><option value='131'>131/1367</option><option value='132'>132/1367</option><option value='133'>133/1367</option><option value='134'>134/1367</option><option value='135'>135/1367</option><option value='136'>136/1367</option><option value='137'>137/1367</option><option value='138'>138/1367</option><option value='139'>139/1367</option><option value='140'>140/1367</option><option value='141'>141/1367</option><option value='142'>142/1367</option><option value='143'>143/1367</option><option value='144'>144/1367</option><option value='145'>145/1367</option><option value='146'>146/1367</option><option value='147'>147/1367</option><option value='148'>148/1367</option><option value='149'>149/1367</option><option value='150'>150/1367</option><option value='151'>151/1367</option><option value='152'>152/1367</option><option value='153'>153/1367</option><option value='154'>154/1367</option><option value='155'>155/1367</option><option value='156'>156/1367</option><option value='157'>157/1367</option><option value='158'>158/1367</option><option value='159'>159/1367</option><option value='160'>160/1367</option><option value='161'>161/1367</option><option value='162'>162/1367</option><option value='163'>163/1367</option><option value='164'>164/1367</option><option value='165'>165/1367</option><option value='166'>166/1367</option><option value='167'>167/1367</option><option value='168'>168/1367</option><option value='169'>169/1367</option><option value='170'>170/1367</option><option value='171'>171/1367</option><option value='172'>172/1367</option><option value='173'>173/1367</option><option value='174'>174/1367</option><option value='175'>175/1367</option><option value='176'>176/1367</option><option value='177'>177/1367</option><option value='178'>178/1367</option><option value='179'>179/1367</option><option value='180'>180/1367</option><option value='181'>181/1367</option><option value='182'>182/1367</option><option value='183'>183/1367</option><option value='184'>184/1367</option><option value='185'>185/1367</option><option value='186'>186/1367</option><option value='187'>187/1367</option><option value='188'>188/1367</option><option value='189'>189/1367</option><option value='190'>190/1367</option><option value='191'>191/1367</option><option value='192'>192/1367</option><option value='193'>193/1367</option><option value='194'>194/1367</option><option value='195'>195/1367</option><option value='196'>196/1367</option><option value='197'>197/1367</option><option value='198'>198/1367</option><option value='199'>199/1367</option><option value='200'>200/1367</option><option value='201'>201/1367</option><option value='202'>202/1367</option><option value='203'>203/1367</option><option value='204'>204/1367</option><option value='205'>205/1367</option><option value='206'>206/1367</option><option value='207'>207/1367</option><option value='208'>208/1367</option><option value='209'>209/1367</option><option value='210'>210/1367</option><option value='211'>211/1367</option><option value='212'>212/1367</option><option value='213'>213/1367</option><option value='214'>214/1367</option><option value='215'>215/1367</option><option value='216'>216/1367</option><option value='217'>217/1367</option><option value='218'>218/1367</option><option value='219'>219/1367</option><option value='220'>220/1367</option><option value='221'>221/1367</option><option value='222'>222/1367</option><option value='223'>223/1367</option><option value='224'>224/1367</option><option value='225'>225/1367</option><option value='226'>226/1367</option><option value='227'>227/1367</option><option value='228'>228/1367</option><option value='229'>229/1367</option><option value='230'>230/1367</option><option value='231'>231/1367</option><option value='232'>232/1367</option><option value='233'>233/1367</option><option value='234'>234/1367</option><option value='235'>235/1367</option><option value='236'>236/1367</option><option value='237'>237/1367</option><option value='238'>238/1367</option><option value='239'>239/1367</option><option value='240'>240/1367</option><option value='241'>241/1367</option><option value='242'>242/1367</option><option value='243'>243/1367</option><option value='244'>244/1367</option><option value='245'>245/1367</option><option value='246'>246/1367</option><option value='247'>247/1367</option><option value='248'>248/1367</option><option value='249'>249/1367</option><option value='250'>250/1367</option><option value='251'>251/1367</option><option value='252'>252/1367</option><option value='253'>253/1367</option><option value='254'>254/1367</option><option value='255'>255/1367</option><option value='256'>256/1367</option><option value='257'>257/1367</option><option value='258'>258/1367</option><option value='259'>259/1367</option><option value='260'>260/1367</option><option value='261'>261/1367</option><option value='262'>262/1367</option><option value='263'>263/1367</option><option value='264'>264/1367</option><option value='265'>265/1367</option><option value='266'>266/1367</option><option value='267'>267/1367</option><option value='268'>268/1367</option><option value='269'>269/1367</option><option value='270'>270/1367</option><option value='271'>271/1367</option><option value='272'>272/1367</option><option value='273'>273/1367</option><option value='274'>274/1367</option><option value='275'>275/1367</option><option value='276'>276/1367</option><option value='277'>277/1367</option><option value='278'>278/1367</option><option value='279'>279/1367</option><option value='280'>280/1367</option><option value='281'>281/1367</option><option value='282'>282/1367</option><option value='283'>283/1367</option><option value='284'>284/1367</option><option value='285'>285/1367</option><option value='286'>286/1367</option><option value='287'>287/1367</option><option value='288'>288/1367</option><option value='289'>289/1367</option><option value='290'>290/1367</option><option value='291'>291/1367</option><option value='292'>292/1367</option><option value='293'>293/1367</option><option value='294'>294/1367</option><option value='295'>295/1367</option><option value='296'>296/1367</option><option value='297'>297/1367</option><option value='298'>298/1367</option><option value='299'>299/1367</option><option value='300'>300/1367</option><option value='301'>301/1367</option><option value='302'>302/1367</option><option value='303'>303/1367</option><option value='304'>304/1367</option><option value='305'>305/1367</option><option value='306'>306/1367</option><option value='307'>307/1367</option><option value='308'>308/1367</option><option value='309'>309/1367</option><option value='310'>310/1367</option><option value='311'>311/1367</option><option value='312'>312/1367</option><option value='313'>313/1367</option><option value='314'>314/1367</option><option value='315'>315/1367</option><option value='316'>316/1367</option><option value='317'>317/1367</option><option value='318'>318/1367</option><option value='319'>319/1367</option><option value='320'>320/1367</option><option value='321'>321/1367</option><option value='322'>322/1367</option><option value='323'>323/1367</option><option value='324'>324/1367</option><option value='325'>325/1367</option><option value='326'>326/1367</option><option value='327'>327/1367</option><option value='328'>328/1367</option><option value='329'>329/1367</option><option value='330'>330/1367</option><option value='331'>331/1367</option><option value='332'>332/1367</option><option value='333'>333/1367</option><option value='334'>334/1367</option><option value='335'>335/1367</option><option value='336'>336/1367</option><option value='337'>337/1367</option><option value='338'>338/1367</option><option value='339'>339/1367</option><option value='340'>340/1367</option><option value='341'>341/1367</option><option value='342'>342/1367</option><option value='343'>343/1367</option><option value='344'>344/1367</option><option value='345'>345/1367</option><option value='346'>346/1367</option><option value='347'>347/1367</option><option value='348'>348/1367</option><option value='349'>349/1367</option><option value='350'>350/1367</option><option value='351'>351/1367</option><option value='352'>352/1367</option><option value='353'>353/1367</option><option value='354'>354/1367</option><option value='355'>355/1367</option><option value='356'>356/1367</option><option value='357'>357/1367</option><option value='358'>358/1367</option><option value='359'>359/1367</option><option value='360'>360/1367</option><option value='361'>361/1367</option><option value='362'>362/1367</option><option value='363'>363/1367</option><option value='364'>364/1367</option><option value='365'>365/1367</option><option value='366'>366/1367</option><option value='367'>367/1367</option><option value='368'>368/1367</option><option value='369'>369/1367</option><option value='370'>370/1367</option><option value='371'>371/1367</option><option value='372'>372/1367</option><option value='373'>373/1367</option><option value='374'>374/1367</option><option value='375'>375/1367</option><option value='376'>376/1367</option><option value='377'>377/1367</option><option value='378'>378/1367</option><option value='379'>379/1367</option><option value='380'>380/1367</option><option value='381'>381/1367</option><option value='382'>382/1367</option><option value='383'>383/1367</option><option value='384'>384/1367</option><option value='385'>385/1367</option><option value='386'>386/1367</option><option value='387'>387/1367</option><option value='388'>388/1367</option><option value='389'>389/1367</option><option value='390'>390/1367</option><option value='391'>391/1367</option><option value='392'>392/1367</option><option value='393'>393/1367</option><option value='394'>394/1367</option><option value='395'>395/1367</option><option value='396'>396/1367</option><option value='397'>397/1367</option><option value='398'>398/1367</option><option value='399'>399/1367</option><option value='400'>400/1367</option><option value='401'>401/1367</option><option value='402'>402/1367</option><option value='403'>403/1367</option><option value='404'>404/1367</option><option value='405'>405/1367</option><option value='406'>406/1367</option><option value='407'>407/1367</option><option value='408'>408/1367</option><option value='409'>409/1367</option><option value='410'>410/1367</option><option value='411'>411/1367</option><option value='412'>412/1367</option><option value='413'>413/1367</option><option value='414'>414/1367</option><option value='415'>415/1367</option><option value='416'>416/1367</option><option value='417'>417/1367</option><option value='418'>418/1367</option><option value='419'>419/1367</option><option value='420'>420/1367</option><option value='421'>421/1367</option><option value='422'>422/1367</option><option value='423'>423/1367</option><option value='424'>424/1367</option><option value='425'>425/1367</option><option value='426'>426/1367</option><option value='427'>427/1367</option><option value='428'>428/1367</option><option value='429'>429/1367</option><option value='430'>430/1367</option><option value='431'>431/1367</option><option value='432'>432/1367</option><option value='433'>433/1367</option><option value='434'>434/1367</option><option value='435'>435/1367</option><option value='436'>436/1367</option><option value='437'>437/1367</option><option value='438'>438/1367</option><option value='439'>439/1367</option><option value='440'>440/1367</option><option value='441'>441/1367</option><option value='442'>442/1367</option><option value='443'>443/1367</option><option value='444'>444/1367</option><option value='445'>445/1367</option><option value='446'>446/1367</option><option value='447'>447/1367</option><option value='448'>448/1367</option><option value='449'>449/1367</option><option value='450'>450/1367</option><option value='451'>451/1367</option><option value='452'>452/1367</option><option value='453'>453/1367</option><option value='454'>454/1367</option><option value='455'>455/1367</option><option value='456'>456/1367</option><option value='457'>457/1367</option><option value='458'>458/1367</option><option value='459'>459/1367</option><option value='460'>460/1367</option><option value='461'>461/1367</option><option value='462'>462/1367</option><option value='463'>463/1367</option><option value='464'>464/1367</option><option value='465'>465/1367</option><option value='466'>466/1367</option><option value='467'>467/1367</option><option value='468'>468/1367</option><option value='469'>469/1367</option><option value='470'>470/1367</option><option value='471'>471/1367</option><option value='472'>472/1367</option><option value='473'>473/1367</option><option value='474'>474/1367</option><option value='475'>475/1367</option><option value='476'>476/1367</option><option value='477'>477/1367</option><option value='478'>478/1367</option><option value='479'>479/1367</option><option value='480'>480/1367</option><option value='481'>481/1367</option><option value='482'>482/1367</option><option value='483'>483/1367</option><option value='484'>484/1367</option><option value='485'>485/1367</option><option value='486'>486/1367</option><option value='487'>487/1367</option><option value='488'>488/1367</option><option value='489'>489/1367</option><option value='490'>490/1367</option><option value='491'>491/1367</option><option value='492'>492/1367</option><option value='493'>493/1367</option><option value='494'>494/1367</option><option value='495'>495/1367</option><option value='496'>496/1367</option><option value='497'>497/1367</option><option value='498'>498/1367</option><option value='499'>499/1367</option><option value='500'>500/1367</option><option value='501'>501/1367</option><option value='502'>502/1367</option><option value='503'>503/1367</option><option value='504'>504/1367</option><option value='505'>505/1367</option><option value='506'>506/1367</option><option value='507'>507/1367</option><option value='508'>508/1367</option><option value='509'>509/1367</option><option value='510'>510/1367</option><option value='511'>511/1367</option><option value='512'>512/1367</option><option value='513'>513/1367</option><option value='514'>514/1367</option><option value='515'>515/1367</option><option value='516'>516/1367</option><option value='517'>517/1367</option><option value='518'>518/1367</option><option value='519'>519/1367</option><option value='520'>520/1367</option><option value='521'>521/1367</option><option value='522'>522/1367</option><option value='523'>523/1367</option><option value='524'>524/1367</option><option value='525'>525/1367</option><option value='526'>526/1367</option><option value='527'>527/1367</option><option value='528'>528/1367</option><option value='529'>529/1367</option><option value='530'>530/1367</option><option value='531'>531/1367</option><option value='532'>532/1367</option><option value='533'>533/1367</option><option value='534'>534/1367</option><option value='535'>535/1367</option><option value='536'>536/1367</option><option value='537'>537/1367</option><option value='538'>538/1367</option><option value='539'>539/1367</option><option value='540'>540/1367</option><option value='541'>541/1367</option><option value='542'>542/1367</option><option value='543'>543/1367</option><option value='544'>544/1367</option><option value='545'>545/1367</option><option value='546'>546/1367</option><option value='547'>547/1367</option><option value='548'>548/1367</option><option value='549'>549/1367</option><option value='550'>550/1367</option><option value='551'>551/1367</option><option value='552'>552/1367</option><option value='553'>553/1367</option><option value='554'>554/1367</option><option value='555'>555/1367</option><option value='556'>556/1367</option><option value='557'>557/1367</option><option value='558'>558/1367</option><option value='559'>559/1367</option><option value='560'>560/1367</option><option value='561'>561/1367</option><option value='562'>562/1367</option><option value='563'>563/1367</option><option value='564'>564/1367</option><option value='565'>565/1367</option><option value='566'>566/1367</option><option value='567'>567/1367</option><option value='568'>568/1367</option><option value='569'>569/1367</option><option value='570'>570/1367</option><option value='571'>571/1367</option><option value='572'>572/1367</option><option value='573'>573/1367</option><option value='574'>574/1367</option><option value='575'>575/1367</option><option value='576'>576/1367</option><option value='577'>577/1367</option><option value='578'>578/1367</option><option value='579'>579/1367</option><option value='580'>580/1367</option><option value='581'>581/1367</option><option value='582'>582/1367</option><option value='583'>583/1367</option><option value='584'>584/1367</option><option value='585'>585/1367</option><option value='586'>586/1367</option><option value='587'>587/1367</option><option value='588'>588/1367</option><option value='589'>589/1367</option><option value='590'>590/1367</option><option value='591'>591/1367</option><option value='592'>592/1367</option><option value='593'>593/1367</option><option value='594'>594/1367</option><option value='595'>595/1367</option><option value='596'>596/1367</option><option value='597'>597/1367</option><option value='598'>598/1367</option><option value='599'>599/1367</option><option value='600'>600/1367</option><option value='601'>601/1367</option><option value='602'>602/1367</option><option value='603'>603/1367</option><option value='604'>604/1367</option><option value='605'>605/1367</option><option value='606'>606/1367</option><option value='607'>607/1367</option><option value='608'>608/1367</option><option value='609'>609/1367</option><option value='610'>610/1367</option><option value='611'>611/1367</option><option value='612'>612/1367</option><option value='613'>613/1367</option><option value='614'>614/1367</option><option value='615'>615/1367</option><option value='616'>616/1367</option><option value='617'>617/1367</option><option value='618'>618/1367</option><option value='619'>619/1367</option><option value='620'>620/1367</option><option value='621'>621/1367</option><option value='622'>622/1367</option><option value='623'>623/1367</option><option value='624'>624/1367</option><option value='625'>625/1367</option><option value='626'>626/1367</option><option value='627'>627/1367</option><option value='628'>628/1367</option><option value='629'>629/1367</option><option value='630'>630/1367</option><option value='631'>631/1367</option><option value='632'>632/1367</option><option value='633'>633/1367</option><option value='634'>634/1367</option><option value='635'>635/1367</option><option value='636'>636/1367</option><option value='637'>637/1367</option><option value='638'>638/1367</option><option value='639'>639/1367</option><option value='640'>640/1367</option><option value='641'>641/1367</option><option value='642'>642/1367</option><option value='643'>643/1367</option><option value='644'>644/1367</option><option value='645'>645/1367</option><option value='646'>646/1367</option><option value='647'>647/1367</option><option value='648'>648/1367</option><option value='649'>649/1367</option><option value='650'>650/1367</option><option value='651'>651/1367</option><option value='652'>652/1367</option><option value='653'>653/1367</option><option value='654'>654/1367</option><option value='655'>655/1367</option><option value='656'>656/1367</option><option value='657'>657/1367</option><option value='658'>658/1367</option><option value='659'>659/1367</option><option value='660'>660/1367</option><option value='661'>661/1367</option><option value='662'>662/1367</option><option value='663'>663/1367</option><option value='664'>664/1367</option><option value='665'>665/1367</option><option value='666'>666/1367</option><option value='667'>667/1367</option><option value='668'>668/1367</option><option value='669'>669/1367</option><option value='670'>670/1367</option><option value='671'>671/1367</option><option value='672'>672/1367</option><option value='673'>673/1367</option><option value='674'>674/1367</option><option value='675'>675/1367</option><option value='676'>676/1367</option><option value='677'>677/1367</option><option value='678'>678/1367</option><option value='679'>679/1367</option><option value='680'>680/1367</option><option value='681'>681/1367</option><option value='682'>682/1367</option><option value='683'>683/1367</option><option value='684'>684/1367</option><option value='685'>685/1367</option><option value='686'>686/1367</option><option value='687'>687/1367</option><option value='688'>688/1367</option><option value='689'>689/1367</option><option value='690'>690/1367</option><option value='691'>691/1367</option><option value='692'>692/1367</option><option value='693'>693/1367</option><option value='694'>694/1367</option><option value='695'>695/1367</option><option value='696'>696/1367</option><option value='697'>697/1367</option><option value='698'>698/1367</option><option value='699'>699/1367</option><option value='700'>700/1367</option><option value='701'>701/1367</option><option value='702'>702/1367</option><option value='703'>703/1367</option><option value='704'>704/1367</option><option value='705'>705/1367</option><option value='706'>706/1367</option><option value='707'>707/1367</option><option value='708'>708/1367</option><option value='709'>709/1367</option><option value='710'>710/1367</option><option value='711'>711/1367</option><option value='712'>712/1367</option><option value='713'>713/1367</option><option value='714'>714/1367</option><option value='715'>715/1367</option><option value='716'>716/1367</option><option value='717'>717/1367</option><option value='718'>718/1367</option><option value='719'>719/1367</option><option value='720'>720/1367</option><option value='721'>721/1367</option><option value='722'>722/1367</option><option value='723'>723/1367</option><option value='724'>724/1367</option><option value='725'>725/1367</option><option value='726'>726/1367</option><option value='727'>727/1367</option><option value='728'>728/1367</option><option value='729'>729/1367</option><option value='730'>730/1367</option><option value='731'>731/1367</option><option value='732'>732/1367</option><option value='733'>733/1367</option><option value='734'>734/1367</option><option value='735'>735/1367</option><option value='736'>736/1367</option><option value='737'>737/1367</option><option value='738'>738/1367</option><option value='739'>739/1367</option><option value='740'>740/1367</option><option value='741'>741/1367</option><option value='742'>742/1367</option><option value='743'>743/1367</option><option value='744'>744/1367</option><option value='745'>745/1367</option><option value='746'>746/1367</option><option value='747'>747/1367</option><option value='748'>748/1367</option><option value='749'>749/1367</option><option value='750'>750/1367</option><option value='751'>751/1367</option><option value='752'>752/1367</option><option value='753'>753/1367</option><option value='754'>754/1367</option><option value='755'>755/1367</option><option value='756'>756/1367</option><option value='757'>757/1367</option><option value='758'>758/1367</option><option value='759'>759/1367</option><option value='760'>760/1367</option><option value='761'>761/1367</option><option value='762'>762/1367</option><option value='763'>763/1367</option><option value='764'>764/1367</option><option value='765'>765/1367</option><option value='766'>766/1367</option><option value='767'>767/1367</option><option value='768'>768/1367</option><option value='769'>769/1367</option><option value='770'>770/1367</option><option value='771'>771/1367</option><option value='772'>772/1367</option><option value='773'>773/1367</option><option value='774'>774/1367</option><option value='775'>775/1367</option><option value='776'>776/1367</option><option value='777'>777/1367</option><option value='778'>778/1367</option><option value='779'>779/1367</option><option value='780'>780/1367</option><option value='781'>781/1367</option><option value='782'>782/1367</option><option value='783'>783/1367</option><option value='784'>784/1367</option><option value='785'>785/1367</option><option value='786'>786/1367</option><option value='787'>787/1367</option><option value='788'>788/1367</option><option value='789'>789/1367</option><option value='790'>790/1367</option><option value='791'>791/1367</option><option value='792'>792/1367</option><option value='793'>793/1367</option><option value='794'>794/1367</option><option value='795'>795/1367</option><option value='796'>796/1367</option><option value='797'>797/1367</option><option value='798'>798/1367</option><option value='799'>799/1367</option><option value='800'>800/1367</option><option value='801'>801/1367</option><option value='802'>802/1367</option><option value='803'>803/1367</option><option value='804'>804/1367</option><option value='805'>805/1367</option><option value='806'>806/1367</option><option value='807'>807/1367</option><option value='808'>808/1367</option><option value='809'>809/1367</option><option value='810'>810/1367</option><option value='811'>811/1367</option><option value='812'>812/1367</option><option value='813'>813/1367</option><option value='814'>814/1367</option><option value='815'>815/1367</option><option value='816'>816/1367</option><option value='817'>817/1367</option><option value='818'>818/1367</option><option value='819'>819/1367</option><option value='820'>820/1367</option><option value='821'>821/1367</option><option value='822'>822/1367</option><option value='823'>823/1367</option><option value='824'>824/1367</option><option value='825'>825/1367</option><option value='826'>826/1367</option><option value='827'>827/1367</option><option value='828'>828/1367</option><option value='829'>829/1367</option><option value='830'>830/1367</option><option value='831'>831/1367</option><option value='832'>832/1367</option><option value='833'>833/1367</option><option value='834'>834/1367</option><option value='835'>835/1367</option><option value='836'>836/1367</option><option value='837'>837/1367</option><option value='838'>838/1367</option><option value='839'>839/1367</option><option value='840'>840/1367</option><option value='841'>841/1367</option><option value='842'>842/1367</option><option value='843'>843/1367</option><option value='844'>844/1367</option><option value='845'>845/1367</option><option value='846'>846/1367</option><option value='847'>847/1367</option><option value='848'>848/1367</option><option value='849'>849/1367</option><option value='850'>850/1367</option><option value='851'>851/1367</option><option value='852'>852/1367</option><option value='853'>853/1367</option><option value='854'>854/1367</option><option value='855'>855/1367</option><option value='856'>856/1367</option><option value='857'>857/1367</option><option value='858'>858/1367</option><option value='859'>859/1367</option><option value='860'>860/1367</option><option value='861'>861/1367</option><option value='862'>862/1367</option><option value='863'>863/1367</option><option value='864'>864/1367</option><option value='865'>865/1367</option><option value='866'>866/1367</option><option value='867'>867/1367</option><option value='868'>868/1367</option><option value='869'>869/1367</option><option value='870'>870/1367</option><option value='871'>871/1367</option><option value='872'>872/1367</option><option value='873'>873/1367</option><option value='874'>874/1367</option><option value='875'>875/1367</option><option value='876'>876/1367</option><option value='877'>877/1367</option><option value='878'>878/1367</option><option value='879'>879/1367</option><option value='880'>880/1367</option><option value='881'>881/1367</option><option value='882'>882/1367</option><option value='883'>883/1367</option><option value='884'>884/1367</option><option value='885'>885/1367</option><option value='886'>886/1367</option><option value='887'>887/1367</option><option value='888'>888/1367</option><option value='889'>889/1367</option><option value='890'>890/1367</option><option value='891'>891/1367</option><option value='892'>892/1367</option><option value='893'>893/1367</option><option value='894'>894/1367</option><option value='895'>895/1367</option><option value='896'>896/1367</option><option value='897'>897/1367</option><option value='898'>898/1367</option><option value='899'>899/1367</option><option value='900'>900/1367</option><option value='901'>901/1367</option><option value='902'>902/1367</option><option value='903'>903/1367</option><option value='904'>904/1367</option><option value='905'>905/1367</option><option value='906'>906/1367</option><option value='907'>907/1367</option><option value='908'>908/1367</option><option value='909'>909/1367</option><option value='910'>910/1367</option><option value='911'>911/1367</option><option value='912'>912/1367</option><option value='913'>913/1367</option><option value='914'>914/1367</option><option value='915'>915/1367</option><option value='916'>916/1367</option><option value='917'>917/1367</option><option value='918'>918/1367</option><option value='919'>919/1367</option><option value='920'>920/1367</option><option value='921'>921/1367</option><option value='922'>922/1367</option><option value='923'>923/1367</option><option value='924'>924/1367</option><option value='925'>925/1367</option><option value='926'>926/1367</option><option value='927'>927/1367</option><option value='928'>928/1367</option><option value='929'>929/1367</option><option value='930'>930/1367</option><option value='931'>931/1367</option><option value='932'>932/1367</option><option value='933'>933/1367</option><option value='934'>934/1367</option><option value='935'>935/1367</option><option value='936'>936/1367</option><option value='937'>937/1367</option><option value='938'>938/1367</option><option value='939'>939/1367</option><option value='940'>940/1367</option><option value='941'>941/1367</option><option value='942'>942/1367</option><option value='943'>943/1367</option><option value='944'>944/1367</option><option value='945'>945/1367</option><option value='946'>946/1367</option><option value='947'>947/1367</option><option value='948'>948/1367</option><option value='949'>949/1367</option><option value='950'>950/1367</option><option value='951'>951/1367</option><option value='952'>952/1367</option><option value='953'>953/1367</option><option value='954'>954/1367</option><option value='955'>955/1367</option><option value='956'>956/1367</option><option value='957'>957/1367</option><option value='958'>958/1367</option><option value='959'>959/1367</option><option value='960'>960/1367</option><option value='961'>961/1367</option><option value='962'>962/1367</option><option value='963'>963/1367</option><option value='964'>964/1367</option><option value='965'>965/1367</option><option value='966'>966/1367</option><option value='967'>967/1367</option><option value='968'>968/1367</option><option value='969'>969/1367</option><option value='970'>970/1367</option><option value='971'>971/1367</option><option value='972'>972/1367</option><option value='973'>973/1367</option><option value='974'>974/1367</option><option value='975'>975/1367</option><option value='976'>976/1367</option><option value='977'>977/1367</option><option value='978'>978/1367</option><option value='979'>979/1367</option><option value='980'>980/1367</option><option value='981'>981/1367</option><option value='982'>982/1367</option><option value='983'>983/1367</option><option value='984'>984/1367</option><option value='985'>985/1367</option><option value='986'>986/1367</option><option value='987'>987/1367</option><option value='988'>988/1367</option><option value='989'>989/1367</option><option value='990'>990/1367</option><option value='991'>991/1367</option><option value='992'>992/1367</option><option value='993'>993/1367</option><option value='994'>994/1367</option><option value='995'>995/1367</option><option value='996'>996/1367</option><option value='997'>997/1367</option><option value='998'>998/1367</option><option value='999'>999/1367</option><option value='1000'>1000/1367</option><option value='1001'>1001/1367</option><option value='1002'>1002/1367</option><option value='1003'>1003/1367</option><option value='1004'>1004/1367</option><option value='1005'>1005/1367</option><option value='1006'>1006/1367</option><option value='1007'>1007/1367</option><option value='1008'>1008/1367</option><option value='1009'>1009/1367</option><option value='1010'>1010/1367</option><option value='1011'>1011/1367</option><option value='1012'>1012/1367</option><option value='1013'>1013/1367</option><option value='1014'>1014/1367</option><option value='1015'>1015/1367</option><option value='1016'>1016/1367</option><option value='1017'>1017/1367</option><option value='1018'>1018/1367</option><option value='1019'>1019/1367</option><option value='1020'>1020/1367</option><option value='1021'>1021/1367</option><option value='1022'>1022/1367</option><option value='1023'>1023/1367</option><option value='1024'>1024/1367</option><option value='1025'>1025/1367</option><option value='1026'>1026/1367</option><option value='1027'>1027/1367</option><option value='1028'>1028/1367</option><option value='1029'>1029/1367</option><option value='1030'>1030/1367</option><option value='1031'>1031/1367</option><option value='1032'>1032/1367</option><option value='1033'>1033/1367</option><option value='1034'>1034/1367</option><option value='1035'>1035/1367</option><option value='1036'>1036/1367</option><option value='1037'>1037/1367</option><option value='1038'>1038/1367</option><option value='1039'>1039/1367</option><option value='1040'>1040/1367</option><option value='1041'>1041/1367</option><option value='1042'>1042/1367</option><option value='1043'>1043/1367</option><option value='1044'>1044/1367</option><option value='1045'>1045/1367</option><option value='1046'>1046/1367</option><option value='1047'>1047/1367</option><option value='1048'>1048/1367</option><option value='1049'>1049/1367</option><option value='1050'>1050/1367</option><option value='1051'>1051/1367</option><option value='1052'>1052/1367</option><option value='1053'>1053/1367</option><option value='1054'>1054/1367</option><option value='1055'>1055/1367</option><option value='1056'>1056/1367</option><option value='1057'>1057/1367</option><option value='1058'>1058/1367</option><option value='1059'>1059/1367</option><option value='1060'>1060/1367</option><option value='1061'>1061/1367</option><option value='1062'>1062/1367</option><option value='1063'>1063/1367</option><option value='1064'>1064/1367</option><option value='1065'>1065/1367</option><option value='1066'>1066/1367</option><option value='1067'>1067/1367</option><option value='1068'>1068/1367</option><option value='1069'>1069/1367</option><option value='1070'>1070/1367</option><option value='1071'>1071/1367</option><option value='1072'>1072/1367</option><option value='1073'>1073/1367</option><option value='1074'>1074/1367</option><option value='1075'>1075/1367</option><option value='1076'>1076/1367</option><option value='1077'>1077/1367</option><option value='1078'>1078/1367</option><option value='1079'>1079/1367</option><option value='1080'>1080/1367</option><option value='1081'>1081/1367</option><option value='1082'>1082/1367</option><option value='1083'>1083/1367</option><option value='1084'>1084/1367</option><option value='1085'>1085/1367</option><option value='1086'>1086/1367</option><option value='1087'>1087/1367</option><option value='1088'>1088/1367</option><option value='1089'>1089/1367</option><option value='1090'>1090/1367</option><option value='1091'>1091/1367</option><option value='1092'>1092/1367</option><option value='1093'>1093/1367</option><option value='1094'>1094/1367</option><option value='1095'>1095/1367</option><option value='1096'>1096/1367</option><option value='1097'>1097/1367</option><option value='1098'>1098/1367</option><option value='1099'>1099/1367</option><option value='1100'>1100/1367</option><option value='1101'>1101/1367</option><option value='1102'>1102/1367</option><option value='1103'>1103/1367</option><option value='1104'>1104/1367</option><option value='1105'>1105/1367</option><option value='1106'>1106/1367</option><option value='1107'>1107/1367</option><option value='1108'>1108/1367</option><option value='1109'>1109/1367</option><option value='1110'>1110/1367</option><option value='1111'>1111/1367</option><option value='1112'>1112/1367</option><option value='1113'>1113/1367</option><option value='1114'>1114/1367</option><option value='1115'>1115/1367</option><option value='1116'>1116/1367</option><option value='1117'>1117/1367</option><option value='1118'>1118/1367</option><option value='1119'>1119/1367</option><option value='1120'>1120/1367</option><option value='1121'>1121/1367</option><option value='1122'>1122/1367</option><option value='1123'>1123/1367</option><option value='1124'>1124/1367</option><option value='1125'>1125/1367</option><option value='1126'>1126/1367</option><option value='1127'>1127/1367</option><option value='1128'>1128/1367</option><option value='1129'>1129/1367</option><option value='1130'>1130/1367</option><option value='1131'>1131/1367</option><option value='1132'>1132/1367</option><option value='1133'>1133/1367</option><option value='1134'>1134/1367</option><option value='1135'>1135/1367</option><option value='1136'>1136/1367</option><option value='1137'>1137/1367</option><option value='1138'>1138/1367</option><option value='1139'>1139/1367</option><option value='1140'>1140/1367</option><option value='1141'>1141/1367</option><option value='1142'>1142/1367</option><option value='1143'>1143/1367</option><option value='1144'>1144/1367</option><option value='1145'>1145/1367</option><option value='1146'>1146/1367</option><option value='1147'>1147/1367</option><option value='1148'>1148/1367</option><option value='1149'>1149/1367</option><option value='1150'>1150/1367</option><option value='1151'>1151/1367</option><option value='1152'>1152/1367</option><option value='1153'>1153/1367</option><option value='1154'>1154/1367</option><option value='1155'>1155/1367</option><option value='1156'>1156/1367</option><option value='1157'>1157/1367</option><option value='1158'>1158/1367</option><option value='1159'>1159/1367</option><option value='1160'>1160/1367</option><option value='1161'>1161/1367</option><option value='1162'>1162/1367</option><option value='1163'>1163/1367</option><option value='1164'>1164/1367</option><option value='1165'>1165/1367</option><option value='1166'>1166/1367</option><option value='1167'>1167/1367</option><option value='1168'>1168/1367</option><option value='1169'>1169/1367</option><option value='1170'>1170/1367</option><option value='1171'>1171/1367</option><option value='1172'>1172/1367</option><option value='1173'>1173/1367</option><option value='1174'>1174/1367</option><option value='1175'>1175/1367</option><option value='1176'>1176/1367</option><option value='1177'>1177/1367</option><option value='1178'>1178/1367</option><option value='1179'>1179/1367</option><option value='1180'>1180/1367</option><option value='1181'>1181/1367</option><option value='1182'>1182/1367</option><option value='1183'>1183/1367</option><option value='1184'>1184/1367</option><option value='1185'>1185/1367</option><option value='1186'>1186/1367</option><option value='1187'>1187/1367</option><option value='1188'>1188/1367</option><option value='1189'>1189/1367</option><option value='1190'>1190/1367</option><option value='1191'>1191/1367</option><option value='1192'>1192/1367</option><option value='1193'>1193/1367</option><option value='1194'>1194/1367</option><option value='1195'>1195/1367</option><option value='1196'>1196/1367</option><option value='1197'>1197/1367</option><option value='1198'>1198/1367</option><option value='1199'>1199/1367</option><option value='1200'>1200/1367</option><option value='1201'>1201/1367</option><option value='1202'>1202/1367</option><option value='1203'>1203/1367</option><option value='1204'>1204/1367</option><option value='1205'>1205/1367</option><option value='1206'>1206/1367</option><option value='1207'>1207/1367</option><option value='1208'>1208/1367</option><option value='1209'>1209/1367</option><option value='1210'>1210/1367</option><option value='1211'>1211/1367</option><option value='1212'>1212/1367</option><option value='1213'>1213/1367</option><option value='1214'>1214/1367</option><option value='1215'>1215/1367</option><option value='1216'>1216/1367</option><option value='1217'>1217/1367</option><option value='1218'>1218/1367</option><option value='1219'>1219/1367</option><option value='1220'>1220/1367</option><option value='1221'>1221/1367</option><option value='1222'>1222/1367</option><option value='1223'>1223/1367</option><option value='1224'>1224/1367</option><option value='1225'>1225/1367</option><option value='1226'>1226/1367</option><option value='1227'>1227/1367</option><option value='1228'>1228/1367</option><option value='1229'>1229/1367</option><option value='1230'>1230/1367</option><option value='1231'>1231/1367</option><option value='1232'>1232/1367</option><option value='1233'>1233/1367</option><option value='1234'>1234/1367</option><option value='1235'>1235/1367</option><option value='1236'>1236/1367</option><option value='1237'>1237/1367</option><option value='1238'>1238/1367</option><option value='1239'>1239/1367</option><option value='1240'>1240/1367</option><option value='1241'>1241/1367</option><option value='1242'>1242/1367</option><option value='1243'>1243/1367</option><option value='1244'>1244/1367</option><option value='1245'>1245/1367</option><option value='1246'>1246/1367</option><option value='1247'>1247/1367</option><option value='1248'>1248/1367</option><option value='1249'>1249/1367</option><option value='1250'>1250/1367</option><option value='1251'>1251/1367</option><option value='1252'>1252/1367</option><option value='1253'>1253/1367</option><option value='1254'>1254/1367</option><option value='1255'>1255/1367</option><option value='1256'>1256/1367</option><option value='1257'>1257/1367</option><option value='1258'>1258/1367</option><option value='1259'>1259/1367</option><option value='1260'>1260/1367</option><option value='1261'>1261/1367</option><option value='1262'>1262/1367</option><option value='1263'>1263/1367</option><option value='1264'>1264/1367</option><option value='1265'>1265/1367</option><option value='1266'>1266/1367</option><option value='1267'>1267/1367</option><option value='1268'>1268/1367</option><option value='1269'>1269/1367</option><option value='1270'>1270/1367</option><option value='1271'>1271/1367</option><option value='1272'>1272/1367</option><option value='1273'>1273/1367</option><option value='1274'>1274/1367</option><option value='1275'>1275/1367</option><option value='1276'>1276/1367</option><option value='1277'>1277/1367</option><option value='1278'>1278/1367</option><option value='1279'>1279/1367</option><option value='1280'>1280/1367</option><option value='1281'>1281/1367</option><option value='1282'>1282/1367</option><option value='1283'>1283/1367</option><option value='1284'>1284/1367</option><option value='1285'>1285/1367</option><option value='1286'>1286/1367</option><option value='1287'>1287/1367</option><option value='1288'>1288/1367</option><option value='1289'>1289/1367</option><option value='1290'>1290/1367</option><option value='1291'>1291/1367</option><option value='1292'>1292/1367</option><option value='1293'>1293/1367</option><option value='1294'>1294/1367</option><option value='1295'>1295/1367</option><option value='1296'>1296/1367</option><option value='1297'>1297/1367</option><option value='1298'>1298/1367</option><option value='1299'>1299/1367</option><option value='1300'>1300/1367</option><option value='1301'>1301/1367</option><option value='1302'>1302/1367</option><option value='1303'>1303/1367</option><option value='1304'>1304/1367</option><option value='1305'>1305/1367</option><option value='1306'>1306/1367</option><option value='1307'>1307/1367</option><option value='1308'>1308/1367</option><option value='1309'>1309/1367</option><option value='1310'>1310/1367</option><option value='1311'>1311/1367</option><option value='1312'>1312/1367</option><option value='1313'>1313/1367</option><option value='1314'>1314/1367</option><option value='1315'>1315/1367</option><option value='1316'>1316/1367</option><option value='1317'>1317/1367</option><option value='1318'>1318/1367</option><option value='1319'>1319/1367</option><option value='1320'>1320/1367</option><option value='1321'>1321/1367</option><option value='1322'>1322/1367</option><option value='1323'>1323/1367</option><option value='1324'>1324/1367</option><option value='1325'>1325/1367</option><option value='1326'>1326/1367</option><option value='1327'>1327/1367</option><option value='1328'>1328/1367</option><option value='1329'>1329/1367</option><option value='1330'>1330/1367</option><option value='1331'>1331/1367</option><option value='1332'>1332/1367</option><option value='1333'>1333/1367</option><option value='1334'>1334/1367</option><option value='1335'>1335/1367</option><option value='1336'>1336/1367</option><option value='1337'>1337/1367</option><option value='1338'>1338/1367</option><option value='1339'>1339/1367</option><option value='1340'>1340/1367</option><option value='1341'>1341/1367</option><option value='1342'>1342/1367</option><option value='1343'>1343/1367</option><option value='1344'>1344/1367</option><option value='1345'>1345/1367</option><option value='1346'>1346/1367</option><option value='1347'>1347/1367</option><option value='1348'>1348/1367</option><option value='1349'>1349/1367</option><option value='1350'>1350/1367</option><option value='1351'>1351/1367</option><option value='1352'>1352/1367</option><option value='1353'>1353/1367</option><option value='1354'>1354/1367</option><option value='1355'>1355/1367</option><option value='1356'>1356/1367</option><option value='1357'>1357/1367</option><option value='1358'>1358/1367</option><option value='1359'>1359/1367</option><option value='1360'>1360/1367</option><option value='1361'>1361/1367</option><option value='1362'>1362/1367</option><option value='1363'>1363/1367</option><option value='1364'>1364/1367</option><option value='1365'>1365/1367</option><option value='1366'>1366/1367</option><option value='1367'>1367/1367</option></select>页&nbsp;&nbsp;&nbsp;<A href="javascript:gotoCurrentPage('2')">下一页</A>&nbsp;&nbsp;&nbsp;<A href="javascript:gotoCurrentPage('1367')">尾页</A>
<script language="javascript">
function ResumeError(){
 return true;
}window.onerror = ResumeError;
function gotoCurrentPage(pageNo) {
if(pageNo=='1')
window.location="Column.shtml?p5=28";
else
window.location="Column.shtml?p5=28&p7="+pageNo;
}
</script></form></td><tr></table></td></tr></table>
<!--栏目稿件分页列表结束--></td>
         
          </tr>
        </table></td>
      </tr>
    </table></td>
    <td width="7" valign="top">&nbsp;</td>
    <td width="242" valign="top"><table width="100%" border="0" align="center" cellpadding="0" cellspacing="0">
      <tr>
        <td height="57"><img src="resource/images/djxlyw/m1_05.jpg" width="242" height="57" /></td>
      </tr>
    </table>
      <table width="100%" border="0" align="center" cellpadding="0" cellspacing="0" background="resource/images/djxlyw/m21.jpg" style="margin-top:8px">
        
        <tr>
          <td valign="top"><table width="100%" border="0" align="center" cellpadding="0" cellspacing="0" background="resource/images/djxlyw/m1_10.jpg" style="background-repeat:repeat-x">
            <tr>
              <td height="495" valign="top" background="resource/images/djxlyw/m5.jpg" style="background-position:bottom; background-repeat:repeat-x "><table width="100%" border="0" align="center" cellpadding="0" cellspacing="0">
                <tr>
                  <td height="34" background="resource/images/djxlyw/m1_09.jpg">&nbsp;</td>
                </tr>
                <tr>
                  <td height="5"></td>
                </tr>
                                <tr>
                  <td height="46" align="center" background="resource/images/djxlyw/yongyong.gif" style="background-position:center; background-repeat:no-repeat"><span><a href="Column.shtml?p5=101" class="lanmu" id="columnH_101">图片新闻</a></span></td>
                </tr>
                <tr>
                  <td height="46" align="center" background="resource/images/djxlyw/yongyong.gif" style="background-position:center; background-repeat:no-repeat"><span><a href="Column.shtml?p5=26" class="lanmu" id="columnH_26">旅游快报</a></span></td>
                </tr>
                <tr>
                  <td height="46" align="center" background="resource/images/djxlyw/yongyong.gif" style="background-position:center; background-repeat:no-repeat"><span><a href="Column.shtml?p5=27" class="lanmu" id="columnH_27">行业动态</a></span></td>
                </tr>
                <tr>
                  <td height="46" align="center" background="resource/images/djxlyw/yongyong.gif" style="background-position:center; background-repeat:no-repeat"><span><a href="Column.shtml?p5=28" class="lanmu" id="columnH_28">地市动态</a></span></td>
                </tr>
                <tr>
                  <td height="46" align="center" background="resource/images/djxlyw/yongyong.gif" style="background-position:center; background-repeat:no-repeat"><span><a href="Column.shtml?p5=3520" class="lanmu" id="columnH_3520">委旅游快报汇编</a></span></td>
                </tr>
                <tr>
                  <td height="46" align="center" background="resource/images/djxlyw/yongyong.gif" style="background-position:center; background-repeat:no-repeat"><span><a href="Column.shtml?p5=3527" class="lanmu" id="columnH_3527">一句话工作动态</a></span></td>
                </tr>
                <tr>
                  <td height="46" align="center" background="resource/images/djxlyw/yongyong.gif" style="background-position:center; background-repeat:no-repeat"><span><a href="Column.shtml?p5=3550" class="lanmu" id="columnH_3550">新闻发布会</a></span></td>
                </tr>
                <tr>
                  <td height="46" align="center" background="resource/images/djxlyw/yongyong.gif" style="background-position:center; background-repeat:no-repeat"><span><a href="Column.shtml?p5=3509" class="lanmu" id="columnH_3509">国务院重要政策信息</a></span></td>
                </tr>
                <tr>
                  <td height="46" align="center" background="resource/images/djxlyw/yongyong.gif" style="background-position:center; background-repeat:no-repeat"><span><a href="Column.shtml?p5=721" class="lanmu" id="columnH_721">通知公告</a></span></td>
                </tr>  
                <tr>
                  <td height="5"></td>
                </tr>
              </table></td>
            </tr>
          </table></td>
        </tr>
      </table></td>
  </tr>
</table>
</div>
</div>
<div id=footer>
<div class=frielink><SPAN>友情链接</SPAN> 
<Select onchange=javascript:window.open(this.options[this.selectedIndex].value);this.selectedIndex=0 id=Select1 size=1 name=select1> 
<Option selected>—省直政府门户网站—</Option>  
<option value="http://www.jxdpc.gov.cn/">省发展和改革委员会</option> 
<option value="http://www.jxciit.gov.cn">省工业和信息化委员会</option> 
<option value="http://www.jxf.gov.cn/">省财政厅</option> 
<option value="http://www.jxhrss.gov.cn/">省人力资源和社会保障厅</option> 
<option value="http://www.jxaudit.gov.cn/">省审计厅</option> 
<option value="http://www.jxstj.gov.cn/">省统计局</option> 
<option value="http://www.jxdaj.gov.cn/">省档案局</option> 
<option value="http://www.jx-n-tax.gov.cn/">省国税局</option> 
<option value="http://www.jxds.gov.cn/">省地税局</option> 
<option value="http://www.jxgzw.gov.cn/">省国资委</option> 
<option value="http://www.jxfazhi.gov.cn/">省法制办</option> 
<option value="http://www.jxga.gov.cn/">省公安厅</option> 
<option value="http://www.jxdi.gov.cn/">省监察厅</option> 
<option value="http://www.jxsf.gov.cn/">省司法厅</option>
<option value="http://www.jxmzw.gov.cn/">省民政厅</option> 
<option value="http://www.jxbb.gov.cn/">省编办</option> 
<option value="http://www.jxbm.gov.cn/">省国家保密局</option>
<option value="http://www.jxzj.gov.cn/">省质量技术监督局</option> 
<option value="http://www.jxmkaqjc.gov.cn/">省煤矿安全监察局</option> 
<option value="http://www.jxsafety.gov.cn/">省安全生产监督管理局</option> 
<option value="http://www.jxjt.gov.cn/">省交通运输厅</option> 
<option value="http://www.jxjst.gov.cn/">省住房和城乡建设厅</option> 
<option value="http://www.jxepb.gov.cn/">省环境保护厅</option> 
<option value="http://www.jxgfgb.gov.cn/">省国防科工办</option> <option value="http://www.jxrf.gov.cn/">省人防办</option> 
<option value="http://www.jxca.gov.cn/">省通信管理局</option> 
<option value="http://www.jx.sgcc.com.cn">省电力公司</option> 
<option value="http://jx.spb.gov.cn/">省邮政管理局</option> 
<option value="http://www.jxdkj.gov.cn/">省地质矿产勘查开发局</option> 
<option value="http://www.hgydzj.jx.cn/">省核工业地质局</option> 
<option value="http://www.jxcehui.gov.cn/">省测绘局</option> 
<option value="http://www.nctlj.com.cn/">南昌铁路局</option> 
<option value="http://www.jxdoftec.gov.cn/">省商务厅</option> 
<option value="http://www.jxwqb.gov.cn/">省外事侨务办</option> 
<option value="http://www.jxta.gov.cn/">省旅发委</option> 
<option value="http://nanchang.customs.gov.cn/">南昌海关</option> 
<option value="http://www.jxciq.gov.cn/">省出入境检验检疫局</option> 
<option value="http://www.jxmtdzj.com/">省煤田地质局</option> 
<option value="http://www.jxysdzkcj.gov.cn/">省有色地质勘查局</option> 
<option value="http://www.jxagri.gov.cn/">省农业厅</option> 
<option value="http://www.jxly.gov.cn/">省林业厅</option> 
<option value="http://www.jxsl.gov.cn/">省水利厅</option> 
<option value="http://www.jxgtt.gov.cn/">省国土资源厅</option> 
<option value="http://www.jxjrb.gov.cn">省政府金融办</option> 
<option value="http://www.weather.org.cn/">省气象局</option> 
<option value="http://www.jxdz.gov.cn/">省地震局</option> <option value="http://www.jxaic.gov.cn/">省工商局</option> 
<option value="http://www.jxgrain.gov.cn">省粮食局</option> 
<option value="http://www.jxfpym.gov.cn/">省扶贫和移民办</option> 
<option value="http://www.jxcoop.gov.cn/">省供销合作社</option> 
<option value="http://www.jxnk.org.cn/">省农垦办</option> 
<option value="http://nanchang.pbc.gov.cn">人民银行南昌中心支行</option> <option value="http://www.jxstc.gov.cn/">省科技厅</option> 
<option value="http://www.jxedu.gov.cn/">省教育厅</option> 
<option value="http://www.jxsport.gov.cn/">省体育局</option> 
<option value="http://www.jxwst.gov.cn/">省卫生计生委</option> 
<option value="http://www.jxfda.gov.cn/">省食品药品监督管理局</option> 
<option value="http://www.jxwh.gov.cn/">省文化厅</option> 
<option value="http://www.jxmzj.gov.cn/">省民族宗教事务局</option> 
<option value="http://www.jxxgj.gov.cn/">省新闻出版广电局</option> 
<option value="http://www.jxgh.org.cn/">省总工会</option> 
<option value="http://www.jxwomen.org.cn/">省妇联</option> 
<option value="http://www.jxkx.gov.cn">省科协</option> 
<option value="http://www.jxql.org">省侨联</option> 
<option value="http://www.jxyouth.org.cn">省团省委</option> 
<option value="http://www.jxdpf.gov.cn/">省残联</option> <option value="http://www.jxsky.org.cn">省社科院</option> 
<option value="http://www.jxss.net.cn/">省社联</option> 
<option value="http://www.jxfic.gov.cn/">省工商业联合会</option> 
<option value="http://www.jx-xinfang.gov.cn">省信访局</option> 
<option value="http://www.jxtyzx.org/">省委统战部</option> 
<option value="http://www.jxyj.org.cn/">省援疆办</option> 
<option value="http://www.jxflac.com">省文联</option> 
<option value="http://www.jxgjl.com/">省工业经济联合会</option> 
<option value="http://www.chinajz.gov.cn/">省减灾委员会</option> 
<option value="http://www.jxszjb.gov.cn/">省驻京办</option> 
<option value="http://www.jiangxi.gov.cn/zhb/">省驻沪办</option> 
<option value="http://www.jxjgdj.gov.cn/">省机关党建</option> 
<option value="http://www.jxjgj.gov.cn/">省机关事务管理局</option> 
<option value="http://www.jxcs.org.cn">江西慈善网</option> 
</Select> 
<Select onchange=javascript:window.open(this.options[this.selectedIndex].value);this.selectedIndex=0;this.selectedIndex=0 id=Select2 size=1 name=select2> 
  <Option selected>—各省（市）旅游网站—</Option> 
  <Option value=http://www.hljtour.gov.cn/>黑龙江</Option> 
  <Option value=http://www.jstour.gov.cn/>江苏</Option> 
  <Option value=http://www.jlta.gov.cn/>吉林</Option> 
  <Option value=http://www.lntour.gov.cn/>辽宁</Option> 
  <Option value=http://tourzj.gov.cn/Default.aspx>浙江</Option> 
  <Option value=http://www.hubeitour.gov.cn/>湖北</Option> 
  <Option value=http://www.hnt.gov.cn>湖南</Option> 
  <Option value=http://www.ahta.com.cn>安徽</Option> 
  <Option value=http://www.gdta.gov.cn/default.html>广东</Option> 
  <Option value=http://www.scta.gov.cn>四川</Option> 
  <Option value=http://www.gz-travel.net>贵州</Option> 
  <Option value=http://www.fjta.com>福建</Option> 
  <Option value=http://www.gxta.gov.cn>广西</Option> 
  <Option value=http://www.visithainan.gov.cn/>海南</Option> 
  <Option value=http://www.bjta.gov.cn>北京</Option> 
  <Option value=http://lyw.sh.gov.cn/lyj_website/HTML/DefaultSite/portal/index/index.htm>上海</Option> 
  <Option value=http://www.tjtour.cn/>天津</Option> 
  <Option value=http://www.cqta.gov.cn/>重庆</Option> 
  <Option value=http://www.hebeitour.com.cn>河北</Option> 
  <Option value=http://www.hnta.cn>河南</Option> 
  <Option value=http://www.sdta.gov.cn>山东</Option> 
  <Option value=http://www.shanxitourismbureau.cn/zh/index.shtml>山西</Option> 
  <Option value=http://www.sxtour.com>陕西</Option> 
  <Option value=http://www.gsta.gov.cn/>甘肃</Option> 
  <Option value=http://www.nxta.gov.cn/>宁夏</Option> 
  <Option value=http://www.qhly.gov.cn/>青海</Option> 
  <Option value=http://www.xinjiangtour.gov.cn>新疆</Option> 
  <Option value=http://www.nmgtour.gov.cn>内蒙</Option> 
  <Option value=http://www.ynta.gov.cn/index.aspx>云南</Option> 
  <Option value=http://www.tibettour.com.cn>西藏</Option> 
  <Option value=http://www.discoverhongkong.com/china/index.jsp>香港</Option>
</Select> 
<Select onchange=javascript:window.open(this.options[this.selectedIndex].value) id=Select2 size=1 name=select3> 
  <Option selected>—各设区市旅游部门—</Option> 
  <Option value="http://www.nctour.com.cn/ ">南昌市旅游发展委员会</Option> 
  <Option value=http://www.jjta.gov.cn/>九江市旅游发展委员会</Option> 
  <Option value=http://www.gzLyw.com.cn>赣州市旅游发展委员会</Option> 
  <Option value=http://www.srta.gov.cn/>上饶市旅游发展委员会</Option> 
  <Option value=www.yctravel.gov.cn>宜春市旅游发展委员会</Option> 
  <Option value=www.jxfzly.gov.cn/>抚州市旅游发展委员会</Option> 
  <Option value=http://www.jata.gov.cn/>吉安市旅游发展委员会</Option> 
  <Option value=http://www.yttour.gov.cn/>鹰潭市旅游发展委员会</Option> 
  <Option value=http://www.jxpxly.ccoo.cn/>萍乡市旅游发展委员会</Option> 
  <Option value=http://www.jxxyly.gov.cn>新余市旅游发展委员会</Option> 
  <Option value=http://www.jdzta.gov.cn/>景德镇市旅游发展委员会</Option>
</Select> 
<Select onchange=javascript:window.open(this.options[this.selectedIndex].value);this.selectedIndex=0 id=Select2 size=1 name=select4> 
  <Option selected>—友情链接—</Option> 
  <Option value=http://www.ctrip.com/>携程</Option> 
  <Option value=http://www.tuniu.com/http://jxlalk.com/>途牛</Option> 
  <Option value=http://www.elong.com/>艺龙</Option> 
  <Option value=http://www.qunar.com/>去哪儿</Option> 
  <Option value=http://www.lvmama.com/>驴妈妈旅游</Option> 
  <Option value=https://www.alitrip.com/>阿里旅游</Option> 
  <Option value=https://www.ly.com/>同程旅游</Option> 
  <Option value=https://www.tripadvisor.cn/>猫途鹰</Option> 
  <Option value=http://www.mafengwo.cn/>蚂蜂窝</Option> 
  <Option value=http://www.qyer.com/>穷游网</Option>
</Select> </div>
<div class=ftnav><A href="News.shtml?p5=86627">联系我们</A> | <A onclick="SetHome(this,'http://www.jxta.gov.cn/')">设为首页</A> | <A onclick=AddFavorite(window.location,document.title)>加入收藏</A> | <A href="News.shtml?p5=86629">隐私声明</A> | <A href="News.shtml?p5=86631">使用帮助</A> | <A href="Column.shtml?p5=74">网站导航</A> </div>
<P>主办：江西省旅游发展委员会 承办：江西省旅游信息和培训中心</P>
<P>江西省旅游发展委员会 版权所有 赣ICP备09007107号</P>
<SCRIPT type=text/javascript>document.write(unescape("%3Cspan id='_ideConac' %3E%3C/span%3E%3Cscript src='http://dcs.conac.cn/js/15/000/0000/41260630/CA150000000412606300005.js' type='text/javascript'%3E%3C/script%3E"));</SCRIPT>
</div>
<SCRIPT type=text/javascript>
//  加入收藏 <a onclick="AddFavorite(window.location,document.title)">加入收藏</a>
function AddFavorite(sURL, sTitle)
{
    try
    {
        window.external.addFavorite(sURL, sTitle);
    }
    catch (e)
    {
        try
        {
            window.sidebar.addPanel(sTitle, sURL, "");
        }
        catch (e)
        {
            alert("加入收藏失败，请使用Ctrl+D进行添加");
        }
    }
}
//设为首页 
function SetHome(obj,url){
    try{
        obj.style.behavior='url(#default#homepage)';
        obj.setHomePage(url);
    }catch(e){
        if(window.netscape){
            try{
                netscape.security.PrivilegeManager.enablePrivilege("UniversalXPConnect");
            }catch(e){
                alert("抱歉，此操作被浏览器拒绝！请在浏览器地址栏输入“about:config”并回车然后将[signed.applets.codebase_principal_support]设置为'true'");
            }
        }else{
            alert("抱歉，您所使用的浏览器无法完成此操作。您需要手动将【"+url+"】设置为首页。");
        }
    }
}
</SCRIPT>
<SPAN id=_ideConac></SPAN>
</body>
</html>
																							
																							
																							
																							
																							
"""

doc2 = """

																																																<!DOCTYPE html PUBLIC "-//W3C//DTD XHTML 1.0 Transitional//EN" "http://www.w3.org/TR/xhtml1/DTD/xhtml1-transitional.dtd">
<html xmlns="http://www.w3.org/1999/xhtml">
<head>
<meta http-equiv="Content-Type" content="text/html; charset=utf-8" />
 <meta http-equiv="X-UA-Compatible" content="IE=Edge,chrome=1 ">
<title>江西旅游网_旅游快报</title>
<link href="/css/zh_cn/DefaultSkin.css" type=text/css rel=stylesheet>
<style type="text/css">
<!--
.neiye  {
	font-size: 12px;
	color: #000000;
	text-decoration: none;
	
}
.dangqian  {
	font-size: 12px;
	color: #005ba1;
	text-decoration: none;
}
.lanmu {
	font-family:'Microsoft Yahei',"\5b8b\4f53", sans-serif; 
	font-size: 16px;
	/*font-weight: bold;*/
	color: #0065b3;
	text-decoration: none;
}
.lanmudao {
	font-size: 16px;
	font-weight: bold;
	color: #ffffff;
	text-decoration: none;
}

-->
</style>

<SCRIPT language=javascript src="/resource/uploadfile/zh_cn/gb20170801/js/jquery.js"></SCRIPT>
<SCRIPT language=javascript src="/resource/uploadfile/zh_cn/gb20170801/js/kxbdMarquee.js"></SCRIPT>
<SCRIPT language=javascript src="/resource/uploadfile/zh_cn/gb20170801/js/wza.js"></SCRIPT>
<script type="text/javascript" src="/resource/uploadfile/zh_cn/gb20170801/js/swfobject_modified.js"></script>
</head>

<body>
<STYLE type=text/css>
  #nav{ background: url('/resource/uploadfile/zh_cn/navbar.png') no-repeat top center;position:absolute;top:289px;left:0;right:0 }
    .Qcenter{ width: 1030px; height: 70px; margin: 0 auto;  }
      .Qul{ margin-left: 22px; margin-top: 39px;  height: 59px; }
        .Qul .Qlib{ float: left; height: 59px; margin-right: 1px; position: relative; overflow:visible; }
        .Qul .Qlib a{ display: block; height: 30px; font-size: 16px; color: #fff; font-family: "微软雅黑";}
          #Qli1{ width: 168px; background: url('/resource/uploadfile/zh_cn/Qindex.png') no-repeat center; }
          #Qli2{ width: 182px; background: url('/resource/uploadfile/zh_cn/Qlydt.png') no-repeat center; }
          #Qli3{ width: 219px; background: url('/resource/uploadfile/zh_cn/Qlvwjj.png') no-repeat center; }
          #Qli4{ width: 204px; background: url('/resource/uploadfile/zh_cn/Qzwgk.png') no-repeat center; }
          #Qli5{ width: 208px; background: url('/resource/uploadfile/zh_cn/Qbsfw.png') no-repeat center; }
          .Qul .Qlib:hover #Qli1{ width: 168px; background: url('/resource/uploadfile/zh_cn/Qindex2.png') no-repeat center;  }
          .Qul .Qlib:hover #Qli2{ width: 182px; background: url('/resource/uploadfile/zh_cn/Qlydt2.png') no-repeat center;}
          .Qul .Qlib:hover #Qli3{ width: 219px; background: url('/resource/uploadfile/zh_cn/Qlvwjj2.png') no-repeat center;}
          .Qul .Qlib:hover #Qli4{ width: 204px; background: url('/resource/uploadfile/zh_cn/Qzwgk2.png') no-repeat center; }
          .Qul .Qlib:hover #Qli5{ width: 208px; background: url('/resource/uploadfile/zh_cn/Qbsfw2.png') no-repeat center;}
        .Qdiv{ width: 182px; min-height:255px; position: absolute; z-index:10000; font-size: 0; margin-left: -40px; display: none; }
        .Qdiv1{ top: 44px; left: 39px; }
        .Qdiv2{ top: 44px; left: 56px; }
        .Qdiv3{ top: 44px; left: 53px; }
          .Qdiv li,.Qdiv2 li,.Qdiv3 li{ height: 39px; line-height: 38px; text-align: center; margin: 0; padding: 0; background: url('/resource/uploadfile/zh_cn/Qcen.png') repeat-y center; }
          .Qimg{ margin-top: -1px; }
        .Qul .Qlib:hover .Qdiv{ display: block; }
</STYLE>
<div class=headWrap>
<div class=top>
<div class=center>
<div class=fle>
<P>欢迎来到江西省旅游委员会政务网<SPAN id=weltime>
<SCRIPT language=javascript>
    $(function(){
    var Mdate = new Date();
    var Mnow = "";
    Mnow = Mdate.getFullYear()+"年"; 
    Mnow = Mnow + (Mdate.getMonth()+1)+"月"; 
    Mnow = Mnow + Mdate.getDate()+"日";
    var Week = ['日','一','二','三','四','五','六'];
    Mnow = Mnow + " 星期" + Week[Mdate.getDay()];
    $("#weltime").text(Mnow); 
    });
             </SCRIPT>
 </SPAN></P></div>
<div class=fri><A href="Column.shtml?p5=3474">快速通道</A> 丨 <A onclick=OpentoolBar(); href="javascript:void(0);">无障碍服务</A> 丨 <A href="Column.shtml?p5=14">一站式服务</A> | <A href="http://mail.jxta.gov.cn" target=_blank>邮箱登录</A><!-- &nbsp;&nbsp; <A href="http://tour.jxnews.com.cn/">江西旅游网</A>&nbsp;&nbsp;<A href="http://www.jxhsly.cn/">江西红色旅游网</A> --> </div></div></div>
<div id=header>
<div class=banner>
<object id="FlashID" classid="clsid:D27CDB6E-AE6D-11cf-96B8-444553540000" width="1002" height="326">
  <param name="movie" value="/resource/uploadfile/zh_cn/gb20170801/flash.swf" />
  <param name="quality" value="high" />
  <param name="wmode" value="Transparent" />
  <param name="swfversion" value="8.0.35.0" />
  <!-- 此 param 标签提示使用 Flash Player 6.0 r65 和更高版本的用户下载最新版本的 Flash Player。如果您不想让用户看到该提示，请将其删除。 -->
  <param name="expressinstall" value="Scripts/expressInstall.swf" />
  <!-- 下一个对象标签用于非 IE 浏览器。所以使用 IECC 将其从 IE 隐藏。 -->
  <!--[if !IE]>-->
  <object type="application/x-shockwave-flash" data="/resource/uploadfile/zh_cn/gb20170801/flash.swf" width="1002" height="326">
    <!--<![endif]-->
    <param name="quality" value="high" />
    <param name="wmode" value="transparent" />
    <param name="swfversion" value="8.0.35.0" />
    <param name="expressinstall" value="Scripts/expressInstall.swf" />
    <!-- 浏览器将以下替代内容显示给使用 Flash Player 6.0 和更低版本的用户。 -->
    <div>
      <h4>此页面上的内容需要较新版本的 Adobe Flash Player。</h4>
      <p><a href="http://www.adobe.com/go/getflashplayer"><img src="http://www.adobe.com/images/shared/download_buttons/get_flash_player.gif" alt="获取 Adobe Flash Player" width="112" height="33" /></a></p>
    </div>
    <!--[if !IE]>-->
  </object>
  <!--<![endif]-->
</object>
<script type="text/javascript">
swfobject.registerObject("FlashID");
</script></div></div>
<div id="nav" class="nav">
<div class="Qcenter">
<UL class="Qul">
<LI class="Qcurrent Qlib"><A id="Qli1" href="/"></A></LI>
<LI class="Qlib"><A id="Qli2" href="/Column.shtml?p5=13"></A>
<UL class="Qdiv1 Qdiv"><IMG alt="" src="/resource/uploadfile/zh_cn/Qtop.png"> 
<LI><A href="/Column.shtml?p5=101">图片新闻</A> </LI>
<LI><A href="/Column.shtml?p5=26">旅游快报</A> </LI>
<LI><A href="/Column.shtml?p5=28">地市动态</A> </LI>
<LI><A href="/Column.shtml?p5=27">行业动态</A> </LI>
<LI><A href="/Column.shtml?p5=721">通知公告</A> </LI>
<LI><A href="/Column.shtml?p5=3550">新闻发布会</A></LI>
<LI><A href="/Column.shtml?p5=3527">一句话工作动态</A></LI>
<LI><A href="/Column.shtml?p5=3509">国务院重要政策信息</A>  </LI>
<IMG class="Qimg"  alt="" src="/resource/uploadfile/zh_cn/Qbootom.png"></UL></LI>
<LI class="Qlib"><A id="Qli3" href="/Column.shtml?p5=12"></A>
<UL class="Qdiv2 Qdiv"><IMG alt="" src="/resource/uploadfile/zh_cn/Qtop.png"> 
<LI><A href="/Column.shtml?p5=75">办公位置</A> </LI>
<LI><A href="/Column.shtml?p5=76">职能介绍</A> </LI>
<LI><A href="/Column.shtml?p5=77">领导介绍</A> </LI>
<LI><A href="/Column.shtml?p5=3553">兼职委员介绍</A> </LI>
<LI><A href="/Column.shtml?p5=78">机构设置</A> </LI>
<LI><A href="/Column.shtml?p5=704">地市旅游委</A> </LI><IMG class="Qimg"  alt="" src="/resource/uploadfile/zh_cn/Qbootom.png"> </UL></LI>
<LI class="Qlib"><A id="Qli4" href="/Column.shtml?p5=11"></A>
<UL class="Qdiv3 Qdiv"><IMG alt="" src="/resource/uploadfile/zh_cn/Qtop.png"> 
<LI><A href="/Column.shtml?p5=3514">文件通知</A> </LI>
<LI><A href="/Column.shtml?p5=3430">财政公开</A> </LI>
<LI><A href="/Column.shtml?p5=3439">财政预决算</A> </LI>
<LI><A href="/Column.shtml?p5=3437">招标采购</A> </LI>
<LI><A href="/Column.shtml?p5=3440">人事信息</A> </LI>
<LI><A href="/Column.shtml?p5=707">旅游规划</A> </LI>
<LI><A href="/Column.shtml?p5=3488">政策与解读</A> </LI>
<LI><A href="/Column.shtml?p5=16">政策法规</A> </LI>
<LI><A href="/Column.shtml?p5=722">旅游统计</A> </LI>
<LI><A href="/Column.shtml?p5=3599 ">减税降费</A> </LI>
<LI><A href="/Column.shtml?p5=3489">权利责任清单</A>  </LI><IMG class="Qimg"  alt="" src="/resource/uploadfile/zh_cn/Qbootom.png"></UL></LI>
<LI class="Qlib"><A id="Qli5" href="/Column.shtml?p5=708"></A>
<UL class="Qdiv2 Qdiv"><IMG alt="" src="/resource/uploadfile/zh_cn/Qtop.png"> 
<LI><A href="/Column.shtml?p5=709">行政审批</A> </LI>
<LI><A href="/ReferForm.shtml?p5=101">在线咨询</A> </LI>
<LI><A href="http://www.jxzwfww.gov.cn/xzpp/bmfl/slfw_1897/">在线申报</A> </LI>
<LI><A href="/Column.shtml?p5=711">办事指南</A> </LI>
<LI><A href="/Column.shtml?p5=712">在线下载</A> </LI>
<LI><A href="/Column.shtml?p5=3551">整理汇编</A> </LI><IMG class="Qimg" alt="" src="/resource/uploadfile/zh_cn/Qbootom.png"> </UL></LI></UL></div>
</div></div>
<div id="c">
 <div id="container">
<table width="990" border="0" align="center" cellpadding="0" cellspacing="0">
  <tr>
    <td width="752" valign="top"><table width="100%" border="0" align="center" cellpadding="0" cellspacing="0">
      <tr>
        <td height="28" background="resource/images/djxlyw/m1_03.jpg" class="dangqian" style="padding-left:28px; padding-top:4px"><a href='Index.shtml'>首页</a>&nbsp;&nbsp;&nbsp;>>&nbsp;&nbsp;&nbsp;<a href='Column.shtml?p5=13'>旅游动态</a>&nbsp;&nbsp;&nbsp;>>&nbsp;&nbsp;&nbsp;<a href='Column.shtml?p5=26'>旅游快报</a></td>
      </tr>
      <tr>
        <td><table width="100%" border="0" align="center" cellpadding="0" cellspacing="0" background="resource/images/djxlyw/m31.jpg">
          <tr>
            <td height="522" valign="top" background="resource/images/djxlyw/m1_07.jpg" class="neiye" style="background-repeat:repeat-x; padding-left:24px; padding-top:6px; padding-right:5px; line-height:26px"><!--栏目稿件分页列表开始-->
<table width=100% id=Table cellpadding=1 cellspacing=1 align=left>
<tr>
<td width=87%><img src='resource/images/djxlyw/dicon02.gif' border=0>&nbsp;<a href='News.shtml?p5=530937' title='故宫首设旅游综合执法站 游客可在此咨询投诉'  target='_blank' ><font color='0'>故宫首设旅游综合执法站 游客可在此咨询投诉</font></a></td><td width=13%><font color='0'>2017-10-06</font></td></tr>
<tr>
<td width=87%><img src='resource/images/djxlyw/dicon02.gif' border=0>&nbsp;<a href='News.shtml?p5=530940' title='超级黄金周有望带旺香港零售业 这些港股不可错过'  target='_blank' ><font color='0'>超级黄金周有望带旺香港零售业 这些港股不可错过</font></a></td><td width=13%><font color='0'>2017-10-06</font></td></tr>
<tr>
<td width=87%><img src='resource/images/djxlyw/dicon02.gif' border=0>&nbsp;<a href='News.shtml?p5=530934' title='景区火了 游客笑了 村民乐了'  target='_blank' ><font color='0'>景区火了 游客笑了 村民乐了</font></a></td><td width=13%><font color='0'>2017-10-06</font></td></tr>
<tr>
<td width=87%><img src='resource/images/djxlyw/dicon02.gif' border=0>&nbsp;<a href='News.shtml?p5=530555' title='旅游新供给，“玩”出更多幸福感'  target='_blank' ><font color='0'>旅游新供给，“玩”出更多幸福感</font></a></td><td width=13%><font color='0'>2017-10-05</font></td></tr>
<tr>
<td width=87%><img src='resource/images/djxlyw/dicon02.gif' border=0>&nbsp;<a href='News.shtml?p5=530549' title='澳门举行丰富多彩活动庆祝新中国成立68周年'  target='_blank' ><font color='0'>澳门举行丰富多彩活动庆祝新中国成立68周年</font></a></td><td width=13%><font color='0'>2017-10-05</font></td></tr>
<tr>
<td width=87%><img src='resource/images/djxlyw/dicon02.gif' border=0>&nbsp;<a href='News.shtml?p5=530552' title='黄金周，将文明旅游进行到底'  target='_blank' ><font color='0'>黄金周，将文明旅游进行到底</font></a></td><td width=13%><font color='0'>2017-10-05</font></td></tr>
<tr>
<td width=87%><img src='resource/images/djxlyw/dicon02.gif' border=0>&nbsp;<a href='News.shtml?p5=530328' title='“90后”成今年假期出游主力军 旅游自由度高'  target='_blank' ><font color='0'>“90后”成今年假期出游主力军 旅游自由度高</font></a></td><td width=13%><font color='0'>2017-10-04</font></td></tr>
<tr>
<td width=87%><img src='resource/images/djxlyw/dicon02.gif' border=0>&nbsp;<a href='News.shtml?p5=530331' title='新加坡滨海湾花园以璀璨影音迎中秋 展现多元文化'  target='_blank' ><font color='0'>新加坡滨海湾花园以璀璨影音迎中秋 展现多元文化</font></a></td><td width=13%><font color='0'>2017-10-04</font></td></tr>
<tr>
<td width=87%><img src='resource/images/djxlyw/dicon02.gif' border=0>&nbsp;<a href='News.shtml?p5=530325' title='破解旅游淡旺季落差 旅游迈向全域全季全业态'  target='_blank' ><font color='0'>破解旅游淡旺季落差 旅游迈向全域全季全业态</font></a></td><td width=13%><font color='0'>2017-10-04</font></td></tr>
<tr>
<td width=87%><img src='resource/images/djxlyw/dicon02.gif' border=0>&nbsp;<a href='News.shtml?p5=529807' title='黄金周赴鼓浪屿旅游应先购船票'  target='_blank' ><font color='0'>黄金周赴鼓浪屿旅游应先购船票</font></a></td><td width=13%><font color='0'>2017-10-02</font></td></tr>
<tr>
<td width=87%><img src='resource/images/djxlyw/dicon02.gif' border=0>&nbsp;<a href='News.shtml?p5=529810' title='迎国庆“祝福祖国”大花篮点亮天安门'  target='_blank' ><font color='0'>迎国庆“祝福祖国”大花篮点亮天安门</font></a></td><td width=13%><font color='0'>2017-10-02</font></td></tr>
<tr>
<td width=87%><img src='resource/images/djxlyw/dicon02.gif' border=0>&nbsp;<a href='News.shtml?p5=529804' title='著名景区新疆喀纳斯专项治理违建 恢复古村风貌'  target='_blank' ><font color='0'>著名景区新疆喀纳斯专项治理违建 恢复古村风貌</font></a></td><td width=13%><font color='0'>2017-10-02</font></td></tr>
<tr>
<td width=87%><img src='resource/images/djxlyw/dicon02.gif' border=0>&nbsp;<a href='News.shtml?p5=529801' title='内蒙古：开通旅游专列带游客欣赏额济纳胡杨美景'  target='_blank' ><font color='0'>内蒙古：开通旅游专列带游客欣赏额济纳胡杨美景</font></a></td><td width=13%><font color='0'>2017-10-02</font></td></tr>
<tr>
<td width=87%><img src='resource/images/djxlyw/dicon02.gif' border=0>&nbsp;<a href='News.shtml?p5=529474' title='首届中国黄河旅游大会举行 沿黄城市共铸旅游产业'  target='_blank' ><font color='0'>首届中国黄河旅游大会举行 沿黄城市共铸旅游产业</font></a></td><td width=13%><font color='0'>2017-10-01</font></td></tr>
<tr>
<td width=87%><img src='resource/images/djxlyw/dicon02.gif' border=0>&nbsp;<a href='News.shtml?p5=529468' title='中国景区联盟首期沙龙举办 景区托管成话题焦点'  target='_blank' ><font color='0'>中国景区联盟首期沙龙举办 景区托管成话题焦点</font></a></td><td width=13%><font color='0'>2017-10-01</font></td></tr>
<tr><td class='' colspan=2>
<table width="100%"><tr><td class="pagenextclass">&nbsp;</td></tr><tr><td><form name='strongPageNext' id='strongPageNext' action='toto.asp'>
共&nbsp;192页&nbsp;&nbsp;&nbsp;2880&nbsp;条记录&nbsp;&nbsp;&nbsp;当前页:&nbsp;1&nbsp;&nbsp;&nbsp;首页&nbsp;&nbsp;&nbsp;上一页&nbsp;&nbsp;&nbsp;
第<select class="conditionSelectBox" name='pageNo' onChange='javascript:gotoCurrentPage(this.value)'><option value='1' selected='selected' >1/192</option><option value='2'>2/192</option><option value='3'>3/192</option><option value='4'>4/192</option><option value='5'>5/192</option><option value='6'>6/192</option><option value='7'>7/192</option><option value='8'>8/192</option><option value='9'>9/192</option><option value='10'>10/192</option><option value='11'>11/192</option><option value='12'>12/192</option><option value='13'>13/192</option><option value='14'>14/192</option><option value='15'>15/192</option><option value='16'>16/192</option><option value='17'>17/192</option><option value='18'>18/192</option><option value='19'>19/192</option><option value='20'>20/192</option><option value='21'>21/192</option><option value='22'>22/192</option><option value='23'>23/192</option><option value='24'>24/192</option><option value='25'>25/192</option><option value='26'>26/192</option><option value='27'>27/192</option><option value='28'>28/192</option><option value='29'>29/192</option><option value='30'>30/192</option><option value='31'>31/192</option><option value='32'>32/192</option><option value='33'>33/192</option><option value='34'>34/192</option><option value='35'>35/192</option><option value='36'>36/192</option><option value='37'>37/192</option><option value='38'>38/192</option><option value='39'>39/192</option><option value='40'>40/192</option><option value='41'>41/192</option><option value='42'>42/192</option><option value='43'>43/192</option><option value='44'>44/192</option><option value='45'>45/192</option><option value='46'>46/192</option><option value='47'>47/192</option><option value='48'>48/192</option><option value='49'>49/192</option><option value='50'>50/192</option><option value='51'>51/192</option><option value='52'>52/192</option><option value='53'>53/192</option><option value='54'>54/192</option><option value='55'>55/192</option><option value='56'>56/192</option><option value='57'>57/192</option><option value='58'>58/192</option><option value='59'>59/192</option><option value='60'>60/192</option><option value='61'>61/192</option><option value='62'>62/192</option><option value='63'>63/192</option><option value='64'>64/192</option><option value='65'>65/192</option><option value='66'>66/192</option><option value='67'>67/192</option><option value='68'>68/192</option><option value='69'>69/192</option><option value='70'>70/192</option><option value='71'>71/192</option><option value='72'>72/192</option><option value='73'>73/192</option><option value='74'>74/192</option><option value='75'>75/192</option><option value='76'>76/192</option><option value='77'>77/192</option><option value='78'>78/192</option><option value='79'>79/192</option><option value='80'>80/192</option><option value='81'>81/192</option><option value='82'>82/192</option><option value='83'>83/192</option><option value='84'>84/192</option><option value='85'>85/192</option><option value='86'>86/192</option><option value='87'>87/192</option><option value='88'>88/192</option><option value='89'>89/192</option><option value='90'>90/192</option><option value='91'>91/192</option><option value='92'>92/192</option><option value='93'>93/192</option><option value='94'>94/192</option><option value='95'>95/192</option><option value='96'>96/192</option><option value='97'>97/192</option><option value='98'>98/192</option><option value='99'>99/192</option><option value='100'>100/192</option><option value='101'>101/192</option><option value='102'>102/192</option><option value='103'>103/192</option><option value='104'>104/192</option><option value='105'>105/192</option><option value='106'>106/192</option><option value='107'>107/192</option><option value='108'>108/192</option><option value='109'>109/192</option><option value='110'>110/192</option><option value='111'>111/192</option><option value='112'>112/192</option><option value='113'>113/192</option><option value='114'>114/192</option><option value='115'>115/192</option><option value='116'>116/192</option><option value='117'>117/192</option><option value='118'>118/192</option><option value='119'>119/192</option><option value='120'>120/192</option><option value='121'>121/192</option><option value='122'>122/192</option><option value='123'>123/192</option><option value='124'>124/192</option><option value='125'>125/192</option><option value='126'>126/192</option><option value='127'>127/192</option><option value='128'>128/192</option><option value='129'>129/192</option><option value='130'>130/192</option><option value='131'>131/192</option><option value='132'>132/192</option><option value='133'>133/192</option><option value='134'>134/192</option><option value='135'>135/192</option><option value='136'>136/192</option><option value='137'>137/192</option><option value='138'>138/192</option><option value='139'>139/192</option><option value='140'>140/192</option><option value='141'>141/192</option><option value='142'>142/192</option><option value='143'>143/192</option><option value='144'>144/192</option><option value='145'>145/192</option><option value='146'>146/192</option><option value='147'>147/192</option><option value='148'>148/192</option><option value='149'>149/192</option><option value='150'>150/192</option><option value='151'>151/192</option><option value='152'>152/192</option><option value='153'>153/192</option><option value='154'>154/192</option><option value='155'>155/192</option><option value='156'>156/192</option><option value='157'>157/192</option><option value='158'>158/192</option><option value='159'>159/192</option><option value='160'>160/192</option><option value='161'>161/192</option><option value='162'>162/192</option><option value='163'>163/192</option><option value='164'>164/192</option><option value='165'>165/192</option><option value='166'>166/192</option><option value='167'>167/192</option><option value='168'>168/192</option><option value='169'>169/192</option><option value='170'>170/192</option><option value='171'>171/192</option><option value='172'>172/192</option><option value='173'>173/192</option><option value='174'>174/192</option><option value='175'>175/192</option><option value='176'>176/192</option><option value='177'>177/192</option><option value='178'>178/192</option><option value='179'>179/192</option><option value='180'>180/192</option><option value='181'>181/192</option><option value='182'>182/192</option><option value='183'>183/192</option><option value='184'>184/192</option><option value='185'>185/192</option><option value='186'>186/192</option><option value='187'>187/192</option><option value='188'>188/192</option><option value='189'>189/192</option><option value='190'>190/192</option><option value='191'>191/192</option><option value='192'>192/192</option></select>页&nbsp;&nbsp;&nbsp;<A href="javascript:gotoCurrentPage('2')">下一页</A>&nbsp;&nbsp;&nbsp;<A href="javascript:gotoCurrentPage('192')">尾页</A>
<script language="javascript">
function ResumeError(){
 return true;
}window.onerror = ResumeError;
function gotoCurrentPage(pageNo) {
if(pageNo=='1')
window.location="Column.shtml?p5=26";
else
window.location="Column.shtml?p5=26&p7="+pageNo;
}
</script></form></td><tr></table></td></tr></table>
<!--栏目稿件分页列表结束--></td>
          </tr>
        </table></td>
      </tr>
    </table></td>
    <td width="7" valign="top">&nbsp;</td>
    <td width="242" valign="top"><table width="100%" border="0" align="center" cellpadding="0" cellspacing="0">
      <tr>
        <td height="57" background="resource/images/djxlyw/djxlyw04.gif" valign="top"><div class=searchtag>
<FORM id=SearchResultForm method=post name=SearchResultForm action=SearchResult.shtml>
<SCRIPT>
  function search(){
  var form=document.getElementById("SearchResultForm");
  var Contents=form.tempTitle.value;
  Contents=encodeURIComponent(Contents);
  Contents=Contents.replace(/%/g,"@");
  form.searchContent.value=Contents;
  form.submit();
  }
  function textkey(event) {
  var keyCode = event.keyCode ? event.keyCode : event.which ? event.which : event.charCode;
   if (keyCode == 13) {
     search();
     return false;
   }else return true;
  }
</SCRIPT>
<STYLE>
.seartext{ border:0px; width:160px; height:22px; line-height:22px;}
.searchtag{ margin:22px 0 0 39px;}
.searbut{ background:url(resource/images/djxlyw/sraech_go.jpg) no-repeat; width:23px; height:21px; border:0;}
</STYLE>
  <Input type=hidden name=searchContent> 
  <Input onclick="if (this.value =='请输入关键字') this.value='';" onkeypress="return textkey(event)" class=seartext value=请输入关键字 name=tempTitle> 
  <Input onclick=search() class=searbut type=button></FORM></div></td>
      </tr>
    </table>
      <table width="100%" border="0" align="center" cellpadding="0" cellspacing="0" background="resource/images/djxlyw/m21.jpg" style="margin-top:8px">
        
        <tr>
          <td valign="top"><table width="100%" border="0" align="center" cellpadding="0" cellspacing="0" background="resource/images/djxlyw/m1_10.jpg" style="background-repeat:repeat-x">
            <tr>
              <td height="495" valign="top" background="resource/images/djxlyw/m5.jpg" style="background-position:bottom; background-repeat:repeat-x "><table width="100%" border="0" align="center" cellpadding="0" cellspacing="0">
                <tr>
                  <td height="34" background="resource/images/djxlyw/m1_09.jpg">&nbsp;</td>
                </tr>
                <tr>
                  <td height="5"></td>
                </tr>
                                <tr>
                  <td height="46" align="center" background="resource/images/djxlyw/yongyong.gif" style="background-position:center; background-repeat:no-repeat"><span><a href="Column.shtml?p5=101" class="lanmu" id="columnH_101">图片新闻</a></span></td>
                </tr>
                <tr>
                  <td height="46" align="center" background="resource/images/djxlyw/yongyong.gif" style="background-position:center; background-repeat:no-repeat"><span><a href="Column.shtml?p5=26" class="lanmu" id="columnH_26">旅游快报</a></span></td>
                </tr>
                <tr>
                  <td height="46" align="center" background="resource/images/djxlyw/yongyong.gif" style="background-position:center; background-repeat:no-repeat"><span><a href="Column.shtml?p5=27" class="lanmu" id="columnH_27">行业动态</a></span></td>
                </tr>
                <tr>
                  <td height="46" align="center" background="resource/images/djxlyw/yongyong.gif" style="background-position:center; background-repeat:no-repeat"><span><a href="Column.shtml?p5=28" class="lanmu" id="columnH_28">地市动态</a></span></td>
                </tr>
                <tr>
                  <td height="46" align="center" background="resource/images/djxlyw/yongyong.gif" style="background-position:center; background-repeat:no-repeat"><span><a href="Column.shtml?p5=3520" class="lanmu" id="columnH_3520">委旅游快报汇编</a></span></td>
                </tr>
                <tr>
                  <td height="46" align="center" background="resource/images/djxlyw/yongyong.gif" style="background-position:center; background-repeat:no-repeat"><span><a href="Column.shtml?p5=3527" class="lanmu" id="columnH_3527">一句话工作动态</a></span></td>
                </tr>
                <tr>
                  <td height="46" align="center" background="resource/images/djxlyw/yongyong.gif" style="background-position:center; background-repeat:no-repeat"><span><a href="Column.shtml?p5=3550" class="lanmu" id="columnH_3550">新闻发布会</a></span></td>
                </tr>
                <tr>
                  <td height="46" align="center" background="resource/images/djxlyw/yongyong.gif" style="background-position:center; background-repeat:no-repeat"><span><a href="Column.shtml?p5=3509" class="lanmu" id="columnH_3509">国务院重要政策...</a></span></td>
                </tr>
                <tr>
                  <td height="46" align="center" background="resource/images/djxlyw/yongyong.gif" style="background-position:center; background-repeat:no-repeat"><span><a href="Column.shtml?p5=721" class="lanmu" id="columnH_721">通知公告</a></span></td>
                </tr>  
                <tr>
                  <td height="5"></td>
                </tr>
              </table></td>
            </tr>
          </table></td>
        </tr>
      </table></td>
  </tr>
</table>
</div>
</div>
<div id=footer>
<div class=frielink><SPAN>友情链接</SPAN> 
<Select onchange=javascript:window.open(this.options[this.selectedIndex].value);this.selectedIndex=0 id=Select1 size=1 name=select1> 
<Option selected>—省直政府门户网站—</Option>  
<option value="http://www.jxdpc.gov.cn/">省发展和改革委员会</option> 
<option value="http://www.jxciit.gov.cn">省工业和信息化委员会</option> 
<option value="http://www.jxf.gov.cn/">省财政厅</option> 
<option value="http://www.jxhrss.gov.cn/">省人力资源和社会保障厅</option> 
<option value="http://www.jxaudit.gov.cn/">省审计厅</option> 
<option value="http://www.jxstj.gov.cn/">省统计局</option> 
<option value="http://www.jxdaj.gov.cn/">省档案局</option> 
<option value="http://www.jx-n-tax.gov.cn/">省国税局</option> 
<option value="http://www.jxds.gov.cn/">省地税局</option> 
<option value="http://www.jxgzw.gov.cn/">省国资委</option> 
<option value="http://www.jxfazhi.gov.cn/">省法制办</option> 
<option value="http://www.jxga.gov.cn/">省公安厅</option> 
<option value="http://www.jxdi.gov.cn/">省监察厅</option> 
<option value="http://www.jxsf.gov.cn/">省司法厅</option>
<option value="http://www.jxmzw.gov.cn/">省民政厅</option> 
<option value="http://www.jxbb.gov.cn/">省编办</option> 
<option value="http://www.jxbm.gov.cn/">省国家保密局</option>
<option value="http://www.jxzj.gov.cn/">省质量技术监督局</option> 
<option value="http://www.jxmkaqjc.gov.cn/">省煤矿安全监察局</option> 
<option value="http://www.jxsafety.gov.cn/">省安全生产监督管理局</option> 
<option value="http://www.jxjt.gov.cn/">省交通运输厅</option> 
<option value="http://www.jxjst.gov.cn/">省住房和城乡建设厅</option> 
<option value="http://www.jxepb.gov.cn/">省环境保护厅</option> 
<option value="http://www.jxgfgb.gov.cn/">省国防科工办</option> <option value="http://www.jxrf.gov.cn/">省人防办</option> 
<option value="http://www.jxca.gov.cn/">省通信管理局</option> 
<option value="http://www.jx.sgcc.com.cn">省电力公司</option> 
<option value="http://jx.spb.gov.cn/">省邮政管理局</option> 
<option value="http://www.jxdkj.gov.cn/">省地质矿产勘查开发局</option> 
<option value="http://www.hgydzj.jx.cn/">省核工业地质局</option> 
<option value="http://www.jxcehui.gov.cn/">省测绘局</option> 
<option value="http://www.nctlj.com.cn/">南昌铁路局</option> 
<option value="http://www.jxdoftec.gov.cn/">省商务厅</option> 
<option value="http://www.jxwqb.gov.cn/">省外事侨务办</option> 
<option value="http://www.jxta.gov.cn/">省旅发委</option> 
<option value="http://nanchang.customs.gov.cn/">南昌海关</option> 
<option value="http://www.jxciq.gov.cn/">省出入境检验检疫局</option> 
<option value="http://www.jxmtdzj.com/">省煤田地质局</option> 
<option value="http://www.jxysdzkcj.gov.cn/">省有色地质勘查局</option> 
<option value="http://www.jxagri.gov.cn/">省农业厅</option> 
<option value="http://www.jxly.gov.cn/">省林业厅</option> 
<option value="http://www.jxsl.gov.cn/">省水利厅</option> 
<option value="http://www.jxgtt.gov.cn/">省国土资源厅</option> 
<option value="http://www.jxjrb.gov.cn">省政府金融办</option> 
<option value="http://www.weather.org.cn/">省气象局</option> 
<option value="http://www.jxdz.gov.cn/">省地震局</option> <option value="http://www.jxaic.gov.cn/">省工商局</option> 
<option value="http://www.jxgrain.gov.cn">省粮食局</option> 
<option value="http://www.jxfpym.gov.cn/">省扶贫和移民办</option> 
<option value="http://www.jxcoop.gov.cn/">省供销合作社</option> 
<option value="http://www.jxnk.org.cn/">省农垦办</option> 
<option value="http://nanchang.pbc.gov.cn">人民银行南昌中心支行</option> <option value="http://www.jxstc.gov.cn/">省科技厅</option> 
<option value="http://www.jxedu.gov.cn/">省教育厅</option> 
<option value="http://www.jxsport.gov.cn/">省体育局</option> 
<option value="http://www.jxwst.gov.cn/">省卫生计生委</option> 
<option value="http://www.jxfda.gov.cn/">省食品药品监督管理局</option> 
<option value="http://www.jxwh.gov.cn/">省文化厅</option> 
<option value="http://www.jxmzj.gov.cn/">省民族宗教事务局</option> 
<option value="http://www.jxxgj.gov.cn/">省新闻出版广电局</option> 
<option value="http://www.jxgh.org.cn/">省总工会</option> 
<option value="http://www.jxwomen.org.cn/">省妇联</option> 
<option value="http://www.jxkx.gov.cn">省科协</option> 
<option value="http://www.jxql.org">省侨联</option> 
<option value="http://www.jxyouth.org.cn">省团省委</option> 
<option value="http://www.jxdpf.gov.cn/">省残联</option> <option value="http://www.jxsky.org.cn">省社科院</option> 
<option value="http://www.jxss.net.cn/">省社联</option> 
<option value="http://www.jxfic.gov.cn/">省工商业联合会</option> 
<option value="http://www.jx-xinfang.gov.cn">省信访局</option> 
<option value="http://www.jxtyzx.org/">省委统战部</option> 
<option value="http://www.jxyj.org.cn/">省援疆办</option> 
<option value="http://www.jxflac.com">省文联</option> 
<option value="http://www.jxgjl.com/">省工业经济联合会</option> 
<option value="http://www.chinajz.gov.cn/">省减灾委员会</option> 
<option value="http://www.jxszjb.gov.cn/">省驻京办</option> 
<option value="http://www.jiangxi.gov.cn/zhb/">省驻沪办</option> 
<option value="http://www.jxjgdj.gov.cn/">省机关党建</option> 
<option value="http://www.jxjgj.gov.cn/">省机关事务管理局</option> 
<option value="http://www.jxcs.org.cn">江西慈善网</option> 
</Select> 
<Select onchange=javascript:window.open(this.options[this.selectedIndex].value);this.selectedIndex=0;this.selectedIndex=0 id=Select2 size=1 name=select2> 
  <Option selected>—各省（市）旅游网站—</Option> 
  <Option value=http://www.hljtour.gov.cn/>黑龙江</Option> 
  <Option value=http://www.jstour.gov.cn/>江苏</Option> 
  <Option value=http://www.jlta.gov.cn/>吉林</Option> 
  <Option value=http://www.lntour.gov.cn/>辽宁</Option> 
  <Option value=http://tourzj.gov.cn/Default.aspx>浙江</Option> 
  <Option value=http://www.hubeitour.gov.cn/>湖北</Option> 
  <Option value=http://www.hnt.gov.cn>湖南</Option> 
  <Option value=http://www.ahta.com.cn>安徽</Option> 
  <Option value=http://www.gdta.gov.cn/default.html>广东</Option> 
  <Option value=http://www.scta.gov.cn>四川</Option> 
  <Option value=http://www.gz-travel.net>贵州</Option> 
  <Option value=http://www.fjta.com>福建</Option> 
  <Option value=http://www.gxta.gov.cn>广西</Option> 
  <Option value=http://www.visithainan.gov.cn/>海南</Option> 
  <Option value=http://www.bjta.gov.cn>北京</Option> 
  <Option value=http://lyw.sh.gov.cn/lyj_website/HTML/DefaultSite/portal/index/index.htm>上海</Option> 
  <Option value=http://www.tjtour.cn/>天津</Option> 
  <Option value=http://www.cqta.gov.cn/>重庆</Option> 
  <Option value=http://www.hebeitour.com.cn>河北</Option> 
  <Option value=http://www.hnta.cn>河南</Option> 
  <Option value=http://www.sdta.gov.cn>山东</Option> 
  <Option value=http://www.shanxitourismbureau.cn/zh/index.shtml>山西</Option> 
  <Option value=http://www.sxtour.com>陕西</Option> 
  <Option value=http://www.gsta.gov.cn/>甘肃</Option> 
  <Option value=http://www.nxta.gov.cn/>宁夏</Option> 
  <Option value=http://www.qhly.gov.cn/>青海</Option> 
  <Option value=http://www.xinjiangtour.gov.cn>新疆</Option> 
  <Option value=http://www.nmgtour.gov.cn>内蒙</Option> 
  <Option value=http://www.ynta.gov.cn/index.aspx>云南</Option> 
  <Option value=http://www.tibettour.com.cn>西藏</Option> 
  <Option value=http://www.discoverhongkong.com/china/index.jsp>香港</Option>
</Select> 
<Select onchange=javascript:window.open(this.options[this.selectedIndex].value) id=Select2 size=1 name=select3> 
  <Option selected>—各设区市旅游部门—</Option> 
  <Option value="http://www.nctour.com.cn/ ">南昌市旅游发展委员会</Option> 
  <Option value=http://www.jjta.gov.cn/>九江市旅游发展委员会</Option> 
  <Option value=http://www.gzLyw.com.cn>赣州市旅游发展委员会</Option> 
  <Option value=http://www.srta.gov.cn/>上饶市旅游发展委员会</Option> 
  <Option value=www.yctravel.gov.cn>宜春市旅游发展委员会</Option> 
  <Option value=www.jxfzly.gov.cn/>抚州市旅游发展委员会</Option> 
  <Option value=http://www.jata.gov.cn/>吉安市旅游发展委员会</Option> 
  <Option value=http://www.yttour.gov.cn/>鹰潭市旅游发展委员会</Option> 
  <Option value=http://www.jxpxly.ccoo.cn/>萍乡市旅游发展委员会</Option> 
  <Option value=http://www.jxxyly.gov.cn>新余市旅游发展委员会</Option> 
  <Option value=http://www.jdzta.gov.cn/>景德镇市旅游发展委员会</Option>
</Select> 
<Select onchange=javascript:window.open(this.options[this.selectedIndex].value);this.selectedIndex=0 id=Select2 size=1 name=select4> 
  <Option selected>—友情链接—</Option> 
  <Option value=http://www.ctrip.com/>携程</Option> 
  <Option value=http://www.tuniu.com/http://jxlalk.com/>途牛</Option> 
  <Option value=http://www.elong.com/>艺龙</Option> 
  <Option value=http://www.qunar.com/>去哪儿</Option> 
  <Option value=http://www.lvmama.com/>驴妈妈旅游</Option> 
  <Option value=https://www.alitrip.com/>阿里旅游</Option> 
  <Option value=https://www.ly.com/>同程旅游</Option> 
  <Option value=https://www.tripadvisor.cn/>猫途鹰</Option> 
  <Option value=http://www.mafengwo.cn/>蚂蜂窝</Option> 
  <Option value=http://www.qyer.com/>穷游网</Option>
</Select> </div>
<div class=ftnav><A href="News.shtml?p5=86627">联系我们</A> | <A onclick="SetHome(this,'http://www.jxta.gov.cn/')">设为首页</A> | <A onclick=AddFavorite(window.location,document.title)>加入收藏</A> | <A href="News.shtml?p5=86629">隐私声明</A> | <A href="News.shtml?p5=86631">使用帮助</A> | <A href="Column.shtml?p5=74">网站导航</A> </div>
<P>主办：江西省旅游发展委员会 承办：江西省旅游信息和培训中心</P>
<P>江西省旅游发展委员会 版权所有 赣ICP备09007107号</P>
<SCRIPT type=text/javascript>document.write(unescape("%3Cspan id='_ideConac' %3E%3C/span%3E%3Cscript src='http://dcs.conac.cn/js/15/000/0000/41260630/CA150000000412606300005.js' type='text/javascript'%3E%3C/script%3E"));</SCRIPT>
</div>
<SCRIPT type=text/javascript>
//  加入收藏 <a onclick="AddFavorite(window.location,document.title)">加入收藏</a>
function AddFavorite(sURL, sTitle)
{
    try
    {
        window.external.addFavorite(sURL, sTitle);
    }
    catch (e)
    {
        try
        {
            window.sidebar.addPanel(sTitle, sURL, "");
        }
        catch (e)
        {
            alert("加入收藏失败，请使用Ctrl+D进行添加");
        }
    }
}
//设为首页 
function SetHome(obj,url){
    try{
        obj.style.behavior='url(#default#homepage)';
        obj.setHomePage(url);
    }catch(e){
        if(window.netscape){
            try{
                netscape.security.PrivilegeManager.enablePrivilege("UniversalXPConnect");
            }catch(e){
                alert("抱歉，此操作被浏览器拒绝！请在浏览器地址栏输入“about:config”并回车然后将[signed.applets.codebase_principal_support]设置为'true'");
            }
        }else{
            alert("抱歉，您所使用的浏览器无法完成此操作。您需要手动将【"+url+"】设置为首页。");
        }
    }
}
</SCRIPT>
<SPAN id=_ideConac></SPAN>
</body>
</html>
																							
																							

"""

soup = BeautifulSoup(''.join(doc))

table = soup.find('table',{'id':'Table'})
article_link = []
datetime_t = str(datetime.date.today()).split('-')  # 对当天日期进行拆分，返回一个['2017', '10', '09']形式的列表

for tr in table.findAll('tr'):  # td,p14两个条件找出来的标签包含了链接块中的日期

    find_today = re.compile('(\d\d)-(\d\d)</font>')  # 构建找到末尾发布日期的正则表达式
    month = find_today.search(str(tr))  # 把上面构建的表达式作用于findAll找出来的内容
    try:
        d1 = datetime.date.today()  # 获取今天的日期
        d2 = datetime.date(int(datetime_t[0]), int(month.group(1)), int(month.group(2)))  # 获取新闻的日期
        days_betwen = (d1 - d2).days  # 获取时间差，结果为整数
        if days_betwen <= 13:  # 限定抓取几天内的新闻，当天的则为days_betwen == 0
            article_link.append(str(tr))  # 注意要转换为字符串，beautifusoup不接受列表和其他类型的数据
    except:
        pass

print(article_link)

soup2 = BeautifulSoup(''.join(article_link))

for link in soup2.findAll('a'):
    if not 'News' in link['href']:
        continue

    print(link['href'])
    print(link.contents[0].contents[0].strip())
"""

def link():
    for link in table.findAll('a'):
        if not 'News' in link['href']:
            continue
        print(link)
print('\n\n\nLINK\n')
link()

def linkhref():
    for link in table.findAll('a'):
        if not 'News' in link['href']:
            continue
        print(link['href'])

print('\n\n\nLINKHREF\n')
linkhref()

def linkcontent():
    for link in table.findAll('a'):
        if not 'News' in link['href']:
            continue
        print(link['title'].strip())
#        print(link.contents[0].strip())


print('\n\n\nLINKCONTENTS\n')
linkcontent()

url='www.baidu.com/'
spam = ['cat', 'bat', 'rat', 'elephant']
print ("".join(spam))

murl = []
for v in spam:
    murl.append(url+v)
print(murl)

print(''.join(doc))

dame = 'ljsdlfjlasdf'

print(''.join(dame) + '\n\n\n')


soup2 = [''.join(doc),''.join(doc2)]
articles = []
for i in soup2:
    soup2 = BeautifulSoup(i)
    #print soup2.prettify()

    table2 = soup2.find('table',{'id':'Table'})
    #print(table2)

    for link2 in table2.findAll('a'):
        if not 'News' in link2['href']:
            continue
        #print(link2)
        #print(link2['href'])
        til = link2['title'].strip()
        url = 'http://www.jxta.gov.cn/' + link2['href']
        #print(til+'\n'+url)
        a = {'title': til, 'url': url}
        articles.append(a)
print(articles)

"""
#jurl = 'http://www.jxta.gov.cn/Column.shtml?p5='
#soup3=[]
#for nu in range(26,29):
#    soup3.append(jurl+str(nu))
#for ur in soup3:
#    print(ur)

