<section>
  <header>
    <h1 id="project-header">{{PROJECT_NAME}}</h1>
    <p>{{ONE_LINE_DESC}}</p>
    <div id="badges">
      <img src="https://img.shields.io/badge/license-MIT-blue.svg" alt="License">
      <img src="https://img.shields.io/badge/version-1.0.0-green.svg" alt="Version">
    </div>
  </header>

  <nav>
    <h2 id="table-of-contents">Table of Contents</h2>
    <ul>
      <li><a href="#about-project">About / Project Details</a></li>
      <li><a href="#installation">Installation</a></li>
      <li><a href="#usage">Usage</a></li>
      <li><a href="#results">Results / Screenshots</a></li>
      <li><a href="#configuration">Configuration / Customization</a></li>
      <li><a href="#contributing-license">Contributing + License</a></li>
      <li><a href="#footer">Footer</a></li>
    </ul>
  </nav>

  <section id="about-project">
    <h2>About / Project Details</h2>
    <p>This section provides a brief overview of the project, explaining its purpose, functionality, and the problem it solves. It's designed to give visitors a quick understanding of what the project is all about.</p>
    <h3>Key Features:</h3>
    <ul>
      {{FEATURE_LIST}}
      <li><strong>Feature One:</strong> Describe the first key feature.</li>
      <li><strong>Feature Two:</strong> Describe the second key feature.</li>
      <li><strong>Feature Three:</strong> Describe the third key feature.</li>
    </ul>
    <p><strong>Technologies used:</strong> {{TECH_STACK}}</p>
  </section>

  <section id="installation">
    <h2>Installation</h2>
    <p>Follow these steps to set up the project locally. Ensure you have the necessary prerequisites installed.</p>
    <pre><code>{{INSTALL_COMMANDS}}</code></pre>
  </section>

  <section id="usage">
    <h2>Usage</h2>
    <p>After installation, you can run the project using the following command:</p>
    <pre><code>{{USAGE_EXAMPLE}}</code></pre>
    <p>This will start the application. You can then interact with it as described in the project's documentation.</p>
  </section>

  <section id="results">
    <h2>Results / Screenshots</h2>
    <figure>
      <img src="assets/screenshots/result-1.png" alt="A screenshot showing the main interface of the application." loading="lazy" style="max-width:100%;height:auto;">
      <figcaption>Figure 1: The main dashboard view of the application. </figcaption>
    </figure>
    <figure>
      <img src="assets/screenshots/result-2.png" alt="A screenshot showing a key feature or result from the project." loading="lazy" style="max-width:100%;height:auto;">
      <figcaption>Figure 2: A view demonstrating a core feature in action. </figcaption>
    </figure>
  </section>

  <section id="configuration">
    <h2>Configuration / Customization</h2>
    <p>This project can be configured by modifying the <code>config.json</code> file. Key options include API endpoints, theme settings, and data source parameters. Refer to the comments in the configuration file for more details.</p>
  </section>

  <section id="contributing-license">
    <h2>Contributing + License</h2>
    <p>Contributions are welcome! Please read the <a href="{{CONTRIBUTE_LINK}}">contributing guidelines</a> and submit pull requests for any improvements.</p>
    <p>This project is licensed under the {{LICENSE_NAME}} License. See the <code>LICENSE</code> file for details.</p>
  </section>

  <footer id="footer">
    <p>Maintained by {{MAINTAINER_CONTACT}}.</p>
  </footer>
</section>
