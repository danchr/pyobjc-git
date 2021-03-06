from Cocoa import NSDocument
import objc
from loader import MHTLoader


class MHTDocument(NSDocument):
    locationbox = objc.IBOutlet()
    webview = objc.IBOutlet()

    path = None
    statusText = None

    @objc.IBAction
    def navigateHistory_(self, sender):
        if sender.selectedSegment() == 0:
            self.webview.goBack_(sender)
        else:
            self.webview.goForward_(sender)

    def windowNibName(self):
        return "MHTDocument"

    def readFromFile_ofType_(self, path, tp):
        if self.webview is None:
            self.path = path
        else:
            self.readMHT_(path)

        return True

    def writeToFile_ofType_(self, path, tp):
        # TODO: "save-as" functionality
        return False

    def windowControllerDidLoadNib_(self, controller):
        if self.path:
            self.readMHT_(self.path)

    def readMHT_(self, path):
        self.mht = MHTLoader(path)
        self.locationbox.setStringValue_(self.mht.fixupURL(self.mht.root))
        archive = self.mht.asWebArchive()
        print("Archive", archive.description())
        with open("/tmp/archive.webarchive", "wb") as fp:
            fp.write(archive.data().bytes())
        self.webview.mainFrame().stopLoading()
        self.webview.mainFrame().loadArchive_(archive)
        1 / 0
