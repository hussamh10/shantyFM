const electron = require('electron');
const url = require('url');
const path = require('path');

const {app, BrowserWindow, Menu, ipcMain} = electron;

let mainWindow

//Listen for app to be ready
app.on('ready', function(){
	//create new win
	mainWindow = new BrowserWindow({});
	//load html
	mainWindow.loadURL(url.format({
		pathname: path.join(__dirname, 'mainWindow.html'),
		protocol:'file:',
		slashes: true
	}));

	const main_menu = Menu.buildFromTemplate(mainMenuTemplate);
	Menu.setApplicationMenu(main_menu);
});


ipcMain.on('play:song', function(e, song){
	playSong(song);
});

function playSong(song){
	console.log(song);
}


// Toolbar
const mainMenuTemplate = [
	{
		label:'File',
		submenu:[
			{
				label:'Exit',
				click(){
					app.quit()
				}
			}
		]
	}
]
