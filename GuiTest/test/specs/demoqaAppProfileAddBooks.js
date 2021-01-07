describe("Connect to BookStore and log in", function() {
    it("The login function authenticates and allows all the following functions to proceed", function() {
        browser.url("/login");
        $("#userName").waitForDisplayed();
        $("#userName").addValue("dean");
        $("#password").addValue("Password*1");
        $("#login").click();

        expect ($("#searchBox")).toBeDisplayed();

        browser.pause(2000);
    });
});

describe("Go to the bookstore from profile", function() {
    it("Add a book to the users list of books", function() {
        browser.url("/profile");
        $("#gotoStore").waitForClickable();  //Go to Book Store Button
        $("#gotoStore").click();
        $("//*[contains(@id, 'see-book-Git')]").waitForClickable();  //Add the Git book
        $("//*[contains(@id, 'see-book-Git')]").click();
        $("//button[@id='addNewRecordButton']/parent::div/following-sibling::div").waitForClickable();  //Add To Yor Collection Button
        $("//button[@id='addNewRecordButton']/parent::div/following-sibling::div").click();

        var bookUrls = ["https://demoqa.com/books?book=9781491904244", //add four more books
            "https://demoqa.com/books?book=9781449331818",
            "https://demoqa.com/books?book=9781449337711",
            "https://demoqa.com/books?book=9781449365035"];

    
        for(var i=0; i<bookUrls.length; i++) {
            browser.url(bookUrls[i]);
            $("//button[@id='addNewRecordButton']/parent::div/following-sibling::div").waitForClickable();  //Add To Yor Collection Button
            $("//button[@id='addNewRecordButton']/parent::div/following-sibling::div").click();
           
            browser.pause(10000);  //I didn't find a waitForAlert() call. I may be able to replace with with an action or javascript later.
            browser.acceptAlert();

        }

        browser.url("/profile");
        expect ($("//*[contains(@id, 'see-book-Speaking')]")).toBeDisplayed();  // see if the last book has been added

        browser.pause(5000);
    });
});

describe("Remove one book", function() {
    it("Remove a book", function() {
        browser.url("/profile");
        browser.pause(5000); // pause to see profile page
        $$("#delete-record-undefined")[3].waitForClickable(); //select the 4th book 
        $$("#delete-record-undefined")[3].click();
        $("#closeSmallModal-cancel").waitForClickable();  // cancel
        $("#closeSmallModal-cancel").click();

        $$("#delete-record-undefined")[3].waitForClickable(); //select the 4th book (Designing)
        $$("#delete-record-undefined")[3].click();
        $("#closeSmallModal-ok").waitForClickable();  // ok - delete
        $("#closeSmallModal-ok").click();


        browser.url("/profile");
        bookExists = $("//*[contains(@id, 'see-book-Designing')]").isDisplayed();
    
        expect (!bookExists);  // see if the book is gone
    });
});

