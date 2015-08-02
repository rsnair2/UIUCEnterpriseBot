//
//  keychain.m
//  UIUCWebby
//
//  Created by Rajiv Nair on 8/2/15.
//  Copyright (c) 2015 Hopsy. All rights reserved.
//

#import <Foundation/Foundation.h>

//Call SecKeychainAddGenericPassword to add a new password to the keychain:
OSStatus StoreLoginInfo (NSString *password, NSString *username)
{
    NSString *serviceName = [[NSBundle mainBundle] bundleIdentifier];
    OSStatus status;
    status = SecKeychainAddGenericPassword (
                                            NULL,   // default keychain
                                            (int)[serviceName length],  // length of service name
                                            [serviceName cStringUsingEncoding:NSASCIIStringEncoding],   // service name
                                            (int)[username length], // length of account name
                                            [username cStringUsingEncoding:NSASCIIStringEncoding],  // account name
                                            (int)[password length], // length of password
                                            [password cStringUsingEncoding:NSASCIIStringEncoding],  // pointer to password data
                                            NULL    // the item reference
                                            );
    return (status);
}

//Call SecKeychainFindGenericPassword to get a password from the keychain:
NSString * GetLoginInfo (NSString *username)
{
    NSString *serviceName = [[NSBundle mainBundle] bundleIdentifier];
    OSStatus status;
    void *passwordData;
    UInt32 passwordLength;
    SecKeychainItemRef itemRef;
    status = SecKeychainFindGenericPassword (
                                              NULL,           // default keychain
                                              (int)[serviceName length],  // length of service name
                                              [serviceName cStringUsingEncoding:NSASCIIStringEncoding],   // service name
                                              (int)[username length], // length of account name
                                              [username cStringUsingEncoding:NSASCIIStringEncoding],  // account name
                                              &passwordLength,  // length of password
                                              &passwordData,   // pointer to password data
                                              &itemRef // the item reference
                                              );
    
    NSString * password = [NSString stringWithFormat:@"%s", (char *)passwordData];
    return password;
}

//Call SecKeychainItemModifyAttributesAndData to change the password for
// an item already in the keychain:
OSStatus DeleteLoginInfo (NSString * username)
{
    OSStatus status;
    NSString *serviceName = [[NSBundle mainBundle] bundleIdentifier];
    void *passwordData;
    UInt32 passwordLength;
    SecKeychainItemRef itemRef;
    status = SecKeychainFindGenericPassword (
                                              NULL,           // default keychain
                                              (int)[serviceName length],  // length of service name
                                              [serviceName cStringUsingEncoding:NSASCIIStringEncoding],   // service name
                                              (int)[username length], // length of account name
                                              [username cStringUsingEncoding:NSASCIIStringEncoding],  // account name
                                              &passwordLength,  // length of password
                                              &passwordData,   // pointer to password data
                                              &itemRef // the item reference
                                              );
    status = SecKeychainItemDelete(itemRef);
    return (status);
}
