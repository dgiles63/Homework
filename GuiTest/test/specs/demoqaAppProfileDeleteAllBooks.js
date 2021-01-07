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

describe("Test elements on the profile page", function() {
    it("Test Delet All Books", function() {
        browser.url("/profile");
        $("//button[@id='gotoStore']/parent::div/following-sibling::div[2]").waitForClickable();
        $("//button[@id='gotoStore']/parent::div/following-sibling::div[2]").click();
        $("#closeSmallModal-cancel").waitForClickable();
        $("#closeSmallModal-cancel").click();

        $("//button[@id='gotoStore']/parent::div/following-sibling::div[2]").waitForClickable();
        $("//button[@id='gotoStore']/parent::div/following-sibling::div[2]").click();
        $("#closeSmallModal-ok").waitForClickable();
        $("#closeSmallModal-ok").click();

        browser.pause(2000);
        browser.acceptAlert();

        bookExists = $("#delete-record-undefined").isDisplayed();
        expect (!bookExists);

        browser.pause(5000);
    });
});