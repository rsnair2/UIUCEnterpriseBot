//
//  ViewController.swift
//  UIUCWebby
//
//  Created by Rajiv Nair on 8/1/15.
//  Copyright (c) 2015 Hopsy. All rights reserved.
//

import Cocoa

class LoginViewController: NSViewController {

    @IBOutlet weak var UIUCLoginUsername: NSTextField!
    @IBOutlet weak var UIUCLoginPassword: NSSecureTextField!
    var loggedIn: Bool!
    
    @IBAction func LoginButtonAction(sender: AnyObject) {
        let username = UIUCLoginUsername.stringValue
        let password = UIUCLoginPassword.stringValue
        StoreLoginInfo(password, username)
        let defaults = NSUserDefaults.standardUserDefaults()
        defaults.setObject(username, forKey: "username")
        self.transitionToLoggedInUX()
    }
    
    func transitionToLoggedInUX() {
    }
    
    override func viewDidAppear() {
        super.viewDidAppear()
        let defaults = NSUserDefaults.standardUserDefaults()
        let username: String? = defaults.objectForKey("username") as? String
        
        var itemRef: UnsafeMutablePointer<SecKeychainItemRef>
        if((username) != nil) {
            let password = GetLoginInfo(username)
            if((password) != nil) {
                self.transitionToLoggedInUX()
            }
        }

        // Do any additional setup after loading the view.
    }

    override var representedObject: AnyObject? {
        didSet {
        // Update the view, if already loaded.
        }
    }
}

