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
    
    @IBAction func LoginButtonAction(sender: AnyObject) {
        // add new username, password item to keychain
        let username = UIUCLoginUsername.stringValue
        let password = UIUCLoginPassword.stringValue
        StoreLoginInfo(password, username)
        let defaults = NSUserDefaults.standardUserDefaults()
        defaults.setObject(username, forKey: "username")
        self.transitionToLoggedInUX()
    }
    
    func transitionToLoggedInUX() {
    }
    
    override func viewWillAppear() {
        super.viewWillAppear()
        
        // try and load password from keychain
        let defaults = NSUserDefaults.standardUserDefaults()
        let username: String? = defaults.objectForKey("username") as? String
        
        if((username) != nil) {
            let password = GetLoginInfo(username)
            if((password) != nil) {
                self.transitionToLoggedInUX()
            }
        }
    }

    override var representedObject: AnyObject? {
        didSet {
        }
    }
}

