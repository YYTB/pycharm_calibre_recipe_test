# coding=utf-8
from BeautifulSoup import BeautifulSoup
import datetime, re  # 导入日期时间模块，各版面的url根据发行日期改变。

html = '''

<!doctype html>
<html>
<head>
<meta charset="utf-8">
<meta http-equiv="X-UA-Compatible" content="IE=edge">
<link href="..//images/base.css" rel="stylesheet" />
<link href="..//images/zw.css" rel="stylesheet" />
<title>重点工作</title>
<script src="..//images/jquery-1.11.0.min.js" /></script>
<script src="..//images/nav_er.js" /></script>
<!--[if IE 6]>
<script type="text/javascript" src="png.js"></script>
<script>
PNG.fix('*'); 
</script>
<![endif]-->
<script>
function uaredirect(f) {
 try {
  if (document.getElementById("bdmark") != null) {
   return
  }
  var b = false;
  if (arguments[1]) {
   var e = window.location.host;
   var a = window.location.href;
   if (isSubdomain(arguments[1], e) == 1) {
    f = f + "/#m/" + a;
    b = true
   } else {
    if (isSubdomain(arguments[1], e) == 2) {
     f = f + "/#m/" + a;
     b = true
    } else {
     f = a;
     b = false
    }
   }
  } else {
   b = true
  }
  if (b) {
   var c = window.location.hash;
   if (!c.match("fromapp")) {
    if ((navigator.userAgent.match(/(iPhone|iPod|Android|ios|SymbianOS)/i))) {
     location.replace(f)
    }
   }
  }
 } catch(d) {}
}
function isSubdomain(c, d) {
 this.getdomain = function(f) {
  var e = f.indexOf("://");
  if (e > 0) {
   var h = f.substr(e + 3)
  } else {
   var h = f
  }
  var g = /^www\./;
  if (g.test(h)) {
   h = h.substr(4)
  }
  return h
 };
 if (c == d) {
  return 1
 } else {
  var c = this.getdomain(c);
  var b = this.getdomain(d);
  if (c == b) {
   return 1
  } else {
   c = c.replace(".", "\\.");
   var a = new RegExp("\\." + c + "$");
   if (b.match(a)) {
    return 2
   } else {
    return 0
   }
  }
 }
};
</script>
<SCRIPT type=text/javascript>uaredirect("http://m.cnta.gov.cn");</SCRIPT>

</head>
<body>
<link rel="Shortcut Icon" type="image/x-icon" href="../../images/favicon.ico">
<script language='javascript' src='http://www.cnta.gov.cn/images/zh.js'></script>
<div class="top">
	<div class="top1">
    	<div class="top_left">
            <a href="javascript:zh_tran('s');" target="_self">简体</a>
            <a href="javascript:zh_tran('t');" target="_self">繁体</a>
            <a href="http://en.cnta.gov.cn">English</a>
        </div>
        <div class="top_left top_right">
            <a href="http://www.cnta.gov.cn">返回首页</a>
        	<a href="javascript:;" onclick="AddFavorite('http://www.cnta.gov.cn/',location.href)">加入收藏</a>
          <!--  <a href="http://www1.cnta.gov.cn">返回旧版</a>-->
            <a href="http://mail.cnta.gov.cn/" target="_blank">邮箱登录</a>
        </div>
    </div>
</div>
<div class="main">
<script type="text/javascript">
  var today = new Date();
  var date = today.getDate();
  var day = today.getDay();
  var month = today.getMonth()+1;
  var year = today.getYear();
</script>
<script>
    var   CalendarData=new   Array(20);
    var   madd=new Array(12);
    var   TheDate=new Date();
    var   tgString="甲乙丙丁戊己庚辛壬癸";
    var   dzString="子丑寅卯辰巳午未申酉戌亥";
    var   numString="一二三四五六七八九十";
    var   monString="正二三四五六七八九十冬腊";
    var   weekString="日一二三四五六";
    var   sx="鼠牛虎兔龙蛇马羊猴鸡狗猪";
    var   cYear;
    var   cMonth;
    var   cDay;
    var   cHour;
    var   cDateString;
    var   DateString;
    var   Browser=navigator.appName;

    function   init()
    {
        CalendarData[0]=0x41A95;
        CalendarData[1]=0xD4A;
        CalendarData[2]=0xDA5;
        CalendarData[3]=0x20B55;
        CalendarData[4]=0x56A;
        CalendarData[5]=0x7155B;
        CalendarData[6]=0x25D;
        CalendarData[7]=0x92D;
        CalendarData[8]=0x5192B;
        CalendarData[9]=0xA95;
        CalendarData[10]=0xB4A;
        CalendarData[11]=0x416AA;
        CalendarData[12]=0xAD5;
        CalendarData[13]=0x90AB5;
        CalendarData[14]=0x4BA;
        CalendarData[15]=0xA5B;
        CalendarData[16]=0x60A57;
        CalendarData[17]=0x52B;
        CalendarData[18]=0xA93;
        CalendarData[19]=0x40E95;
        madd[0]=0;
        madd[1]=31;
        madd[2]=59;
        madd[3]=90;
        madd[4]=120;
        madd[5]=151;
        madd[6]=181;
        madd[7]=212;
        madd[8]=243;
        madd[9]=273;
        madd[10]=304;
        madd[11]=334;
    }

    function   GetBit(m,n)
    {
        return   (m>>n)&1;
    }

    function   e2c()
    {
        var   totalmnk;
        var   isEnd=false;
        var   tmp=TheDate.getYear();
        if   (tmp<1900)     tmp+=1900;
        total=(tmp-2001)*365
                +Math.floor((tmp-2001)/4)
                +madd[TheDate.getMonth()]
                +TheDate.getDate()
                -23;
        if   (TheDate.getYear()%4==0&&TheDate.getMonth()>1)
            total++;
        for(m=0;;m++)
        {
            k=(CalendarData[m]<0xfff)?11:12;
            for(n=k;n>=0;n--)
            {
                if(total<=29+GetBit(CalendarData[m],n))
                {
                    isEnd=true;
                    break;
                }
                total=total-29-GetBit(CalendarData[m],n);
            }
            if(isEnd)break;
        }
        cYear=2001   +   m;
        cMonth=k-n+1;
        cDay=total;
        if(k==12)
        {
            if(cMonth==Math.floor(CalendarData[m]/0x10000)+1)
                cMonth=1-cMonth;
            if(cMonth>Math.floor(CalendarData[m]/0x10000)+1)
                cMonth--;
        }
        cHour=Math.floor((TheDate.getHours()+3)/2);
    }

    function   GetcDateString()
    {   var   tmp="";

        if(cMonth<1)
        {
            tmp+="闰";
            tmp+=monString.charAt(-cMonth-1);
			
        }
        else
            tmp+=monString.charAt(cMonth-1);
        tmp+="月";
        tmp+=(cDay<11)?"初":((cDay<20)?"十":((cDay<30)?"廿":"卅"));
        if(cDay%10!=0||cDay==10)
            tmp+=numString.charAt((cDay-1)%10);
        tmp+="    ";
        cDateString=tmp;
        return   tmp;
    }

    function   GetDateString()
    {
        var   tmp="";
        var   t1=TheDate.getYear();
        if   (t1<1900)t1+=1900;
        tmp+=t1
                +"年"
                +(TheDate.getMonth()+1)+"月"
                +TheDate.getDate()+"日   "
                +TheDate.getHours()+":"
                +((TheDate.getMinutes()<10)?"0":"")
                +TheDate.getMinutes()
                +" 星期"+weekString.charAt(TheDate.getDay());
        DateString=tmp;
        return   tmp;
    }

    init();
    e2c();
    GetDateString();
    GetcDateString();
    //document.write(DateString+" 农历"+cDateString);
</script>
<style>
.nav li{padding-left:40px;width:auto;}
</style>
<div class="logo">
    	
        <div class="logo_right">
            <a class="text"><script type="text/javascript">document.write(month);</script>月<script type="text/javascript">document.write(date);</script>日<br>农历&nbsp;&nbsp;<script type="text/javascript">document.write(cDateString);</script>&nbsp;&nbsp;寒露</a>
			
			
					
			
			
			
			

			
					
			
			
			
			

			
					
			
			
			
					<img src="http://www.cnta.gov.cn/images/hanlu.png" />
			
			

			
					
			
			
			
			
			
        </div>
        <a href="http://www.cnta.gov.cn"><img src="/images/logo.png" />

</a>
    </div>
 <div class="nav">
    	<ul>
        	
            <li class="m1"><a  href="http://www.cnta.gov.cn/jgjj/lyjjj/">机构简介</a></li>     
            <li class="m2"><a  href="http://www.cnta.gov.cn/xxfb/">信息发布</a></li>
            <li class="m3"><a  href="http://www.cnta.gov.cn/zwgk/">政府信息公开</a></li>
            <li class="m4"><a   href="http://www.cnta.gov.cn/hygq/">回应关切</a></li>
            <li class="m5"><a  href="http://www.cnta.gov.cn/bsdt/zwgk/">办事大厅</a></li>
            <li class="m6"><a  href="http://www.cnta.gov.cn/zdzx/">重点专项</a></li>
            <li class="m7"><a  href="http://www.cnta.gov.cn/was5/web/search?channelid=242887">旅游名录</a></li>
            <li class="m8" style="padding-left:40px; width:72px;"><a  href="http://www.cnta.gov.cn/xwfbh/" style="letter-spacing:-2px;">新闻发布会</a></li>
            <li class="m9"><a  href="http://www.cnta.gov.cn/spzl" style="letter-spacing:-2px;">视频专栏</a></li>
            <div class="nav_h"></div>
            <div class="nav_h1"></div>
        </ul>
    </div>
<div class="main_local" style='margin-left:0px;'>
    	当前位置：<a href="../" target="_blank" title="首页">首页</a>><a href="./" title="重点工作" class='blue CurrChnlCls'>重点工作</a>
</div>
</div>
<style>
.xxfb_right_text1 ul li span{float:right;width:auto;line-height:30px;}
</style>

<div class="xxfb_cont" style='margin-top:0px'>

	<div class="xxfb_left1" style="margin-top:0px;">
        
		<div class="xxfb_left_til2">
			<div class="text">全域旅游</div>
			<a class="more" href="./qyly/"></a>
		</div>
		<div class="xxfb_left03">
			<ul>
                
			<li><a href="./qyly/201710/t20171010_842040.shtml">从小县城到“大景区”：浙江桐庐...<span class="time">10.11</span></a></li>
                
			<li><a href="./qyly/201710/t20171010_841981.shtml">全域旅游“青岛路径”获点赞 未...<span class="time">10.11</span></a></li>
                
			<li><a href="./qyly/201710/t20171010_841975.shtml">山东推进全域旅游，旅游+演绎产...<span class="time">10.11</span></a></li>
                
			<li><a href="./qyly/201710/t20171008_841689.shtml">鹰潭全域旅游平台启用<span class="time">10.08</span></a></li>
                
			<li><a href="./qyly/201710/t20171003_841405.shtml">象山设立“旅游警察”护航全域旅游<span class="time">10.07</span></a></li>
                
			<li><a href="./qyly/201709/t20170920_839862.shtml">创建全国全域旅游示范省动员大会...<span class="time">09.25</span></a></li>
                
			<li><a href="./qyly/201709/t20170924_840395.shtml">天长市抓重点提档次推进全域旅游...<span class="time">09.25</span></a></li>
                
			<li><a href="./qyly/201709/t20170920_839854.shtml">沁县文旅中心召开推进全域旅游交...<span class="time">09.25</span></a></li>
                
			<li><a href="./qyly/201709/t20170915_839347.shtml">祖拉布当选UNWTO秘书长 赞赏中国...<span class="time">09.15</span></a></li>
                
			</ul>
		</div>
		<div class="xxfb_left04">
			<ul>
		
			<li><a href="./qyly/201709/t20170915_839372.shtml">河北全域旅游破茧成蝶<span class="time">09.15</span></a></li>
                
			<li><a href="./qyly/201709/t20170914_839280.shtml">秦皇岛：旅游新起点全域大创新<span class="time">09.14</span></a></li>
                
			<li><a href="./qyly/201709/t20170913_839105.shtml">全域旅游、全球共享：李金早心中的...<span class="time">09.13</span></a></li>
                
			<li><a href="./qyly/201708/P020170822603620823148.pdf">2017全域旅游发展报告<span class="time">08.22</span></a></li>
                
			<li><a href="./qyly/201708/t20170828_837177.shtml">广西：双创双促全域发展<span class="time">08.28</span></a></li>
                
			<li><a href="./qyly/201708/t20170828_837178.shtml">全域旅游开启美丽河北新篇章<span class="time">08.28</span></a></li>
                
			<li><a href="./qyly/201708/t20170822_836502.shtml">旅游+马文化助力鄂尔多斯全域旅游发展<span class="time">08.23</span></a></li>
                
			<li><a href="./qyly/201708/t20170822_836419.shtml">郑人豪率队到徐闻县调研，规划建设...<span class="time">08.23</span></a></li>
                
			<li><a href="./qyly/201708/t20170822_836453.shtml">鹰潭市推进全域旅游发展奖励办法<span class="time">08.23</span></a></li>
                
			</ul>
			
		</div>
	
	</div>
<!-----------------------------------------第一块结束----------------------------------------------------- -->
	<div class="xxfb_right1" style="margin-top:0px;">
	 
		<div class="xxfb_right_til2">
			<div class="text">供给侧改革</div>
			<a class="more" href="./gjcgg/"></a>
		</div>
		<div class="xxfb_right_text1">
			<ul>
			
				<li><span>09.20</span><a href="./gjcgg/201709/t20170919_839806.shtml" class="">福建：推进供给侧改革打造大生态景区</a></li>
                        
				<li><span>08.15</span><a href="./gjcgg/201708/t20170814_835282.shtml" class="">南平延平区星级饭店三举措探索供给...</a></li>
                        
				<li><span>08.14</span><a href="./gjcgg/201708/t20170813_835155.shtml" class="">推进供给侧结构性改革 日照从“景区...</a></li>
                        
				<li><span>07.23</span><a href="./gjcgg/201707/t20170722_832708.shtml" class="">于风贵主任应邀在山东省深化农业供...</a></li>
                        
				<li><span>04.24</span><a href="./gjcgg/201704/t20170424_823182.shtml" class="">嘉峪关市积极推进旅游供给侧改革</a></li>
                        
				<li><span>04.24</span><a href="./gjcgg/201704/t20170420_822969.shtml" class="">新疆旅游加大供给侧改革力度 推动旅...</a></li>
                        
				<li><span>04.16</span><a href="./gjcgg/201704/t20170415_822410.shtml" class="">南平：深化旅游供给侧改革 做大做强...</a></li>
                        
				<li><span>04.13</span><a href="./gjcgg/201704/t20170412_822052.shtml" class="">福建省省长于伟国主持专题会议 以供...</a></li>
                        
				<li><span>04.10</span><a href="./gjcgg/201704/t20170410_821796.shtml" class="">吉林：推进供给侧结构性改革 提升旅...</a></li>
                        
			</ul>
		</div>
		
	</div>
<!-----------------------------------------第二块结束----------------------------------------------------- -->	

	<div class="xxfb_left1">
		      
		<div class="xxfb_left03">
		
			<div class="zw_left_til1">
				<div class="text">文明旅游</div>
				<a class="more" href="./ws/"></a>
			</div>
	                 <div style="padding-top: 37px;">
			<ul>
			 
				<li><a href="./ws/201710/t20171002_841330.shtml">黄金周，将文明旅游进行到底<span class="time">
10.05</span></a></li>
 
				<li><a href="./ws/201709/t20170918_839649.shtml">江苏省旅游局举办全省旅游行...<span class="time">
09.18</span></a></li>
 
				<li><a href="./ws/201709/t20170916_839472.shtml">安徽省旅游局组织开展“文明...<span class="time">
09.17</span></a></li>
 
				<li><a href="./ws/201709/t20170914_839191.shtml">让文明成为山东最美的风景—...<span class="time">
09.15</span></a></li>
 
				<li><a href="./ws/201709/t20170912_838918.shtml">滁州：加强文明旅游宣传 扩大...<span class="time">
09.13</span></a></li>
 
				<li><a href="./ws/201708/t20170822_836515.shtml">黄山市旅委着力营造文明旅游环境<span class="time">
08.22</span></a></li>
 
				<li><a href="./ws/201708/t20170821_836370.shtml">天津：文明旅游迎全运 手绘地...<span class="time">
08.21</span></a></li>
 
				<li><a href="./ws/201707/t20170717_832001.shtml">梅州市旅游局召开旅游系统创...<span class="time">
07.18</span></a></li>
 
				<li><a href="./ws/201707/t20170717_831993.shtml">营造文明旅游环境 淄博市召开...<span class="time">
07.18</span></a></li>
	
			</ul>
		 </div>
		</div>
		
		<div class="xxfb_left04">
		
			<div class="zw_left_til2">
				<div class="text">市场监管</div>
				<a class="more" href="./scjg/"></a>
			</div>
	                <div style="padding-top: 37px;">
			<ul>
			 
				<li><a href="./scjg/201710/t20171010_842016.shtml">持续开展节日执法检查 全力确保...<span class="time">10.11</span></a></li>
			 
				<li><a href="./scjg/201710/t20171010_842053.shtml">云南旅游监管整治再发力 旅行社...<span class="time">10.10</span></a></li>
			 
				<li><a href="./scjg/201710/t20171003_841403.shtml">江西省首个县级旅游诚信退赔中心...<span class="time">10.07</span></a></li>
			 
				<li><a href="./scjg/201710/t20171002_841332.shtml">福建省国庆假日旅游督查组莅漳督查<span class="time">10.05</span></a></li>
			 
				<li><a href="./scjg/201709/t20170922_840167.shtml">汕尾市旅游局组织执法人员参加《...<span class="time">09.23</span></a></li>
			 
				<li><a href="./scjg/201709/t20170920_839882.shtml">四川省旅游发展委员会召开2017年...<span class="time">09.21</span></a></li>
			 
				<li><a href="./scjg/201709/t20170920_839873.shtml">黄山风景区市场监管局开展集中整...<span class="time">09.21</span></a></li>
			 
				<li><a href="./scjg/201709/t20170918_839662.shtml">庆阳市旅游局开展旅游市场监管和...<span class="time">09.20</span></a></li>
			 
				<li><a href="./scjg/201709/t20170915_839452.shtml">搭建新疆旅游监管服务平台，助推...<span class="time">09.17</span></a></li>
			 			
			</ul>
		        </div>
		</div>
	</div>

	
	<div class="xxfb_right1">
		<div class="xxfb_right_til2">
			<div class="text">旅游人才</div>
			<a class="more" href="./lyrc/"></a>
		</div>
		<div class="xxfb_right_text1">

			<ul>
			   
				<li><a href="http://www.zgdaoyou.com/">导游云课堂研修培训<span class="time">11.09</span></a></li>
			   
				<li><a href="./lyrc/201710/t20171012_842307.shtml">国家旅游局办公室关于举办2017年度...<span class="time">10.12</span></a></li>
			   
				<li><a href="./lyrc/201708/t20170815_835515.shtml">一张“成绩单”透视旅游人才培养大...<span class="time">08.15</span></a></li>
			   
				<li><a href="./lyrc/201707/t20170707_830949.shtml">国家旅游局办公室关于组织开展2014...<span class="time">07.07</span></a></li>
			   
				<li><a href="./lyrc/201707/t20170703_830373.shtml">国家旅游局办公室关于印发 “十三...<span class="time">07.03</span></a></li>
			   
				<li><a href="./lyrc/201707/t20170703_830370.shtml">关于印发《2017年全国中高级导游等...<span class="time">07.03</span></a></li>
			   
				<li><a href="./lyrc/201706/t20170627_829936.shtml">2017年全国中、高级导游等级考试大纲<span class="time">06.27</span></a></li>
			   
				<li><a href="./lyrc/201705/t20170512_825217.shtml">国家旅游局办公室关于举办旅游数据...<span class="time">05.12</span></a></li>
			   
				<li><a href="./lyrc/201702/t20170227_815856.shtml">国家旅游局办公室关于组织开展2015...<span class="time">02.27</span></a></li>
			 				
			</ul>
		</div>
	</div>
<!-------------------------------------------第六块结束-------------------------------------------------- -->
	
	<div class="xxfb_left1">
		
		<div class="xxfb_left03">
			<div class="zw_left_til1">
				<div class="text">旅游“双+双创”</div>
				<a class="more" href="./lyssc/"></a>
			</div>
                        <div style="padding-top: 37px;">
			<ul>
			
				<li><a href="./lyssc/201710/t20171008_841718.shtml">福州“旅游+”产品假期走俏 游客...<span class="time">10.09</span></a></li>
			
				<li><a href="./lyssc/201710/t20171007_841653.shtml">山东：“旅游+”演绎产业融合之美<span class="time">10.08</span></a></li>
			
				<li><a href="./lyssc/201710/t20171010_842041.shtml">黄金周 浙江“旅游+体育”模式成...<span class="time">10.11</span></a></li>
			
				<li><a href="./lyssc/201709/t20170927_840724.shtml">旅游富市 “旅游+”加出日照全域...<span class="time">09.27</span></a></li>
			
				<li><a href="./lyssc/201709/t20170925_840537.shtml">江山积极探索“旅游+体育”<span class="time">09.26</span></a></li>
			
				<li><a href="./lyssc/201709/t20170922_840300.shtml">定西渭源：“旅游+”助力精准扶贫<span class="time">09.25</span></a></li>
			
				<li><a href="./lyssc/201709/t20170921_840117.shtml">海安“旅游+”做热沪上市场<span class="time">09.21</span></a></li>
			
				<li><a href="./lyssc/201709/t20170919_839683.shtml">山东邹城挖掘红色旅游资源，做好...<span class="time">09.20</span></a></li>
			
				<li><a href="./lyssc/201709/t20170919_839780.shtml">“旅游+体育”让天柱山更添活力<span class="time">09.20</span></a></li>
			 			
			</ul>
</div>
		</div>
		<div class="xxfb_left04">
			<div class="zw_left_til2">
				<div class="text">旅游投资</div>
				<a class="more" href="./lytz/"></a>
			</div>
	                <div style="padding-top: 37px;">
			<ul>
				
				<li><a href="./lytz/201709/t20170921_840052.shtml">2017年全球旅游投资将超8396亿美...<span class="time">09.21</span></a></li>
			
				<li><a href="./lytz/201709/t20170924_840409.shtml">浙江：旅游投资首破万亿元　民营...<span class="time">09.24</span></a></li>
			
				<li><a href="./lytz/201709/t20170922_840194.shtml">“918”现代服务业专场对接会推...<span class="time">09.23</span></a></li>
			
				<li><a href="./lytz/201709/t20170920_839864.shtml">第二届河北省旅发大会上总投资18...<span class="time">09.20</span></a></li>
			
				<li><a href="./lytz/201709/t20170918_839670.shtml">100亿浙江省旅游IP投资基金设立<span class="time">09.18</span></a></li>
			
				<li><a href="./lytz/201709/t20170915_839453.shtml">自治区旅游行业固定资产投资情况...<span class="time">09.17</span></a></li>
			
				<li><a href="./lytz/201709/t20170916_839471.shtml">亳州：拓宽投资渠道 开发旅游产品<span class="time">09.17</span></a></li>
			
				<li><a href="./lytz/201709/t20170913_839050.shtml">自驾车营地项目落地忻州 总投资9...<span class="time">09.14</span></a></li>
			
				<li><a href="./lytz/201709/t20170912_838899.shtml">成都市旅游投资项目推介会举行 6...<span class="time">09.13</span></a></li>
			 			
			</ul>
                       </div>
		</div>
	</div>
<!-------------------------------------------第七块结束-------------------------------------------------- -->
	
	<div class="xxfb_right1">
		<div class="xxfb_right_til2">
			<div class="text">旅游消费</div>
			<a class="more" href="./lyxf/"></a>
		</div>
		<div class="xxfb_right_text1">

			<ul>
				
				<li><a href="./lyxf/201710/t20171010_842055.shtml">离岛免税带旺海南旅游消费市场<span class="time">10.10</span></a></li>
			
				<li><a href="./lyxf/201710/t20171010_841973.shtml">七彩云南魅力无限 双节假日旅游火...<span class="time">10.11</span></a></li>
			
				<li><a href="./lyxf/201710/t20171009_841922.shtml">重庆文化市场消费火热<span class="time">10.10</span></a></li>
			
				<li><a href="./lyxf/201710/t20171008_841693.shtml">节后错峰出境游 最高降价6000元<span class="time">10.08</span></a></li>
			
				<li><a href="./lyxf/201710/t20171003_841397.shtml">桂林：守护“金饭碗” 改革助旅游...<span class="time">10.06</span></a></li>
			
				<li><a href="./lyxf/201710/t20171003_841395.shtml">海口推出水上飞机空中观光<span class="time">10.06</span></a></li>
			
				<li><a href="./lyxf/201710/t20171002_841331.shtml">武汉市发布旅游线路指导价 让游客...<span class="time">10.05</span></a></li>
			
				<li><a href="./lyxf/201709/t20170924_840396.shtml">合肥万达乐园一周年客流量超三百万...<span class="time">09.25</span></a></li>
			
				<li><a href="./lyxf/201709/t20170920_839873.shtml">黄山风景区市场监管局开展集中整治...<span class="time">09.21</span></a></li>
			 			
			</ul>
		</div>
	</div>
	
	<div class="clear"></div>
	<!-------------------------------------------第八块结束-------------------------------------------------- -->
<div class="xxfb_left1">
		
		<div class="xxfb_left03">
			<div class="zw_left_til1">
				<div class="text">厕所革命</div>
				<a class="more" href="./csgm/"></a>
			</div>
                        <div style="padding-top: 37px;">
			<ul>
			
				<li><a href="../xxfb/xxfb_dfxw/gx/201710/t20171006_841604.shtml">（广西）桂林：“厕所革命”提升...<span class="time">10.08</span></a></li>
			
				<li><a href="../xxfb/xxfb_dfxw/sc/201710/t20171004_841503.shtml">（四川）四川印发“厕所革命”实...<span class="time">10.07</span></a></li>
			
				<li><a href="../ztwz/csgm/gdjc/201710/t20171006_841628.shtml">（陕西）临潼：厕所革命成绩斐然...<span class="time">10.06</span></a></li>
			
				<li><a href="../ztwz/csgm/gdjc/201710/t20171005_841575.shtml">（福建）永定土楼：厕所革命为世...<span class="time">10.05</span></a></li>
			
				<li><a href="../ztwz/csgm/gdjc/201709/t20170927_840744.shtml">（河南）2017年全河南省厕所革命...<span class="time">09.27</span></a></li>
			
				<li><a href="../ztwz/csgm/gdjc/201708/t20170823_836664.shtml">（青海）西宁市旅游局专项检查组...<span class="time">08.23</span></a></li>
			
				<li><a href="../ztwz/csgm/gdjc/201708/t20170823_836611.shtml">（江苏）苏州：企业自建旅游厕所...<span class="time">08.23</span></a></li>
			
				<li><a href="../ztwz/csgm/gdjc/201708/t20170818_836080.shtml">（河北）2017年河北省厕所革命公...<span class="time">08.18</span></a></li>
			
				<li><a href="../ztwz/csgm/gdjc/201707/t20170724_832878.shtml">（广东）“厕所+”模式 助力广东...<span class="time">07.24</span></a></li>
			 			
			</ul>
</div>
		</div>
		<div class="xxfb_left04">
			<div class="zw_left_til2">
				<div class="text">体制创新</div>
				<a class="more" href="./tzcx/"></a>
			</div>
	                <div style="padding-top: 37px;">
			<ul>
				
				<li><a href="./tzcx/201706/t20170602_827237.shtml">全国已有23省份设立旅游发展委员会<span class="time">06.02</span></a></li>
			
				<li><a href="./tzcx/201705/t20170527_826760.shtml">陕西省成立旅游发展委员会助力旅...<span class="time">05.27</span></a></li>
			
				<li><a href="./tzcx/201705/t20170501_823812.shtml">新疆维吾尔自治区旅发委挂牌成立<span class="time">05.01</span></a></li>
			
				<li><a href="./tzcx/201703/t20170329_820907.shtml">山西省旅发委及全省11个市旅发委...<span class="time">03.29</span></a></li>
			
				<li><a href="./tzcx/201703/t20170324_819573.shtml">福州市旅游局更名为福州市旅游发...<span class="time">03.25</span></a></li>
			
				<li><a href="./tzcx/201612/t20161209_808862.shtml">吉林省旅游发展委员会挂牌<span class="time">12.09</span></a></li>
			
				<li><a href="./tzcx/201611/t20161129_808056.shtml">山东省14市同时成立旅游发展委员会<span class="time">11.29</span></a></li>
			
				<li><a href="./tzcx/201610/t20161025_787404.shtml">青海省旅游发展委员会揭牌<span class="time">10.25</span></a></li>
			
				<li><a href="./tzcx/201608/t20160804_779744.shtml">国企改革稳步推进成效显著<span class="time">08.05</span></a></li>
			 			
			</ul>
                       </div>
		</div>
	</div>
<!-------------------------------------------第七块结束-------------------------------------------------- -->
	
	<div class="xxfb_right1">
		<div class="xxfb_right_til2">
			<div class="text">市场推广</div>
			<a class="more" href="./sctg/"></a>
		</div>
		<div class="xxfb_right_text1">

			<ul>
				
				<li><a href="./sctg/201710/t20171013_842393.shtml">区域品牌化 浙江绍兴美丽乡村成“...<span class="time">10.14</span></a></li>
			
				<li><a href="./sctg/201710/t20171009_841863.shtml">“多家电视媒体走进大别山风景道采...<span class="time">10.10</span></a></li>
			
				<li><a href="./sctg/201710/t20171013_842368.shtml">2017慈溪养生旅游节隆重开幕<span class="time">10.15</span></a></li>
			
				<li><a href="./sctg/201710/t20171010_842017.shtml">魅力北京温哥华推介会及图片展成功...<span class="time">10.11</span></a></li>
			
				<li><a href="./sctg/201710/t20171013_842337.shtml">千岛湖登全球热搜榜第13位 “双节...<span class="time">10.14</span></a></li>
			
				<li><a href="./sctg/201710/t20171002_841328.shtml">“丝路明珠 魅力银川”全域旅游嘉...<span class="time">10.05</span></a></li>
			
				<li><a href="./sctg/201710/t20171001_841310.shtml">四川推出川南和川东北区域十条精品...<span class="time">10.04</span></a></li>
			
				<li><a href="./sctg/201710/t20171001_841306.shtml">惠州推出八大精彩旅游产品<span class="time">10.03</span></a></li>
			
				<li><a href="./sctg/201710/t20171001_841303.shtml">北京国际旅游节开幕 丝路主题展现...<span class="time">10.03</span></a></li>
			 			
			</ul>
		</div>
	</div>
	
	<div class="clear"></div>
	<!-------------------------------------------第八块结束-------------------------------------------------- -->



</div>

<script language="javascript" type="text/javascript"> 
				function location1(s)
                {       var d = s.options[s.selectedIndex].value;
						if ((navigator.userAgent.match(/(iPhone|iPod|Android|ios|SymbianOS)/i))) {
						 	location.href=d;
						}
                     	else
							window.open(d,"_blank");
						s.selectedIndex=0;       
                }

</script>
<script>
$(function(){
$('.r_close').click(function(){
$('.r_close, .weibo, .weixin, .gaibian, .searchf').hide();




})
if($(window).width()<1282){
$('.r_close, .weibo, .weixin').css('left', 'auto').css('right', '10px');
$('.gaibian, .searchf').css('left', 'auto').css('right', '25px');
}else{
$('.r_close, .weibo, .weixin, .gaibian, .searchf').css('left', '50%').css('right', 'auto');
}
$(window).resize(function() {
 if($(window).width()<1282){
$('.r_close, .weibo, .weixin').css('left', 'auto').css('right', '10px');
$('.gaibian, .searchf').css('left', 'auto').css('right', '25px');
}else{
$('.r_close, .weibo, .weixin, .gaibian, .searchf').css('left', '50%').css('right', 'auto');
}
})
})
</script>
<div class="foot">
	<div class="footer">
    	<div class="footer_t">
        	<select name="m1" onChange="location1(this)" ID="Select1">
        <option selected="selected">国务院部委网站</option>
          
          <option value="http://www.mfa.gov.cn/mfa_chn/">外交部</option>
          
          <option value="http://www.mod.gov.cn/">国防部</option>
          
          <option value="http://www.ndrc.gov.cn/">发展改革委</option>
          
          <option value="http://www.moe.gov.cn/">教育部</option>
          
          <option value="http://www.most.gov.cn/">科技部</option>
          
          <option value="http://www.miit.gov.cn/n11293472/index.html">工业和信息化部</option>
          
          <option value="http://www.seac.gov.cn/">国家民委</option>
          
          <option value="http://www.mps.gov.cn/n16/index.html?_v=1435138159749">公安部</option>
          
          <option value="http://www.ccdi.gov.cn/">监察部</option>
          
          <option value="http://www.mca.gov.cn/">民政部</option>
          
          <option value="http://www.moj.gov.cn/">司法部</option>
          
          <option value="http://www.mof.gov.cn/index.htm">财政部</option>
          
          <option value="http://www.mohrss.gov.cn/">人力资源社会保障部</option>
          
          <option value="http://www.mlr.gov.cn/">国土资源部</option>
          
          <option value="http://www.mep.gov.cn/">环境保护部</option>
          
          <option value="http://www.mohurd.gov.cn/">住房城乡建设部</option>
          
          <option value="http://www.mot.gov.cn/">交通运输部</option>
          
          <option value="http://www.mwr.gov.cn/">水利部</option>
          
          <option value="http://www.moa.gov.cn/">农业部</option>
          
          <option value="http://www.mofcom.gov.cn/">商务部</option>
          
          <option value="http://www.mcprc.gov.cn/">文化部</option>
          
          <option value="http://www.nhfpc.gov.cn/">卫生计生委</option>
          
          <option value="http://www.pbc.gov.cn/">人民银行</option>
          
          <option value="http://www.audit.gov.cn/">审计署</option>
          
          <option value="http://www.china-language.gov.cn/">国家语委</option>
          
          <option value="http://www.cnsa.gov.cn/">航天局</option>
          
          <option value="http://www.caea.gov.cn/">原子能机构</option>
          
          <option value="http://www.sasac.gov.cn/">国资委</option>
          
          <option value="http://www.customs.gov.cn/publish/portal0/">海关总署</option>
          
          <option value="http://www.chinatax.gov.cn/">税务总局</option>
          
          <option value="http://www.saic.gov.cn/">工商总局</option>
          
          <option value="http://www.aqsiq.gov.cn/">质检总局</option>
          
          <option value="http://www.sapprft.gov.cn/">新闻出版广电总局</option>
          
          <option value="http://www.sport.gov.cn/">体育总局</option>
          
          <option value="http://www.chinasafety.gov.cn/newpage/">安全监管总局</option>
          
          <option value="http://www.sda.gov.cn/WS01/CL0001/">食品药品监管总局</option>
          
          <option value="http://www.stats.gov.cn/">统计局</option>
          
          <option value="http://www.forestry.gov.cn/">林业局</option>
          
          <option value="http://www.sipo.gov.cn/">知识产权局</option>
          
          <option value="http://www.sara.gov.cn/">宗教局</option>
          
          <option value="http://www.counsellor.gov.cn/">参事室</option>
          
          <option value="http://www.ggj.gov.cn/">国管局</option>
          
          <option value="http://www.ncac.gov.cn/">版权局</option>
          
          <option value="http://www.gqb.gov.cn/">侨办</option>
          
          <option value="http://www.hmo.gov.cn/">港澳办</option>
          
          <option value="http://www.chinalaw.gov.cn/">法制办</option>
          
          <option value="http://www.gov.cn/guoqing/2005-12/26/content_2652073.htm">国研室</option>
          
          <option value="http://www.gwytb.gov.cn/">台办</option>
          
          <option value="http://www.scio.gov.cn/">新闻办</option>
          
          <option value="http://www.xinhuanet.com/">新华社</option>
          
          <option value="http://www.cas.cn/">中科院</option>
          
          <option value="http://cass.cssn.cn/">社科院</option>
          
          <option value="http://www.cae.cn/cae/html/main/index.html">工程院</option>
          
          <option value="http://www.drc.gov.cn/">发展研究中心</option>
          
          <option value="http://www.nsa.gov.cn/web/index.php">行政学院</option>
          
          <option value="http://www.cea.gov.cn/">地震局</option>
          
          <option value="http://www.cma.gov.cn/">气象局</option>
          
          <option value="http://www.cbrc.gov.cn/index.html">银监会</option>
          
          <option value="http://www.csrc.gov.cn/pub/newsite/">证监会</option>
          
          <option value="http://www.circ.gov.cn/web/site0/">保监会</option>
          
          <option value="http://www.ssf.gov.cn/">社保基金会</option>
          
          <option value="http://www.nsfc.gov.cn/">自然科学基金会</option>
          
          <option value="http://www.gjxfj.gov.cn/">信访局</option>
          
          <option value="http://www.chinagrain.gov.cn/">粮食局</option>
          
          <option value="http://www.nea.gov.cn/">能源局</option>
          
          <option value="http://www.sastind.gov.cn/">国防科工局</option>
          
          <option value="http://www.tobacco.gov.cn/">烟草局</option>
          
          <option value="http://www.safea.gov.cn/">外专局</option>
          
          <option value="http://www.scs.gov.cn/">公务员局</option>
          
          <option value="http://www.soa.gov.cn/">海洋局</option>
          
          <option value="http://www.sbsm.gov.cn/">测绘地信局</option>
          
          <option value="http://www.nra.gov.cn/">铁路局</option>
          
          <option value="http://www.caac.gov.cn/">民航局</option>
          
          <option value="http://www.spb.gov.cn/">邮政局</option>
          
          <option value="http://www.sach.gov.cn/">文物局</option>
          
          <option value="http://www.satcm.gov.cn/">中医药局</option>
          
          <option value="http://www.safe.gov.cn/">外汇局</option>
          
          <option value="http://www.chinacoal-safety.gov.cn/mkaj/">煤矿安监局</option>
          
          <option value="http://www.saac.gov.cn/">档案局</option>
          
          <option value="http://www.oscca.gov.cn/">密码局</option>
          
          <option value="http://www.cpad.gov.cn/">扶贫办</option>
          
          <option value="http://www.3g.gov.cn/index.ycs">三峡办</option>
          
          <option value="http://www.nsbd.gov.cn/">南水北调办</option>
          
        </select>
        <select name="m2" onChange="location1(this)" ID="Select1">
        <option selected="selected">各省旅游政务网</option>
          
          <option value="http://www.bjta.gov.cn/">北京旅游网</option>
          
          <option value="http://www.tjtour.cn/">天津旅游网</option>
          
          <option value="http://www.hebeitour.gov.cn/index.php">河北旅游网</option>
          
          <option value="http://www.shanxichina.gov.cn">山西旅游网</option>
          
          <option value="http://www.nmgtour.gov.cn/">内蒙古旅游网</option>
          
          <option value="http://www.lntour.gov.cn/">辽宁旅游网</option>
          
          <option value="http://www.jlta.gov.cn/">吉林旅游网</option>
          
          <option value="http://www.hljtour.gov.cn/">黑龙江旅游网</option>
          
          <option value="http://lyw.sh.gov.cn/">上海旅游网</option>
          
          <option value="http://www.jstour.com/">江苏旅游网</option>
          
          <option value="http://www.tourzj.gov.cn/">浙江旅游网</option>
          
          <option value="http://www.ahta.com.cn/">安徽旅游网</option>
          
          <option value="http://www.fjta.gov.cn/">福建旅游网</option>
          
          <option value="http://www.jxta.gov.cn/">江西旅游网</option>
          
          <option value="http://www.sdta.gov.cn/">山东旅游网</option>
          
          <option value="http://www.hnta.cn/">河南旅游网</option>
          
          <option value="http://www.hubeitour.gov.cn/">湖北旅游网</option>
          
          <option value="http://www.hnt.gov.cn/">湖南旅游网</option>
          
          <option value="http://www.gdta.gov.cn/">广东旅游网</option>
          
          <option value="http://www.gxta.gov.cn/">广西旅游网</option>
          
          <option value="http://www.visithainan.gov.cn/government/">海南旅游网</option>
          
          <option value="http://www.cqta.gov.cn/">重庆旅游网</option>
          
          <option value="http://www.scta.gov.cn/sclyj/">四川旅游网</option>
          
          <option value="http://www.gztour.gov.cn/">贵州旅游网</option>
          
          <option value="http://www.innyo.com/">云南旅游网</option>
          
          <option value="http://www.xzta.gov.cn/index.html">西藏旅游网</option>
          
          <option value="http://sxta.gov.cn/sxtourgov/proscenium/index.html">陕西旅游网</option>
          
          <option value="http://www.gsta.gov.cn/">甘肃旅游网</option>
          
          <option value="http://www.nxtour.com.cn/">宁夏旅游网</option>
          
          <option value="http://www.qhly.gov.cn/">青海旅游网</option>
          
          <option value="http://www.xinjiangtour.gov.cn/">新疆旅游网</option>
          
          <option value="http://www.discoverhongkong.com/china/index.jsp">香港旅游发展局</option>
          
          <option value="http://www.macautourism.gov.mo/">澳门特别行政区旅游局</option>
          
          <option value="http://www.btwql.gov.cn/">兵团旅游网</option>
          
        </select>
        <select name="m3" onChange="location1(this)" ID="Select1">
        <option selected="selected">国际旅游组织</option>
          
          <option value="http://www2.unwto.org/">联合国世界旅游组织</option>
          
          <option value="http://www.fia.com/">国际汽车运动联合会</option>
          
          <option value="http://www.pata.org/">亚太旅游协会</option>
          
          <option value="http://www.apec.org/">亚太经合组织</option>
          
          <option value="http://www.asta.org/">美国旅行代理商协会</option>
          
          <option value="http://ih-ra.com/">国际饭店与餐饮协会</option>
          
        </select>
        <select name="m4" onChange="location1(this)" ID="Select1">
        <option selected="selected">驻华旅游组织</option>
          
          <option value="../../yqlj/zhlyzz/201507/t20150701_719902.shtml">港澳台驻内地办事处</option>
          
          <option value="../../yqlj/zhlyzz/201506/t20150624_273197.shtml">各国旅游机构驻华办事处</option>
          
        </select>
        <select name="m5" onChange="location1(this)" ID="Select1">
        <option selected="selected">友情链接</option>
          
          <option value="https://zygjjg.12388.gov.cn/">中央国家机关举报网站</option>
          
          <option value="../../yqlj/yqlj/lyyx/">旅游院校</option>
          
          <option value="../../yqlj/yqlj/lypd/">旅游频道</option>
          
          <option value="../../yqlj/yqlj/yqljqt/">其他</option>
          
        </select>
        </div>
        <div class="footer_l">
     
<script type="text/javascript">document.write(unescape("%3Cspan id='_ideConac' %3E%3C/span%3E%3Cscript src='http://dcs.conac.cn/js/33/000/0000/40672416/CA330000000406724160003.js' type='text/javascript'%3E%3C/script%3E"));</script>

            <a><img src="http://www.cnta.gov.cn/images/red1.png" /></a>
        </div>
        <div class="footer_r">
        	<p><a target="_blank" href="http://www.cnta.gov.cn/lxwm/" >联系我们 </a>| <a target="_blank" href="http://www.cnta.gov.cn/wzdt/" >网站地图</a> | <a target="_blank" href="http://www.cnta.gov.cn/download/" >下载中心</a></p>
            <p>版权所有：中华人民共和国国家旅游局  网站管理：国家旅游局信息中心</p>
            <p>管理员邮箱：webmaster@cnta.gov.cn  京ICP备15046657号</p>
            <p>建议使用IE8以上浏览器</p>
        </div>
        <div style="float:left;width:120px;height:55px;margin-left:15px;margin-top:65px;">
        <script id="_jiucuo_" sitecode='bm39000001' src='http://pucha.kaipuyun.cn/exposure/jiucuo.js'></script>
        </div>
        <div class="clear"></div>
    </div>
</div>
<script type="text/javascript">
    var _bdhmProtocol = (("https:" == document.location.protocol) ? " https://" : " http://");
    document.write(unescape("%3Cscript src='" + _bdhmProtocol + "hm.baidu.com/h.js%3F1012c8757d7968f19279de5b5d3bc73b' type='text/javascript'%3E%3C/script%3E"));
</script>
<script type='text/javascript' src='http://static.gridsumdissector.com/js/Clients/GWD-801536-A2CC10/gs.js'></script>
<noscript><img src="http://ta.trs.cn/c/1.gif?mpId=364&jsoff=1" style="border:0" alt="" /></noscript>
<script>
var _taq = _taq || [];
_taq.home = 'http://ta.trs.cn/c';
_taq.push(['_mpId', '364']);
_taq.push(['_cli', '1']);
(function(d, o, t) {
	if (window.inTRSDesignMode) return;
	var ma = d.createElement(o); ma.async = true; ma.commonresource="1"; ma.src = t;
	var s = d.getElementsByTagName(o)[0]; s.parentNode.insertBefore(ma, s);
})(document, 'script', 'http://ta.trs.cn/c/js/ta.js');
</script>
<div class="r_close" style='bottom:340px;'>
<img src='http://www.cnta.gov.cn/images/close140403.gif' />
</div>
<!--<div  class="weibo" style='margin-left: -663px; bottom:366px;padding: 4px; height:134px'>
<a href='http://www.cnta.gov.cn/ztwz/czczl/'><img src="http://www.cnta.gov.cn/zylcfctpwh/images/P020161130627556356561.jpg" width="66" height="134" style="height:134px;" /></a>
</div>-->
<!--20170411注释
<div  class="weibo" style='margin-left: -663px; bottom: 366px;padding: 4px; height:134px'>
<a href='http://www.cnta.gov.cn/ztwz/lxyz/'><img src="http://www.cnta.gov.cn/zylcfctpwh/images/P020161019552215694719.jpg" width="66" height="134" style="height:134px;" /></a>
</div>

<div  class="weibo" style='margin-left: -663px; bottom: 214px;padding: 4px; height:134px'>
<a href='http://www.cnta.gov.cn/ztwz/lmhdzt/'><img src="http://www.cnta.gov.cn/zylcfctpwh/images/P020161019552576053500.jpg" width="66" height="134" style="height:134px;" /></a>
</div>

<div  class="weibo" style='margin-left: -663px; bottom: 62px;padding: 4px; height:134px'>
<a href='http://www.cnta.gov.cn/ztwz/dsjqgdyds/'><img src="http://www.cnta.gov.cn/zylcfctpwh/images/P020170314589555319942.jpg" width="66" height="134" style="height:134px;" /></a>
</div>






<div class="weixin" style="height:auto;bottom:363px;padding:4px;">
	<a href='http://www.cnta.gov.cn/ztwz/2017bflyngycfz/'><img src="http://www.cnta.gov.cn/zylcfctpwh/images/P020170203348421395926.jpg" width="66" height="134" style="height:134px;" /></a>
</div>

<div class="weixin" style="height:auto;bottom:212px;padding:4px;">
	<a href='http://dj.cnta.gov.cn/'><img src="http://www.cnta.gov.cn/zylcfctpwh/images/P020161019552462328276.jpg" width="66" height="134" style="height:134px;" /></a>
</div>
<div class="weixin" style="height:auto;bottom:60px;padding:4px;">
	<a href='http://www.cnta.gov.cn/ztwz/jtly/'><img src="http://www.cnta.gov.cn/zylcfctpwh/images/P020170228612233591893.jpg" width="66" height="134" style="height:134px;" /></a>
</div>-->
<div class="weibo" style="bottom:90px;padding:4px;">
	<img src="http://www.cnta.gov.cn/images/weibo.jpg" />
    <span>国家旅游局</span>
    <span style="letter-spacing:3px;">官方微博</span>
</div>
<div class="weixin" style="bottom:220px;padding:4px;">
	<img src="http://www.cnta.gov.cn/ty/includefooter/images/P020160309356126439106.jpg" width="66" />
    <span>国家旅游局</span>
    <span style="letter-spacing:3px;">官方微信</span>
</div>
<!--
<a class="gaibian" href="http://www.cnta.gov.cn/xxfb/gbtz/"  ignoreapd="true" >
	图片征集
</a>-->
<!--<a class="gaibian" href="http://city.sina.com.cn/2016lyzj/index.shtml?qq-pf-to=pcqq.c2c"  ignoreapd="true" style='background:none;bottom:80px;margin-left:590px;'>
<img src="http://www.cnta.gov.cn/images/Icon_logo20160530.jpg" width="52" height="52" style='margin-top:-30px' />
</a>-->
<!--30,180-->
<div class="searchf" style="bottom:20px;margin-left:590px;">
	搜 索
    <div class="searchf2">
        <div class="searchf1">
        <form name="searchform" id="searchform" action="http://www.cnta.gov.cn/was5/web/search?channelid=261012" method="post" target="_blank">
            <input id="textfield" type="text" name="searchword" class="" value="" />
				<input type="hidden" name="perpage" value="" />
				<input type="hidden" name="templet" value="" />
				<input type="hidden" name="token" value="" />
				<input type="hidden" name="channelid" value="261012" />
				<input type="submit" value="搜索" />
        </form>
        </div>
    </div>
</div>



<script>
var _hmt = _hmt || [];
(function() {
  var hm = document.createElement("script");
  hm.src = "//hm.baidu.com/hm.js?2a7d9fd86036a721a0f0895061ae1ad7";
  var s = document.getElementsByTagName("script")[0]; 
  s.parentNode.insertBefore(hm, s);
})();
</script>
</body>
</html>

'''

