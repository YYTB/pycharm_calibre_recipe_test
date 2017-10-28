# coding=utf-8

from BeautifulSoup import BeautifulSoup
import datetime, re

doc = """

var baseurl  = "http://www.gaxww.com/system/count/";
var maxpage = 304;
var schannelId= "0088001000000000000";
var firsturl = "http://www.gaxww.com/hot/index.shtml";
maxpage = maxpage+1;
schannelId = "0000000000000000000"+ schannelId ;
schannelId = schannelId.substring(schannelId.length-19); 
window.onload = function(){
	if(maxpage*1>1){
	   var pagehtmlcontent ="<div class='mod-ft pager-b' node-type='pagination' style=' display: block;text-align: center; font-size: 0px; margin-bottom: 30px;'>";
	    pagehtmlcontent +="<span node-type='pager' style='display: inline-block;vertical-align: top;font-size: 13px;margin: 0px 2px 0px 3px;line-height: 26px;'>";
	    pagehtmlcontent +="<span class='pagination' style='display: inline-block;vertical-align: top;font-size: 13px;margin: 0px 2px 0px 3px;line-height: 26px;'>";
	    pagehtmlcontent +="<a rel='prev' class='prev' id='uppage' style=' color: #000;text-decoration: none;width: 50px;border: 1px solid #D7D7D7;border-radius: 3px;height: 26px; line-height: 26px; padding: 0px 6px; color: #000; display: inline-block; vertical-align: top; font-size: 13px; line-height: 26px;' href='javascript:void(0)' onclick='nextpage(1)'>上一页</a>";
	    pagehtmlcontent +="<a rel='next' class='next' id='downpage' style=' color: #000;text-decoration: none;width: 50px;border: 1px solid #D7D7D7;border-radius: 3px;height: 26px; line-height: 26px; padding: 0px 6px; color: #000; display: inline-block; vertical-align: top; font-size: 13px;' href='javascript:void(0)' onclick='nextpage(2)'>下一页</a>&nbsp;";
	    pagehtmlcontent +="第<span node-type='total' id='currentid'></span>/<span node-type='total' id='allid'></span>页&nbsp;到第&nbsp;<input  id='jumppageId' node-type='num' type='text' style='width:40px; display: inline-block; vertical-align: top; font-size: 13px; height: 26px;margin-top:1px;padding: 0px;'>&nbsp;页</span>  ";
	    pagehtmlcontent +="<a href='javascript:;' class='pager-a-jump' node-type='btn' onclick='changepage()' style=' color: #000;text-decoration: none;width: 50px;border: 1px solid #D7D7D7;border-radius: 3px;height: 26px; line-height: 26px; padding: 0px 6px; color: #000; display: inline-block; vertical-align: top; font-size: 13px; line-height: 26px;float:right' >确定</a></span>";
	    pagehtmlcontent +="<input type='hidden' id='currentpage' value=''/>";
	
	    document.getElementById("pagetemple").innerHTML=pagehtmlcontent;
	
	     var currenturl = window.location.href;
	
	     var  allurl = currenturl .match("([0-9]+)_([0-9]+)");
	
	     if(allurl==null||allurl=="null"){
	     	     //  maxpage = document.getElementById("maxpage").value;
	                //当前页数
	               document .getElementById("currentpage").value=maxpage ; 
	                //第一页时隐藏上一页
	               document .getElementById("uppage").style.display="none";
	             
	      }else{
	             var chanelandpage = allurl[0].split("_");
	             var currentpage = chanelandpage[1];
	             //schannelId = chanelandpage[0];
	             //尾页时隐藏下一页
	             if(currentpage*1 == 1){
	            	 document .getElementById("downpage").style.display="none";
	             }
	             //当前页数
	             document.getElementById("currentpage").value=chanelandpage[1]*1;
	      }
	      
	       document.getElementById("currentid").innerHTML=maxpage*1-document.getElementById("currentpage").value*1+1;
	       document.getElementById("allid").innerHTML=maxpage;
	}

};

function nextpage(value){
   //上一页
    var pagenum = document.getElementById("currentpage").value;
  
    if(value == 1){
//那最后一段
      var uppagelast= pagenum ;
      uppagelast = uppagelast*1+1;
      if(uppagelast==maxpage){
          window.location.href=firsturl;
      }else{
      uppagelast= "000000000"+ uppagelast;
      uppagelast= uppagelast.substring(uppagelast.length-9);
      baseurl= baseurl+"/"+schannelId.substring(0,7)+"/"+schannelId.substring(7,19)+"/"+uppagelast.substring(0,3)+"/"+uppagelast.substring(3,6)+"/c"+schannelId+"_"+uppagelast+".shtml";
      window.location.href=baseurl;
      }
   }else {
      var uppagelast= pagenum ;
      uppagelast = uppagelast*1-1;
      uppagelast= "000000000"+ uppagelast;
      uppagelast= uppagelast.substring(uppagelast.length-9);
      baseurl= baseurl+"/"+schannelId.substring(0,7)+"/"+schannelId.substring(7,19)+"/"+uppagelast.substring(0,3)+"/"+uppagelast.substring(3,6)+"/c"+schannelId+"_"+uppagelast+".shtml";
      window.location.href=baseurl;
    }
}

 function changepage(){
              var jumpnum = document .getElementById("jumppageId").value;
              var downpagelase = maxpage;
              var downpagelasecenter = maxpage ;
              var r = /^\+?[1-9][0-9]*$/;
	     if(!r.test(jumpnum)){
	          alert("跳转页数必须为正整数");
                  return;
              }else if(jumpnum.trim()==""||jumpnum.trim()<=0||(jumpnum.trim()*1-1)>=(downpagelase*1)){
                        alert("输入的页数必须大于0小于最大页数");
                        return;
              }else if(jumpnum.trim() == 1){
                    window.location.href=firsturl;
              }else{
                       downpagelase = downpagelase*1-jumpnum.trim()+1;
                       downpagelase = "000000000"+ downpagelase ;
                       downpagelase = downpagelase .substring(downpagelase.length-9);                 
                       baseurl= baseurl+"/"+schannelId.substring(0,7)+"/"+schannelId.substring(7,19)+"/"+downpagelase.substring(0,3)+"/"+downpagelase.substring(3,6)+"/c"+schannelId+"_"+downpagelase+".shtml";
                       window.location.href=baseurl;
              }
    }


"""

soup = BeautifulSoup(''.join(doc))

div = soup.findAll()

page_refind = re.compile(r'maxpage = (\d*?);')

find = page_refind.search(str(div))

for nu in range(304,304-3,-1):
    print(nu)

print(''.join(div))

print(find.group(1))
#find_script = re.compile(r'http.*count_page_list_.*?.js')
#month = find_script.search(str(div))
#print(month.group())
