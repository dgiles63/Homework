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

describe("Search Books", function() {
    it("Should search Books", function() {
        browser.url("/profile");
        $("#searchBox").waitForDisplayed();
        $("#searchBox").addValue("Git");

        expect ($("//*[contains(@id, 'see-book-Git')]")).toBeDisplayed();

        $("#searchBox").clearValue();
    });
});

describe("Change the number of display rows", function() {
    it("Should change the display row numbers", function() {

        $("//*[contains(@class, '-pageSizeOptions')]").waitForClickable();
        $("//*[contains(@class, '-pageSizeOptions')]").click();

        list = $$("//*[contains(@class, '-pageSizeOptions')]").length;

        for(var i=0; i<list.length; i++) {
            $$("//*[contains(@class, '-pageSizeOptions')]")[i].waitForClickable();
            $$("//*[contains(@class, '-pageSizeOptions')]")[i].click();
            $("//*[contains(@class, '-pageSizeOptions')]").waitForClickable();
            $("//*[contains(@class, '-pageSizeOptions')]").click();
        }
        
    });
});