html1 = """

<!doctype html>
<html>
<head>
<meta charset="utf-8">
<meta http-equiv="X-UA-Compatible" content="IE=edge">
<link href="../../images/base.css" rel="stylesheet" />
<link href="../../images/lby.css" rel="stylesheet" />
<title>市场推广</title>
<script src="../../images/jquery-1.11.0.min.js" /></script>
<script src="../../images/nav_er.js" /></script>
<!--[if IE 6]>
<script type="text/javascript" src="../../images/png.js"></script>
<script>
PNG.fix('*'); 
</script>
<![endif]-->
</head>
<body>
<link rel="Shortcut Icon" type="image/x-icon" href="../../images/favicon.ico">
<script language='javascript' src='http://www.cnta.gov.cn/images/zh.js'></script>
<div class="top">
	<div class="top1">
    	<div class="top_left">
            <a href="javascript:zh_tran('s');" target="_self">简体</a>
            <a href="javascript:zh_tran('t');" target="_self">繁体</a>
            <a href="http://en.cnta.gov.cn">English</a>
        </div>
        <div class="top_left top_right">
            <a href="http://www.cnta.gov.cn">返回首页</a>
        	<a href="javascript:;" onclick="AddFavorite('http://www.cnta.gov.cn/',location.href)">加入收藏</a>
          <!--  <a href="http://www1.cnta.gov.cn">返回旧版</a>-->
            <a href="http://mail.cnta.gov.cn/" target="_blank">邮箱登录</a>
        </div>
    </div>
</div>
<div class="main">
    <script type="text/javascript">
  var today = new Date();
  var date = today.getDate();
  var day = today.getDay();
  var month = today.getMonth()+1;
  var year = today.getYear();
</script>
<script>
    var   CalendarData=new   Array(20);
    var   madd=new Array(12);
    var   TheDate=new Date();
    var   tgString="甲乙丙丁戊己庚辛壬癸";
    var   dzString="子丑寅卯辰巳午未申酉戌亥";
    var   numString="一二三四五六七八九十";
    var   monString="正二三四五六七八九十冬腊";
    var   weekString="日一二三四五六";
    var   sx="鼠牛虎兔龙蛇马羊猴鸡狗猪";
    var   cYear;
    var   cMonth;
    var   cDay;
    var   cHour;
    var   cDateString;
    var   DateString;
    var   Browser=navigator.appName;

    function   init()
    {
        CalendarData[0]=0x41A95;
        CalendarData[1]=0xD4A;
        CalendarData[2]=0xDA5;
        CalendarData[3]=0x20B55;
        CalendarData[4]=0x56A;
        CalendarData[5]=0x7155B;
        CalendarData[6]=0x25D;
        CalendarData[7]=0x92D;
        CalendarData[8]=0x5192B;
        CalendarData[9]=0xA95;
        CalendarData[10]=0xB4A;
        CalendarData[11]=0x416AA;
        CalendarData[12]=0xAD5;
        CalendarData[13]=0x90AB5;
        CalendarData[14]=0x4BA;
        CalendarData[15]=0xA5B;
        CalendarData[16]=0x60A57;
        CalendarData[17]=0x52B;
        CalendarData[18]=0xA93;
        CalendarData[19]=0x40E95;
        madd[0]=0;
        madd[1]=31;
        madd[2]=59;
        madd[3]=90;
        madd[4]=120;
        madd[5]=151;
        madd[6]=181;
        madd[7]=212;
        madd[8]=243;
        madd[9]=273;
        madd[10]=304;
        madd[11]=334;
    }

    function   GetBit(m,n)
    {
        return   (m>>n)&1;
    }

    function   e2c()
    {
        var   totalmnk;
        var   isEnd=false;
        var   tmp=TheDate.getYear();
        if   (tmp<1900)     tmp+=1900;
        total=(tmp-2001)*365
                +Math.floor((tmp-2001)/4)
                +madd[TheDate.getMonth()]
                +TheDate.getDate()
                -23;
        if   (TheDate.getYear()%4==0&&TheDate.getMonth()>1)
            total++;
        for(m=0;;m++)
        {
            k=(CalendarData[m]<0xfff)?11:12;
            for(n=k;n>=0;n--)
            {
                if(total<=29+GetBit(CalendarData[m],n))
                {
                    isEnd=true;
                    break;
                }
                total=total-29-GetBit(CalendarData[m],n);
            }
            if(isEnd)break;
        }
        cYear=2001   +   m;
        cMonth=k-n+1;
        cDay=total;
        if(k==12)
        {
            if(cMonth==Math.floor(CalendarData[m]/0x10000)+1)
                cMonth=1-cMonth;
            if(cMonth>Math.floor(CalendarData[m]/0x10000)+1)
                cMonth--;
        }
        cHour=Math.floor((TheDate.getHours()+3)/2);
    }

    function   GetcDateString()
    {   var   tmp="";

        if(cMonth<1)
        {
            tmp+="闰";
            tmp+=monString.charAt(-cMonth-1);
			
        }
        else
            tmp+=monString.charAt(cMonth-1);
        tmp+="月";
        tmp+=(cDay<11)?"初":((cDay<20)?"十":((cDay<30)?"廿":"卅"));
        if(cDay%10!=0||cDay==10)
            tmp+=numString.charAt((cDay-1)%10);
        tmp+="    ";
        cDateString=tmp;
        return   tmp;
    }

    function   GetDateString()
    {
        var   tmp="";
        var   t1=TheDate.getYear();
        if   (t1<1900)t1+=1900;
        tmp+=t1
                +"年"
                +(TheDate.getMonth()+1)+"月"
                +TheDate.getDate()+"日   "
                +TheDate.getHours()+":"
                +((TheDate.getMinutes()<10)?"0":"")
                +TheDate.getMinutes()
                +" 星期"+weekString.charAt(TheDate.getDay());
        DateString=tmp;
        return   tmp;
    }

    init();
    e2c();
    GetDateString();
    GetcDateString();
    //document.write(DateString+" 农历"+cDateString);
</script>
<style>
.nav li{padding-left:40px;width:auto;}
</style>
<div class="logo">
    	
        <div class="logo_right">
            <a class="text"><script type="text/javascript">document.write(month);</script>月<script type="text/javascript">document.write(date);</script>日<br>农历&nbsp;&nbsp;<script type="text/javascript">document.write(cDateString);</script>&nbsp;&nbsp;霜降</a>
			
			
					
			
			
			
			

			
					
			
			
			
			

			
					
			
			
			
			
					<img src="http://www.cnta.gov.cn/images/shuangjiang.png" />
			

			
					
			
			
			
			
			
        </div>
        <a href="http://www.cnta.gov.cn"><img src="/images/logo.png" />

</a>
    </div>
 <div class="nav">
    	<ul>
        	
            <li class="m1"><a  href="http://www.cnta.gov.cn/jgjj/lyjjj/">机构简介</a></li>     
            <li class="m2"><a  href="http://www.cnta.gov.cn/xxfb/">信息发布</a></li>
            <li class="m3"><a  href="http://www.cnta.gov.cn/zwgk/">政府信息公开</a></li>
            <li class="m4"><a   href="http://www.cnta.gov.cn/hygq/">回应关切</a></li>
            <li class="m5"><a  href="http://www.cnta.gov.cn/bsdt/zwgk/">办事大厅</a></li>
            <li class="m6"><a  href="http://www.cnta.gov.cn/zdzx/">重点专项</a></li>
            <li class="m7"><a  href="http://www.cnta.gov.cn/was5/web/search?channelid=242887">旅游名录</a></li>
            <li class="m8" style="padding-left:40px; width:72px;"><a  href="http://www.cnta.gov.cn/xwfbh/" style="letter-spacing:-2px;">新闻发布会</a></li>
            <li class="m9"><a  href="http://www.cnta.gov.cn/spzl" style="letter-spacing:-2px;">视频专栏</a></li>
            <div class="nav_h"></div>
            <div class="nav_h1"></div>
        </ul>
    </div>
    <div class="main_local marl30">
    	当前位置：<a href="../../" target="_blank" title="首页">首页</a>><a href="../" target="_blank" title="重点工作">重点工作</a>><a href="./" title="市场推广" class='blue CurrChnlCls'>市场推广</a>
    </div>
	<div class="liebiao">
        
    	        <div class="lie_main_m">
            <ul>
                
                <li><a target="_blank" href="./201710/t20171013_842393.shtml"><span>2017-10-14</span>区域品牌化 浙江绍兴美丽乡村成“旅游胜地”</a></li>
                
                <li><a target="_blank" href="./201710/t20171009_841863.shtml"><span>2017-10-10</span>“多家电视媒体走进大别山风景道采风活动”成功举办</a></li>
                
                <li><a target="_blank" href="./201710/t20171013_842368.shtml"><span>2017-10-15</span>2017慈溪养生旅游节隆重开幕</a></li>
                
                <li><a target="_blank" href="./201710/t20171010_842017.shtml"><span>2017-10-11</span>魅力北京温哥华推介会及图片展成功举办</a></li>
                
                <li><a target="_blank" href="./201710/t20171013_842337.shtml"><span>2017-10-14</span>千岛湖登全球热搜榜第13位 “双节”旅游大丰收</a></li>
                
                <li><a target="_blank" href="./201710/t20171002_841328.shtml"><span>2017-10-05</span>“丝路明珠 魅力银川”全域旅游嘉年华启幕</a></li>
                
                <li><a target="_blank" href="./201710/t20171001_841310.shtml"><span>2017-10-04</span>四川推出川南和川东北区域十条精品旅游线路</a></li>
                
                <li><a target="_blank" href="./201710/t20171001_841306.shtml"><span>2017-10-03</span>惠州推出八大精彩旅游产品</a></li>
                
                <li><a target="_blank" href="./201710/t20171001_841303.shtml"><span>2017-10-03</span>北京国际旅游节开幕 丝路主题展现各国风情</a></li>
                
                <li><a target="_blank" href="./201709/t20170926_840605.shtml"><span>2017-09-27</span>“七彩云南 乐享世博”旅游生活推介会在玉溪举行</a></li>
                
                <li><a target="_blank" href="./201709/t20170926_840586.shtml"><span>2017-09-27</span>琼州海峡交通港航旅游一体化推介会在广东徐闻县举行</a></li>
                
                <li><a target="_blank" href="./201709/t20170925_840521.shtml"><span>2017-09-26</span>黄山市特色小镇专题培训班和招商推介会在上海举办</a></li>
                
                <li><a target="_blank" href="./201709/t20170925_840487.shtml"><span>2017-09-26</span>梅州、潮州旅游推介走进大连 资源优势互补</a></li>
                
                <li><a target="_blank" href="./201709/t20170926_840692.shtml"><span>2017-09-26</span>内蒙古旅游暨“万里茶道”国际旅游推介会在呼和浩特市举办</a></li>
                
                <li><a target="_blank" href="./201709/t20170917_839529.shtml"><span>2017-09-17</span>世界旅游合作引起强烈共鸣——与会代表高度评价本届大会总结发言</a></li>
                
                <li><a target="_blank" href="./201709/t20170915_839429.shtml"><span>2017-09-15</span>2017年中俄红色旅游合作交流系列活动暨首届湘赣边红色旅游节将于湖南举行</a></li>
                
                <li><a target="_blank" href="./201708/t20170828_837192.shtml"><span>2017-08-28</span>山东打破旅游商品研发瓶颈 向海内外推荐60个“新作”</a></li>
                
                <li><a target="_blank" href="./201708/t20170827_837100.shtml"><span>2017-08-27</span>香港旅游热度上涨 多元“港味”成发展新趋势</a></li>
                
                <li><a target="_blank" href="./201708/t20170824_836756.shtml"><span>2017-08-24</span>增进两岸感情促进业界合作</a></li>
                
                <li><a target="_blank" href="./201708/t20170825_836934.shtml"><span>2017-08-25</span>全域旅游广西模式提升与推广座谈会举行</a></li>
                
            </ul>
        </div>
        
        <div class='page'><script language="javascript">
	var currentPage=0;
	var prevPage=currentPage-1;
	var nextPage=currentPage+1;
	var countPage=11;
	var endPage=countPage-1;
	if(countPage>1){
	document.write("<a href=\"index.shtml\" target=\"_self\" class='index'>首页</a>&nbsp;");
	}
	if(countPage>1&&currentPage!=0&&currentPage!=1)
document.write("<a href=\"index"+"_"+prevPage+"."+"shtml\" target=\"_self\">上一页</a>&nbsp;");
	else if(countPage>1&&currentPage!=0&&currentPage==1)
document.write("<a  href=\"index.shtml\" target=\"_self\">上一页</a>&nbsp;");
	else
document.write("<a class='tow'>上一页</a>&nbsp;");
	var num=6;
	var startPage=currentPage-2;
	if(startPage<0)startPage=0;
	var endpage=startPage+num;
	if(endpage>countPage)
	endpage=countPage;
	startPage=endpage-6;
	if(startPage<0)startPage=0;
	for(var i=startPage;i<endpage;i++){
		if(currentPage==i)
document.write("<a class='hover'>"+(i+1)+"</a>&nbsp;");
	else if(i==0){
document.write("<a  href=\"index.shtml\" target=\"_self\">"+1+"</a>&nbsp;");
		 }else
document.write("<a href=\"index"+"_"+i+"."+"shtml\" target=\"_self\">"+(i+1)+"</a>&nbsp;");}
	if(countPage>1&&currentPage!=(countPage-1))
document.write("<a class='tow' href=\"index"+"_"+nextPage+"."+"shtml\" target=\"_self\">下一页</a>&nbsp;");
	else
document.write("<a class='tow'>下一页</a>&nbsp;");
    	if(countPage>1){
	document.write("<a class='index'  href=\"index_"+endPage+".shtml\" target=\"_self\">尾页</a>");
		}
</script></div>
    </div>
</div>
<!--footer嵌套开始-->
<script language="javascript" type="text/javascript"> 
				function location1(s)
                {       var d = s.options[s.selectedIndex].value;
						if ((navigator.userAgent.match(/(iPhone|iPod|Android|ios|SymbianOS)/i))) {
						 	location.href=d;
						}
                     	else
							window.open(d,"_blank");
						s.selectedIndex=0;       
                }

</script>
<script>
$(function(){
$('.r_close').click(function(){
$('.r_close, .weibo, .weixin, .gaibian, .searchf').hide();




})
if($(window).width()<1282){
$('.r_close, .weibo, .weixin').css('left', 'auto').css('right', '10px');
$('.gaibian, .searchf').css('left', 'auto').css('right', '25px');
}else{
$('.r_close, .weibo, .weixin, .gaibian, .searchf').css('left', '50%').css('right', 'auto');
}
$(window).resize(function() {
 if($(window).width()<1282){
$('.r_close, .weibo, .weixin').css('left', 'auto').css('right', '10px');
$('.gaibian, .searchf').css('left', 'auto').css('right', '25px');
}else{
$('.r_close, .weibo, .weixin, .gaibian, .searchf').css('left', '50%').css('right', 'auto');
}
})
})
</script>
<div class="foot">
	<div class="footer">
    	<div class="footer_t">
        	<select name="m1" onChange="location1(this)" ID="Select1">
        <option selected="selected">国务院部委网站</option>
          
          <option value="http://www.mfa.gov.cn/mfa_chn/">外交部</option>
          
          <option value="http://www.mod.gov.cn/">国防部</option>
          
          <option value="http://www.ndrc.gov.cn/">发展改革委</option>
          
          <option value="http://www.moe.gov.cn/">教育部</option>
          
          <option value="http://www.most.gov.cn/">科技部</option>
          
          <option value="http://www.miit.gov.cn/n11293472/index.html">工业和信息化部</option>
          
          <option value="http://www.seac.gov.cn/">国家民委</option>
          
          <option value="http://www.mps.gov.cn/n16/index.html?_v=1435138159749">公安部</option>
          
          <option value="http://www.ccdi.gov.cn/">监察部</option>
          
          <option value="http://www.mca.gov.cn/">民政部</option>
          
          <option value="http://www.moj.gov.cn/">司法部</option>
          
          <option value="http://www.mof.gov.cn/index.htm">财政部</option>
          
          <option value="http://www.mohrss.gov.cn/">人力资源社会保障部</option>
          
          <option value="http://www.mlr.gov.cn/">国土资源部</option>
          
          <option value="http://www.mep.gov.cn/">环境保护部</option>
          
          <option value="http://www.mohurd.gov.cn/">住房城乡建设部</option>
          
          <option value="http://www.mot.gov.cn/">交通运输部</option>
          
          <option value="http://www.mwr.gov.cn/">水利部</option>
          
          <option value="http://www.moa.gov.cn/">农业部</option>
          
          <option value="http://www.mofcom.gov.cn/">商务部</option>
          
          <option value="http://www.mcprc.gov.cn/">文化部</option>
          
          <option value="http://www.nhfpc.gov.cn/">卫生计生委</option>
          
          <option value="http://www.pbc.gov.cn/">人民银行</option>
          
          <option value="http://www.audit.gov.cn/">审计署</option>
          
          <option value="http://www.china-language.gov.cn/">国家语委</option>
          
          <option value="http://www.cnsa.gov.cn/">航天局</option>
          
          <option value="http://www.caea.gov.cn/">原子能机构</option>
          
          <option value="http://www.sasac.gov.cn/">国资委</option>
          
          <option value="http://www.customs.gov.cn/publish/portal0/">海关总署</option>
          
          <option value="http://www.chinatax.gov.cn/">税务总局</option>
          
          <option value="http://www.saic.gov.cn/">工商总局</option>
          
          <option value="http://www.aqsiq.gov.cn/">质检总局</option>
          
          <option value="http://www.sapprft.gov.cn/">新闻出版广电总局</option>
          
          <option value="http://www.sport.gov.cn/">体育总局</option>
          
          <option value="http://www.chinasafety.gov.cn/newpage/">安全监管总局</option>
          
          <option value="http://www.sda.gov.cn/WS01/CL0001/">食品药品监管总局</option>
          
          <option value="http://www.stats.gov.cn/">统计局</option>
          
          <option value="http://www.forestry.gov.cn/">林业局</option>
          
          <option value="http://www.sipo.gov.cn/">知识产权局</option>
          
          <option value="http://www.sara.gov.cn/">宗教局</option>
          
          <option value="http://www.counsellor.gov.cn/">参事室</option>
          
          <option value="http://www.ggj.gov.cn/">国管局</option>
          
          <option value="http://www.ncac.gov.cn/">版权局</option>
          
          <option value="http://www.gqb.gov.cn/">侨办</option>
          
          <option value="http://www.hmo.gov.cn/">港澳办</option>
          
          <option value="http://www.chinalaw.gov.cn/">法制办</option>
          
          <option value="http://www.gov.cn/guoqing/2005-12/26/content_2652073.htm">国研室</option>
          
          <option value="http://www.gwytb.gov.cn/">台办</option>
          
          <option value="http://www.scio.gov.cn/">新闻办</option>
          
          <option value="http://www.xinhuanet.com/">新华社</option>
          
          <option value="http://www.cas.cn/">中科院</option>
          
          <option value="http://cass.cssn.cn/">社科院</option>
          
          <option value="http://www.cae.cn/cae/html/main/index.html">工程院</option>
          
          <option value="http://www.drc.gov.cn/">发展研究中心</option>
          
          <option value="http://www.nsa.gov.cn/web/index.php">行政学院</option>
          
          <option value="http://www.cea.gov.cn/">地震局</option>
          
          <option value="http://www.cma.gov.cn/">气象局</option>
          
          <option value="http://www.cbrc.gov.cn/index.html">银监会</option>
          
          <option value="http://www.csrc.gov.cn/pub/newsite/">证监会</option>
          
          <option value="http://www.circ.gov.cn/web/site0/">保监会</option>
          
          <option value="http://www.ssf.gov.cn/">社保基金会</option>
          
          <option value="http://www.nsfc.gov.cn/">自然科学基金会</option>
          
          <option value="http://www.gjxfj.gov.cn/">信访局</option>
          
          <option value="http://www.chinagrain.gov.cn/">粮食局</option>
          
          <option value="http://www.nea.gov.cn/">能源局</option>
          
          <option value="http://www.sastind.gov.cn/">国防科工局</option>
          
          <option value="http://www.tobacco.gov.cn/">烟草局</option>
          
          <option value="http://www.safea.gov.cn/">外专局</option>
          
          <option value="http://www.scs.gov.cn/">公务员局</option>
          
          <option value="http://www.soa.gov.cn/">海洋局</option>
          
          <option value="http://www.sbsm.gov.cn/">测绘地信局</option>
          
          <option value="http://www.nra.gov.cn/">铁路局</option>
          
          <option value="http://www.caac.gov.cn/">民航局</option>
          
          <option value="http://www.spb.gov.cn/">邮政局</option>
          
          <option value="http://www.sach.gov.cn/">文物局</option>
          
          <option value="http://www.satcm.gov.cn/">中医药局</option>
          
          <option value="http://www.safe.gov.cn/">外汇局</option>
          
          <option value="http://www.chinacoal-safety.gov.cn/mkaj/">煤矿安监局</option>
          
          <option value="http://www.saac.gov.cn/">档案局</option>
          
          <option value="http://www.oscca.gov.cn/">密码局</option>
          
          <option value="http://www.cpad.gov.cn/">扶贫办</option>
          
          <option value="http://www.3g.gov.cn/index.ycs">三峡办</option>
          
          <option value="http://www.nsbd.gov.cn/">南水北调办</option>
          
        </select>
        <select name="m2" onChange="location1(this)" ID="Select1">
        <option selected="selected">各省旅游政务网</option>
          
          <option value="http://www.bjta.gov.cn/">北京旅游网</option>
          
          <option value="http://www.tjtour.cn/">天津旅游网</option>
          
          <option value="http://www.hebeitour.gov.cn/index.php">河北旅游网</option>
          
          <option value="http://www.shanxichina.gov.cn">山西旅游网</option>
          
          <option value="http://www.nmgtour.gov.cn/">内蒙古旅游网</option>
          
          <option value="http://www.lntour.gov.cn/">辽宁旅游网</option>
          
          <option value="http://www.jlta.gov.cn/">吉林旅游网</option>
          
          <option value="http://www.hljtour.gov.cn/">黑龙江旅游网</option>
          
          <option value="http://lyw.sh.gov.cn/">上海旅游网</option>
          
          <option value="http://www.jstour.com/">江苏旅游网</option>
          
          <option value="http://www.tourzj.gov.cn/">浙江旅游网</option>
          
          <option value="http://www.ahta.com.cn/">安徽旅游网</option>
          
          <option value="http://www.fjta.gov.cn/">福建旅游网</option>
          
          <option value="http://www.jxta.gov.cn/">江西旅游网</option>
          
          <option value="http://www.sdta.gov.cn/">山东旅游网</option>
          
          <option value="http://www.hnta.cn/">河南旅游网</option>
          
          <option value="http://www.hubeitour.gov.cn/">湖北旅游网</option>
          
          <option value="http://www.hnt.gov.cn/">湖南旅游网</option>
          
          <option value="http://www.gdta.gov.cn/">广东旅游网</option>
          
          <option value="http://www.gxta.gov.cn/">广西旅游网</option>
          
          <option value="http://www.visithainan.gov.cn/government/">海南旅游网</option>
          
          <option value="http://www.cqta.gov.cn/">重庆旅游网</option>
          
          <option value="http://www.scta.gov.cn/sclyj/">四川旅游网</option>
          
          <option value="http://www.gztour.gov.cn/">贵州旅游网</option>
          
          <option value="http://www.innyo.com/">云南旅游网</option>
          
          <option value="http://www.xzta.gov.cn/index.html">西藏旅游网</option>
          
          <option value="http://sxta.gov.cn/sxtourgov/proscenium/index.html">陕西旅游网</option>
          
          <option value="http://www.gsta.gov.cn/">甘肃旅游网</option>
          
          <option value="http://www.nxtour.com.cn/">宁夏旅游网</option>
          
          <option value="http://www.qhly.gov.cn/">青海旅游网</option>
          
          <option value="http://www.xinjiangtour.gov.cn/">新疆旅游网</option>
          
          <option value="http://www.discoverhongkong.com/china/index.jsp">香港旅游发展局</option>
          
          <option value="http://www.macautourism.gov.mo/">澳门特别行政区旅游局</option>
          
          <option value="http://www.btwql.gov.cn/">兵团旅游网</option>
          
        </select>
        <select name="m3" onChange="location1(this)" ID="Select1">
        <option selected="selected">国际旅游组织</option>
          
          <option value="http://www2.unwto.org/">联合国世界旅游组织</option>
          
          <option value="http://www.fia.com/">国际汽车运动联合会</option>
          
          <option value="http://www.pata.org/">亚太旅游协会</option>
          
          <option value="http://www.apec.org/">亚太经合组织</option>
          
          <option value="http://www.asta.org/">美国旅行代理商协会</option>
          
          <option value="http://ih-ra.com/">国际饭店与餐饮协会</option>
          
        </select>
        <select name="m4" onChange="location1(this)" ID="Select1">
        <option selected="selected">驻华旅游组织</option>
          
          <option value="../../yqlj/zhlyzz/201507/t20150701_719902.shtml">港澳台驻内地办事处</option>
          
          <option value="../../yqlj/zhlyzz/201506/t20150624_273197.shtml">各国旅游机构驻华办事处</option>
          
        </select>
        <select name="m5" onChange="location1(this)" ID="Select1">
        <option selected="selected">友情链接</option>
          
          <option value="https://zygjjg.12388.gov.cn/">中央国家机关举报网站</option>
          
          <option value="../../yqlj/yqlj/lyyx/">旅游院校</option>
          
          <option value="../../yqlj/yqlj/lypd/">旅游频道</option>
          
          <option value="../../yqlj/yqlj/yqljqt/">其他</option>
          
        </select>
        </div>
        <div class="footer_l">
     
<script type="text/javascript">document.write(unescape("%3Cspan id='_ideConac' %3E%3C/span%3E%3Cscript src='http://dcs.conac.cn/js/33/000/0000/40672416/CA330000000406724160003.js' type='text/javascript'%3E%3C/script%3E"));</script>

            <a><img src="http://www.cnta.gov.cn/images/red1.png" /></a>
        </div>
        <div class="footer_r">
        	<p><a target="_blank" href="http://www.cnta.gov.cn/lxwm/" >联系我们 </a>| <a target="_blank" href="http://www.cnta.gov.cn/wzdt/" >网站地图</a> | <a target="_blank" href="http://www.cnta.gov.cn/download/" >下载中心</a></p>
            <p>版权所有：中华人民共和国国家旅游局  网站管理：国家旅游局信息中心</p>
            <p>管理员邮箱：webmaster@cnta.gov.cn  京ICP备15046657号</p>
            <p>建议使用IE8以上浏览器</p>
        </div>
        <div style="float:left;width:120px;height:55px;margin-left:15px;margin-top:65px;">
        <script id="_jiucuo_" sitecode='bm39000001' src='http://pucha.kaipuyun.cn/exposure/jiucuo.js'></script>
        </div>
        <div class="clear"></div>
    </div>
</div>
<script type="text/javascript">
    var _bdhmProtocol = (("https:" == document.location.protocol) ? " https://" : " http://");
    document.write(unescape("%3Cscript src='" + _bdhmProtocol + "hm.baidu.com/h.js%3F1012c8757d7968f19279de5b5d3bc73b' type='text/javascript'%3E%3C/script%3E"));
</script>
<script type='text/javascript' src='http://static.gridsumdissector.com/js/Clients/GWD-801536-A2CC10/gs.js'></script>
<noscript><img src="http://ta.trs.cn/c/1.gif?mpId=364&jsoff=1" style="border:0" alt="" /></noscript>
<script>
var _taq = _taq || [];
_taq.home = 'http://ta.trs.cn/c';
_taq.push(['_mpId', '364']);
_taq.push(['_cli', '1']);
(function(d, o, t) {
	if (window.inTRSDesignMode) return;
	var ma = d.createElement(o); ma.async = true; ma.commonresource="1"; ma.src = t;
	var s = d.getElementsByTagName(o)[0]; s.parentNode.insertBefore(ma, s);
})(document, 'script', 'http://ta.trs.cn/c/js/ta.js');
</script>
<div class="r_close" style='bottom:340px;'>
<img src='http://www.cnta.gov.cn/images/close140403.gif' />
</div>
<!--<div  class="weibo" style='margin-left: -663px; bottom:366px;padding: 4px; height:134px'>
<a href='http://www.cnta.gov.cn/ztwz/czczl/'><img src="http://www.cnta.gov.cn/zylcfctpwh/images/P020161130627556356561.jpg" width="66" height="134" style="height:134px;" /></a>
</div>-->
<!--20170411注释
<div  class="weibo" style='margin-left: -663px; bottom: 366px;padding: 4px; height:134px'>
<a href='http://www.cnta.gov.cn/ztwz/lxyz/'><img src="http://www.cnta.gov.cn/zylcfctpwh/images/P020161019552215694719.jpg" width="66" height="134" style="height:134px;" /></a>
</div>

<div  class="weibo" style='margin-left: -663px; bottom: 214px;padding: 4px; height:134px'>
<a href='http://www.cnta.gov.cn/ztwz/lmhdzt/'><img src="http://www.cnta.gov.cn/zylcfctpwh/images/P020161019552576053500.jpg" width="66" height="134" style="height:134px;" /></a>
</div>

<div  class="weibo" style='margin-left: -663px; bottom: 62px;padding: 4px; height:134px'>
<a href='http://www.cnta.gov.cn/ztwz/dsjqgdyds/'><img src="http://www.cnta.gov.cn/zylcfctpwh/images/P020170314589555319942.jpg" width="66" height="134" style="height:134px;" /></a>
</div>






<div class="weixin" style="height:auto;bottom:363px;padding:4px;">
	<a href='http://www.cnta.gov.cn/ztwz/2017bflyngycfz/'><img src="http://www.cnta.gov.cn/zylcfctpwh/images/P020170203348421395926.jpg" width="66" height="134" style="height:134px;" /></a>
</div>

<div class="weixin" style="height:auto;bottom:212px;padding:4px;">
	<a href='http://dj.cnta.gov.cn/'><img src="http://www.cnta.gov.cn/zylcfctpwh/images/P020161019552462328276.jpg" width="66" height="134" style="height:134px;" /></a>
</div>
<div class="weixin" style="height:auto;bottom:60px;padding:4px;">
	<a href='http://www.cnta.gov.cn/ztwz/jtly/'><img src="http://www.cnta.gov.cn/zylcfctpwh/images/P020170228612233591893.jpg" width="66" height="134" style="height:134px;" /></a>
</div>-->
<div class="weibo" style="bottom:90px;padding:4px;">
	<img src="http://www.cnta.gov.cn/images/weibo.jpg" />
    <span>国家旅游局</span>
    <span style="letter-spacing:3px;">官方微博</span>
</div>
<div class="weixin" style="bottom:220px;padding:4px;">
	<img src="http://www.cnta.gov.cn/ty/includefooter/images/P020160309356126439106.jpg" width="66" />
    <span>国家旅游局</span>
    <span style="letter-spacing:3px;">官方微信</span>
</div>
<!--
<a class="gaibian" href="http://www.cnta.gov.cn/xxfb/gbtz/"  ignoreapd="true" >
	图片征集
</a>-->
<!--<a class="gaibian" href="http://city.sina.com.cn/2016lyzj/index.shtml?qq-pf-to=pcqq.c2c"  ignoreapd="true" style='background:none;bottom:80px;margin-left:590px;'>
<img src="http://www.cnta.gov.cn/images/Icon_logo20160530.jpg" width="52" height="52" style='margin-top:-30px' />
</a>-->
<!--30,180-->
<div class="searchf" style="bottom:20px;margin-left:590px;">
	搜 索
    <div class="searchf2">
        <div class="searchf1">
        <form name="searchform" id="searchform" action="http://www.cnta.gov.cn/was5/web/search?channelid=261012" method="post" target="_blank">
            <input id="textfield" type="text" name="searchword" class="" value="" />
				<input type="hidden" name="perpage" value="" />
				<input type="hidden" name="templet" value="" />
				<input type="hidden" name="token" value="" />
				<input type="hidden" name="channelid" value="261012" />
				<input type="submit" value="搜索" />
        </form>
        </div>
    </div>
</div>



<script>
var _hmt = _hmt || [];
(function() {
  var hm = document.createElement("script");
  hm.src = "//hm.baidu.com/hm.js?2a7d9fd86036a721a0f0895061ae1ad7";
  var s = document.getElementsByTagName("script")[0]; 
  s.parentNode.insertBefore(hm, s);
})();
</script>
<!--footer嵌套结束-->

</body>
</html>
"""

