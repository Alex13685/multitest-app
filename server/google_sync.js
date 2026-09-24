// ==============================================================================
// ВСТАВЬТЕ ВЕСЬ ЭТОТ КОД В Google Apps Script (Код.gs)
// Предварительно выделите всё в редакторе (Ctrl + A) и удалите старый текст!
// ==============================================================================

var FILE_NAME = "trainer_state.json";

function doPost(e) {
  try {
    if (!e || !e.postData || !e.postData.contents) {
      return ContentService.createTextOutput(JSON.stringify({ 
        error: "Empty payload received" 
      })).setMimeType(ContentService.MimeType.JSON);
    }

    var payload = JSON.parse(e.postData.contents);
    var files = DriveApp.getFilesByName(FILE_NAME);
    var file;

    if (files.hasNext()) {
      file = files.next();
    } else {
      file = DriveApp.createFile(FILE_NAME, "{}", MimeType.PLAIN_TEXT);
    }

    file.setContent(JSON.stringify(payload, null, 2));

    var responseData = {
      status: "success",
      synced_at: new Date().getTime(),
      items_count: (payload.user_states || []).length
    };

    return ContentService.createTextOutput(JSON.stringify(responseData))
      .setMimeType(ContentService.MimeType.JSON);

  } catch (err) {
    return ContentService.createTextOutput(JSON.stringify({ 
      error: err.toString() 
    })).setMimeType(ContentService.MimeType.JSON);
  }
}

function doGet(e) {
  try {
    var files = DriveApp.getFilesByName(FILE_NAME);
    var content = "{}";

    if (files.hasNext()) {
      content = files.next().getBlob().getDataAsString();
    }

    return ContentService.createTextOutput(content)
      .setMimeType(ContentService.MimeType.JSON);

  } catch (err) {
    return ContentService.createTextOutput(JSON.stringify({ 
      error: err.toString() 
    })).setMimeType(ContentService.MimeType.JSON);
  }
}
