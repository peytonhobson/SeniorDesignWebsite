# SeniorDesignWebsite

In particular the documentation for [Structure](https://docs.startbootstrap.com/sb-admin-pro-angular/structure-root-level),
and the documentation for [SBPro Schematics](https://docs.startbootstrap.com/sb-admin-pro-angular/development-general#sb-pro-schematics)

## Links

[Click here for demo](https://sb-clean-blog.startbootstrap.com/)

[Click here for the backend.](https://github.com/StartBootstrap/sb-clean-blog-node)
Built with Node.js, Typescript, Fastify, and TypeORM

[Click here to view Angular code coverage](https://sb-clean-blog.startbootstrap.com/coverage/sb-clean-blog-angular/index.html)

[Click here to view Node code coverage](https://sb-clean-blog.startbootstrap.com/coverage/sb-clean-blog-node/index.html)

## Quick Start

```bash
git clone git@github.com:peytonhobson/SeniorDesignProject.git
cd SeniorDesignProject
npm install
npm start
```

`npm start` should open a browser window to <http://localhost:4200>

By default angular runs on port 4200. To change this port you can run:

```bash
# This starts the development server on port 4205,
# but you can use any port you'd like
export PORT=4205 && npm start
```

## Tests

### Unit Tests

```bash
npm run test

# To keep the test runner going as you devleop tests use:
npm run test:dev
```

### e2e

```bash
npm run e2e

# To run against currently running server instead of launching a new server
npm run e2e:running
```

## Production

SB Clean Blog Angular comes with a production ready Dockerfile and build scripts.

You can get Docker [here](https://www.docker.com/get-started)

```bash
# Be sure to build the app first
npm run build

# Then build the docker image
npm run docker:build

# Then run the image
npm run docker:run
```

## Generate Code

```bash
npm run generate:module -- --path src/modules --name Test
npm run generate:component -- --path src/modules/test/containers --name Test
npm run generate:component -- --path src/modules/test/components --name Test
npm run generate:directive -- --path src/modules/test/directives --name Test
npm run generate:service -- --path src/modules/test/services --name Test
```

_Note: Creating a Component and a Container use the same command,
the difference is just the paths and how they are used._

### MVCC

Containers and Components are both Angular Components, but used in different ways.

Containers should arrange Components.

Obviously this can become subjective, but MVCC is the paradigm that we subscribe to.

## Troubleshooting

### npm start

If you receive memory issues adjust
`max_old_space_size` in the `ng` command of the `package.json`:

```json
"ng": "cross-env NODE_OPTIONS=--max_old_space_size=2048 ./node_modules/.bin/ngngu",
```

You can adjust 2048 to any number you need.

For more information about why you may need `--max_old_space_size`
see [this article](https://medium.com/@ashleydavis75/node-js-memory-limitations-30d3fe2664c0).

Keep in mind that this project only uses node to build the angular application.
There is no production dependency on node.