html3 = """

<!doctype html>
<html>
<head>
<meta charset="utf-8">
<meta http-equiv="X-UA-Compatible" content="IE=edge">
<link href="../../images/base.css" rel="stylesheet" />
<link href="../../images/lby.css" rel="stylesheet" />
<title>文明旅游</title>
<script src="../../images/jquery-1.11.0.min.js" /></script>
<script src="../../images/nav_er.js" /></script>
<!--[if IE 6]>
<script type="text/javascript" src="../../images/png.js"></script>
<script>
PNG.fix('*'); 
</script>
<![endif]-->
</head>
<body>
<link rel="Shortcut Icon" type="image/x-icon" href="../../images/favicon.ico">
<script language='javascript' src='http://www.cnta.gov.cn/images/zh.js'></script>
<div class="top">
	<div class="top1">
    	<div class="top_left">
            <a href="javascript:zh_tran('s');" target="_self">简体</a>
            <a href="javascript:zh_tran('t');" target="_self">繁体</a>
            <a href="http://en.cnta.gov.cn">English</a>
        </div>
        <div class="top_left top_right">
            <a href="http://www.cnta.gov.cn">返回首页</a>
        	<a href="javascript:;" onclick="AddFavorite('http://www.cnta.gov.cn/',location.href)">加入收藏</a>
          <!--  <a href="http://www1.cnta.gov.cn">返回旧版</a>-->
            <a href="http://mail.cnta.gov.cn/" target="_blank">邮箱登录</a>
        </div>
    </div>
</div>
<div class="main">
    <script type="text/javascript">
  var today = new Date();
  var date = today.getDate();
  var day = today.getDay();
  var month = today.getMonth()+1;
  var year = today.getYear();
</script>
<script>
    var   CalendarData=new   Array(20);
    var   madd=new Array(12);
    var   TheDate=new Date();
    var   tgString="甲乙丙丁戊己庚辛壬癸";
    var   dzString="子丑寅卯辰巳午未申酉戌亥";
    var   numString="一二三四五六七八九十";
    var   monString="正二三四五六七八九十冬腊";
    var   weekString="日一二三四五六";
    var   sx="鼠牛虎兔龙蛇马羊猴鸡狗猪";
    var   cYear;
    var   cMonth;
    var   cDay;
    var   cHour;
    var   cDateString;
    var   DateString;
    var   Browser=navigator.appName;

    function   init()
    {
        CalendarData[0]=0x41A95;
        CalendarData[1]=0xD4A;
        CalendarData[2]=0xDA5;
        CalendarData[3]=0x20B55;
        CalendarData[4]=0x56A;
        CalendarData[5]=0x7155B;
        CalendarData[6]=0x25D;
        CalendarData[7]=0x92D;
        CalendarData[8]=0x5192B;
        CalendarData[9]=0xA95;
        CalendarData[10]=0xB4A;
        CalendarData[11]=0x416AA;
        CalendarData[12]=0xAD5;
        CalendarData[13]=0x90AB5;
        CalendarData[14]=0x4BA;
        CalendarData[15]=0xA5B;
        CalendarData[16]=0x60A57;
        CalendarData[17]=0x52B;
        CalendarData[18]=0xA93;
        CalendarData[19]=0x40E95;
        madd[0]=0;
        madd[1]=31;
        madd[2]=59;
        madd[3]=90;
        madd[4]=120;
        madd[5]=151;
        madd[6]=181;
        madd[7]=212;
        madd[8]=243;
        madd[9]=273;
        madd[10]=304;
        madd[11]=334;
    }

    function   GetBit(m,n)
    {
        return   (m>>n)&1;
    }

    function   e2c()
    {
        var   totalmnk;
        var   isEnd=false;
        var   tmp=TheDate.getYear();
        if   (tmp<1900)     tmp+=1900;
        total=(tmp-2001)*365
                +Math.floor((tmp-2001)/4)
                +madd[TheDate.getMonth()]
                +TheDate.getDate()
                -23;
        if   (TheDate.getYear()%4==0&&TheDate.getMonth()>1)
            total++;
        for(m=0;;m++)
        {
            k=(CalendarData[m]<0xfff)?11:12;
            for(n=k;n>=0;n--)
            {
                if(total<=29+GetBit(CalendarData[m],n))
                {
                    isEnd=true;
                    break;
                }
                total=total-29-GetBit(CalendarData[m],n);
            }
            if(isEnd)break;
        }
        cYear=2001   +   m;
        cMonth=k-n+1;
        cDay=total;
        if(k==12)
        {
            if(cMonth==Math.floor(CalendarData[m]/0x10000)+1)
                cMonth=1-cMonth;
            if(cMonth>Math.floor(CalendarData[m]/0x10000)+1)
                cMonth--;
        }
        cHour=Math.floor((TheDate.getHours()+3)/2);
    }

    function   GetcDateString()
    {   var   tmp="";

        if(cMonth<1)
        {
            tmp+="闰";
            tmp+=monString.charAt(-cMonth-1);
			
        }
        else
            tmp+=monString.charAt(cMonth-1);
        tmp+="月";
        tmp+=(cDay<11)?"初":((cDay<20)?"十":((cDay<30)?"廿":"卅"));
        if(cDay%10!=0||cDay==10)
            tmp+=numString.charAt((cDay-1)%10);
        tmp+="    ";
        cDateString=tmp;
        return   tmp;
    }

    function   GetDateString()
    {
        var   tmp="";
        var   t1=TheDate.getYear();
        if   (t1<1900)t1+=1900;
        tmp+=t1
                +"年"
                +(TheDate.getMonth()+1)+"月"
                +TheDate.getDate()+"日   "
                +TheDate.getHours()+":"
                +((TheDate.getMinutes()<10)?"0":"")
                +TheDate.getMinutes()
                +" 星期"+weekString.charAt(TheDate.getDay());
        DateString=tmp;
        return   tmp;
    }

    init();
    e2c();
    GetDateString();
    GetcDateString();
    //document.write(DateString+" 农历"+cDateString);
</script>
<style>
.nav li{padding-left:40px;width:auto;}
</style>
<div class="logo">
    	
        <div class="logo_right">
            <a class="text"><script type="text/javascript">document.write(month);</script>月<script type="text/javascript">document.write(date);</script>日<br>农历&nbsp;&nbsp;<script type="text/javascript">document.write(cDateString);</script>&nbsp;&nbsp;霜降</a>
			
			
					
			
			
			
			

			
					
			
			
			
			

			
					
			
			
			
			
					<img src="http://www.cnta.gov.cn/images/shuangjiang.png" />
			

			
					
			
			
			
			
			
        </div>
        <a href="http://www.cnta.gov.cn"><img src="/images/logo.png" />

</a>
    </div>
 <div class="nav">
    	<ul>
        	
            <li class="m1"><a  href="http://www.cnta.gov.cn/jgjj/lyjjj/">机构简介</a></li>     
            <li class="m2"><a  href="http://www.cnta.gov.cn/xxfb/">信息发布</a></li>
            <li class="m3"><a  href="http://www.cnta.gov.cn/zwgk/">政府信息公开</a></li>
            <li class="m4"><a   href="http://www.cnta.gov.cn/hygq/">回应关切</a></li>
            <li class="m5"><a  href="http://www.cnta.gov.cn/bsdt/zwgk/">办事大厅</a></li>
            <li class="m6"><a  href="http://www.cnta.gov.cn/zdzx/">重点专项</a></li>
            <li class="m7"><a  href="http://www.cnta.gov.cn/was5/web/search?channelid=242887">旅游名录</a></li>
            <li class="m8" style="padding-left:40px; width:72px;"><a  href="http://www.cnta.gov.cn/xwfbh/" style="letter-spacing:-2px;">新闻发布会</a></li>
            <li class="m9"><a  href="http://www.cnta.gov.cn/spzl" style="letter-spacing:-2px;">视频专栏</a></li>
            <div class="nav_h"></div>
            <div class="nav_h1"></div>
        </ul>
    </div>
    <div class="main_local marl30">
    	当前位置：<a href="../../" target="_blank" title="首页">首页</a>><a href="../" target="_blank" title="重点工作">重点工作</a>><a href="./" title="文明旅游" class='blue CurrChnlCls'>文明旅游</a>
    </div>
	<div class="liebiao">
        
    	        <div class="lie_main_m">
            <ul>
                
                <li><a target="_blank" href="./201710/t20171002_841330.shtml"><span>2017-10-05</span>黄金周，将文明旅游进行到底</a></li>
                
                <li><a target="_blank" href="./201709/t20170918_839649.shtml"><span>2017-09-18</span>江苏省旅游局举办全省旅游行业青年文明号创建负责人培训班</a></li>
                
                <li><a target="_blank" href="./201709/t20170916_839472.shtml"><span>2017-09-17</span>安徽省旅游局组织开展“文明旅游进社区”志愿者服务活动</a></li>
                
                <li><a target="_blank" href="./201709/t20170914_839191.shtml"><span>2017-09-15</span>山东省启动2017文明旅游志愿服务行动</a></li>
                
                <li><a target="_blank" href="./201709/t20170912_838918.shtml"><span>2017-09-13</span>滁州：加强文明旅游宣传 扩大网络文明阵地</a></li>
                
                <li><a target="_blank" href="./201708/t20170822_836515.shtml"><span>2017-08-22</span>黄山市旅委着力营造文明旅游环境</a></li>
                
                <li><a target="_blank" href="./201708/t20170821_836370.shtml"><span>2017-08-21</span>天津：文明旅游迎全运 手绘地图免费发</a></li>
                
                <li><a target="_blank" href="./201707/t20170717_832001.shtml"><span>2017-07-18</span>梅州市旅游局召开旅游系统创建“全国文明城市”工作会议</a></li>
                
                <li><a target="_blank" href="./201707/t20170717_831993.shtml"><span>2017-07-18</span>营造文明旅游环境 淄博市召开文明旅游工作布署视频会议</a></li>
                
                <li><a target="_blank" href="./201707/t20170716_831962.shtml"><span>2017-07-17</span>福州市部署暑期文明旅游工作 出境游先学文明课</a></li>
                
                <li><a target="_blank" href="./201707/t20170712_831471.shtml"><span>2017-07-13</span>暑期游迎高峰省旅发委提醒游客文明安全出行</a></li>
                
                <li><a target="_blank" href="./201707/t20170707_831032.shtml"><span>2017-07-10</span>暑运出行正当时 昆明机场开展宣传活动倡导文明出游</a></li>
                
                <li><a target="_blank" href="./201706/t20170616_828783.shtml"><span>2017-06-17</span>“文明旅游进社区”主题活动在津正式启动</a></li>
                
                <li><a target="_blank" href="./201706/t20170615_828591.shtml"><span>2017-06-16</span>济宁曲阜：优秀传统文化孕育曲阜文明旅游新风尚</a></li>
                
                <li><a target="_blank" href="./201706/t20170613_828458.shtml"><span>2017-06-13</span>广西举办大学生文明旅游主题活动</a></li>
                
                <li><a target="_blank" href="./201706/t20170609_827953.shtml"><span>2017-06-09</span>四名不文明游客被列入“黑名单”</a></li>
                
                <li><a target="_blank" href="./201706/t20170608_827897.shtml"><span>2017-06-08</span>山西依托青年文明号宣传文明旅游</a></li>
                
                <li><a target="_blank" href="./201706/t20170608_827894.shtml"><span>2017-06-08</span>贵州省2017年首例旅游不文明行为曝光</a></li>
                
                <li><a target="_blank" href="./201705/t20170531_827001.shtml"><span>2017-05-30</span>数说端午出行：对比五一拥堵大幅缓解 骑行出游热度高</a></li>
                
                <li><a target="_blank" href="./201705/t20170531_827000.shtml"><span>2017-05-30</span>成都机场迎来假期客流高峰 值机柜台提前至凌晨4时办理</a></li>
                
            </ul>
        </div>
        
        <div class='page'><script language="javascript">
	var currentPage=0;
	var prevPage=currentPage-1;
	var nextPage=currentPage+1;
	var countPage=12;
	var endPage=countPage-1;
	if(countPage>1){
	document.write("<a href=\"index.shtml\" target=\"_self\" class='index'>首页</a>&nbsp;");
	}
	if(countPage>1&&currentPage!=0&&currentPage!=1)
document.write("<a href=\"index"+"_"+prevPage+"."+"shtml\" target=\"_self\">上一页</a>&nbsp;");
	else if(countPage>1&&currentPage!=0&&currentPage==1)
document.write("<a  href=\"index.shtml\" target=\"_self\">上一页</a>&nbsp;");
	else
document.write("<a class='tow'>上一页</a>&nbsp;");
	var num=6;
	var startPage=currentPage-2;
	if(startPage<0)startPage=0;
	var endpage=startPage+num;
	if(endpage>countPage)
	endpage=countPage;
	startPage=endpage-6;
	if(startPage<0)startPage=0;
	for(var i=startPage;i<endpage;i++){
		if(currentPage==i)
document.write("<a class='hover'>"+(i+1)+"</a>&nbsp;");
	else if(i==0){
document.write("<a  href=\"index.shtml\" target=\"_self\">"+1+"</a>&nbsp;");
		 }else
document.write("<a href=\"index"+"_"+i+"."+"shtml\" target=\"_self\">"+(i+1)+"</a>&nbsp;");}
	if(countPage>1&&currentPage!=(countPage-1))
document.write("<a class='tow' href=\"index"+"_"+nextPage+"."+"shtml\" target=\"_self\">下一页</a>&nbsp;");
	else
document.write("<a class='tow'>下一页</a>&nbsp;");
    	if(countPage>1){
	document.write("<a class='index'  href=\"index_"+endPage+".shtml\" target=\"_self\">尾页</a>");
		}
</script></div>
    </div>
</div>
<!--footer嵌套开始-->
<script language="javascript" type="text/javascript"> 
				function location1(s)
                {       var d = s.options[s.selectedIndex].value;
						if ((navigator.userAgent.match(/(iPhone|iPod|Android|ios|SymbianOS)/i))) {
						 	location.href=d;
						}
                     	else
							window.open(d,"_blank");
						s.selectedIndex=0;       
                }

</script>
<script>
$(function(){
$('.r_close').click(function(){
$('.r_close, .weibo, .weixin, .gaibian, .searchf').hide();




})
if($(window).width()<1282){
$('.r_close, .weibo, .weixin').css('left', 'auto').css('right', '10px');
$('.gaibian, .searchf').css('left', 'auto').css('right', '25px');
}else{
$('.r_close, .weibo, .weixin, .gaibian, .searchf').css('left', '50%').css('right', 'auto');
}
$(window).resize(function() {
 if($(window).width()<1282){
$('.r_close, .weibo, .weixin').css('left', 'auto').css('right', '10px');
$('.gaibian, .searchf').css('left', 'auto').css('right', '25px');
}else{
$('.r_close, .weibo, .weixin, .gaibian, .searchf').css('left', '50%').css('right', 'auto');
}
})
})
</script>
<div class="foot">
	<div class="footer">
    	<div class="footer_t">
        	<select name="m1" onChange="location1(this)" ID="Select1">
        <option selected="selected">国务院部委网站</option>
          
          <option value="http://www.mfa.gov.cn/mfa_chn/">外交部</option>
          
          <option value="http://www.mod.gov.cn/">国防部</option>
          
          <option value="http://www.ndrc.gov.cn/">发展改革委</option>
          
          <option value="http://www.moe.gov.cn/">教育部</option>
          
          <option value="http://www.most.gov.cn/">科技部</option>
          
          <option value="http://www.miit.gov.cn/n11293472/index.html">工业和信息化部</option>
          
          <option value="http://www.seac.gov.cn/">国家民委</option>
          
          <option value="http://www.mps.gov.cn/n16/index.html?_v=1435138159749">公安部</option>
          
          <option value="http://www.ccdi.gov.cn/">监察部</option>
          
          <option value="http://www.mca.gov.cn/">民政部</option>
          
          <option value="http://www.moj.gov.cn/">司法部</option>
          
          <option value="http://www.mof.gov.cn/index.htm">财政部</option>
          
          <option value="http://www.mohrss.gov.cn/">人力资源社会保障部</option>
          
          <option value="http://www.mlr.gov.cn/">国土资源部</option>
          
          <option value="http://www.mep.gov.cn/">环境保护部</option>
          
          <option value="http://www.mohurd.gov.cn/">住房城乡建设部</option>
          
          <option value="http://www.mot.gov.cn/">交通运输部</option>
          
          <option value="http://www.mwr.gov.cn/">水利部</option>
          
          <option value="http://www.moa.gov.cn/">农业部</option>
          
          <option value="http://www.mofcom.gov.cn/">商务部</option>
          
          <option value="http://www.mcprc.gov.cn/">文化部</option>
          
          <option value="http://www.nhfpc.gov.cn/">卫生计生委</option>
          
          <option value="http://www.pbc.gov.cn/">人民银行</option>
          
          <option value="http://www.audit.gov.cn/">审计署</option>
          
          <option value="http://www.china-language.gov.cn/">国家语委</option>
          
          <option value="http://www.cnsa.gov.cn/">航天局</option>
          
          <option value="http://www.caea.gov.cn/">原子能机构</option>
          
          <option value="http://www.sasac.gov.cn/">国资委</option>
          
          <option value="http://www.customs.gov.cn/publish/portal0/">海关总署</option>
          
          <option value="http://www.chinatax.gov.cn/">税务总局</option>
          
          <option value="http://www.saic.gov.cn/">工商总局</option>
          
          <option value="http://www.aqsiq.gov.cn/">质检总局</option>
          
          <option value="http://www.sapprft.gov.cn/">新闻出版广电总局</option>
          
          <option value="http://www.sport.gov.cn/">体育总局</option>
          
          <option value="http://www.chinasafety.gov.cn/newpage/">安全监管总局</option>
          
          <option value="http://www.sda.gov.cn/WS01/CL0001/">食品药品监管总局</option>
          
          <option value="http://www.stats.gov.cn/">统计局</option>
          
          <option value="http://www.forestry.gov.cn/">林业局</option>
          
          <option value="http://www.sipo.gov.cn/">知识产权局</option>
          
          <option value="http://www.sara.gov.cn/">宗教局</option>
          
          <option value="http://www.counsellor.gov.cn/">参事室</option>
          
          <option value="http://www.ggj.gov.cn/">国管局</option>
          
          <option value="http://www.ncac.gov.cn/">版权局</option>
          
          <option value="http://www.gqb.gov.cn/">侨办</option>
          
          <option value="http://www.hmo.gov.cn/">港澳办</option>
          
          <option value="http://www.chinalaw.gov.cn/">法制办</option>
          
          <option value="http://www.gov.cn/guoqing/2005-12/26/content_2652073.htm">国研室</option>
          
          <option value="http://www.gwytb.gov.cn/">台办</option>
          
          <option value="http://www.scio.gov.cn/">新闻办</option>
          
          <option value="http://www.xinhuanet.com/">新华社</option>
          
          <option value="http://www.cas.cn/">中科院</option>
          
          <option value="http://cass.cssn.cn/">社科院</option>
          
          <option value="http://www.cae.cn/cae/html/main/index.html">工程院</option>
          
          <option value="http://www.drc.gov.cn/">发展研究中心</option>
          
          <option value="http://www.nsa.gov.cn/web/index.php">行政学院</option>
          
          <option value="http://www.cea.gov.cn/">地震局</option>
          
          <option value="http://www.cma.gov.cn/">气象局</option>
          
          <option value="http://www.cbrc.gov.cn/index.html">银监会</option>
          
          <option value="http://www.csrc.gov.cn/pub/newsite/">证监会</option>
          
          <option value="http://www.circ.gov.cn/web/site0/">保监会</option>
          
          <option value="http://www.ssf.gov.cn/">社保基金会</option>
          
          <option value="http://www.nsfc.gov.cn/">自然科学基金会</option>
          
          <option value="http://www.gjxfj.gov.cn/">信访局</option>
          
          <option value="http://www.chinagrain.gov.cn/">粮食局</option>
          
          <option value="http://www.nea.gov.cn/">能源局</option>
          
          <option value="http://www.sastind.gov.cn/">国防科工局</option>
          
          <option value="http://www.tobacco.gov.cn/">烟草局</option>
          
          <option value="http://www.safea.gov.cn/">外专局</option>
          
          <option value="http://www.scs.gov.cn/">公务员局</option>
          
          <option value="http://www.soa.gov.cn/">海洋局</option>
          
          <option value="http://www.sbsm.gov.cn/">测绘地信局</option>
          
          <option value="http://www.nra.gov.cn/">铁路局</option>
          
          <option value="http://www.caac.gov.cn/">民航局</option>
          
          <option value="http://www.spb.gov.cn/">邮政局</option>
          
          <option value="http://www.sach.gov.cn/">文物局</option>
          
          <option value="http://www.satcm.gov.cn/">中医药局</option>
          
          <option value="http://www.safe.gov.cn/">外汇局</option>
          
          <option value="http://www.chinacoal-safety.gov.cn/mkaj/">煤矿安监局</option>
          
          <option value="http://www.saac.gov.cn/">档案局</option>
          
          <option value="http://www.oscca.gov.cn/">密码局</option>
          
          <option value="http://www.cpad.gov.cn/">扶贫办</option>
          
          <option value="http://www.3g.gov.cn/index.ycs">三峡办</option>
          
          <option value="http://www.nsbd.gov.cn/">南水北调办</option>
          
        </select>
        <select name="m2" onChange="location1(this)" ID="Select1">
        <option selected="selected">各省旅游政务网</option>
          
          <option value="http://www.bjta.gov.cn/">北京旅游网</option>
          
          <option value="http://www.tjtour.cn/">天津旅游网</option>
          
          <option value="http://www.hebeitour.gov.cn/index.php">河北旅游网</option>
          
          <option value="http://www.shanxichina.gov.cn">山西旅游网</option>
          
          <option value="http://www.nmgtour.gov.cn/">内蒙古旅游网</option>
          
          <option value="http://www.lntour.gov.cn/">辽宁旅游网</option>
          
          <option value="http://www.jlta.gov.cn/">吉林旅游网</option>
          
          <option value="http://www.hljtour.gov.cn/">黑龙江旅游网</option>
          
          <option value="http://lyw.sh.gov.cn/">上海旅游网</option>
          
          <option value="http://www.jstour.com/">江苏旅游网</option>
          
          <option value="http://www.tourzj.gov.cn/">浙江旅游网</option>
          
          <option value="http://www.ahta.com.cn/">安徽旅游网</option>
          
          <option value="http://www.fjta.gov.cn/">福建旅游网</option>
          
          <option value="http://www.jxta.gov.cn/">江西旅游网</option>
          
          <option value="http://www.sdta.gov.cn/">山东旅游网</option>
          
          <option value="http://www.hnta.cn/">河南旅游网</option>
          
          <option value="http://www.hubeitour.gov.cn/">湖北旅游网</option>
          
          <option value="http://www.hnt.gov.cn/">湖南旅游网</option>
          
          <option value="http://www.gdta.gov.cn/">广东旅游网</option>
          
          <option value="http://www.gxta.gov.cn/">广西旅游网</option>
          
          <option value="http://www.visithainan.gov.cn/government/">海南旅游网</option>
          
          <option value="http://www.cqta.gov.cn/">重庆旅游网</option>
          
          <option value="http://www.scta.gov.cn/sclyj/">四川旅游网</option>
          
          <option value="http://www.gztour.gov.cn/">贵州旅游网</option>
          
          <option value="http://www.innyo.com/">云南旅游网</option>
          
          <option value="http://www.xzta.gov.cn/index.html">西藏旅游网</option>
          
          <option value="http://sxta.gov.cn/sxtourgov/proscenium/index.html">陕西旅游网</option>
          
          <option value="http://www.gsta.gov.cn/">甘肃旅游网</option>
          
          <option value="http://www.nxtour.com.cn/">宁夏旅游网</option>
          
          <option value="http://www.qhly.gov.cn/">青海旅游网</option>
          
          <option value="http://www.xinjiangtour.gov.cn/">新疆旅游网</option>
          
          <option value="http://www.discoverhongkong.com/china/index.jsp">香港旅游发展局</option>
          
          <option value="http://www.macautourism.gov.mo/">澳门特别行政区旅游局</option>
          
          <option value="http://www.btwql.gov.cn/">兵团旅游网</option>
          
        </select>
        <select name="m3" onChange="location1(this)" ID="Select1">
        <option selected="selected">国际旅游组织</option>
          
          <option value="http://www2.unwto.org/">联合国世界旅游组织</option>
          
          <option value="http://www.fia.com/">国际汽车运动联合会</option>
          
          <option value="http://www.pata.org/">亚太旅游协会</option>
          
          <option value="http://www.apec.org/">亚太经合组织</option>
          
          <option value="http://www.asta.org/">美国旅行代理商协会</option>
          
          <option value="http://ih-ra.com/">国际饭店与餐饮协会</option>
          
        </select>
        <select name="m4" onChange="location1(this)" ID="Select1">
        <option selected="selected">驻华旅游组织</option>
          
          <option value="../../yqlj/zhlyzz/201507/t20150701_719902.shtml">港澳台驻内地办事处</option>
          
          <option value="../../yqlj/zhlyzz/201506/t20150624_273197.shtml">各国旅游机构驻华办事处</option>
          
        </select>
        <select name="m5" onChange="location1(this)" ID="Select1">
        <option selected="selected">友情链接</option>
          
          <option value="https://zygjjg.12388.gov.cn/">中央国家机关举报网站</option>
          
          <option value="../../yqlj/yqlj/lyyx/">旅游院校</option>
          
          <option value="../../yqlj/yqlj/lypd/">旅游频道</option>
          
          <option value="../../yqlj/yqlj/yqljqt/">其他</option>
          
        </select>
        </div>
        <div class="footer_l">
     
<script type="text/javascript">document.write(unescape("%3Cspan id='_ideConac' %3E%3C/span%3E%3Cscript src='http://dcs.conac.cn/js/33/000/0000/40672416/CA330000000406724160003.js' type='text/javascript'%3E%3C/script%3E"));</script>

            <a><img src="http://www.cnta.gov.cn/images/red1.png" /></a>
        </div>
        <div class="footer_r">
        	<p><a target="_blank" href="http://www.cnta.gov.cn/lxwm/" >联系我们 </a>| <a target="_blank" href="http://www.cnta.gov.cn/wzdt/" >网站地图</a> | <a target="_blank" href="http://www.cnta.gov.cn/download/" >下载中心</a></p>
            <p>版权所有：中华人民共和国国家旅游局  网站管理：国家旅游局信息中心</p>
            <p>管理员邮箱：webmaster@cnta.gov.cn  京ICP备15046657号</p>
            <p>建议使用IE8以上浏览器</p>
        </div>
        <div style="float:left;width:120px;height:55px;margin-left:15px;margin-top:65px;">
        <script id="_jiucuo_" sitecode='bm39000001' src='http://pucha.kaipuyun.cn/exposure/jiucuo.js'></script>
        </div>
        <div class="clear"></div>
    </div>
</div>
<script type="text/javascript">
    var _bdhmProtocol = (("https:" == document.location.protocol) ? " https://" : " http://");
    document.write(unescape("%3Cscript src='" + _bdhmProtocol + "hm.baidu.com/h.js%3F1012c8757d7968f19279de5b5d3bc73b' type='text/javascript'%3E%3C/script%3E"));
</script>
<script type='text/javascript' src='http://static.gridsumdissector.com/js/Clients/GWD-801536-A2CC10/gs.js'></script>
<noscript><img src="http://ta.trs.cn/c/1.gif?mpId=364&jsoff=1" style="border:0" alt="" /></noscript>
<script>
var _taq = _taq || [];
_taq.home = 'http://ta.trs.cn/c';
_taq.push(['_mpId', '364']);
_taq.push(['_cli', '1']);
(function(d, o, t) {
	if (window.inTRSDesignMode) return;
	var ma = d.createElement(o); ma.async = true; ma.commonresource="1"; ma.src = t;
	var s = d.getElementsByTagName(o)[0]; s.parentNode.insertBefore(ma, s);
})(document, 'script', 'http://ta.trs.cn/c/js/ta.js');
</script>
<div class="r_close" style='bottom:340px;'>
<img src='http://www.cnta.gov.cn/images/close140403.gif' />
</div>
<!--<div  class="weibo" style='margin-left: -663px; bottom:366px;padding: 4px; height:134px'>
<a href='http://www.cnta.gov.cn/ztwz/czczl/'><img src="http://www.cnta.gov.cn/zylcfctpwh/images/P020161130627556356561.jpg" width="66" height="134" style="height:134px;" /></a>
</div>-->
<!--20170411注释
<div  class="weibo" style='margin-left: -663px; bottom: 366px;padding: 4px; height:134px'>
<a href='http://www.cnta.gov.cn/ztwz/lxyz/'><img src="http://www.cnta.gov.cn/zylcfctpwh/images/P020161019552215694719.jpg" width="66" height="134" style="height:134px;" /></a>
</div>

<div  class="weibo" style='margin-left: -663px; bottom: 214px;padding: 4px; height:134px'>
<a href='http://www.cnta.gov.cn/ztwz/lmhdzt/'><img src="http://www.cnta.gov.cn/zylcfctpwh/images/P020161019552576053500.jpg" width="66" height="134" style="height:134px;" /></a>
</div>

<div  class="weibo" style='margin-left: -663px; bottom: 62px;padding: 4px; height:134px'>
<a href='http://www.cnta.gov.cn/ztwz/dsjqgdyds/'><img src="http://www.cnta.gov.cn/zylcfctpwh/images/P020170314589555319942.jpg" width="66" height="134" style="height:134px;" /></a>
</div>






<div class="weixin" style="height:auto;bottom:363px;padding:4px;">
	<a href='http://www.cnta.gov.cn/ztwz/2017bflyngycfz/'><img src="http://www.cnta.gov.cn/zylcfctpwh/images/P020170203348421395926.jpg" width="66" height="134" style="height:134px;" /></a>
</div>

<div class="weixin" style="height:auto;bottom:212px;padding:4px;">
	<a href='http://dj.cnta.gov.cn/'><img src="http://www.cnta.gov.cn/zylcfctpwh/images/P020161019552462328276.jpg" width="66" height="134" style="height:134px;" /></a>
</div>
<div class="weixin" style="height:auto;bottom:60px;padding:4px;">
	<a href='http://www.cnta.gov.cn/ztwz/jtly/'><img src="http://www.cnta.gov.cn/zylcfctpwh/images/P020170228612233591893.jpg" width="66" height="134" style="height:134px;" /></a>
</div>-->
<div class="weibo" style="bottom:90px;padding:4px;">
	<img src="http://www.cnta.gov.cn/images/weibo.jpg" />
    <span>国家旅游局</span>
    <span style="letter-spacing:3px;">官方微博</span>
</div>
<div class="weixin" style="bottom:220px;padding:4px;">
	<img src="http://www.cnta.gov.cn/ty/includefooter/images/P020160309356126439106.jpg" width="66" />
    <span>国家旅游局</span>
    <span style="letter-spacing:3px;">官方微信</span>
</div>
<!--
<a class="gaibian" href="http://www.cnta.gov.cn/xxfb/gbtz/"  ignoreapd="true" >
	图片征集
</a>-->
<!--<a class="gaibian" href="http://city.sina.com.cn/2016lyzj/index.shtml?qq-pf-to=pcqq.c2c"  ignoreapd="true" style='background:none;bottom:80px;margin-left:590px;'>
<img src="http://www.cnta.gov.cn/images/Icon_logo20160530.jpg" width="52" height="52" style='margin-top:-30px' />
</a>-->
<!--30,180-->
<div class="searchf" style="bottom:20px;margin-left:590px;">
	搜 索
    <div class="searchf2">
        <div class="searchf1">
        <form name="searchform" id="searchform" action="http://www.cnta.gov.cn/was5/web/search?channelid=261012" method="post" target="_blank">
            <input id="textfield" type="text" name="searchword" class="" value="" />
				<input type="hidden" name="perpage" value="" />
				<input type="hidden" name="templet" value="" />
				<input type="hidden" name="token" value="" />
				<input type="hidden" name="channelid" value="261012" />
				<input type="submit" value="搜索" />
        </form>
        </div>
    </div>
</div>



<script>
var _hmt = _hmt || [];
(function() {
  var hm = document.createElement("script");
  hm.src = "//hm.baidu.com/hm.js?2a7d9fd86036a721a0f0895061ae1ad7";
  var s = document.getElementsByTagName("script")[0]; 
  s.parentNode.insertBefore(hm, s);
})();
</script>
<!--footer嵌套结束-->

</body>
</html>
"""

