Hier ist eine Auflistung zu finden, welche Webseiten im Quellcode einen Hinweis auf captcha enthalten

Aufgelistet wird hier die Webseite und ein Auszug aus dem Quellcode der Seite

Geprüft wurde wie folgt:

  1. Webseite besucht und Quellcode auf captcha geprüft
  
  2. Webseite besucht, Stream gestartet und Quellcode auf captcha geprüft

Folgende  Webseite zeigen Captcha im Quellcode:

**anime-loads.org**

<div class="captcha">

<div class="captcha-holder">

**hd-streams.org**

<div class="movie-cover" @click="recaptcha(1, 1, 'de', '')">

<script src="https://www.google.com/recaptcha/api.js?onload=vueRecaptchaInit&render=explicit" async defer></script>

**kinoger.com**

<div id="dle_recaptcha"></div>

<script type="text/javascript" src="//www.google.com/recaptcha/api/js/recaptcha_ajax.js"></script>

function reload () {

	var rndval = new Date().getTime(); 

	document.getElementById('dle-captcha').innerHTML = '<img src="/engine/modules/antibot/antibot.php?rndval=' + rndval + '" width="160" height="80" alt="" /><br /><a onclick="reload(); return false;" href="#">aktualisieren, wenn Sie den Code nicht sehen</a>';

$(function(){

	Recaptcha.create("6LfoOroSAAAAAEg7PViyas0nRqCN9nIztKxWcDp_",
  
     "dle_recaptcha",
     
     {
     
**kinox.tv**

<div class="login_label">Captcha:</div>
<div id="login_recaptcha_div"></div>
<script type="text/javascript" src="https://www.google.com/recaptcha/api/js/recaptcha_ajax.js"></script>
<script> 
               function showRecaptcha(element) {
                 Recaptcha.create("6LcxeMUSAAAAABtLiAoW0YZtF83tQaCq5Hqk776V", element, {
                   theme: "white",
                   lang: "de",
                   callback: Recaptcha.focus_response_field});


**szene-streamz.com**
		       
<script type="text/javascript" async defer src="https://www.google.com/recaptcha/api.js?onload=reCallback&render=explicit&hl=de"></script>
	<script type="text/javascript">//------------UCOZ-JS-CODE-----------

	function reCallback() {
		$('.g-recaptcha').each(function(index, element ) {
			element.setAttribute('rcid', index );
			if ($(element).is(':empty') ) grecaptcha.render(element, {sitekey:element.getAttribute('data-sitekey'), theme:element.getAttribute('data-theme'), size:element.getAttribute('data-size') });
		});
	}
	function reReset(reset ) {
		reset && grecaptcha.reset(reset.previousElementSibling.getAttribute('rcid') );
		if (!reset ) for (rel in ___grecaptcha_cfg.clients ) grecaptcha.reset(rel );
	}
		       
