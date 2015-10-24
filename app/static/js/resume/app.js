
window.onload=function(){
	var iDrew=false;
	var color=['#1BBC9D','#E74D3D','#2ACB6E','#F1C410'];
	addColor(color);
	changeColor();
	var menuA=document.getElementById("menu").getElementsByTagName("a");
	for(var i=1;i<=5;i++){
			menuA[i-1].index=i-1;
			menuA[i-1].onclick=function(){
				var dis=this.index*700
				fnStartRun(document,{scrollTop:dis});
			}
			var page=document.getElementById("page"+i);
			page.index=i;
			page.onclick=function(){
			var dis=this.index==5?0:this.index*700;
			fnStartRun(document,{scrollTop:dis});
			}
	}
	window.onscroll=function(){
		scrollFix();
		showCirle();
		function showCirle(){
			var scrollTop=document.documentElement.scrollTop||document.body.scrollTop;
			if(scrollTop>=1400&&!iDrew){
					
					addCircle("js",60,'#1BBC9D');
					addCircle("html",90,'#2ACB6E');
					addCircle("css",80,'#E74D3D');
					addCircle("photoshop",80,'#F1C410');

					iDrew=true;
			}
		}
	}
}

function addCircle(id,number,iColor){
	var circle = new ProgressBar.Circle("#"+id, {
		color: iColor,
		strokeWidth: 4,
		trailWidth: 1,
		duration: 1500*number*0.01,
		text: {
		value: '0'
		},
	step: function(state, bar) {
		bar.setText((bar.value() * 100).toFixed(0));
	}
	});

		circle.animate(number*0.01)
}
function addColor(color){
	var circle=document.getElementById("cirle");
	var p=circle.getElementsByTagName("p");
	for(var i=0,j=0;i<p.length;i++){
		if(p[i].className=="text"){
			p[i].style.color=color[j];
			j++;
		}
	}
}
function scrollFix(){
	var scrollTop=document.documentElement.scrollTop||document.body.scrollTop;
	var menu=document.getElementById("menu");
	if(scrollTop>=700){
		menu.style.position="fixed";
		menu.style.top=0;
	}else{
		menu.style.position="absolute";
		menu.style.top=700+"px";
	}
}
function addPage(){
	var page=document.getElementById("page4");
}

function changeColor(){
	var colors=["#1abc9c","#2ecc71","#3498db","#9b59b6","#34495e","#16a085","#27ae60","#2980b9","#8e44ad","#2c3e50"
	,"#f1c40f","#e67e22","#e74c3c","#f39c12","#d35400","#c0392b"];
	var li=document.getElementById("webDesign").getElementsByTagName("li");
	for(var i in li){
		li[i].onmouseover=function(e){
			if(checkHover(e,this)){
			fnStartRun(this,{opacity:"100"});
			this.style.background=colors[selectFrom(0,colors.length)];
			}
		}
		li[i].onmouseout=function(e){
			if(checkHover(e,this)){
			fnStartRun(this,{opacity:"30"});
			}
		}
	}
	var selectFrom=function(lowerValue,upperValue){
		var choices=upperValue-lowerValue+1;
		return Math.floor(Math.random()*choices+lowerValue);
	}
}
/*引入运动框架*/
function getStyle(obj,attr){
		if(obj.currentStyle){
			return obj.currentStyle[attr];//兼容IE
		}
		else{
			return getComputedStyle(obj,false)[attr];//兼容FF
		}
	}
function fnStartRun(obj,json,fn){
		clearInterval(obj.timer);
		obj.timer=setInterval(function(){
			var bStop=true;
			for(attr in json){
			var iCur=0;
			if(attr=='opacity')/*兼容透明度*/
			{
			iCur=parseInt(parseFloat(getStyle(obj, attr))*100);/*去掉小数避免小数带来的BUG*/
			}
			else if (attr='scrollTop'){
				iCur=document.documentElement.scrollTop||document.body.scrollTop;
			}
			else
			{
			iCur=parseInt(getStyle(obj, attr));
			}
		
			var iSpeed=(json[attr]-iCur)/8;
			iSpeed=iSpeed>0?Math.ceil(iSpeed):Math.floor(iSpeed);
			if(iCur!=json[attr]){
				bStop=false;
			}
			if(attr=="opacity"){
				obj.style.filter='alpha(opacity:'+(iCur+iSpeed)+')';
				obj.style.opacity=(iCur+iSpeed)/100;
				}
			else if(attr=="scrollTop"){
					document.documentElement.scrollTop=document.body.scrollTop=iCur+iSpeed;
				}else{
				obj.style[attr]=iCur+iSpeed+"px";
			}
			if(bStop){
				clearInterval(obj.timer);
			
				if(fn)
				{
					fn();
				}
			}
		}
		},30);
	}
/*防止js鼠标事件多次触发*/
function contains(parentNode, childNode) {
    if (parentNode.contains) {
        return parentNode != childNode && parentNode.contains(childNode);
    } else {
        return !!(parentNode.compareDocumentPosition(childNode) & 16);
    }
}
function checkHover(e,target){
    if (getEvent(e).type=="mouseover")  {
        return !contains(target,getEvent(e).relatedTarget||getEvent(e).fromElement) && !((getEvent(e).relatedTarget||getEvent(e).fromElement)===target);
    } else {
        return !contains(target,getEvent(e).relatedTarget||getEvent(e).toElement) && !((getEvent(e).relatedTarget||getEvent(e).toElement)===target);
    }
}function getEvent(e){
    return e||window.event;
}