html2 = """

<!doctype html>
<html>
<head>
<meta charset="utf-8">
<meta http-equiv="X-UA-Compatible" content="IE=edge">
<link href="../../images/base.css" rel="stylesheet" />
<link href="../../images/lby.css" rel="stylesheet" />
<title>旅游人才</title>
<script src="../../images/jquery-1.11.0.min.js" /></script>
<script src="../../images/nav_er.js" /></script>
<!--[if IE 6]>
<script type="text/javascript" src="../../images/png.js"></script>
<script>
PNG.fix('*'); 
</script>
<![endif]-->
</head>
<body>
<link rel="Shortcut Icon" type="image/x-icon" href="../../images/favicon.ico">
<script language='javascript' src='http://www.cnta.gov.cn/images/zh.js'></script>
<div class="top">
	<div class="top1">
    	<div class="top_left">
            <a href="javascript:zh_tran('s');" target="_self">简体</a>
            <a href="javascript:zh_tran('t');" target="_self">繁体</a>
            <a href="http://en.cnta.gov.cn">English</a>
        </div>
        <div class="top_left top_right">
            <a href="http://www.cnta.gov.cn">返回首页</a>
        	<a href="javascript:;" onclick="AddFavorite('http://www.cnta.gov.cn/',location.href)">加入收藏</a>
          <!--  <a href="http://www1.cnta.gov.cn">返回旧版</a>-->
            <a href="http://mail.cnta.gov.cn/" target="_blank">邮箱登录</a>
        </div>
    </div>
</div>
<div class="main">
    <script type="text/javascript">
  var today = new Date();
  var date = today.getDate();
  var day = today.getDay();
  var month = today.getMonth()+1;
  var year = today.getYear();
</script>
<script>
    var   CalendarData=new   Array(20);
    var   madd=new Array(12);
    var   TheDate=new Date();
    var   tgString="甲乙丙丁戊己庚辛壬癸";
    var   dzString="子丑寅卯辰巳午未申酉戌亥";
    var   numString="一二三四五六七八九十";
    var   monString="正二三四五六七八九十冬腊";
    var   weekString="日一二三四五六";
    var   sx="鼠牛虎兔龙蛇马羊猴鸡狗猪";
    var   cYear;
    var   cMonth;
    var   cDay;
    var   cHour;
    var   cDateString;
    var   DateString;
    var   Browser=navigator.appName;

    function   init()
    {
        CalendarData[0]=0x41A95;
        CalendarData[1]=0xD4A;
        CalendarData[2]=0xDA5;
        CalendarData[3]=0x20B55;
        CalendarData[4]=0x56A;
        CalendarData[5]=0x7155B;
        CalendarData[6]=0x25D;
        CalendarData[7]=0x92D;
        CalendarData[8]=0x5192B;
        CalendarData[9]=0xA95;
        CalendarData[10]=0xB4A;
        CalendarData[11]=0x416AA;
        CalendarData[12]=0xAD5;
        CalendarData[13]=0x90AB5;
        CalendarData[14]=0x4BA;
        CalendarData[15]=0xA5B;
        CalendarData[16]=0x60A57;
        CalendarData[17]=0x52B;
        CalendarData[18]=0xA93;
        CalendarData[19]=0x40E95;
        madd[0]=0;
        madd[1]=31;
        madd[2]=59;
        madd[3]=90;
        madd[4]=120;
        madd[5]=151;
        madd[6]=181;
        madd[7]=212;
        madd[8]=243;
        madd[9]=273;
        madd[10]=304;
        madd[11]=334;
    }

    function   GetBit(m,n)
    {
        return   (m>>n)&1;
    }

    function   e2c()
    {
        var   totalmnk;
        var   isEnd=false;
        var   tmp=TheDate.getYear();
        if   (tmp<1900)     tmp+=1900;
        total=(tmp-2001)*365
                +Math.floor((tmp-2001)/4)
                +madd[TheDate.getMonth()]
                +TheDate.getDate()
                -23;
        if   (TheDate.getYear()%4==0&&TheDate.getMonth()>1)
            total++;
        for(m=0;;m++)
        {
            k=(CalendarData[m]<0xfff)?11:12;
            for(n=k;n>=0;n--)
            {
                if(total<=29+GetBit(CalendarData[m],n))
                {
                    isEnd=true;
                    break;
                }
                total=total-29-GetBit(CalendarData[m],n);
            }
            if(isEnd)break;
        }
        cYear=2001   +   m;
        cMonth=k-n+1;
        cDay=total;
        if(k==12)
        {
            if(cMonth==Math.floor(CalendarData[m]/0x10000)+1)
                cMonth=1-cMonth;
            if(cMonth>Math.floor(CalendarData[m]/0x10000)+1)
                cMonth--;
        }
        cHour=Math.floor((TheDate.getHours()+3)/2);
    }

    function   GetcDateString()
    {   var   tmp="";

        if(cMonth<1)
        {
            tmp+="闰";
            tmp+=monString.charAt(-cMonth-1);
			
        }
        else
            tmp+=monString.charAt(cMonth-1);
        tmp+="月";
        tmp+=(cDay<11)?"初":((cDay<20)?"十":((cDay<30)?"廿":"卅"));
        if(cDay%10!=0||cDay==10)
            tmp+=numString.charAt((cDay-1)%10);
        tmp+="    ";
        cDateString=tmp;
        return   tmp;
    }

    function   GetDateString()
    {
        var   tmp="";
        var   t1=TheDate.getYear();
        if   (t1<1900)t1+=1900;
        tmp+=t1
                +"年"
                +(TheDate.getMonth()+1)+"月"
                +TheDate.getDate()+"日   "
                +TheDate.getHours()+":"
                +((TheDate.getMinutes()<10)?"0":"")
                +TheDate.getMinutes()
                +" 星期"+weekString.charAt(TheDate.getDay());
        DateString=tmp;
        return   tmp;
    }

    init();
    e2c();
    GetDateString();
    GetcDateString();
    //document.write(DateString+" 农历"+cDateString);
</script>
<style>
.nav li{padding-left:40px;width:auto;}
</style>
<div class="logo">
    	
        <div class="logo_right">
            <a class="text"><script type="text/javascript">document.write(month);</script>月<script type="text/javascript">document.write(date);</script>日<br>农历&nbsp;&nbsp;<script type="text/javascript">document.write(cDateString);</script>&nbsp;&nbsp;霜降</a>
			
			
					
			
			
			
			

			
					
			
			
			
			

			
					
			
			
			
			
					<img src="http://www.cnta.gov.cn/images/shuangjiang.png" />
			

			
					
			
			
			
			
			
        </div>
        <a href="http://www.cnta.gov.cn"><img src="/images/logo.png" />

</a>
    </div>
 <div class="nav">
    	<ul>
        	
            <li class="m1"><a  href="http://www.cnta.gov.cn/jgjj/lyjjj/">机构简介</a></li>     
            <li class="m2"><a  href="http://www.cnta.gov.cn/xxfb/">信息发布</a></li>
            <li class="m3"><a  href="http://www.cnta.gov.cn/zwgk/">政府信息公开</a></li>
            <li class="m4"><a   href="http://www.cnta.gov.cn/hygq/">回应关切</a></li>
            <li class="m5"><a  href="http://www.cnta.gov.cn/bsdt/zwgk/">办事大厅</a></li>
            <li class="m6"><a  href="http://www.cnta.gov.cn/zdzx/">重点专项</a></li>
            <li class="m7"><a  href="http://www.cnta.gov.cn/was5/web/search?channelid=242887">旅游名录</a></li>
            <li class="m8" style="padding-left:40px; width:72px;"><a  href="http://www.cnta.gov.cn/xwfbh/" style="letter-spacing:-2px;">新闻发布会</a></li>
            <li class="m9"><a  href="http://www.cnta.gov.cn/spzl" style="letter-spacing:-2px;">视频专栏</a></li>
            <div class="nav_h"></div>
            <div class="nav_h1"></div>
        </ul>
    </div>
    <div class="main_local marl30">
    	当前位置：<a href="../../" target="_blank" title="首页">首页</a>><a href="../" target="_blank" title="重点工作">重点工作</a>><a href="./" title="旅游人才" class='blue CurrChnlCls'>旅游人才</a>
    </div>
	<div class="liebiao">
        
    	        <div class="lie_main_m">
            <ul>
                
                <li><a target="_blank" href="http://www.zgdaoyou.com/"><span>2016-11-09</span>导游云课堂研修培训</a></li>
                
                <li><a target="_blank" href="./201710/t20171012_842307.shtml"><span>2017-10-12</span>国家旅游局办公室关于举办2017年度万名旅游英才计划创新创业型英才培养项目——乡村旅游“双创”人才培...</a></li>
                
                <li><a target="_blank" href="./201708/t20170815_835515.shtml"><span>2017-08-15</span>一张“成绩单”透视旅游人才培养大格局</a></li>
                
                <li><a target="_blank" href="./201707/t20170707_830949.shtml"><span>2017-07-07</span>国家旅游局办公室关于组织开展2014年度入选旅游业青年专家培养总结工作的通知</a></li>
                
                <li><a target="_blank" href="./201707/t20170703_830373.shtml"><span>2017-07-03</span>国家旅游局办公室关于印发 “十三五”旅游人才发展规划纲要的通知</a></li>
                
                <li><a target="_blank" href="./201707/t20170703_830370.shtml"><span>2017-07-03</span>关于印发《2017年全国中高级导游等级考试工作实施方案》的通知</a></li>
                
                <li><a target="_blank" href="./201706/t20170627_829936.shtml"><span>2017-06-27</span>2017年全国中、高级导游等级考试大纲</a></li>
                
                <li><a target="_blank" href="./201705/t20170512_825217.shtml"><span>2017-05-12</span>国家旅游局办公室关于举办旅游数据与旅游统计人才能力提升高级研修班的通知</a></li>
                
                <li><a target="_blank" href="./201702/t20170227_815856.shtml"><span>2017-02-27</span>国家旅游局办公室关于组织开展2015年度万名旅游英才计划项目验收总结工作的通知</a></li>
                
                <li><a target="_blank" href="./201702/t20170208_814275.shtml"><span>2017-02-09</span>聚才引智 助推民族地区旅游腾飞</a></li>
                
                <li><a target="_blank" href="./201611/t20161128_807785.shtml"><span>2016-11-28</span>旅游业青年专家课程资源目录（2016.11公布）</a></li>
                
                <li><a target="_blank" href="./201701/t20170121_812828.shtml"><span>2017-01-21</span>《中国旅游报》整版报道三亚旅游人才发展白皮书</a></li>
                
                <li><a target="_blank" href="./201701/t20170111_812020.shtml"><span>2017-01-12</span>三亚发布中英文双语版本旅游人才发展白皮书</a></li>
                
                <li><a target="_blank" href="./201612/t20161213_809189.shtml"><span>2016-12-13</span>国家旅游局办公室关于组织开展2016年全国旅游教育培训统计工作的通知</a></li>
                
                <li><a target="_blank" href="./201612/t20161205_808497.shtml"><span>2016-12-05</span>2016年西藏和四省藏区旅游经济发展研讨班成功举办</a></li>
                
                <li><a target="_blank" href="./201611/t20161124_807536.shtml"><span>2016-11-24</span>四部门联合印发《关于举办第三届全国导游大赛的通知》</a></li>
                
                <li><a target="_blank" href="./201611/t20161128_807889.shtml"><span>2016-11-28</span>以全国大赛展导游风采</a></li>
                
                <li><a target="_blank" href="./201611/t20161121_789624.shtml"><span>2016-11-21</span>桂林培训旅游统计人才</a></li>
                
                <li><a target="_blank" href="./201611/t20161108_788542.shtml"><span>2016-11-08</span>推进文旅人才队伍建设</a></li>
                
                <li><a target="_blank" href="./201611/t20161102_788140.shtml"><span>2016-11-03</span>河南省旅游景区旅游投诉工作人员培训班成功举办</a></li>
                
            </ul>
        </div>
        
        <div class='page'><script language="javascript">
	var currentPage=0;
	var prevPage=currentPage-1;
	var nextPage=currentPage+1;
	var countPage=4;
	var endPage=countPage-1;
	if(countPage>1){
	document.write("<a href=\"index.shtml\" target=\"_self\" class='index'>首页</a>&nbsp;");
	}
	if(countPage>1&&currentPage!=0&&currentPage!=1)
document.write("<a href=\"index"+"_"+prevPage+"."+"shtml\" target=\"_self\">上一页</a>&nbsp;");
	else if(countPage>1&&currentPage!=0&&currentPage==1)
document.write("<a  href=\"index.shtml\" target=\"_self\">上一页</a>&nbsp;");
	else
document.write("<a class='tow'>上一页</a>&nbsp;");
	var num=6;
	var startPage=currentPage-2;
	if(startPage<0)startPage=0;
	var endpage=startPage+num;
	if(endpage>countPage)
	endpage=countPage;
	startPage=endpage-6;
	if(startPage<0)startPage=0;
	for(var i=startPage;i<endpage;i++){
		if(currentPage==i)
document.write("<a class='hover'>"+(i+1)+"</a>&nbsp;");
	else if(i==0){
document.write("<a  href=\"index.shtml\" target=\"_self\">"+1+"</a>&nbsp;");
		 }else
document.write("<a href=\"index"+"_"+i+"."+"shtml\" target=\"_self\">"+(i+1)+"</a>&nbsp;");}
	if(countPage>1&&currentPage!=(countPage-1))
document.write("<a class='tow' href=\"index"+"_"+nextPage+"."+"shtml\" target=\"_self\">下一页</a>&nbsp;");
	else
document.write("<a class='tow'>下一页</a>&nbsp;");
    	if(countPage>1){
	document.write("<a class='index'  href=\"index_"+endPage+".shtml\" target=\"_self\">尾页</a>");
		}
</script></div>
    </div>
</div>
<!--footer嵌套开始-->
<script language="javascript" type="text/javascript"> 
				function location1(s)
                {       var d = s.options[s.selectedIndex].value;
						if ((navigator.userAgent.match(/(iPhone|iPod|Android|ios|SymbianOS)/i))) {
						 	location.href=d;
						}
                     	else
							window.open(d,"_blank");
						s.selectedIndex=0;       
                }

</script>
<script>
$(function(){
$('.r_close').click(function(){
$('.r_close, .weibo, .weixin, .gaibian, .searchf').hide();




})
if($(window).width()<1282){
$('.r_close, .weibo, .weixin').css('left', 'auto').css('right', '10px');
$('.gaibian, .searchf').css('left', 'auto').css('right', '25px');
}else{
$('.r_close, .weibo, .weixin, .gaibian, .searchf').css('left', '50%').css('right', 'auto');
}
$(window).resize(function() {
 if($(window).width()<1282){
$('.r_close, .weibo, .weixin').css('left', 'auto').css('right', '10px');
$('.gaibian, .searchf').css('left', 'auto').css('right', '25px');
}else{
$('.r_close, .weibo, .weixin, .gaibian, .searchf').css('left', '50%').css('right', 'auto');
}
})
})
</script>
<div class="foot">
	<div class="footer">
    	<div class="footer_t">
        	<select name="m1" onChange="location1(this)" ID="Select1">
        <option selected="selected">国务院部委网站</option>
          
          <option value="http://www.mfa.gov.cn/mfa_chn/">外交部</option>
          
          <option value="http://www.mod.gov.cn/">国防部</option>
          
          <option value="http://www.ndrc.gov.cn/">发展改革委</option>
          
          <option value="http://www.moe.gov.cn/">教育部</option>
          
          <option value="http://www.most.gov.cn/">科技部</option>
          
          <option value="http://www.miit.gov.cn/n11293472/index.html">工业和信息化部</option>
          
          <option value="http://www.seac.gov.cn/">国家民委</option>
          
          <option value="http://www.mps.gov.cn/n16/index.html?_v=1435138159749">公安部</option>
          
          <option value="http://www.ccdi.gov.cn/">监察部</option>
          
          <option value="http://www.mca.gov.cn/">民政部</option>
          
          <option value="http://www.moj.gov.cn/">司法部</option>
          
          <option value="http://www.mof.gov.cn/index.htm">财政部</option>
          
          <option value="http://www.mohrss.gov.cn/">人力资源社会保障部</option>
          
          <option value="http://www.mlr.gov.cn/">国土资源部</option>
          
          <option value="http://www.mep.gov.cn/">环境保护部</option>
          
          <option value="http://www.mohurd.gov.cn/">住房城乡建设部</option>
          
          <option value="http://www.mot.gov.cn/">交通运输部</option>
          
          <option value="http://www.mwr.gov.cn/">水利部</option>
          
          <option value="http://www.moa.gov.cn/">农业部</option>
          
          <option value="http://www.mofcom.gov.cn/">商务部</option>
          
          <option value="http://www.mcprc.gov.cn/">文化部</option>
          
          <option value="http://www.nhfpc.gov.cn/">卫生计生委</option>
          
          <option value="http://www.pbc.gov.cn/">人民银行</option>
          
          <option value="http://www.audit.gov.cn/">审计署</option>
          
          <option value="http://www.china-language.gov.cn/">国家语委</option>
          
          <option value="http://www.cnsa.gov.cn/">航天局</option>
          
          <option value="http://www.caea.gov.cn/">原子能机构</option>
          
          <option value="http://www.sasac.gov.cn/">国资委</option>
          
          <option value="http://www.customs.gov.cn/publish/portal0/">海关总署</option>
          
          <option value="http://www.chinatax.gov.cn/">税务总局</option>
          
          <option value="http://www.saic.gov.cn/">工商总局</option>
          
          <option value="http://www.aqsiq.gov.cn/">质检总局</option>
          
          <option value="http://www.sapprft.gov.cn/">新闻出版广电总局</option>
          
          <option value="http://www.sport.gov.cn/">体育总局</option>
          
          <option value="http://www.chinasafety.gov.cn/newpage/">安全监管总局</option>
          
          <option value="http://www.sda.gov.cn/WS01/CL0001/">食品药品监管总局</option>
          
          <option value="http://www.stats.gov.cn/">统计局</option>
          
          <option value="http://www.forestry.gov.cn/">林业局</option>
          
          <option value="http://www.sipo.gov.cn/">知识产权局</option>
          
          <option value="http://www.sara.gov.cn/">宗教局</option>
          
          <option value="http://www.counsellor.gov.cn/">参事室</option>
          
          <option value="http://www.ggj.gov.cn/">国管局</option>
          
          <option value="http://www.ncac.gov.cn/">版权局</option>
          
          <option value="http://www.gqb.gov.cn/">侨办</option>
          
          <option value="http://www.hmo.gov.cn/">港澳办</option>
          
          <option value="http://www.chinalaw.gov.cn/">法制办</option>
          
          <option value="http://www.gov.cn/guoqing/2005-12/26/content_2652073.htm">国研室</option>
          
          <option value="http://www.gwytb.gov.cn/">台办</option>
          
          <option value="http://www.scio.gov.cn/">新闻办</option>
          
          <option value="http://www.xinhuanet.com/">新华社</option>
          
          <option value="http://www.cas.cn/">中科院</option>
          
          <option value="http://cass.cssn.cn/">社科院</option>
          
          <option value="http://www.cae.cn/cae/html/main/index.html">工程院</option>
          
          <option value="http://www.drc.gov.cn/">发展研究中心</option>
          
          <option value="http://www.nsa.gov.cn/web/index.php">行政学院</option>
          
          <option value="http://www.cea.gov.cn/">地震局</option>
          
          <option value="http://www.cma.gov.cn/">气象局</option>
          
          <option value="http://www.cbrc.gov.cn/index.html">银监会</option>
          
          <option value="http://www.csrc.gov.cn/pub/newsite/">证监会</option>
          
          <option value="http://www.circ.gov.cn/web/site0/">保监会</option>
          
          <option value="http://www.ssf.gov.cn/">社保基金会</option>
          
          <option value="http://www.nsfc.gov.cn/">自然科学基金会</option>
          
          <option value="http://www.gjxfj.gov.cn/">信访局</option>
          
          <option value="http://www.chinagrain.gov.cn/">粮食局</option>
          
          <option value="http://www.nea.gov.cn/">能源局</option>
          
          <option value="http://www.sastind.gov.cn/">国防科工局</option>
          
          <option value="http://www.tobacco.gov.cn/">烟草局</option>
          
          <option value="http://www.safea.gov.cn/">外专局</option>
          
          <option value="http://www.scs.gov.cn/">公务员局</option>
          
          <option value="http://www.soa.gov.cn/">海洋局</option>
          
          <option value="http://www.sbsm.gov.cn/">测绘地信局</option>
          
          <option value="http://www.nra.gov.cn/">铁路局</option>
          
          <option value="http://www.caac.gov.cn/">民航局</option>
          
          <option value="http://www.spb.gov.cn/">邮政局</option>
          
          <option value="http://www.sach.gov.cn/">文物局</option>
          
          <option value="http://www.satcm.gov.cn/">中医药局</option>
          
          <option value="http://www.safe.gov.cn/">外汇局</option>
          
          <option value="http://www.chinacoal-safety.gov.cn/mkaj/">煤矿安监局</option>
          
          <option value="http://www.saac.gov.cn/">档案局</option>
          
          <option value="http://www.oscca.gov.cn/">密码局</option>
          
          <option value="http://www.cpad.gov.cn/">扶贫办</option>
          
          <option value="http://www.3g.gov.cn/index.ycs">三峡办</option>
          
          <option value="http://www.nsbd.gov.cn/">南水北调办</option>
          
        </select>
        <select name="m2" onChange="location1(this)" ID="Select1">
        <option selected="selected">各省旅游政务网</option>
          
          <option value="http://www.bjta.gov.cn/">北京旅游网</option>
          
          <option value="http://www.tjtour.cn/">天津旅游网</option>
          
          <option value="http://www.hebeitour.gov.cn/index.php">河北旅游网</option>
          
          <option value="http://www.shanxichina.gov.cn">山西旅游网</option>
          
          <option value="http://www.nmgtour.gov.cn/">内蒙古旅游网</option>
          
          <option value="http://www.lntour.gov.cn/">辽宁旅游网</option>
          
          <option value="http://www.jlta.gov.cn/">吉林旅游网</option>
          
          <option value="http://www.hljtour.gov.cn/">黑龙江旅游网</option>
          
          <option value="http://lyw.sh.gov.cn/">上海旅游网</option>
          
          <option value="http://www.jstour.com/">江苏旅游网</option>
          
          <option value="http://www.tourzj.gov.cn/">浙江旅游网</option>
          
          <option value="http://www.ahta.com.cn/">安徽旅游网</option>
          
          <option value="http://www.fjta.gov.cn/">福建旅游网</option>
          
          <option value="http://www.jxta.gov.cn/">江西旅游网</option>
          
          <option value="http://www.sdta.gov.cn/">山东旅游网</option>
          
          <option value="http://www.hnta.cn/">河南旅游网</option>
          
          <option value="http://www.hubeitour.gov.cn/">湖北旅游网</option>
          
          <option value="http://www.hnt.gov.cn/">湖南旅游网</option>
          
          <option value="http://www.gdta.gov.cn/">广东旅游网</option>
          
          <option value="http://www.gxta.gov.cn/">广西旅游网</option>
          
          <option value="http://www.visithainan.gov.cn/government/">海南旅游网</option>
          
          <option value="http://www.cqta.gov.cn/">重庆旅游网</option>
          
          <option value="http://www.scta.gov.cn/sclyj/">四川旅游网</option>
          
          <option value="http://www.gztour.gov.cn/">贵州旅游网</option>
          
          <option value="http://www.innyo.com/">云南旅游网</option>
          
          <option value="http://www.xzta.gov.cn/index.html">西藏旅游网</option>
          
          <option value="http://sxta.gov.cn/sxtourgov/proscenium/index.html">陕西旅游网</option>
          
          <option value="http://www.gsta.gov.cn/">甘肃旅游网</option>
          
          <option value="http://www.nxtour.com.cn/">宁夏旅游网</option>
          
          <option value="http://www.qhly.gov.cn/">青海旅游网</option>
          
          <option value="http://www.xinjiangtour.gov.cn/">新疆旅游网</option>
          
          <option value="http://www.discoverhongkong.com/china/index.jsp">香港旅游发展局</option>
          
          <option value="http://www.macautourism.gov.mo/">澳门特别行政区旅游局</option>
          
          <option value="http://www.btwql.gov.cn/">兵团旅游网</option>
          
        </select>
        <select name="m3" onChange="location1(this)" ID="Select1">
        <option selected="selected">国际旅游组织</option>
          
          <option value="http://www2.unwto.org/">联合国世界旅游组织</option>
          
          <option value="http://www.fia.com/">国际汽车运动联合会</option>
          
          <option value="http://www.pata.org/">亚太旅游协会</option>
          
          <option value="http://www.apec.org/">亚太经合组织</option>
          
          <option value="http://www.asta.org/">美国旅行代理商协会</option>
          
          <option value="http://ih-ra.com/">国际饭店与餐饮协会</option>
          
        </select>
        <select name="m4" onChange="location1(this)" ID="Select1">
        <option selected="selected">驻华旅游组织</option>
          
          <option value="../../yqlj/zhlyzz/201507/t20150701_719902.shtml">港澳台驻内地办事处</option>
          
          <option value="../../yqlj/zhlyzz/201506/t20150624_273197.shtml">各国旅游机构驻华办事处</option>
          
        </select>
        <select name="m5" onChange="location1(this)" ID="Select1">
        <option selected="selected">友情链接</option>
          
          <option value="https://zygjjg.12388.gov.cn/">中央国家机关举报网站</option>
          
          <option value="../../yqlj/yqlj/lyyx/">旅游院校</option>
          
          <option value="../../yqlj/yqlj/lypd/">旅游频道</option>
          
          <option value="../../yqlj/yqlj/yqljqt/">其他</option>
          
        </select>
        </div>
        <div class="footer_l">
     
<script type="text/javascript">document.write(unescape("%3Cspan id='_ideConac' %3E%3C/span%3E%3Cscript src='http://dcs.conac.cn/js/33/000/0000/40672416/CA330000000406724160003.js' type='text/javascript'%3E%3C/script%3E"));</script>

            <a><img src="http://www.cnta.gov.cn/images/red1.png" /></a>
        </div>
        <div class="footer_r">
        	<p><a target="_blank" href="http://www.cnta.gov.cn/lxwm/" >联系我们 </a>| <a target="_blank" href="http://www.cnta.gov.cn/wzdt/" >网站地图</a> | <a target="_blank" href="http://www.cnta.gov.cn/download/" >下载中心</a></p>
            <p>版权所有：中华人民共和国国家旅游局  网站管理：国家旅游局信息中心</p>
            <p>管理员邮箱：webmaster@cnta.gov.cn  京ICP备15046657号</p>
            <p>建议使用IE8以上浏览器</p>
        </div>
        <div style="float:left;width:120px;height:55px;margin-left:15px;margin-top:65px;">
        <script id="_jiucuo_" sitecode='bm39000001' src='http://pucha.kaipuyun.cn/exposure/jiucuo.js'></script>
        </div>
        <div class="clear"></div>
    </div>
</div>
<script type="text/javascript">
    var _bdhmProtocol = (("https:" == document.location.protocol) ? " https://" : " http://");
    document.write(unescape("%3Cscript src='" + _bdhmProtocol + "hm.baidu.com/h.js%3F1012c8757d7968f19279de5b5d3bc73b' type='text/javascript'%3E%3C/script%3E"));
</script>
<script type='text/javascript' src='http://static.gridsumdissector.com/js/Clients/GWD-801536-A2CC10/gs.js'></script>
<noscript><img src="http://ta.trs.cn/c/1.gif?mpId=364&jsoff=1" style="border:0" alt="" /></noscript>
<script>
var _taq = _taq || [];
_taq.home = 'http://ta.trs.cn/c';
_taq.push(['_mpId', '364']);
_taq.push(['_cli', '1']);
(function(d, o, t) {
	if (window.inTRSDesignMode) return;
	var ma = d.createElement(o); ma.async = true; ma.commonresource="1"; ma.src = t;
	var s = d.getElementsByTagName(o)[0]; s.parentNode.insertBefore(ma, s);
})(document, 'script', 'http://ta.trs.cn/c/js/ta.js');
</script>
<div class="r_close" style='bottom:340px;'>
<img src='http://www.cnta.gov.cn/images/close140403.gif' />
</div>
<!--<div  class="weibo" style='margin-left: -663px; bottom:366px;padding: 4px; height:134px'>
<a href='http://www.cnta.gov.cn/ztwz/czczl/'><img src="http://www.cnta.gov.cn/zylcfctpwh/images/P020161130627556356561.jpg" width="66" height="134" style="height:134px;" /></a>
</div>-->
<!--20170411注释
<div  class="weibo" style='margin-left: -663px; bottom: 366px;padding: 4px; height:134px'>
<a href='http://www.cnta.gov.cn/ztwz/lxyz/'><img src="http://www.cnta.gov.cn/zylcfctpwh/images/P020161019552215694719.jpg" width="66" height="134" style="height:134px;" /></a>
</div>

<div  class="weibo" style='margin-left: -663px; bottom: 214px;padding: 4px; height:134px'>
<a href='http://www.cnta.gov.cn/ztwz/lmhdzt/'><img src="http://www.cnta.gov.cn/zylcfctpwh/images/P020161019552576053500.jpg" width="66" height="134" style="height:134px;" /></a>
</div>

<div  class="weibo" style='margin-left: -663px; bottom: 62px;padding: 4px; height:134px'>
<a href='http://www.cnta.gov.cn/ztwz/dsjqgdyds/'><img src="http://www.cnta.gov.cn/zylcfctpwh/images/P020170314589555319942.jpg" width="66" height="134" style="height:134px;" /></a>
</div>






<div class="weixin" style="height:auto;bottom:363px;padding:4px;">
	<a href='http://www.cnta.gov.cn/ztwz/2017bflyngycfz/'><img src="http://www.cnta.gov.cn/zylcfctpwh/images/P020170203348421395926.jpg" width="66" height="134" style="height:134px;" /></a>
</div>

<div class="weixin" style="height:auto;bottom:212px;padding:4px;">
	<a href='http://dj.cnta.gov.cn/'><img src="http://www.cnta.gov.cn/zylcfctpwh/images/P020161019552462328276.jpg" width="66" height="134" style="height:134px;" /></a>
</div>
<div class="weixin" style="height:auto;bottom:60px;padding:4px;">
	<a href='http://www.cnta.gov.cn/ztwz/jtly/'><img src="http://www.cnta.gov.cn/zylcfctpwh/images/P020170228612233591893.jpg" width="66" height="134" style="height:134px;" /></a>
</div>-->
<div class="weibo" style="bottom:90px;padding:4px;">
	<img src="http://www.cnta.gov.cn/images/weibo.jpg" />
    <span>国家旅游局</span>
    <span style="letter-spacing:3px;">官方微博</span>
</div>
<div class="weixin" style="bottom:220px;padding:4px;">
	<img src="http://www.cnta.gov.cn/ty/includefooter/images/P020160309356126439106.jpg" width="66" />
    <span>国家旅游局</span>
    <span style="letter-spacing:3px;">官方微信</span>
</div>
<!--
<a class="gaibian" href="http://www.cnta.gov.cn/xxfb/gbtz/"  ignoreapd="true" >
	图片征集
</a>-->
<!--<a class="gaibian" href="http://city.sina.com.cn/2016lyzj/index.shtml?qq-pf-to=pcqq.c2c"  ignoreapd="true" style='background:none;bottom:80px;margin-left:590px;'>
<img src="http://www.cnta.gov.cn/images/Icon_logo20160530.jpg" width="52" height="52" style='margin-top:-30px' />
</a>-->
<!--30,180-->
<div class="searchf" style="bottom:20px;margin-left:590px;">
	搜 索
    <div class="searchf2">
        <div class="searchf1">
        <form name="searchform" id="searchform" action="http://www.cnta.gov.cn/was5/web/search?channelid=261012" method="post" target="_blank">
            <input id="textfield" type="text" name="searchword" class="" value="" />
				<input type="hidden" name="perpage" value="" />
				<input type="hidden" name="templet" value="" />
				<input type="hidden" name="token" value="" />
				<input type="hidden" name="channelid" value="261012" />
				<input type="submit" value="搜索" />
        </form>
        </div>
    </div>
</div>



<script>
var _hmt = _hmt || [];
(function() {
  var hm = document.createElement("script");
  hm.src = "//hm.baidu.com/hm.js?2a7d9fd86036a721a0f0895061ae1ad7";
  var s = document.getElementsByTagName("script")[0]; 
  s.parentNode.insertBefore(hm, s);
})();
</script>
<!--footer嵌套结束-->

</body>
</html>

"""

