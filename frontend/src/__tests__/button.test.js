/*
 * test to check if the button is rendered
 * test to check if the button is clickable
 * test to check if the onclick function is called
 */
const puppeteer = require("puppeteer");

let browser;
let page;
const width = 1920;
const height = 1080;

beforeAll(async () => {
 browser = await puppeteer.launch({
  headless: false,
  slowMo: 100,
  args: [`--window-size=${width},${height}`],
 });
 page = await browser.newPage();
 await page.setViewport({width, height});
});

afterAll(() => {
 browser.close();
});

test("button is rendered", async () => {
 await page.goto("http://localhost:3000");
 await page.waitForSelector("button");
 const button = await page.$("button");
 expect(button).not.toBeNull();
});
