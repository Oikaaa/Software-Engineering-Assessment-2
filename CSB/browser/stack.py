class Browser:
    def __init__(self):
        self.back_stack = [] #Play as back and current page, first element always current page
        self.forward_stack = []

    def visit_page(self, url):
        self.back_stack.append(url)
        self.forward_stack.clear()
        print(f"You are browsing {url}")

    def back(self):
        if len(self.back_stack) >= 2:
            current_page = self.back_stack.pop()
            self.forward_stack.append(current_page)
            previous_page = self.back_stack[-1]
            print(f"Going back to {previous_page}")
        else:
            print("Can't go back more")

    def forward(self):
        if len(self.forward_stack):
            next_page = self.forward_stack.pop()
            self.back_stack.append(next_page)
            print(f"Going forward to {next_page}")
        else:
            print("Can't forward more")

if __name__ == "__main__":
    browser = Browser()

    browser.visit_page("google.com")
    browser.visit_page("facebook.com")
    browser.visit_page("instagram.com")

    browser.back()
    browser.back()
    browser.back()

    browser.forward()
    browser.forward()
    browser.forward()
