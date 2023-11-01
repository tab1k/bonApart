"use strict";window.Element.prototype.removeClass=function(){let e=arguments.length>0&&void 0!==arguments[0]?arguments[0]:"",t=this;return t instanceof HTMLElement||null===t||(t=document.querySelector(t)),this.isVariableDefined(t)&&e&&t.classList.remove(e),this},window.Element.prototype.addClass=function(){let e=arguments.length>0&&void 0!==arguments[0]?arguments[0]:"",t=this;return t instanceof HTMLElement||null===t||(t=document.querySelector(t)),this.isVariableDefined(t)&&e&&t.classList.add(e),this},window.Element.prototype.toggleClass=function(){let e=arguments.length>0&&void 0!==arguments[0]?arguments[0]:"",t=this;return t instanceof HTMLElement||null===t||(t=document.querySelector(t)),this.isVariableDefined(t)&&e&&t.classList.toggle(e),this},window.Element.prototype.isVariableDefined=function(){return!!this&&void 0!==this&&null!=this};var ThemeColor={getCssVariableValue:function(e){var t=getComputedStyle(document.documentElement).getPropertyValue(e);return t&&t.length>0&&(t=t.trim()),t}},e={init:function(){e.preLoader(),e.megaMenu(),e.stickyHeader(),e.tinySlider(),e.stickyBar(),e.toolTipFunc(),e.popOverFunc(),e.backTotop(),e.lightBox(),e.choicesSelect(),e.aosFunc(),e.quill(),e.stepper(),e.pricing(),e.stickyElement(),e.flatPicker(),e.splideSlider(),e.rangeSlider(),e.dropZone(),e.fakePwd(),e.autoTabinput(),e.trafficstatsChart(),e.trafficChart(),e.guestSelector(),e.parallaxBG(),e.overlayScrollbars(),e.trafficsplineChart(),e.trafficroomChart()},isVariableDefined:function(e){return typeof!!e&&"undefined"!=e&&null!=e},getParents:function(t,a,i){const r=[],o=t.matches||t.webkitMatchesSelector||t.mozMatchesSelector||t.msMatchesSelector;for(t=t.parentElement;t&&!o.call(t,a);){if(i)o.call(t,i)&&r.push(t);else if(a){if(o.call(t,a))return r.push(t)}else r.push(t);if(t=t.parentElement,e.isVariableDefined(t)&&o.call(t,a))return t}return r},getNextSiblings:function(e,t,a){let i=[],r=e.parentNode.firstChild;const o=e.matches||e.webkitMatchesSelector||e.mozMatchesSelector||e.msMatchesSelector;do{if(3!==r.nodeType&&r!==e&&r===e.nextElementSibling&&(!a||a(e))){if(t){if(o.call(r,t))return r}else i.push(r);e=r}}while(r=r.nextSibling);return i},on:function(e,t,a){document.addEventListener("DOMContentLoaded",(()=>{e instanceof HTMLElement||null===e||(e=document.querySelector(e)),e.addEventListener(t,a)}))},onAll:function(e,t,a){document.addEventListener("DOMContentLoaded",(()=>{document.querySelectorAll(e).forEach((e=>{if(t.indexOf(",")>-1){t.split(",").forEach((t=>{e.addEventListener(t,a)}))}else e.addEventListener(t,a)}))}))},removeClass:function(t,a){t instanceof HTMLElement||null===t||(t=document.querySelector(t)),e.isVariableDefined(t)&&t.removeClass(a)},removeAllClass:function(t,a){e.isVariableDefined(t)&&t instanceof HTMLElement&&document.querySelectorAll(t).forEach((e=>{e.removeClass(a)}))},toggleClass:function(t,a){t instanceof HTMLElement||null===t||(t=document.querySelector(t)),e.isVariableDefined(t)&&t.toggleClass(a)},toggleAllClass:function(t,a){e.isVariableDefined(t)&&t instanceof HTMLElement&&document.querySelectorAll(t).forEach((e=>{e.toggleClass(a)}))},addClass:function(t,a){t instanceof HTMLElement||null===t||(t=document.querySelector(t)),e.isVariableDefined(t)&&t.addClass(a)},select:function(e){return document.querySelector(e)},selectAll:function(e){return document.querySelectorAll(e)},preLoader:function(){window.onload=function(){var t=e.select(".preloader");e.isVariableDefined(t)&&(t.className+=" animate__animated animate__fadeOut",setTimeout((function(){t.style.display="none"}),200))}},megaMenu:function(){e.onAll(".dropdown-menu a.dropdown-item.dropdown-toggle","click",(function(t){var a=this;if(t.preventDefault(),t.stopImmediatePropagation(),e.isVariableDefined(a.nextElementSibling)&&!a.nextElementSibling.classList.contains("show")){const t=e.getParents(a,".dropdown-menu");e.removeClass(t.querySelector(".show"),"show"),e.isVariableDefined(t.querySelector(".dropdown-opened"))&&e.removeClass(t.querySelector(".dropdown-opened"),"dropdown-opened")}var i=e.getNextSiblings(a,".dropdown-menu");e.toggleClass(i,"show"),i.previousElementSibling.toggleClass("dropdown-opened");var r=e.getParents(a,"li.nav-item.dropdown.show");e.isVariableDefined(r)&&r.length>0&&e.on(r,"hidden.bs.dropdown",(function(t){e.removeAllClass(".dropdown-submenu .show")}))}))},stickyHeader:function(){var t=e.select(".header-sticky");if(e.isVariableDefined(t)){var a=t.offsetHeight;t.insertAdjacentHTML("afterend",'<div id="sticky-space"></div>');var i=e.select("#sticky-space");e.isVariableDefined(i)&&document.addEventListener("scroll",(function(r){(window.pageYOffset||document.documentElement.scrollTop)>=400?(i.addClass("active"),e.select("#sticky-space.active").style.height=a+"px",t.addClass("header-sticky-on")):(i.removeClass("active"),i.style.height="0px",t.removeClass("header-sticky-on"))}))}},tinySlider:function(){var t=e.select(".tiny-slider-inner");e.isVariableDefined(t)&&e.selectAll(".tiny-slider-inner").forEach((t=>{var a=t,i=a.getAttribute("data-mode")?a.getAttribute("data-mode"):"carousel",r=a.getAttribute("data-axis")?a.getAttribute("data-axis"):"horizontal",o=a.getAttribute("data-gutter")?a.getAttribute("data-gutter"):30,n=a.getAttribute("data-edge")?a.getAttribute("data-edge"):0,l=a.getAttribute("data-items")?a.getAttribute("data-items"):4,s=a.getAttribute("data-items-xl")?a.getAttribute("data-items-xl"):Number(l),c=a.getAttribute("data-items-lg")?a.getAttribute("data-items-lg"):Number(s),d=a.getAttribute("data-items-md")?a.getAttribute("data-items-md"):Number(c),u=a.getAttribute("data-items-sm")?a.getAttribute("data-items-sm"):Number(d),f=a.getAttribute("data-items-xs")?a.getAttribute("data-items-xs"):Number(u),m=a.getAttribute("data-speed")?a.getAttribute("data-speed"):500,p="true"===a.getAttribute("data-autowidth"),g="false"!==a.getAttribute("data-arrow"),b="false"!==a.getAttribute("data-dots"),h="false"!==a.getAttribute("data-autoplay"),v=a.getAttribute("data-autoplaytime")?a.getAttribute("data-autoplaytime"):4e3,y="true"===a.getAttribute("data-hoverpause");if(e.isVariableDefined(e.select(".custom-thumb")))var w=e.select(".custom-thumb");var A,S="false"!==a.getAttribute("data-loop"),C="true"===a.getAttribute("data-rewind"),E="true"===a.getAttribute("data-autoheight"),k="true"===a.getAttribute("data-autowidth"),V="true"===a.getAttribute("data-fixedwidth"),x="false"!==a.getAttribute("data-touch"),D="false"!==a.getAttribute("data-drag");"rtl"===document.getElementsByTagName("html")[0].getAttribute("dir")&&(A="rtl");tns({container:t,mode:i,axis:r,gutter:o,edgePadding:n,speed:m,autoWidth:p,controls:g,nav:b,autoplay:h,autoplayTimeout:v,autoplayHoverPause:y,autoplayButton:!1,autoplayButtonOutput:!1,controlsPosition:top,navContainer:w,navPosition:top,autoplayPosition:top,controlsText:['<i class="bi bi-arrow-left"></i>','<i class="bi bi-arrow-right"></i>'],loop:S,rewind:C,autoHeight:E,autoWidth:k,fixedWidth:V,touch:x,mouseDrag:D,arrowKeys:!0,items:l,textDirection:A,responsive:{0:{items:Number(f)},576:{items:Number(u)},768:{items:Number(d)},992:{items:Number(c)},1200:{items:Number(s)}}})}))},stickyBar:function(){var t=e.select("[data-sticky]");if(e.isVariableDefined(t))new Sticky("[data-sticky]")},toolTipFunc:function(){[].slice.call(e.selectAll('[data-bs-toggle="tooltip"]')).map((function(e){return new bootstrap.Tooltip(e)}))},popOverFunc:function(){[].slice.call(e.selectAll('[data-bs-toggle="popover"]')).map((function(e){return new bootstrap.Popover(e)}))},backTotop:function(){window.scrollY;var t=e.select(".back-top");if(e.isVariableDefined(t)){window.addEventListener("scroll",(function(){window.scrollY>=800?t.addClass("back-top-show"):t.removeClass("back-top-show")})),t.addEventListener("click",(()=>window.scrollTo({top:0,behavior:"smooth"})))}},lightBox:function(){var t=e.select("[data-glightbox]");if(e.isVariableDefined(t))GLightbox({selector:"*[data-glightbox]",openEffect:"fade",closeEffect:"fade"})},choicesSelect:function(){var t=e.select(".js-choice");e.isVariableDefined(t)&&document.querySelectorAll(".js-choice").forEach((function(e){var t="true"==e.getAttribute("data-remove-item-button"),a="false"!=e.getAttribute("data-placeholder"),i=e.getAttribute("data-placeholder-val")?e.getAttribute("data-placeholder-val"):"Type and hit enter",r=e.getAttribute("data-max-item-count")?e.getAttribute("data-max-item-count"):3,o="true"==e.getAttribute("data-search-enabled");new Choices(e,{removeItemButton:t,placeholder:a,placeholderValue:i,maxItemCount:r,searchEnabled:o,shouldSort:!1})}))},aosFunc:function(){var t=e.select(".aos");e.isVariableDefined(t)&&AOS.init({duration:500,easing:"ease-out-quart",once:!0})},quill:function(){var t=e.select(".quilleditor");e.isVariableDefined(t)&&e.selectAll(".quilleditor").forEach((function(e){var t=e.previousElementSibling;new Quill(e,{modules:{toolbar:t},theme:"snow"})}))},stepper:function(){var t=e.select("#stepper");if(e.isVariableDefined(t)){var a=document.querySelectorAll(".next-btn"),i=document.querySelectorAll(".prev-btn"),r=new Stepper(document.querySelector("#stepper"),{linear:!1,animation:!0});a.forEach((function(e){e.addEventListener("click",(()=>{r.next()}))})),i.forEach((function(e){e.addEventListener("click",(()=>{r.previous()}))}))}},pricing:function(){var t=e.select(".price-wrap");e.isVariableDefined(t)&&e.selectAll(".price-wrap").forEach((e=>{var t=e.querySelector(".price-toggle"),a=e.querySelectorAll(".plan-price");t.addEventListener("change",(function(){t.checked?a.forEach((e=>{var t=e.getAttribute("data-annual-price");e.innerHTML=t})):a.forEach((e=>{var t=e.getAttribute("data-monthly-price");e.innerHTML=t}))}))}))},stickyElement:function(){window.scrollY;var t=e.select(".sticky-element");if(e.isVariableDefined(t)){window.addEventListener("scroll",(function(){window.scrollY>=800?t.addClass("sticky-element-sticked"):t.removeClass("sticky-element-sticked")}))}},flatPicker:function(){var t=e.select(".flatpickr");e.isVariableDefined(t)&&e.selectAll(".flatpickr").forEach((function(e){var t="multiple"==e.getAttribute("data-mode")?"multiple":"range"==e.getAttribute("data-mode")?"range":"single",a="true"==e.getAttribute("data-enableTime"),i="true"==e.getAttribute("data-noCalendar"),r="true"==e.getAttribute("data-inline"),o=e.getAttribute("data-date-format")?e.getAttribute("data-date-format"):"true"==e.getAttribute("data-enableTime")?"h:i K":"d M";flatpickr(e,{mode:t,enableTime:a,noCalendar:i,inline:r,animate:"false",position:"top",dateFormat:o,disableMobile:"true"})}))},splideSlider:function(){var t=e.select(".splide-main");if(e.isVariableDefined(t)){var a=new Splide(".splide-thumb",{rewind:!0,fixedWidth:200,fixedHeight:120,isNavigation:!0,gap:10,focus:"center",pagination:!1,cover:!0,breakpoints:{600:{fixedWidth:150,fixedHeight:100}}}).mount();new Splide(".splide-main",{type:"fade",heightRatio:.5,pagination:!1,arrows:!1,autoplay:!0,cover:!0}).sync(a).mount()}},rangeSlider:function(){var t=e.select(".noui-slider-range");e.isVariableDefined(t)&&e.selectAll(".noui-slider-range").forEach((e=>{var t=parseInt(e.getAttribute("data-range-min")),a=parseInt(e.getAttribute("data-range-max")),i=parseInt(e.getAttribute("data-range-selected-min")),r=parseInt(e.getAttribute("data-range-selected-max")),o=e.previousElementSibling,n=[o.firstElementChild,o.lastElementChild];noUiSlider.create(e,{start:[i,r],connect:!0,step:1,range:{min:[t],max:[a]}}),e.noUiSlider.on("update",(function(e,t){n[t].value=e[t]}))}))},dropZone:function(){e.isVariableDefined(e.select("[data-dropzone]"))&&(window.Dropzone.autoDiscover=!1,e.isVariableDefined(e.select(".dropzone-default"))&&e.selectAll(".dropzone-default").forEach((e=>{const t={...{url:"/upload",init:function(){this.on("error",(function(e,t){if(e.accepted){var a=document.getElementsByClassName("dz-error");(a=a[a.length-1]).classList.toggle("dz-error"),a.classList.toggle("dz-success")}}))}},...e.dataset.dropzone?JSON.parse(e.dataset.dropzone):{}};new Dropzone(e,t)})),e.isVariableDefined(e.select(".dropzone-custom"))&&e.selectAll(".dropzone-custom").forEach((e=>{const t=e.dataset.dropzone?JSON.parse(e.dataset.dropzone):{},a={...{addRemoveLinks:!0,previewsContainer:e.querySelector(".dz-preview"),previewTemplate:e.querySelector(".dz-preview").innerHTML,url:"/upload",init:function(){this.on("error",(function(e,t){if(e.accepted){var a=document.getElementsByClassName("dz-error");(a=a[a.length-1]).classList.toggle("dz-error"),a.classList.toggle("dz-success")}}))}},...t};e.querySelector(".dz-preview").innerHTML="",new Dropzone(e,a)})))},fakePwd:function(){if(e.isVariableDefined(e.select(".fakepassword"))){var t=document.querySelector(".fakepassword"),a=document.querySelector(".fakepasswordicon");a.addEventListener("click",(()=>{"password"==t.type?(t.setAttribute("type","text"),a.classList.add("fa-eye")):(a.classList.remove("fa-eye"),t.setAttribute("type","password"))}))}},autoTabinput:function(){var t=document.getElementsByClassName("autotab")[0];e.isVariableDefined(t)&&(t.onkeyup=function(e){var t=e.srcElement,a=parseInt(t.attributes.maxlength.value,10);if(t.value.length>=a)for(var i=t;(i=i.nextElementSibling)&&null!=i;)if("input"==i.tagName.toLowerCase()){i.focus();break}})},guestSelector:function(){if(e.isVariableDefined(e.select(".guest-selector"))){let t=2,a=0,i=1,r=2,o=document.querySelector(".selection-result"),n=document.querySelector(".adults"),l=document.querySelector(".adult-add"),s=document.querySelector(".adult-remove"),c=document.querySelector(".child"),d=document.querySelector(".child-add"),u=document.querySelector(".child-remove"),f=document.querySelector(".rooms"),m=document.querySelector(".room-add"),p=document.querySelector(".room-remove");function g(e){"adult"==e?(t++,r=t+a,b()):"child"==e?(a+=1,console.log(a),r=t+a,b()):"room"==e&&(i++,b())}function b(){n.innerText=t,c.innerText=a,f.innerText=i;let e=r+" "+(r>1?"Guests":"Guest")+" "+i+" "+(i>1?"Rooms":"Room");o.setAttribute("value",e)}function h(e){"adult"==e?(t=t>0?t-1:t,r=t+a,b()):"child"==e?(a=a>0?a-1:a,r=t+a,b()):"room"==e&&(i=i>0?i-1:i,b())}l.addEventListener("click",(function(){g("adult")})),s.addEventListener("click",(function(){h("adult")})),d.addEventListener("click",(function(){g("child")})),u.addEventListener("click",(function(){h("child")})),m.addEventListener("click",(function(){g("room")})),p.addEventListener("click",(function(){h("room")}))}},parallaxBG:function(){var t=e.select(".bg-parallax");e.isVariableDefined(t)&&jarallax(e.selectAll(".bg-parallax"),{speed:.6})},overlayScrollbars:function(){e.select(".custom-scrollbar")&&document.addEventListener("DOMContentLoaded",(function(){document.querySelectorAll(".custom-scrollbar").forEach((e=>{OverlayScrollbars(e,{scrollbars:{autoHide:"leave",autoHideDelay:200},overflowBehavior:{x:"visible-hidden",y:"scroll"}})}))}))},trafficstatsChart:function(){var t=e.select("#apexChartTrafficStats");if(e.isVariableDefined(t)){new ApexCharts(document.querySelector("#apexChartTrafficStats"),{colors:["#2163e8"],series:[{name:"Users",data:[100,401,305,501,409,602,609,901,848,602,809,901]}],chart:{height:320,type:"area",toolbar:{show:!1}},grid:{strokeDashArray:4,position:"back"},dataLabels:{enabled:!1},stroke:{curve:"smooth"},legend:{show:!0,horizontalAlign:"right",position:"top",labels:{},markers:{width:8,height:8}},xaxis:{labels:{show:!0},axisBorder:{show:!1},categories:["Jan","Feb","Mar","Apr","May","Jun","Jul","Aug","Sep","Oct","Nov","Dec"]},tooltip:{x:{format:"dd/MM/yy HH:mm"}}}).render()}},trafficChart:function(){var t=e.select("#ChartTrafficViews");if(e.isVariableDefined(t)){var a={series:[70,15,10,5],labels:["Organic","Google","Social media","Referral"],chart:{height:200,width:200,offsetX:0,type:"donut",sparkline:{enabled:!0}},colors:[ThemeColor.getCssVariableValue("--bs-primary"),ThemeColor.getCssVariableValue("--bs-success"),ThemeColor.getCssVariableValue("--bs-warning"),ThemeColor.getCssVariableValue("--bs-danger")],tooltip:{theme:"dark"},responsive:[{breakpoint:480,options:{chart:{width:200,height:200},legend:{position:"bottom"}}}]};new ApexCharts(document.querySelector("#ChartTrafficViews"),a).render()}},trafficsplineChart:function(){var t=e.select("#ChartGuesttraffic");if(e.isVariableDefined(t)){var a={series:[{name:"Check-in",data:[31,40,28,51,42,109,100]},{name:"Check-out",data:[11,32,45,32,34,52,41]}],chart:{height:350,type:"area"},colors:[ThemeColor.getCssVariableValue("--bs-primary"),ThemeColor.getCssVariableValue("--bs-info")],dataLabels:{enabled:!1},stroke:{curve:"smooth"},xaxis:{type:"day",categories:["SUN","MON","TUE","WED","THU","FRI","SAT"]}};new ApexCharts(document.querySelector("#ChartGuesttraffic"),a).render()}},trafficroomChart:function(){var t=e.select("#ChartTrafficRooms");if(e.isVariableDefined(t)){var a={series:[70,30],labels:["Sold Out","Available"],chart:{height:300,width:300,offsetX:0,type:"donut",sparkline:{enabled:!0}},colors:[ThemeColor.getCssVariableValue("--bs-danger"),ThemeColor.getCssVariableValue("--bs-success")],tooltip:{theme:"dark"},responsive:[{breakpoint:480,options:{chart:{width:200,height:200},legend:{position:"bottom"}}}]};new ApexCharts(document.querySelector("#ChartTrafficRooms"),a).render()}}};e.init();