//
//  MainViewController.swift
//  UIUCWebby
//
//  Created by Rajiv Nair on 8/2/15.
//  Copyright (c) 2015 Hopsy. All rights reserved.
//

import Cocoa

class MainViewController: NSViewController {
    
    @IBAction func LogoutButtonAction(sender: AnyObject) {
        let defaults = NSUserDefaults.standardUserDefaults()
        let username: String? = defaults.objectForKey("username") as? String
        DeleteLoginInfo(username)
        defaults.removeObjectForKey("username")
    }
    
    override func viewDidLoad() {
        super.viewDidLoad()
        // Do any additional setup after loading the view.
    }
    
    override var representedObject: AnyObject? {
        didSet {
            // Update the view, if already loaded.
        }
    }
}