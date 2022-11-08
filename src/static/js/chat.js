getInfo = function (image, name) {
  const template = `<div class="chat-pfp">
				<span class="dot"></span>
				<img src="../static/images/png/${image}" alt="${name}">
			</div>
			<div class="chat-name">
				<h2>${name}</h2>
			</div>
			<i class="fa fa-light fa-volume-off fa-lg"></i>`;

  document.getElementsByClassName("chat-usuario").innerHTML = template;
  $('.chat-usuario').html(template)

};
