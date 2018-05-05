const Koa = require('koa');
const serve = require('koa-static');
const router = require('koa-router')();
const koaBody = require('koa-body');
const fs = require('fs');
const app = new Koa();

app.use(serve('static'))

router.post('/send', koaBody(),
  (ctx) => {
    var body = ctx.request.body;
    var time = body.startTime
    fs.writeFile("labels/" + time + ".json", JSON.stringify(body), (err) => {});
  }
)

app.use(router.routes());
app.listen(3000);
