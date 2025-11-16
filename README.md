# Adobe Media and Data Science Research (MDSR) Laboratory

This is the website for the Adobe Media and Data Science Research (MDSR) Laboratory.

## Instructions

1. Fork the repository using your personal Github account, and clone the repository to your local machine.
2. Run `brew install git golang hugo node` to install the dependencies
3. Run `hugo server -D` to start the development server
4. Open `http://localhost:1313/` in your browser to view the website

### Updating the website

#### Adding/Updating your profile

**Note:** Profile files are stored in `content/authors/` (required by Hugo Blox), but appear as `/people/` URLs on the website.

1. Add your profile to the `content/authors/` directory by creating a new folder with your name (use lowercase and hyphens, e.g., `yaman-kumar-singla`).
2. Copy the `_index.md` file from an existing person's folder (e.g., `content/authors/yaman-kumar-singla/_index.md`) to your new folder. Make sure not to rename the file.
3. Update the `_index.md` file with your information. Make sure to set `user_groups` to include `["Researchers"]` to appear on the People page.
4. Add your profile picture to your folder with the name `avatar.jpg` or `avatar.png`.
5. Compile the website and verify the changes by running `hugo server -D`. Your profile will be available at `https://adobe.mdsr.live/people/your-name/`.
6. Commit the changes to the repository by raising a PR on the main branch of the base repository from your forked repository.


#### Adding your publications

1. Add your publication to the `content/publication/` directory by creating a new folder with some short name for your publication.
2. Add 'index.md' file to your folder and add the publication details in it. See the example in `content/publication/long-term-memorability/index.md`. Make sure to update the `date` and `publishDate` fields to the correct date of the publication. Don't change the name of the file.
3. Add 'featured.jpg' or 'featured.png' to your folder and add the publication picture to it.
4. Compile the website and verify the changes by running `hugo server -D` and commit the changes to the repository by raising a PR on the main branch of the base repository from your forked repository.

Credits: https://wowchemy.com/docs/getting-started/