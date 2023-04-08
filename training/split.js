const fs = require('fs')

/**
 * This file will split up each entry in all/labels and all/input into test, train, and val
 * The split is 80/10/10
 */

const labels = fs.readdirSync('./all/labels')

// Label names corrospond to it's matching image name
labels.forEach(label => {
  const lPath = `./all/labels/${label}`
  const iPath = `./all/input/${label.split('.')[0]}.bmp`

  // Move label to one of the folders
  const name = label.split('.')[0]

  const lExt = label.split('.')[1]

  const r = Math.random()

  if (!fs.existsSync(iPath)) return

  if (r < 0.8) {
    fs.copyFileSync(lPath, `./train/labels/${name}.${lExt}`)
    fs.copyFileSync(iPath, `./train/images/${name}.bmp`)
  }

  if (r >= 0.8 && r < 0.9) {
    fs.copyFileSync(lPath, `./val/labels/${name}.${lExt}`)
    fs.copyFileSync(iPath, `./val/images/${name}.bmp`)
  }

  if (r >= 0.9) {
    fs.copyFileSync(lPath, `./test/labels/${name}.${lExt}`)
    fs.copyFileSync(iPath, `./test/images/${name}.bmp`)
  }
})