datetime_t = str(datetime.date.today()).split('-')  # 对日期进行拆分，返回一个['2017', '10', '09']形式的列表

## todo:找出各版面url规律，形成列表。同时生成各版面标题。作为一级标题
url_prefix = 'http://www.cnta.gov.cn/zdgz/'


def ans0():

    soup = BeautifulSoup(''.join(html))

    # lanmu_ur = soup.find('div',{'class':'xxfb_cont'})
    lanmu_tl = soup.findAll('div', {'class': 'text'})
    lanmu_ul = soup.findAll('a', {'class': 'more'})
    lanmu_join = lanmu_tl + lanmu_ul

    # lanmu_ul_join = ''.join(lanmu_ul)
    print(lanmu_tl)
    print(lanmu_ul)
    print(lanmu_join)

    for tl,ul in zip(lanmu_tl,lanmu_ul): #使用zip元素对，用都变量的for循环交替提取各栏目的标题和链接
        vol_tl = tl.contents[0].strip()
        print(vol_tl)
        vol_ul = url_prefix + ul['href'].lstrip('\./')
        print(vol_ul)
        urlist = [vol_ul]  # 定义一个栏目多个页面url的列表，找出规律后在下面用for循环进行添加
        for nu in range(1, 5):  # 生成同一栏目翻页后的多个页面url，第二页形式为http://www.cnta.gov.cn/zdgz/qyly/index_1.shtml
            u = vol_ul + 'index_' + str(nu) + r'.shtml'
            urlist.append(u)
        print(urlist)

    soup2 = BeautifulSoup(''.join(html1))
    article_link = []
    for li in soup2.findAll('li'):
        find_today = re.compile('(\d\d\d\d)-(\d\d)-(\d\d)</span>')
        month = find_today.search(str(li))  # 把上面构建的表达式作用于findAll找出来的内容
        # try/except结构主要是用于正则表达式查找，如果不用这个结构，在部分标签当中查找不到内容的时候，下面引用查找结果group()就会报错，造成崩溃。
        try:
            print(month.group())
            d1 = datetime.date.today()  # 获取今天的日期
            d2 = datetime.date(int(month.group(1)), int(month.group(2)), int(month.group(3)))  # 获取新闻的日期
            days_betwen = (d1 - d2).days  # 获取时间差，结果为整数
            if days_betwen <= 100:  # 限定抓取几天内的新闻，当天的则为days_betwen == 0
                article_link.append(str(li))  # 注意要转换为字符串，beautifusoup不接受列表和其他类型的数据
        except:
            pass
    print(article_link)
    soup3 = BeautifulSoup(''.join(article_link))

    # 下面的for循环在上面找出指定日期范围内的正文链接当中提取url链接，并配合'http://www.jxta.gov.cn/'形成最终的正文链接
    for link in soup3.findAll('a'):
        print(link)
        print(vol_ul + link['href'].lstrip('\./'))
        title_find = re.compile(r'<.*><span>.*</span>(.*)</a>')
        title_search = title_find.search(str(link))
        print(title_search.group(1).strip())
        print(link.contents[0])




ans0()