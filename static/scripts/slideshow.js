(function(window, undefined){

  /* prefrences */
  var slideshowSpeedInSeconds = 5;



	var ShowElements={
		slides:document.querySelectorAll("#slideshow figure"),
    captions:document.getElementsByTagName("figcaption")
	};
	var active = {
		get:0,
		set:function(arrayPosition){
			active.reset(ShowElements.slideNav);
			active.reset(ShowElements.slides);
			ShowElements.slideNav[arrayPosition].className = "slide";
			ShowElements.slides[arrayPosition].className = "show";
		},
		reset:function(array){
			for(let i=0,ilen=array.length;i<ilen;++i){
				array[i].removeAttribute("class");
			}
		},
		auto:function(){++active.get;
			if(ShowElements.slides.length===active.get){
				active.set(0);
				active.get = 0;
			}else{
				active.set(active.get);
			}
		}
	};
	(function setup(){
		// nav setup
		var showNav = document.createElement("ul");
		for(let i=0,ilen=ShowElements.slides.length;i<ilen;++i){
			var link = document.createElement("a");
			link.href="";
			showNav.appendChild(link);
		}
		document.getElementById("slideshow").appendChild(showNav);
		ShowElements.slideNav = document.querySelectorAll("#slideshow ul a");
		active.set(active.get);
    //figcaption delete when empty
    for(let i=0;i<ShowElements.captions.length;){
      ShowElements.captions[i].innerHTML = ShowElements.captions[i].innerHTML.trim();
      if(ShowElements.captions[i].innerHTML===""){
        ShowElements.captions[i].remove();
      }else{
        ++i;
      }
    }
		//click setup
		for(let i=0,ilen=ShowElements.slideNav.length;i<ilen;++i){
			ShowElements.slideNav[i].addEventListener("click",function(e){
				e.preventDefault();
				active.set(i);
				active.get = i;
				clearInterval(autoSlide);
				autoSlide = setInterval(active.auto,slideshowSpeedInSeconds*1000);
			});
		}
		//auto setup
		var autoSlide = setInterval(active.auto,slideshowSpeedInSeconds*1000);
	})()
}(window));
