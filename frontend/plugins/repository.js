import createRepository from '~/api/repository.js'

export default (ctx, inject) => {
  const repo = createRepository(ctx.$axios)

  const repositories = {
    repo
  }

  inject('repositories', repositories)
}
